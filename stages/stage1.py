import os, sys, time
import random,keyboard
#====================================================================================================================
#===========================================BUILDS========================================================================
def worker():
    try:
        if keyboard.is_pressed('ESC'):
            return True

    except:
        return False

def animation_text(frase, time_):
    try:
        for i in list(frase):
            print(i, end='')

            sys.stdout.flush()
            time.sleep(time_)

            isP = worker()
            if (isP == True):
                print("\n"+frase)
                break

    except KeyboardInterrupt:
        exit()

def listen(chaves,Fapoio):
    while True:
        x = 0
        print("\n")
        for i in chaves:
            animation_text("|"+i+"|",0.1)
        print("\n")
        entrada = str(input(f'\n {Fapoio} Digite uma das opcoes acima: '))
        print("\n")

        while x < len(chaves):
            
            if(entrada == chaves[x]):
                return entrada
            else:
                x +=1
                if(entrada not in chaves):
                    animation_text(" Não entendi :(",0.1)
                    break

def NPC(name):
    npc = "\033[1;31m" + name + "\033[0;0m"
    return npc

#====================================================================================================================
#==============================================INICIO=====================================================================
   
class Main:
    
    bot = '\033[1;36m'+"navi"+"\033[0;0m"


    def Main_Phase(self):
        animation_text(f" {self.bot}: Voce esta em uma taverna... o vento forte e a neve densa assolam o tempo la fora, voce pode ver isso pela janela logo ao seu lado... Muita musica, cantorias e conversas tomam conta do ambiente... \n",0.1)
        animation_text(f" {self.bot}: É possivel notar que os grupos são bem divididos... proximo ao balcao da taverna é tomado por anoes, que bebem mais do que ninguem...\n",0.1)
        animation_text(f" {self.bot}: Perto da lareira se reunem alguns cavaleiros do reino, eles contam historias... mas nem sempre sao verdade \n",0.1)
        animation_text(f" {self.bot}: No centro voce pode ver algumas pessoas que estao jogando cartas, e em cima da mesa estao muitas moedas de ouro e prata \n",0.1)
        animation_text(f" {self.bot}: Ha tambem algumas pessoas que jogam dardos perto da porta...",0.1)
        print("\n")
        key = ['Ir aos anoes','Ir aos cavaleiros','Ir aos jogos','Ir aos dardos','Ficar onde esta']
        
        while True:
            result = listen(key,'Onde quer ir? ')
            if(result == 'Ir aos anoes'):
                return 1
            elif(result == 'Ir aos cavaleiros'):
                return 2
            elif (result == 'Ir aos jogos'):
                return 3
            elif (result == 'Ir aos dardos'):
                return 4
            elif (result == 'Ficar onde esta'):
                return 5
