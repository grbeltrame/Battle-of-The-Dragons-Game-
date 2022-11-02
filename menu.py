from tkinter import Button
from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *
import cavernaE


 #Define incremento de dificuldade
global modGame 
global modFacil 
global modMedio 
global modDificil 

#Define qual o dragão escolhido
global prefDragon 
global falkor
global falkorFlying
global mushu
global mushuFlying
global banguela
global banguelaFlying
global elliot
global elliotFlying
global viserion
global viserionFlying
global saphira
global saphiraFlying



def gameChoseDragon():
    janela = Window(1280,720)
    janela.set_title("Batttle of the Dragons")

    #Define imagem de fundo
    fundoChoseDragon = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    choseDragon = Sprite("sprites/icones/DRAGONS.png")
    choseDragon.set_position(janela.width/2 - choseDragon.width/2,janela.height/2 - choseDragon.height)

    falkor = Sprite("sprites/personagens/bran1.png",3)
    falkorFlying = Sprite("sprites/personagens/bran-2.png",3)
    falkor.set_total_duration(1000)
    falkorFlying.set_total_duration(1000)
    mushu = Sprite("sprites/personagens/red-1.png",3)
    mushuFlying = Sprite("sprites/personagens/red-2.png",3)
    mushu.set_total_duration(1000)
    mushuFlying.set_total_duration(1000)
    banguela = Sprite("sprites/personagens/pret-1.png",3)
    banguelaFlying = Sprite("sprites/personagens/pret-2.png",3)
    banguela.set_total_duration(1000)
    banguelaFlying.set_total_duration(1000)
    elliot = Sprite("sprites/personagens/verd-1.png",3)
    elliotFlying = Sprite("sprites/personagens/verd-2.png",3)
    elliot.set_total_duration(1000)
    elliotFlying.set_total_duration(1000)
    viserion =  Sprite("sprites/personagens/amar-1.png",3)
    viserionFlying = Sprite("sprites/personagens/amar-2.png",3)
    viserion.set_total_duration(1000)
    viserionFlying.set_total_duration(1000)
    saphira =  Sprite("sprites/personagens/azul-1.png",3)
    saphiraFlying = Sprite("sprites/personagens/azul-2.png",3)
    saphira.set_total_duration(1000)
    saphiraFlying.set_total_duration(1000)

    #Define botoes dos dragoes
    falkorBTN = Sprite("sprites/icones/FALKOR.png")
    mushuBTN = Sprite("sprites/icones/MUSHU.png")
    banguelaBTN = Sprite("sprites/icones/BANGUELA.png")
    elliotBTN = Sprite("sprites/icones/ELLIOT.png")
    viserionBTN = Sprite("sprites/icones/VISERION.png")
    saphiraBTN = Sprite("sprites/icones/SAPHIRA.png")

    #Define posição dos botoes
    falkorBTN.set_position(250,266)
    mushuBTN.set_position(399,266)
    banguelaBTN.set_position(542,266)
    elliotBTN.set_position(250,442)
    viserionBTN.set_position(399,442)
    saphiraBTN.set_position(542,442)

    #Variavel para solução do problema de varios clicks
    NoDClick = 300

    #Permite entrada de mouse
    mouse = Window.get_mouse()
  
    #Game Loop
    while (True): 
        if(mouse.is_button_pressed(1)) and NoDClick == 0:
            if(mouse.is_over_object(falkorBTN)):
                prefDragon = falkor
                dragaoPrefFlying = falkorFlying
            elif(mouse.is_over_object(mushuBTN)):
                prefDragon = mushu
                dragaoPrefFlying = mushuFlying
            elif(mouse.is_over_object(banguelaBTN)):
                prefDragon = banguela
                dragaoPrefFlying = banguelaFlying
            elif(mouse.is_over_object(elliotBTN)):
                prefDragon = elliot
                dragaoPrefFlying = elliotFlying
            elif(mouse.is_over_object(viserionBTN)):
                prefDragon = viserion
                dragaoPrefFlying = viserionFlying
            elif(mouse.is_over_object(saphiraBTN)):
                prefDragon = saphira
                dragaoPrefFlying = saphiraFlying
            cavernaE.gamePlayCavE(prefDragon,dragaoPrefFlying)
        if(NoDClick>0):
            NoDClick -=1 
        fundoChoseDragon.draw()
        choseDragon.draw()
        falkorBTN.draw()
        mushuBTN.draw()
        banguelaBTN.draw()
        elliot.draw()
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
    menuHowTo.set_position(janela.width/2 - menuHowTo.width/2,janela.height/2 - menuHowTo.height)

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
    menuReload.set_position(janela.width/2 - menuReload.width/2,janela.height/2 - menuReload.height)

    #Game Loop
    while(True):
        fundoReload.draw()
        if(teclado.key_pressed("ESC")):
            gameMenu()
        menuReload.draw()
        janela.update()

def gameDificulty():
    janela = Window(1280,720)
    janela.set_title("Batttle of the Dragons")

    #Define imagem de fundo
    fundoDificuldades = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    menuDificulty = Sprite("sprites/icones/DIFICULTY MENU.png")
    menuDificulty.set_position(janela.width/2 - menuDificulty.width/2,janela.height/2 - menuDificulty.height)

    #Define botões de dificuldade
    facil = Sprite("sprites/icones/EASY.png")
    medio = Sprite("sprites/icones/INTERMEDIATE.png")
    dificil = Sprite("sprites/icones/HARD.png")

    #Define posição dos botões
    facil.set_position(405,215)
    medio.set_position(405,335)
    dificil.set_position(405,455)

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
        if(NoDClick>0):
            NoDClick -=1 
        fundoDificuldades.draw()
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
    menuPrincipal.set_position(janela.width/2 - menuPrincipal.width/2,janela.height/2 - menuPrincipal.height)

    #Define imagem dos botões
    play = Sprite("sprites/icones/PLAY.png")
    dificuldade = Sprite("sprites/icones/DIFICULTY.png")
    reload = Sprite("sprites/icones/LOAD.png")
    howTo = Sprite("sprites/icones/HOW.png")
    sair = Sprite("sprites/icones/EXIT.png")

    #Define posição dos botoes
    play.set_position(400,208)

    dificuldade.set_position(400,270)

    reload.set_position(400,333)

    howTo.set_position(400,406)

    sair.set_position(400,476)

    #Permite entrada de mouse
    mouse = Window.get_mouse()

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

        fundoMenu.draw()
        menuPrincipal.draw()
        play.draw()
        dificuldade.draw()
        reload.draw()
        howTo.draw()
        sair.draw()
        janela.update()

gameMenu()