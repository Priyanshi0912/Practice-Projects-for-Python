import qrcode
import image
qr= qrcode.QRCode(
    version =15,
    box_size= 10,
    border = 5
    )
data = "https://youtu.be/668nUCeBHyY?si=GwqX-W8n7c-UxS_F"
qr.add_data(data)
qr.make( fit= True)
img= qr.make_image(fill="black",black_color="white")
img.save("test.png")
