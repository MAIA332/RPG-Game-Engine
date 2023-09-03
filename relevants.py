import configs as con   
import os, sys, time
import Fx
import json
import pygame,keyboard

class assets: 

    def listen(self,entrada,chaves):
        x = 0
        while x < len(chaves):
           
            if(entrada == chaves[x]):
                return True
            else:
                x +=1
                 
    def worker(self):
        try:
            if keyboard.is_pressed('ESC'):
                return True

        except:
            return False 
            
    def animation_text(self,frase): 
        try:
            for i in list(frase):
                print(i, end='')

                sys.stdout.flush()
                time.sleep(0.1)

                isP = self.worker()
                if (isP == True):
                    print("\n"+frase)
                    break

        except KeyboardInterrupt:
            exit()
                    

    def read_json(self,file,ex):
     with open('datassets/'+file+'.'+ex,'r') as arquivo:
        texto = arquivo.read()
        data = json.loads(texto)
        arquivo.close()
        return data

class builds:
    clear = con.configurations()
    assets = assets()
    fr = Fx.formulas()

    def menu(self):
        keys = ['play','manual']
        self.clear.title_prinsset("Menu")
        self.clear.menu_prinsset()
        while True:
            entrada = str(input("Digite: "))
            type_ = self.assets.listen(entrada,keys)

            if(type_ == True):
                if(entrada == 'play'):
                    time.sleep(2)
                    break

                elif (entrada == 'manual'):
                    print(entrada)#=====> Manual

    def decisao(self):

        while True:
            dec = str(input(" (s/n) "))
            if(dec == "s"):
                return True
            elif (dec == "n"):
                return False
            else:
                print(" Desculpe mestre, acho que não entendi...")

    def combate_data(self,D2,A1,H):
        
        Dano_total,Porcentagem_retirada,Vida_restante = self.fr.ataque(D2,A1,H)

        if(Vida_restante ==0):
            defeated = True
        else:
            defeated = False

        return Dano_total,Porcentagem_retirada,Vida_restante,defeated

  