from datetime import datetime
import random
import os
import pickle
import time
import re


def main():
    os.system("cls")
    print("Benvingut a la teva LLista de Tasques")
    while True:
        first_input = input("Que vols utilitzar fer?: \n[1] Archiu del Dia a Dia\n\
[2] LLista de coses per fer\n")
        if first_input == "1":
            cdd()
        elif first_input == "2":
            ldcpf()
        else:
            print("Opcio no disponible, prem INTRO per continuar:")
            input()


def cdd():
    os.system("cls")
    pass


def ldcpf():
    os.system("cls")
    archiu = "COSAS_PER_FER.txt"
    if not os.path.isfile(archiu):
        print("Es la primera vegada que utilitzes LDCPF, vols crear el archiu txt?")
        ft = input("[S]i\n[N]o\n")
        if ft.lower() == "s":  
            with open(archiu, "w") as a:
                a.write("") 
            if os.path.isfile(archiu):
                print("S'ha creat l'archiu, Prem INTRO per continuar")
                input()
            else:
                print("Algo ha sortit malament reinicia el programa")
                input()
                exit()
        elif ft.lower() == "n":
            print("Prem ENTER per tornar a la pregunta anterior")
            input()
            return
    else:
        file_txt = open(archiu, "r") #No se puede hacer read 2 veces porque se vacia el Buffer
        text_llistat, text_lit = cont_tr(file_txt)
        print(text_llistat)
        print(text_lit)
        file_txt.close()
    
    ldcpf_s(text_llistat, text_lit,archiu)


def ldcpf_s(list,text,file_):

    text_1 = "[A]feixir tasca\n[V]eure les tasques\n[M]arcar tasca\n[R]Modificar tasca\n"
    F_LDC_input = input(text_1)
    match F_LDC_input.lower():
        case "a":
            ldcpf_a(list, text,file_)
        case "v":
            ldcpf_v(list,text,file_)


def ldcpf_v(list, text,file_):
    print(f"Ara hi han un total de {len(list)} tasques.")
    print(text)

                
def ldcpf_a(list,text,file_):
    os.system("cls")
    while True:
        text_2 = "Nom de la tasca que vols afeixir ('q' per cancelar):\n"
        nom_tasca = input(text_2)
        if nom_tasca.lower() == "q":
            return
        text_3 = "Modul de la teva tasca ('q' per cancelar) ('personal' si es personal)\n"
        modul_tasca = input(text_3)
        if modul_tasca.lower() == "q":
            return
        text_4 = "Quina es la data maxima d'entrega DD/MM/YYYY H:M? ('q' per sortir) (posa 'no' si no en te)\n" 
        data_hr_max = input(text_4)
        if data_hr_max.lower() == "q":
            return
        data_hr_usr = datetime.now().strftime("%d/%m/%Y %H:%M") 
        text_for_print = "[ ] " + nom_tasca + "{" + modul_tasca + "} (" + data_hr_usr +") !" + data_hr_max + "!" + "\n"
        with open(file_, "a") as a:
            a.write(text_for_print)
        print("J'ha s'ha posat la tasca!")
        resposta = None
        while not resposta:
            resposta = input("Vols afeixir un altre? \n[S]i\n[N]o")
            if resposta.lower() == "n":
                return
            elif resposta.lower() == "s":
                pass
            else:
                resposta = None
                print("Has escollit una resposta no valida, prem ENTER per continuar")
                input()

        

        
def cont_tr(fil):
    content = fil.read()
    text_ = [list(lineas) for lineas in content.split("\n")]
    return text_, content


def cont_tr_lit(fil):
    content = fil.read()
    return content



def ldcpf_AT():
    pass



if __name__ == "__main__":
    main()