from werkzeug.security import generate_password_hash
from app import app, db


usuarios_demo = [
    {
        "nome": "admin.demo",
        "senha": "admin123",
        "tipo": "ti",
        "setor": "TI",
        "email": "admin.demo@example.com"
    },
    {
        "nome": "tecnico.demo",
        "senha": "ti123",
        "tipo": "ti",
        "setor": "TI",
        "email": "tecnico.demo@example.com"
    },
    {
        "nome": "administracao.demo",
        "senha": "adm123",
        "tipo": "administracao",
        "setor": "Administração",
        "email": "administracao.demo@example.com"
    },
    {
        "nome": "colaborador.demo",
        "senha": "demo123",
        "tipo": "colaborador",
        "setor": "Operações",
        "email": "colaborador.demo@example.com"
    }
]


with app.app_context():

    for usuario in usuarios_demo:

        existente = db.session.execute(
            db.text("""
                SELECT id
                FROM usuarios
                WHERE nome = :nome
            """),
            {
                "nome": usuario["nome"]
            }
        ).fetchone()

        senha_hash = generate_password_hash(usuario["senha"])

        if existente:

            db.session.execute(
                db.text("""
                    UPDATE usuarios
                    SET
                        senha = :senha,
                        tipo = :tipo,
                        setor = :setor,
                        email = :email,
                        ativo = TRUE,
                        precisa_trocar_senha = FALSE
                    WHERE nome = :nome
                """),
                {
                    "nome": usuario["nome"],
                    "senha": senha_hash,
                    "tipo": usuario["tipo"],
                    "setor": usuario["setor"],
                    "email": usuario["email"]
                }
            )

        else:

            db.session.execute(
                db.text("""
                    INSERT INTO usuarios
                    (
                        nome,
                        senha,
                        tipo,
                        setor,
                        email,
                        ativo,
                        precisa_trocar_senha
                    )
                    VALUES
                    (
                        :nome,
                        :senha,
                        :tipo,
                        :setor,
                        :email,
                        TRUE,
                        FALSE
                    )
                """),
                {
                    "nome": usuario["nome"],
                    "senha": senha_hash,
                    "tipo": usuario["tipo"],
                    "setor": usuario["setor"],
                    "email": usuario["email"]
                }
            )

    db.session.commit()

    print("Usuários demo criados/atualizados com sucesso.")