from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import*
import game


 #Define incremento de dificuldade
global modGame 
global modFacil 
global modMedio 
global modDificil 

#Define qual o dragão escolhido
global prefDragon 
global dragaoPrefStand
global dragaoPrefFlying



def gameChoseDragon():
    janela = Window(1280,720)
    janela.set_title("Batttle of the Dragons")


    #Define imagem de fundo
    fundoChoseDragon = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    choseDragon = Sprite("sprites/icones/DRAGONS.png")
    choseDragon.set_position(janela.width/2 - choseDragon.width/2,janela.height/2 - choseDragon.height/2)

    falkor = Sprite("sprites/personagens/bran1.png",4)
    falkorFlying = Sprite("sprites/personagens/bran-2.png",4)
    falkorInvertido = Sprite("sprites/personagens/bran-2 invertido.png",4)
    
    mushu = Sprite("sprites/personagens/red-1.png",4)
    mushuFlying = Sprite("sprites/personagens/red-2.png",4)
    mushuInvertido = Sprite("sprites/personagens/red-2 invertido.png",4)
 
    banguela = Sprite("sprites/personagens/pret-1.png",4)
    banguelaFlying = Sprite("sprites/personagens/pret-2.png",4)
    banguelaInvertido = Sprite("sprites/personagens/pret-2 invertido.png",4)

    elliot = Sprite("sprites/personagens/verd-1.png",4)
    elliotFlying = Sprite("sprites/personagens/verd-2.png",4)
    elliotInvertido = Sprite("sprites/personagens/verd-2 invertido.png",4)
    
    viserion =  Sprite("sprites/personagens/amar-1.png",4)
    viserionFlying = Sprite("sprites/personagens/amar-2.png",4)
    viserionInvertido = Sprite("sprites/personagens/amar-2 invertido.png",4)
   
    saphira =  Sprite("sprites/personagens/azul-1.png",4)
    saphiraFlying = Sprite("sprites/personagens/azul-2.png",4)
    saphiraInvertido = Sprite("sprites/personagens/azul-2 invertido.png",4)
  
    dragoesStanding = [falkor,mushu,banguela,elliot,viserion,saphira]
    dragoesFlying = [falkorFlying,mushuFlying,banguelaFlying,elliotFlying,viserionFlying,saphiraFlying]

    dragoesEnemy = [falkorInvertido,mushuInvertido,banguelaInvertido,elliotInvertido,viserionInvertido,saphiraInvertido] #trocar para imagem ao contrario

    #Define botoes dos dragoes
    falkorBTN = Sprite("sprites/icones/FALKOR.png")
    mushuBTN = Sprite("sprites/icones/MUSHU.png")
    banguelaBTN = Sprite("sprites/icones/BANGUELA.png")
    elliotBTN = Sprite("sprites/icones/ELLIOT.png")
    viserionBTN = Sprite("sprites/icones/VISERION.png")
    saphiraBTN = Sprite("sprites/icones/SAPHIRA.png")

    #Define posição dos botoes
    falkorBTN.set_position(445,240)
    mushuBTN.set_position(589,240)
    banguelaBTN.set_position(733,240)
    elliotBTN.set_position(445,414)
    viserionBTN.set_position(589,414)
    saphiraBTN.set_position(733,414)

    #Variavel para solução do problema de varios clicks
    NoDClick = 300

    #Permite entrada de mouse
    mouse = Window.get_mouse()

   

  
    #Game Loop
    while (True): 
        if(mouse.is_button_pressed(1)) and NoDClick == 0:
            if(mouse.is_over_object(falkorBTN)):
                prefDragon = dragoesStanding[0]
                dragaoPrefFlying = dragoesFlying[0]
                dragoesEnemy.pop(0)
            elif(mouse.is_over_object(mushuBTN)):
                prefDragon = dragoesStanding[1]
                dragaoPrefFlying = dragoesFlying[1]
                dragoesEnemy.pop(1)
            elif(mouse.is_over_object(banguelaBTN)):
                prefDragon = dragoesStanding[2]
                dragaoPrefFlying = dragoesFlying[2]
                dragoesEnemy.pop(2)
            elif(mouse.is_over_object(elliotBTN)):
                prefDragon = dragoesStanding[3]
                dragaoPrefFlying = dragoesFlying[3]
                dragoesEnemy.pop(3)
            elif(mouse.is_over_object(viserionBTN)):
                prefDragon = dragoesStanding[4]
                dragaoPrefFlying = dragoesFlying[4]
                dragoesEnemy.pop(4)
            elif(mouse.is_over_object(saphiraBTN)):
                prefDragon = dragoesStanding[5]
                dragaoPrefFlying = dragoesFlying[5]
                dragoesEnemy.pop(5)
            gameDificulty(prefDragon,dragaoPrefFlying,dragoesEnemy)
        if(NoDClick>0):
            NoDClick -=1 
        fundoChoseDragon.draw()
        choseDragon.draw()
        falkorBTN.draw()
        mushuBTN.draw()
        banguelaBTN.draw()
        elliotBTN.draw()
        viserionBTN.draw()
        saphiraBTN.draw()
        janela.update()

