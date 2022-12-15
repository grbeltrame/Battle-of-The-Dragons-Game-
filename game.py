from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *
import cavernaD
import cavernaE
import florestaD
import florestaE
import casteloD
import casteloE
import endGame

global mensagem
global checkpoint

def game(dragaoPrefFlying,cenario,vetorDragoesInimigos,modGame):
    danoEnemy = 1*modGame
    delay = 30 
    DragaoHP = 10
    vetPlatCavD, vetPlatCavE, vetPlatFlorD, vetPlatFlorE, vetPlatCasD, vetPlatCasE = plataformas()
    #Chamando as fases
    if(cenario == 1):
        init = False
        cenario = cavernaD.gamePlayCavD(dragaoPrefFlying,delay,vetPlatCavD,DragaoHP,danoEnemy,modGame,init)
    if(cenario == 2):
        init = False
        cenario = cavernaE.gamePlayCavE(dragaoPrefFlying,delay,vetPlatCavE,DragaoHP,danoEnemy,modGame)
    if(cenario == 3):
        init = False
        cenario = florestaD.gamePlayFlorD(dragaoPrefFlying,vetorDragoesInimigos,delay,vetPlatFlorD,DragaoHP,danoEnemy,modGame,init)
    if(cenario == 4):
        init = False
        cenario = florestaE.gamePlayFlorE(dragaoPrefFlying,vetorDragoesInimigos,delay,vetPlatFlorE,DragaoHP,danoEnemy,modGame)
    if(cenario == 5):
        init = False
        cenario = casteloD.gamePlayCasD(dragaoPrefFlying,vetorDragoesInimigos,delay,vetPlatCasD,DragaoHP,danoEnemy,modGame,init)
    if(cenario == 6):
        init = False
        cenario = casteloE.gamePlayCasE(dragaoPrefFlying,vetorDragoesInimigos,delay,vetPlatCasE,DragaoHP,danoEnemy,modGame)
    if(cenario == 7):
        endGame.finished(dragaoPrefFlying)

