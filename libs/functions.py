from stegano import lsb

secret = lsb.hide("akatsuki.png", "Hello World")
secret.save("new_akatsuki.png")

clear = lsb.reveal("akatsuki.png")
print(clear)