#====================================================================================================================
#================================================MESAS===============================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------MESA ANOES------------------------------------------------------------------------------------------------------------
    def mesa_anoes(self):
        os.system('cls')
        print("***********Mesa dos anoes*********")
        animation_text(f" {self.bot}: Voce se aproxima e senta em uma cadeira do balcao perto da mesa onde eles estão, eles notam sua presença mas n fazem nada... \n",0.1)
        animation_text(f" {self.bot}: O taverneiro chega em voce e pergunta: -Oque vai beber meu jovem? temos... \n",0.1)
        print("\n")
        key = ['Cerveja','Pinga anã','Hidromel','Agua','Whiski','Leite','Não quero nada']

        while True:
            result = listen(key,'E então, oque vai ser?')
            Eitri = NPC("Eitri")
            #......................................SITUACAO CERVEJA/WHISKI..............................................................
            if(result == 'Cerveja')or (result == 'Whiski'):
                animation_text(f" {self.bot}: Voce pediu {result}, interessante... \n",0.1)
                animation_text(f" {self.bot}: Um anão te chamou... - Ei! Que tal alguma coisinha mais forte?...",0.1)
                animation_text(f" Vamos... não seja timido, meu nome é {Eitri} prazer... chega mais!",0.1)
                print("\n")
                key= ['Não obrigado','No que esta pensando?']
                
                while True:
                    result = listen(key,'Oque vai responder?')
                    
                    if(result == 'Não obrigado'):
                        animation_text(f" {Eitri}: iih, tudo bem então... se mudar de ideia... não me chame! \n",0.1)
                        return 0
                    elif(result == 'No que esta pensando?'):
                        animation_text(f" {Eitri}: Um jogo de bebidas",0.1)
                        animation_text(f" ... \n",0.3)
                        animation_text(f" {Eitri}: Nós dois bebendo, quem cair primeiro perde \n",0.1)
                        animation_text(f" {Eitri}: Eai... topa?",0.1)
                        print("\n")
                        key = ['sim','não']

                        while True:
                            result = listen(key,'Aceitar?')
                            
                            if(result == 'sim'):
                                return 1 #colocar aqui funcao para o jogo de bebidas
                            elif (result == 'não'):
                                return 0 #colocar aqui funcao para proseguir

            #.......................................SITUACAO HIDROMEL/PINGA.............................................................

            elif(result == 'Hidromel') or (result == 'Pinga anã'):
                animation_text(f" {self.bot}: Voce pediu {result}, Wow, vai com calma... \n",0.1)
                animation_text(f" {self.bot}: Um anão te chamou... - Ae novato, curte umas parada forte é? que tal um joguinho?...",0.1)
                animation_text(f" Vamos... não seja timido, meu nome é {Eitri} prazer... chega mais!",0.1)
                print("\n")
                key= ['Não obrigado','Que tipo de jogo?']
                
                while True:
                    result = listen(key,'Oque vai responder?')
                    
                    if(result == 'Não obrigado'):
                        animation_text(f" {Eitri}: bom, tudo bem então... você parece um cara legal... até a próxima! \n",0.1)
                    elif(result == 'Que tipo de jogo?'):
                        animation_text(f" {Eitri}: Um jogo de bebidas",0.1)
                        animation_text(f" ... \n",0.3)
                        animation_text(f" {Eitri}: Nós dois bebendo, quem cair primeiro perde \n",0.1)
                        animation_text(f" {Eitri}: Eai... topa?",0.1)
                        print("\n")
                        key = ['sim','não']

                        while True:
                            result = listen(key,'Aceitar?')
                            
                            if(result == 'sim'):
                                return 1 #colocar aqui funcao para o jogo de bebidas
                            elif (result == 'não'):
                                return 0  #colocar aqui funcao para proseguir

            #......................................SITUACAO LEITE/AGUA..............................................................

            elif (result == 'Leite') or (result == 'Agua'):
                animation_text(f" {self.bot}: Voce pediu {result}, Não quer passar da conta? esperto... \n",0.1)
                animation_text(f" {self.bot}: Um anão falou... - Ae galera, se liga nesse cara HAHAHA... \n",0.1)
                animation_text(f" Oque foi? Não sabe beber? bebezinho HAHAHAHA ...\n",0.1)
                animation_text(f" Ae bebezinho, meu nome é {Eitri} o rei das bebidas! Ta afim de uma aposta?",0.1)
                print("\n")
                key= ['Não obrigado','Que aposta?']
                
                while True:
                    result = listen(key,'Oque vai responder?')
                    
                    if(result == 'Não obrigado'):
                        animation_text(f" {Eitri}: HAHAHA, ta legal bebezinho, fica ai... \n",0.1)
                    elif(result == 'Que aposta?'):
                        animation_text(f" {Eitri}: Um jogo de bebidas",0.1)
                        animation_text(f" ... \n",0.3)
                        animation_text(f" {Eitri}: Quem conseguir beber mais ganha! \n",0.1)
                        animation_text(f" {Eitri}: Eai... topa?",0.1)
                        print("\n")
                        key = ['sim','não']

                        while True:
                            result = listen(key,'Aceitar?')
                            
                            if(result == 'sim'):
                                return 1 #colocar aqui funcao para o jogo de bebidas
                            elif (result == 'não'):
                                return 0 #colocar aqui funcao para proseguir

            #......................................SITUACAO QUERO NADA..............................................................

            elif (result == 'Não quero nada'):
                animation_text(f" {self.bot}: Não vai beber nada? tudo bem então... \n",0.1)
                animation_text(f" {self.bot}: Voce escuta uns murmurios vindo da mesa dos anões... Um deles levanta e vem na sua direção...\n",0.1)
                animation_text(f" {self.bot}: Ele te deu um tapinha nas costas, sentou ao seu lado e disse: -Não vai beber nada? Prazer sou {Eitri}\n",0.1)
                animation_text(f" {Eitri}: Se mudar de ideia quanto a bebida... tenho uma proposta de jogo para voce... \n",0.1)
                animation_text(f" {self.bot}: Ao dizer isso ele levantou e voltou para onde estava sentado...\n",0.1)
                print("\n")
                key= ['Ir ate la','Ficar onde esta']
                
                while True:
                    result = listen(key,'Oque vai fazer?')
                    
                    if(result == 'Ir ate la'):
                        animation_text(f" {self.bot}: Voce se levantou e foi ate a mesa de {Eitri} \n",0.1)
                        animation_text(f" {Eitri}: Ah, olha voce ai... sente-se \n",0.1)
                        animation_text(f" {Eitri}: O jogo é o seguinte... a gente bebe... quem cair primeiro perde \n",0.1)
                        animation_text(f" {Eitri}: Eai... topa?",0.1)
                        print("\n")
                        key = ['sim','não']

                        while True:
                            result = listen(key,'Aceitar?')
                            
                            if(result == 'sim'):
                                return 1 #colocar aqui funcao para o jogo de bebidas
                            elif (result == 'não'):
                                return 0 # funcao para prosseguir
                                
                    elif(result == 'Ficar onde esta'):
                        animation_text(f" {self.bot}: Vai ficar aqui? Tudo bem então",0.1)
                        animation_text(f" ... \n",0.3)
                        return 0
                        
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------MESA CAVALEIROS-----------------------------------------------------------------------------------------------------------


    def mesa_cavaleiros(self,nomeJ):
        os.system('cls')
        print("***********Mesa dos cavaleiros*********")
        nomeJ = '\033[32m'+ f"{nomeJ}"+'\033[0;0m'
        joe = NPC('Joe')
        animation_text(f"{self.bot}: você se levanta e se aproxima da mesa dos cavaleiros, eles estão sentados em roda, aparentemente são uns 5 deles,e dois estão com mulheres...\n",0.1)
        animation_text(f"{self.bot}: Um deles nota que você ta se aproximando e diz: -Eae cara, ta perdido? \n",0.1)
        print(" \n")
        userR = str(input(" Oque vai dizer? "))
        animation_text(f"\n {nomeJ}: {userR} \n",0.1)
        animation_text(f"\n {self.bot}: Ele disse: -Quer sentar com a gente? meu nome é {joe} \n",0.1)
        key = ['Sentar','Passar reto','Não obrigado','Claro']

        while True:
            result=listen(key,'Oque vai fazer? ')
