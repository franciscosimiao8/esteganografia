from stegano import lsb


def hidde_msg(img, msg):
    secret = lsb.hide("imgs/"+img, msg)
    secret.save("imgs/new_"+img)



def show_msg(img):
    clear = lsb.reveal("imgs/new_"+img)
    if clear:
        with open("archives/messages.csv", "a") as file:
            file.write(f"{img},{clear}\n")
        return clear
    return "Nenhuma Mensagem encontrada"


