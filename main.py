import os
import sys
from libs.functions import *


if len(sys.argv) < 3:
    print("Falta argumentos")
    exit()

else:
    image = sys.argv[2]
    nome_img = image.split("/")[-1]
    print(nome_img)
    tipo = sys.argv[2]


    if tipo == "hidde":
        mess = sys.argv[3]
        if "http" in image:
            os.system(f"wget {image} -O imgs/{nome_img}")
            hidde_msg(f"{nome_img}", {mess})


        else:
            hidde_msg(f"{nome_img}", {mess})

    elif tipo == "show":
        print(show_msg(f"{nome_img}"))