def gameHowTo():
    
    janela = Window(1280,720)
    janela.set_title("Battle of the Dragons") 

    teclado = Window.get_keyboard()

    #Define fundo do Reload
    fundoHowTo = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    menuHowTo = Sprite("sprites/icones/HOW TO MENU.png")
    menuHowTo.set_position(janela.width/2 - menuHowTo.width/2,janela.height/2 - menuHowTo.height/2)

    #Game Loop
    while(True):
        fundoHowTo.draw()
        if(teclado.key_pressed("ESC")):
            gameMenu()
        menuHowTo.draw()
        janela.update()
    


def gameReload():

    janela = Window(1280,720)
    janela.set_title("Battle of the Dragons") 

    teclado = Window.get_keyboard()

    #Define fundo do Reload
    fundoReload = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    menuReload = Sprite("sprites/icones/RELOAD MENU.png")
    menuReload.set_position(janela.width/2 - menuReload.width/2,janela.height/2 - menuReload.height/2)

    #Game Loop
    while(True):
        fundoReload.draw()
        if(teclado.key_pressed("ESC")):
            gameMenu()
        menuReload.draw()
        janela.update()

def gameDificulty(prefDragon,dragaoPrefFlying,dragoesEnemy):
    janela = Window(1280,720)
    janela.set_title("Batttle of the Dragons")

    #Define imagem de fundo
    fundoDificuldades = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    menuDificulty = Sprite("sprites/icones/DIFICULTY MENU.png")
    menuDificulty.set_position(janela.width/2 - menuDificulty.width/2,janela.height/2 - menuDificulty.height/2)

    #Define botões de dificuldade
    facil = Sprite("sprites/icones/EASY.png")
    medio = Sprite("sprites/icones/INTERMEDIATE.png")
    dificil = Sprite("sprites/icones/HARD.png")

    #Define posição dos botões
    facil.set_position(522,221)
    medio.set_position(522,339)
    dificil.set_position(522,457)

    #Define incremento de dificuldade
    modGame = 0
    modFacil = 1
    modMedio = 1.5
    modDificil = 2

    #Variavel para solução do problema de varios clicks
    NoDClick = 300

    #Permite entrada de mouse e teclado
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    #Game Loop
    while(True):
        if(teclado.key_pressed("ESC")):
            gameMenu()
        if(mouse.is_button_pressed(1)) and NoDClick == 0:
            if(mouse.is_over_object(facil)):
                modGame = modFacil
                #chama função do jogo
            elif(mouse.is_over_object(medio)):
                modGame = modMedio
                #chama função do jogo
            elif(mouse.is_over_object(dificil)):
                modGame = modDificil
                #chama função do jogo
            game.game(prefDragon,dragaoPrefFlying,1,dragoesEnemy,modGame)
        if(NoDClick>0):
            NoDClick -=1 
        fundoDificuldades.draw()
        menuDificulty.draw()
        facil.draw()
        medio.draw()
        dificil.draw() 
        janela.update()

def gameMenu():
    janela = Window(1280,720)
    janela.set_title("Batttle of the Dragons")

    #Define imagem de fundo
    fundoMenu = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    menuPrincipal = Sprite("sprites/icones/MENU PRINCIPAL.png")
    menuPrincipal.set_position(janela.width/2 - menuPrincipal.width/2,janela.height/2 - menuPrincipal.height/2)

    #Define imagem dos botões
    play = Sprite("sprites/icones/PLAY.png")
    dificuldade = Sprite("sprites/icones/DIFICULTY.png")
    reload = Sprite("sprites/icones/LOAD.png")
    howTo = Sprite("sprites/icones/HOW.png")
    sair = Sprite("sprites/icones/EXIT.png")

    #Define posição dos botoes
    play.set_position(516,207)

    dificuldade.set_position(516,274)

    reload.set_position(516,339)

    howTo.set_position(516,406)

    sair.set_position(516,474)

    #Permite entrada de mouse
    mouse = Window.get_mouse()

    
    # intro = Sound("audio\Medieval Themes (WAV)\intro do jogo.wav")

    #Game Loop
    while (True): 
        if(mouse.is_button_pressed(1)):
            if(mouse.is_over_object(play)):
                gameChoseDragon()
            elif(mouse.is_over_object(dificuldade)):
                gameDificulty()
            elif(mouse.is_over_object(reload)):
                gameReload()
            elif(mouse.is_over_object(howTo)):
                gameHowTo()
            elif(mouse.is_over_object(sair)):
                break
        # intro.load("audio\Medieval Themes (WAV)\intro do jogo.wav")
        fundoMenu.draw()
        menuPrincipal.draw()
        play.draw()
        dificuldade.draw()
        reload.draw()
        howTo.draw()
        sair.draw()
        janela.update()

gameMenu()