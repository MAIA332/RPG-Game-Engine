import configs 
import relevants
import os
import sys
import time
import threading
from multiprocessing import Process
import keyboard

en = configs.enemys()
player = configs.champion('Maia','Mago')
player.register_data()


def read_data():
    f = open("datassets/player.csv","r")

    data = f.read()
    rows = data.split('\n')

    full_data = []

    for row in rows:
        split_row = row.split(",")
        full_data.append(split_row)
    
    return full_data[2]

""" player_data = read_data()
print(player_data)
print(en.name)
print(en.class_data)

#============================================

A1 = en.atk_ # troca parametro
D2 = player.def_ #troca parametro

bd = relevants.builds()
attr_combate = bd.combate_data(D2,A1,player.health) #trocar parametro

print(attr_combate)

H = attr_combate[2]

player.health = H #trocar parametro

print(player.health) #trocar parametro

if(attr_combate[3] == True):
    print("morreu")

os.system("pause")  
 """

def worker():
   try:
       if keyboard.is_pressed('j'):
           return True

   except:
       return False 

def anm(frase):
    try:
        for i in list(frase):
            print(i, end='')

            sys.stdout.flush()
            time.sleep(0.1)

            isP = worker()
            if (isP == True):
                print("\n"+frase+"\n")
                break

    except KeyboardInterrupt:
        print("\n"+frase+"\n")
        pass

""" 
t = threading.Thread(target=worker)
t.start() """
anm("testando a execução se não parar n deu certo")
anm("heloooo bitvheee")
anm("vai pular? okay")


