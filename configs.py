import os
import sys
import csv
import pandas as pd
import random

class configurations:
    user_config = {
        "Personagem_defs":[] # index 0 representa classe

    }

    bot = '\033[1;36m'+"navi"+"\033[0;0m"

    prints = {
    "div":"======================================================",
    "class_choice": " |(1) Viking | |(2) Assasino |(3) Paladino | |(4) Lanceiro | |(5) Mago | |(6) Cavaleiro | |(7) Arqueiro | "


    }

    def title_prinsset(self,var):
        os.system("cls")
        print("\033[1;31m" +"************************"+var+"********************************"+"\033[0;0m"+"\n")

    def menu_prinsset(self):
        print("=========Menu inicial======"+"\n")
        print("\n"+" Digite"+'\033[1;36m'+" play"+"\033[0;0m"+" para iniciar..."+"\n")
        print("\n"+" Digite"+'\033[1;36m'+" manual"+"\033[0;0m"+" para acessar o manual do jogo..."+"\n")


    
    def set_class(self):

        while True:
            
            choice_class = str(input(" E então, Oque vai ser? "))

        
            if(choice_class == "1"):
                self.user_config["Personagem_defs"].append("Viking") 
                break
            elif(choice_class =="2"):
                self.user_config["Personagem_defs"].append("Assasino") 
                break
            elif(choice_class=="3"):
                self.user_config["Personagem_defs"].append("Paladino") 
                break
            elif(choice_class=="4"):
                self.user_config["Personagem_defs"].append("Lanceiro") 
                break
            elif(choice_class=="5"):
                self.user_config["Personagem_defs"].append("Mago") 
                break
            elif(choice_class=="6"):
                self.user_config["Personagem_defs"].append("Cavaleiro") 
                break
            elif(choice_class=="7"):
                self.user_config["Personagem_defs"].append("Arqueiro") 
                break
            else:
                print("\n"+f" {self.bot}: Desculpe, não entendi :("+"\n")
                




    

class champion:


    champions_data = {
        # index 0 = forca, index 1 = resistencia, index 2 = velocidade, index 3 = magia, index 4 = inteligencia, vida =5

        "Viking":[50,60,30,1,15], 
        "Assasino":[34,38,60,1,48], 
        "Paladino":[38,48,50,1,30],
        "Lanceiro":[36,45,54,1,35],
        "Mago":[20,26,30,5,60],
        "Cavaleiro":[32,33,30,1,40],
        "Arqueiro":[34,38,50,1,45],

    }

    fc_ = 0
    res_= 0
    vel_ =0
    mg = 0
    int_ =0

    atk_ = 0
    def_ = 0


    
    def __init__(self,nome, classe):
        self.nome = nome
        self.classe = classe
        self.health = 1000
        def set_att(classe):
            fc_ = self.champions_data[self.classe][0]
            res_ = self.champions_data[self.classe][1]
            vel_ = self.champions_data[self.classe][2]
            mg_ = self.champions_data[self.classe][3]
            int_ = self.champions_data[self.classe][4]
            return fc_, res_, vel_, mg_, int_
           
        self.fc_, self.res_,self.vel_,self.mg,self.int_ = set_att(self.classe)

        self.atk_ = (self.fc_*self.vel_*self.mg) 
        self.def_ = (self.res_*self.mg)**2
        
        self.inventario = {
            'Itens':[],
            'Armas':[],
            'Moedas':{'Prata':[],'Ouro':[],'Bronze':[]}
        
        }
       

    def register_data(self):
        with open('datassets/player.csv','w') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(('Nome', 'Classe', 'Forca', 'Resistencia', 'Velocidade', 'Magia', 'Inteligencia', 'Ataque', 'Defesa','Vida'))
            writer.writerow(( self.nome,self.classe,self.fc_, self.res_,self.vel_,self.mg,self.int_, self.atk_,self.def_,self.health))

    def show_data(self):
        df2 = pd.read_csv("datassets/player.csv")
        print(df2.head())
        
    def read_data(self):
        f = open("datassets/player.csv","r")

        data = f.read()
        rows = data.split('\n')

        full_data = []

        for row in rows:
            split_row = row.split(",")
            full_data.append(split_row)
        
        return full_data[2]


class enemys:

    fc_ = 0
    res_= 0
    vel_ =0
    mg = 0
    int_ =0

    atk_ = 0
    def_ = 0

    health =0

    settings ={

        'Orc':[60,50,10,1,15,4000],
        'Guarda':[45,30,20,1,25,2500],
        'Esqueleto':[15,15,25,1,15,900],
        'Dragão':[70,65,30,2,10,5000],
        'Muzy':[55,35,40,2,30,3000],
        'Asmodai':[46,30,32,2,20,3100],
        'Estirge':[10,10,25,1,5,500],
        'Sabujo Sepulcral':[20,15,10,1,35,700],
        'Espectro':[10,10,40,3,35,800]

    }

    def __init__(self):
        
        def rand_en():
            keys = []
            
            for i in self.settings:
                keys.append(i)


            rd = random.randint(0,len(keys)-1)
            keys_ = keys[rd]
            class_data = self.settings[keys_]

            fc_ = self.settings[keys_][0]
            res_ = self.settings[keys_][1]
            vel_ = self.settings[keys_][2]
            mg_ = self.settings[keys_][3]
            int_ = self.settings[keys_][4]
            health = self.settings[keys_][5]

            return class_data,keys_,fc_,res_,vel_,mg_,int_,health

        self.class_data,self.name,self.fc_,self.res_,self.vel_,self.mg,self.int_,self.health = rand_en()
        self.atk_ = (self.fc_*self.vel_*self.mg) 
        self.def_ = (self.res_*self.mg)**2