#......................................SITUACAO SENTAR..............................................................
            if(result=='Sentar'):
                animation_text(f" {self.bot}: Você simplesmente se sentou... \n",0.1)
                animation_text(f" {joe}: Vcê é bem direto né HAHA, tudo bem então... \n",0.1)
                retorno = "Conversa"
                return retorno
#......................................SITUACAO PASSAR RETO..............................................................
            elif(result=='Passar reto'):
                animation_text(f" {self.bot}: Achei que quisesse ir na mesa deles... você que manda {nomeJ}... \n",0.1)
                animation_text(f" {self.bot}: Você deixou o cavaleiro falando sozinho... \n",0.1)
                print(" \n")
                key = ['Ir aos anoes','Ir aos jogos','Ir aos dardos','Sair da taverna']
                while True:
                    result = listen(key,'Oque vai fazer? ')
                    if(result == 'Ir aos anoes'):
                        return 1
                    elif (result =='Ir aos jogos'):
                        return 2
                    elif (result == 'Ir aos dardos'):
                        return 3
                    elif (result == 'Sair da taverna'):
                        return 4
#......................................SITUACAO NÃO OBRIGADO..............................................................
            elif(result=='Não obrigado'):
                animation_text(f" {joe}: Ta legal... Você que sabe... nós iamos falar sobre a cicatriz arcana... \n",0.1)
                animation_text(f" {self.bot}: {nomeJ}, A cicatriz arcana foi o nome dado ao evento da ultima batalha entre as forças celestes e da escuridão...\n",0.1)
                animation_text(f" {self.bot}: Foi uma batalha tão sangrenta que imensos raios e trovões tomaram os céus por 7 dias e 7 noites... \n",0.1)
                print(" \n")
                key = ['Fale mais','Não to interessado']
                while True:
                    result = listen(key,'Oque dizer? ')
                    if(result == 'Fale mais'):
                        animation_text(f" {joe}: Por favor sente-se...\n ",0.1)
                        retorno = "Conversa"
                        return retorno

                    elif(result == 'Não to interessado'):
                        animation_text(f" {joe}: Ta legal... \n",0.1)
                        print(" \n")
                        key = ['Ir aos anoes','Ir aos jogos','Ir aos dardos']
                        while True:
                            result = listen(key,'Oque vai fazer? ')
                            if(result == 'Ir aos anoes'):
                                return 1
                            elif (result =='Ir aos jogos'):
                                return 2
                            elif (result == 'Ir aos dardos'):
                                return 3
