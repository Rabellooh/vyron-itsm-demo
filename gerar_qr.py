import qrcode

LINK = "http://localhost:5000//chamado_rapido"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(LINK)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save(
    "static/img/qr_chamado_rapido.png"
)

print("QR gerado!")