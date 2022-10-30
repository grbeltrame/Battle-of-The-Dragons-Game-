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

# def gameReload():

#   janela = Window(1280,720)
    # janela.set_title("Caverna fase Estática") 

#     teclado = Window.get_keyboard()

#     #Define fundo do Reload
#     fundoReload = GameImage("sprites/icones/fundo-dragão.jpg")

#     #Game Loop
#     while(True):
#         if(teclado.key_pressed("ESC")):
#             gameMenu()

#         fundoReload.draw()
#         janela.update()

# def gameDificulty():
#     janela = Window(1280,720)
#     janela.set_title("Batttle of the Dragons")

#     #Define imagem de fundo
#     fundoDificuldades = GameImage("sprites/icones/fundo-dragão.jpg")

#     #Define botões de dificuldade
#     facil = Sprite("sprites/facil.png")
#     medio = Sprite("sprites/medio.png")
#     dificil = Sprite("sprites/dificil.png")

#     #Define posição dos botões
#     facil.x = janela.width/2 - facil.width/2
#     facil.y = 200

#     medio.x = janela.width/2 - medio.width/2
#     medio.y = 300

#     dificil.x = janela.width/2 - dificil.width/2
#     dificil.y = 400

#     #Perimte entrada de mouse
#     mouse = Window.get_mouse()
#     teclado = Window.get_keyboard()

#     #Define incremento de dificuldade
#     modGame = 0
#     modFacil = 1
#     modMedio = 1.5
#     modDificil = 2

#     #Variavel para solução do problema de varios clicks
#     NoDClick = 300

#     #Game Loop
#     while(True):
#         if(teclado.key_pressed("ESC")):
#             gameMenu()
#         if(mouse.is_button_pressed(1)) and NoDClick == 0:
#             if(mouse.is_over_object(facil)):
#                 modGame = modFacil
#                 game.gamePlay(modGame)
#             elif(mouse.is_over_object(medio)):
#                 modGame = modMedio
#                 game.gamePlay(modGame)
#             elif(mouse.is_over_object(dificil)):
#                 modGame = modDificil
#                 game.gamePlay(modGame)
#         if(NoDClick>0):
#             NoDClick -=1 
#         fundoDificuldades.draw()
#         facil.draw()
#         medio.draw()
#         dificil.draw() 
#         janela.update()

def gameMenu():
    janela = Window(1280,720)
    janela.set_title("Batttle of the Dragons")

    #Define imagem de fundo
    fundoMenu = GameImage("sprites/icones/fundo-dragão.jpg")

    #Define imagem do Menu na tela 
    menuPrincipal = Sprite("sprites/icones/MENU PRINCIPAL.svg")
    menuPrincipal.set_position(janela.width/2 - menuPrincipal.width/2,janela.height/2 - menuPrincipal.height)

    # #Define imagem dos botões
    # play = Sprite("sprites\icones\PLAY.png")
    # dificuldade = Sprite("sprites\icones\DIFICULTY.png")
    # reload = Sprite("sprites\icones\LOAD.png")
    # howTo = Sprite("sprites\icones\HOW.png")
    # sair = Sprite("sprites\icones\EXIT.png")

    # #Define posição dos botoes
    # play.x = janela.width/2 -play.width/2
    # play.y = 110

    # dificuldade.x = janela.width/2 - dificuldade.width/2
    # dificuldade.y = 220

    # reload.x = janela.width/2 - reload.width/2
    # reload.y = 330

    # sair.x = janela.width/2 - sair.width/2
    # sair.y = 440

    #Permite entrada de mouse
    mouse = Window.get_mouse()

    #Game Loop
    while (True): 
        # if(mouse.is_button_pressed(1)):
        #     if(mouse.is_over_object(play)):
        #         caver
        #     elif(mouse.is_over_object(dificuldade)):
        #         gameDificulty()
        #     elif(mouse.is_over_object(reload)):
        #         gameReload()
        #     elif(mouse.is_over_object(sair)):
        #         break

        fundoMenu.draw()
        menuPrincipal.draw()
        # play.draw()
        # dificuldade.draw()
        # reload.draw()
        # sair.draw()
        janela.update()

gameMenu()