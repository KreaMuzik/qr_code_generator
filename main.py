import segno

# Function for generating the qr code and saving it to local directory
def create_qr_code():
    name = input('Name: ')
    url = input('URL: ')

    qrcode = segno.make_qr(url)
    qrcode.save(name+'.png', scale=5, border=0)


create_qr_code()
