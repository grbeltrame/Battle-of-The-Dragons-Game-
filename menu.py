from tkinter import Button
from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *
import game

 #Define incremento de dificuldade
global modGame 
global modFacil 
global modMedio 
global modDificil 

# def gameRank():

#     janela = Window(1100,800)
#     janela.set_title("Space Invaders")
#     janela.set_background_color((0,255,0))

#     teclado = Window.get_keyboard()

#     #Define fundo do rank
#     fundoRank = GameImage("sprites/planetas.jpg")

#     #Game Loop
#     while(True):
#         if(teclado.key_pressed("ESC")):
#             gameMenu()

#         janela.set_background_color((0,255,0))
#         fundoRank.draw()
#         janela.update()

# def gameDificulty():
#     janela = Window(1100,800)
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

# def gameMenu():
#     janela = Window(1100,800)
#     janela.set_title("Space Invaders")
#     janela.set_background_color((0,255,0))

#     #Define imagem de fundo
#     fundoMenu = GameImage("sprites/planetas.jpg") 


#     #Define imagem dos botões
#     jogar = Sprite("sprites/jogar.png")
#     dificuldade = Sprite("sprites/dificuldade.png")
#     ranking = Sprite("sprites/ranking.png")
#     sair = Sprite("sprites/sair.png")

#     #Define posição dos botoes
#     jogar.x = janela.width/2 - jogar.width/2
#     jogar.y = 110

#     dificuldade.x = janela.width/2 - dificuldade.width/2
#     dificuldade.y = 220

#     ranking.x = janela.width/2 - ranking.width/2
#     ranking.y = 330

#     sair.x = janela.width/2 - sair.width/2
#     sair.y = 440

#     #Permite entrada de mouse
#     mouse = Window.get_mouse()

#     #Game Loop
#     while (True): 
#         if(mouse.is_button_pressed(1)):
#             if(mouse.is_over_object(jogar)):
#                 game.gamePlay(1)
#             elif(mouse.is_over_object(dificuldade)):
#                 gameDificulty()
#             elif(mouse.is_over_object(ranking)):
#                 gameRank()
#             elif(mouse.is_over_object(sair)):
#                 break

#         janela.set_background_color((0,255,0))
#         fundoMenu.draw()
#         jogar.draw()
#         dificuldade.draw()
#         ranking.draw()
#         sair.draw()
#         janela.update()

# gameMenu()