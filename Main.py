import configs as con
import relevants as rv
import datassets.dialogos as dl
from stages import stage1
from Autitions import exec_audio
import os, sys, time

bot = '\033[1;36m'+"navi"+"\033[0;0m"
clear = con.configurations()
assets = rv.assets()
builds = rv.builds()

prints_json = assets.read_json('sys_print','json')

def main_presentation():

    exec_audio.Main_exec('Autitions/IntroSong.mp3')

    builds.menu()

    frases = dl.dialogos
    #=============================
    clear.title_prinsset("Incio de tudo")
    #==============================
    assets.animation_text(frases["intro"])
    #==============================
    assets.animation_text(frases["hist_intro"])
    #=============================
    assets.animation_text(frases["dec_001"])
    desc = builds.decisao()
    if(desc == True):
        assets.animation_text(frases["answer_002"])
        clear.title_prinsset("Incio de tudo")
        #=========================================
        assets.animation_text(prints_json['hist_'])
        assets.animation_text(prints_json['hist_2'])
        assets.animation_text(prints_json['hist_3'])
        time.sleep(2)
        clear.title_prinsset("Incio de tudo")
        #==========================================
        assets.animation_text(frases['finalizacao'])
        main_config()
    else:
        assets.animation_text(frases["answer_001"])
        assets.animation_text(frases['finalizacao_precoce'])
        #==========================================
        main_config()

    

def main_config():
    
    #Definição do nome do jogador
    clear.title_prinsset("Configurações")

    playerName = str(input(f" {bot}: Como quer que eu te chame mestre? Escolha com sabedoria, não poderá trocar! : "))
    #================================================================================== 
    clear.title_prinsset("Configurações")

    assets.animation_text(f" {bot}: Bem vindo "+ '\033[32m'+ f"{playerName}"+'\033[0;0m'+f", conte me mais sobre você que tal?"+"\n")
    #===========================================================================================================
    print("\n"+" "+clear.prints["div"]+"\n")

    assets.animation_text("\n"+f" {bot}: "+"Primeiro começaremos com sua classe! Escolha com sabedoria "+ '\033[32m'+ f"{playerName}"+'\033[0;0m'+", não poderá trocar,"+"\n")
    #=======================================================================
    print("\n"+clear.prints["class_choice"])

    #definição da classe do jogador
    clear.set_class()
    
    assets.animation_text("\n"+f" {bot}: "+ clear.user_config["Personagem_defs"][0]+", hmmm, até que não é má escolha...")
    #===============================================================================
    player = con.champion(playerName,clear.user_config["Personagem_defs"][0])
    player.register_data()
    #inicialização da classe player e registro no arquivo em datassets/player.csv
    #===========================================================================
    assets.animation_text("\n"+f" {bot}: Aqui estão os dados de sua classe senhor "+ '\033[32m'+ f"{player.nome}"+'\033[0;0m'+"\n"+"\n")
    player.show_data()
    print("\n")
    #Exibe os dados do jogador
    #=========================================================================
    os.system("pause")#pausa o sistema
    ms = main_stages()
    ms.stage_one(player)

class main_stages:
   
   def stage_one(self,player_data):
       
        #================================================================
            clear.title_prinsset("Taverna")
            assets.animation_text(f" {bot}: Esta na hora de comecarmos... \n")
        #===============================================================
            exec_audio.Main_exec('Autitions/TavernSong.mp3')
            s1 = stage1.Main()
            mesa = s1.Main_Phase()
        #===============================================================
            while True:
                if(mesa == 1):
                    s1_mini = s1.mesa_anoes()
                    #-----------------------------------------------------------
                    if(s1_mini == 1):
                        is_bebado = s1.jogo_bebidas_anoes(player_data.nome)
                        if(is_bebado == True):
                            print("Terminou o jogo de bebidas com vc bebado") # colocar aqui a funcao para prosseguir
                        elif (is_bebado == False):
                            print("Terminou o jogo de bebidas com vc sobreo") # colocar aqui a funcao para prosseguir
                    
                    elif (s1_mini == 0):
                        print("sem jogo") # colocar aqui funcao para prosseguir 
                    #-----------------------------------------------------------
            #===============================================================
                elif (mesa ==2):
                    s1_mini = s1.mesa_cavaleiros(player_data.nome)
                    #-----------------------------------------------------------
                    if(s1_mini ==1):
                        mesa = 1
                        pass
                    elif (s1_mini==2):
                        mesa = 3
                        pass
                    elif (s1_mini==3):
                        mesa =4
                        pass
                    elif (s1_mini==4):
                        print("proxima fase") # colocar aqui funcao para prosseguir
                    #-----------------------------------------------------------
                    elif (s1_mini == 'Conversa'):
                        exec_audio.Main_exec('Autitions/SuspenseSong.mp3')
                        s1.cv_cavaleiros(player_data.nome)
            #===============================================================
                elif (mesa == 3):
                    s1.mesa_jogos()
                elif (mesa == 4):
                    s1.mesa_dardos()
                elif (mesa == 5):
                    s1.mesa_sua()
            #==============================================================
            
main_presentation()