def plataformas():
    vetPlatCavD =[]
    platCavD1= Sprite("sprites/caverna-dinamico/plataforma_cav2.png",1)
    platCavD1.set_position(0, 568)
    platCavD2= Sprite("sprites/caverna-dinamico/plataforma_cav3.png",1)
    platCavD2.set_position(342, 325)
    platCavD3= Sprite("sprites/caverna-dinamico/plataforma_cav4.png",1)
    platCavD3.set_position(710, 478)
    platCavD4= Sprite("sprites/caverna-dinamico/plataforma_cav1.png",1)
    platCavD4.set_position(1030, 325)
    platCavD5= Sprite("sprites/caverna-dinamico/plataforma_cav5.png",1)
    platCavD5.set_position(1509, 574)
    platCavD6= Sprite("sprites/caverna-dinamico/plataforma_cav3.png",1)
    platCavD6.set_position(1847, 416)
    platCavD7= Sprite("sprites/caverna-dinamico/plataforma_cav4.png",1)
    platCavD7.set_position(2314, 298)
    platCavD8= Sprite("sprites/caverna-dinamico/plataforma_cav6.png",1)
    platCavD8.set_position(2002, 528)
    platCavD9= Sprite("sprites/caverna-dinamico/plataforma_cav5.png",1)
    platCavD9.set_position(2395, 574)
    platCavD10= Sprite("sprites/caverna-dinamico/plataforma_cav5.png",1)
    platCavD10.set_position(2902, 571)
    platCavD11= Sprite("sprites/caverna-dinamico/plataforma_cav3.png",1)
    platCavD11.set_position(2813, 300)
    platCavD12= Sprite("sprites/caverna-dinamico/plataforma_cav4.png",1)
    platCavD12.set_position(3208, 441)
    platCavD13= Sprite("sprites/caverna-dinamico/plataforma_cav7.png",1)    
    platCavD13.set_position(3468, 449)
    
    vetPlatCavD.append(platCavD1)
    vetPlatCavD.append(platCavD2)
    vetPlatCavD.append(platCavD3)
    vetPlatCavD.append(platCavD4)
    vetPlatCavD.append(platCavD5)
    vetPlatCavD.append(platCavD6)
    vetPlatCavD.append(platCavD7)
    vetPlatCavD.append(platCavD8)
    vetPlatCavD.append(platCavD9)
    vetPlatCavD.append(platCavD10)
    vetPlatCavD.append(platCavD11)
    vetPlatCavD.append(platCavD12)
    vetPlatCavD.append(platCavD13)


    vetPlatCavE =[]
    platCavE1 = Sprite("sprites/caverna-estatico/Cave -Platform1.png")
    platCavE1.set_position(1025, 406)
    platCavE2 = Sprite("sprites/caverna-estatico/Cave -Platform2.png")
    platCavE2.set_position(499, 391)
    platCavE3 = Sprite("sprites/caverna-estatico/Cave -Platform3.png")
    platCavE3.set_position(768, 481)
    platCavE4 = Sprite("sprites/caverna-estatico/Cave -Platform4.png")
    platCavE4.set_position(118, 276)
    
    vetPlatCavE.append(platCavE1)
    vetPlatCavE.append(platCavE2)
    vetPlatCavE.append(platCavE3)
    vetPlatCavE.append(platCavE4)

    
    vetPlatFlorD =[]
    platFlorD1 = Sprite("sprites/floresta-dinamico/plataforma_flo1.png", 1)
    platFlorD1.set_position(0, 358)
    platFlorD2 = Sprite("sprites/floresta-dinamico/plataforma_flo2.png", 1)
    platFlorD2.set_position(1281, 658)
    platFlorD3 = Sprite("sprites/floresta-dinamico/plataforma_flo3.png", 1)
    platFlorD3.set_position(1845, 512)
    platFlorD4 = Sprite("sprites/floresta-dinamico/plataforma_flo4.png", 1)
    platFlorD4.set_position(1349, 304)
    platFlorD5 = Sprite("sprites/floresta-dinamico/plataforma_flo4.png", 1)
    platFlorD5.set_position(1634, 458)
    platFlorD6 = Sprite("sprites/floresta-dinamico/plataforma_flo5.png", 1)
    platFlorD6.set_position(2546, 628)
    platFlorD7 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    platFlorD7.set_position(2855, 493)
    platFlorD8 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    platFlorD8.set_position(3154, 283)
    platFlorD9 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    platFlorD9.set_position(3419, 581)
    platFlorD10 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    platFlorD10.set_position(3676, 380)
    platFlorD11 = Sprite("sprites/floresta-dinamico/plataforma_flo7.png", 1)
    platFlorD11.set_position(3844, 523)

    vetPlatFlorD.append(platFlorD1)
    vetPlatFlorD.append(platFlorD2)
    vetPlatFlorD.append(platFlorD3)
    vetPlatFlorD.append(platFlorD4)
    vetPlatFlorD.append(platFlorD5)
    vetPlatFlorD.append(platFlorD6)
    vetPlatFlorD.append(platFlorD7)
    vetPlatFlorD.append(platFlorD8)
    vetPlatFlorD.append(platFlorD9)
    vetPlatFlorD.append(platFlorD10)
    vetPlatFlorD.append(platFlorD11)


    vetPlatFlorE =[]
    platFlorE1 = Sprite("sprites/floresta-estatico/plataforma1.png")
    platFlorE1.set_position(376, 262)
    platFlorE2 = Sprite("sprites/floresta-estatico/plataforma2.png")
    platFlorE2.set_position(672, 383)
    platFlorE3 = Sprite("sprites/floresta-estatico/plataforma3.png")
    platFlorE3.set_position(757, 325)

    vetPlatFlorE.append(platFlorE1)
    vetPlatFlorE.append(platFlorE2)
    vetPlatFlorE.append(platFlorE3)
    
    vetPlatCasD =[]
    platCasD1 = Sprite("sprites/castelo-dinamico/plataforma1.png")
    platCasD1.set_position(0, 407)
    platCasD2 = Sprite("sprites/castelo-dinamico/plataforma2.png")
    platCasD2.set_position(79, 413)
    platCasD3 = Sprite("sprites/castelo-dinamico/plataforma3.png")
    platCasD3.set_position(550, 340)
    platCasD4 = Sprite("sprites/castelo-dinamico/plataforma3.png")
    platCasD4.set_position(900, 460)
    platCasD5 = Sprite("sprites/castelo-dinamico/plataforma4.png")
    platCasD5.set_position(-3, 0)
    platCasD6 = Sprite("sprites/castelo-dinamico/plataforma5.png")
    platCasD6.set_position(1277, 0)
    platCasD7 = Sprite("sprites/castelo-dinamico/plataforma5.png")
    platCasD7.set_position(2553, 0)
    platCasD8 = Sprite("sprites/castelo-dinamico/plataforma6.png")
    platCasD8.set_position(3820, 0)
    platCasD9 = Sprite("sprites/castelo-dinamico/plataforma8.png")
    platCasD9.set_position(1253,465)
    platCasD10 = Sprite("sprites/castelo-dinamico/plataforma7.png")
    platCasD10.set_position(2530,638)
    platCasD11 = Sprite("sprites/castelo-dinamico/plataforma3.png")
    platCasD11.set_position(1180,310)
    platCasD12 = Sprite("sprites/castelo-dinamico/plataforma3.png")
    platCasD12.set_position(2760,380)
    platCasD13 = Sprite("sprites/castelo-dinamico/plataforma3.png")
    platCasD13.set_position(3160,500)
    platCasD14 = Sprite("sprites/castelo-dinamico/plataforma3.png")
    platCasD14.set_position(3580,300)
    platCasD15 = Sprite("sprites/castelo-dinamico/plataforma9.png")
    platCasD15.set_position(2680,650)
    platCasD16 = Sprite("sprites/castelo-dinamico/plataforma11.png")
    platCasD16.set_position(5030,130)
    platCasD17 = Sprite("sprites/castelo-dinamico/plataforma10.png")
    platCasD17.set_position(3752,610)
    platCasD18 = Sprite("sprites/castelo-dinamico/plataforma3.png")
    platCasD18.set_position(2080,350)
    
    vetPlatCasD.append(platCasD1)
    vetPlatCasD.append(platCasD2)
    vetPlatCasD.append(platCasD3)
    vetPlatCasD.append(platCasD4)
    vetPlatCasD.append(platCasD5)
    vetPlatCasD.append(platCasD6)
    vetPlatCasD.append(platCasD7)
    vetPlatCasD.append(platCasD8)
    vetPlatCasD.append(platCasD9)
    vetPlatCasD.append(platCasD10)
    vetPlatCasD.append(platCasD11)
    vetPlatCasD.append(platCasD12)
    vetPlatCasD.append(platCasD13)
    vetPlatCasD.append(platCasD14)
    vetPlatCasD.append(platCasD15)
    vetPlatCasD.append(platCasD16)
    vetPlatCasD.append(platCasD17)
    vetPlatCasD.append(platCasD18)
    
    vetPlatCasE =[]
    
    platCasE1 = Sprite("sprites/castelo-estatico/plataforma1.png")
    platCasE1.set_position(0,354)
    platCasE2 = Sprite("sprites/castelo-estatico/plataforma2.png")
    platCasE2.set_position(935,298)
    
    vetPlatCasE.append(platCasE1)
    vetPlatCasE.append(platCasE2)
    
    return vetPlatCavD, vetPlatCavE, vetPlatFlorD, vetPlatFlorE, vetPlatCasD, vetPlatCasE

