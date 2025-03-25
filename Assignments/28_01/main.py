import qrcode
qr=qrcode.QRCode(version=1,box_size=10,border=5)
data='upi://pay?pa=abdulmannankhan2604-1@okhdfcbank&pn=Abdul%20mannan%20Khan&aid=uGICAgIDdveS1dA'
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('qr.png')