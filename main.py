import os
import sys
from libs.functions import *


if len(sys.argv) < 3:
    print("Falta argumentos")
    exit()

else:
    image = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png" #sys.argv[2]
    nome_img = image.split("/")[-1]
    print(nome_img)
    tipo = sys.argv[2]
    mess = sys.argv[3]

    if tipo == "hidde":
        if "http" in image:
            os.system(f"wget {image} -O imgs/{nome_img}")
            hidde_msg(f"{nome_img}", {mess})


        else:
            hidde_msg(f"{nome_img}", {mess})

    elif tipo == "show":
        print(show_msg(f"{nome_img}"))