def inCheckpoint(checkpoint,init,posX,posY):
    if(init == False):
        checkpoint.set_position(posX,posY)
        init = True        
    checkpoint.draw()
    return checkpoint,init

def imagens(cenario,janela,teclado):
    while True:
        if cenario == 1:
            mensagem = Sprite("sprites\icones\msg fase 1.jpg")
        if cenario == 2 or cenario == 4:
            mensagem = Sprite("sprites\icones\msg eliminar todos.jpg")
        if cenario == 3:
            mensagem = Sprite("sprites\icones\msg shoot.jpg")
        if cenario == 5:
            mensagem = Sprite("sprites\icones\msg ultima dinamica.jpg")
        if cenario == 6:
            mensagem = Sprite("sprites\icones\msg eliminar chefao.jpg")
        if(teclado.key_pressed("ENTER")):
            break
        mensagem.draw()
        janela.update()
   
def gameFail(teclado,janela):
    while True:
        mensagem = Sprite("sprites\icones\msg you loose.jpg")
        if(teclado.key_pressed("ENTER")):
            break
        mensagem.draw()
        janela.update()

def gamePassed(teclado,janela,cenario):
    while True:
        mensagem = Sprite("sprites\icones\msg venceu fase.jpg")
        if(teclado.key_pressed("ENTER")):
            return cenario+1
        mensagem.draw()
        janela.update()