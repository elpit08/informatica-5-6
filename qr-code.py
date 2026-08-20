

rock_world = 'https://www.youtube.com/watch?v=g4tpuu-Up90&list=RDg4tpuu-Up90&start_radio=1'

import qrcode
qr = qrcode.QRCode(version=1, box_size=10,border=4)
qr.add_data(rock_world)
qr.make(fit=True)

img = qr.make_image(fill_color="Black", back_color="White")
img.save("youtube-qr.png")