#......................................SITUACAO CLARO..............................................................
            elif(result=='Claro'):
                animation_text(f" {joe}: Otimo!! \n",0.1)
                animation_text(f" {self.bot}: {joe} puxou uma cadeira e você se sentou com eles... \n",0.1)
                retorno = "Conversa"
                return retorno
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------MESA JOGOS------------------------------------------------------------------------------------------------------------
    def mesa_jogos(self):
        os.system('cls')
        print("***********Mesa dos jogos*********")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------MESA DARDOS------------------------------------------------------------------------------------------------------------
    def mesa_dardos(self):
        os.system('cls')
        print("***********Mesa dos dardos*********")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------SUA MESA------------------------------------------------------------------------------------------------------------
    def mesa_sua(self):
        os.system('cls')
        print("***********Sua mesa*********")

#================================================================================================================
#=================================================MINI GAMES=====================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------ JOGO DE BEBIDAS ANOES--------------------------------------------------------------------------------------

    def jogo_bebidas_anoes(self,nomeJ):
        #......................................DEFINI NPCS..............................................................
        Eitri = NPC("Eitri")
        Ivaldi = NPC("Ivaldi")
        Brook = NPC("Brook")
        nomeJ = '\033[32m'+ f"{nomeJ}"+'\033[0;0m'

        animation_text(f" {Eitri}: Aaah que bom... Esses são meus amigos.. {Ivaldi} e {Brook}.. Qual seu nome? \n",0.1)
        key= ['Se apresentar','Prefiro não dizer']

        while True:
            result = listen(key,'')
        #......................................SITUACAO SE APRESENTAR..............................................................
            if(result == 'Se apresentar'):
                animation_text(f" {nomeJ}: Meu nome é {nomeJ} \n",0.1)
                animation_text(f" {Ivaldi}: Nome bacana \n",0.1)
                animation_text(f" {Brook}: Verdade... \n",0.1)
                animation_text(f" {Eitri}: Bom.. vamos ao jogo! \n",0.1)
                s_n = True
                break
        #......................................SITUACAO NÃO SE APRESENTAR..............................................................
            elif (result == 'Prefiro não dizer'):
                animation_text(f" {Ivaldi}: Não quer dizer seu nome? Tudo bem então \n",0.1)
                animation_text(f" {Brook}: Você é bem direto não? \n",0.1)
                animation_text(f" {Eitri}: Ta legal, vamos direto ao jogo! \n",0.1)
                s_n = False
                break
        #......................................INICIO DO GAME..............................................................
        while True:
            animation_text(f" \n {self.bot}: {Ivaldi} enfilerou cinco copos de pinga anã em sua frente e cinco em frente a {Eitri} \n",0.1)
            animation_text(f" \n {self.bot}: O jogo sera assim {nomeJ}... O senhor e o {Eitri} iram revezar, e cada um beberá um copo de pinga anã...\n",0.1)
            animation_text(f" \n {self.bot}: Sempre que o senhor beber um copo, vai rodar um teste de resistencia, que consiste no lançamento de um dado de 6 lados... \n",0.1)
            animation_text(f" \n {self.bot}: Se o senhor tirar um numero inferior ou igual a 3, então falha no teste e desmaia de bêbado... mas se for superior a 3 o senhor passa no teste e o jogo continua... \n",0.1)
            animation_text(f" \n {self.bot}: Devo alertar o senhor de que a pinga anã é a bebida mais forte das terrar de Lichgard... então o senhor tem 50% de chance de cair com apenas um copo! \n",0.1)
            print("\n")
            os.system('pause')

            n_copos_i = 0
            n_copos_r_p = 5
            n_copos_r_e = 5
            D12 = [x for x in range(1,12)]
        #......................................CASO TENHA SE APRESENTADO..............................................................
            if(s_n == True):
                animation_text(f" {Eitri}: Vamos tirar na moeda {nomeJ}... Para ver quem comeca!\n",0.1)
        #......................................CASO NÃO TENHA SE APRESENTADO..............................................................
            elif (s_n == False):
                animation_text(f" {Eitri}: Que tal tirarmos na moeda meu rapaz?... Para ver quem começa\n",0.1)

            animation_text(f" {Eitri}: Vai querer cara ou coroa? \n",0.1)
            moeda = ['cara','coroa']
        #......................................TIRAR NA MOEDA PARA QUEM COMECAR..............................................................
            while True:
                result = listen(moeda,'Qual lado vai ser? ')

                if (result == 'cara'):
                    moeda_player = result
                    moeda_eitri = 'coroa'
                    animation_text(f" {Eitri}: {result}? Tudo bem entao eu sou {moeda_eitri}! \n",0.1)
                    break
                elif (result == 'coroa'):
                    moeda_player = result
                    moeda_eitri = 'cara'
                    animation_text(f" {Eitri}: {result}? legal, eu sou {moeda_eitri} então! \n",0.1)
                    break

            result_moeda = moeda[random.randint(0,len(moeda)-1)]
        #......................................SE VC GANHOU NA MOEDA..............................................................
            if(result_moeda == moeda_player):
                turn = 1
                animation_text(f" {self.bot}: Deu {result_moeda}...",0.1)
                animation_text(f" {Eitri}: hmmm, parece que você ganhou, pode começar então...\n",0.1)
        #......................................SE VOCE PERDEU NA MOEDA..............................................................
            elif (result_moeda == moeda_eitri):
                turn = 0
                animation_text(f" {self.bot}: Deu {result_moeda}...",0.1)
                animation_text(f" {Eitri}: Parece que eu ganhei... vou começar! \n",0.1)

            key = ['beber','parar']
        #......................................COMECA A BEBEDEIRA..............................................................
            while True:
                if(turn ==1):
                    while turn == 1:
                        result = listen(key,'Oque vai fazer?')

                        if(result == 'beber'):
                            n_copos_i +=1
                            n_copos_r_p -=1
                            resistencia_test = random.choice(D12)

                            if(resistencia_test <= 6):
                                animation_text(f" {self.bot}: Você bebeu um copo... \n",0.1)
                                animation_text(f" \n {self.bot}: Seu teste de resistencia foi {resistencia_test}. O senhor não aguentou... e caiu de bebado.. \n",0.1)
                                return True

                            elif (resistencia_test >6):
                                animation_text(f" {self.bot}: Você bebeu um copo... \n",0.1)
                                animation_text(f"\n {self.bot}: Seu teste de resistencia foi {resistencia_test}. O senhor bebeu {n_copos_i} copos... restam {n_copos_r_p} para o senhor... \n",0.1)
                                turn = 0

                        elif (result == 'parar'):
                            animation_text(f" {self.bot} Deseja parar senhor?... tudo bem então... Não quer cair de bêbado né HAHA, sábia decisão...\n",0.1)
                            animation_text(f" {Eitri}: Foi um bom jogo meu jovem... Eu ganhei HAHAHA... foi bom te conhecer! \n",0.1)
                            return False
                
                elif (turn == 0):
                    n_copos_r_e -=1
                    resistencia_test = random.choice(D12)

                    if(resistencia_test >6):
                        animation_text(f" {self.bot}: {Eitri} Bebeu um copo... \n",0.1)
                        animation_text(f" \n {self.bot}: O teste de resistencia de {Eitri} foi {resistencia_test}. Restam {n_copos_r_e} copos para {Eitri}...\n",0.1)
                        turn = 1

                    elif (resistencia_test <=6):
                        animation_text(f" {self.bot}: {Eitri} Bebeu um copo... \n",0.1)
                        animation_text(f" {self.bot}: O teste de resistencia de {Eitri} foi {resistencia_test}. {Eitri} não aguentou e caiu de bebado...\n",0.1)
                        animation_text(f" {Ivaldi}: {Eitri}!! Seu anão fracote... não acredito que caiu HAHAHA \n",0.1)
                        animation_text(f" {Brook}: Parabens meu jovem, faz muito tempo que não vejo ninguem ganhar do {Eitri}!! \n",0.1)
                        return False
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------ CONVERSAS DOS CAVALEIROS--------------------------------------------------------------------------------------

    def cv_cavaleiros(self,nomeJ):
        os.system('cls')
        print("***********Mesa dos cavaleiros*********")
        joe = NPC('Joe')
        animation_text(f" ... \n",0.3)
        animation_text(f" {joe}: ",0.1)

#================================================================================================================
#=================================================CONTINUAÇÕES REMANESCENTES=====================================================


Main()