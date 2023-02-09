import base64

def string2image(imgstring):
    print("string2image function called--------->",imgstring)
    try:
        imgdata = base64.b64decode(imgstring)
        filename = 'some_image.jpg' 
        with open(filename, 'wb') as f:
            f.write(imgdata)
    except:
        print("error")
    

