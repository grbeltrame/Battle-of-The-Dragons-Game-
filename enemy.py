from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *
import random
import player
from player import *

tirosSoldados = []
tirosChefao = []
tirosBadDragons = []

def badDragons(dragoesEnemy,soldados):
    for dragaoInimigo in dragoesEnemy:
        dragaoInimigo[0].x = random.randint(500,1200)
        dragaoInimigo[0].y = random.randint(100,580)
        for soldado in soldados:
            while soldado.x == dragaoInimigo[0].x:
                dragaoInimigo[0].x = random.randint(500,1200)
            while soldado.y == dragaoInimigo[0].y:
                dragaoInimigo[0].y = random.randint(100,580)

        dragaoInimigo[0].set_total_duration(1000)
    return dragoesEnemy
        
def desenhaInimigo(dragoesEnemy):
    for dragaoInimigo in dragoesEnemy:
        dragaoInimigo[0].draw()
        dragaoInimigo[0].update()

def criaTiroDragaoInimigo(tirosBadDragons,dragoesEnemy,dragao):
    for badDragon in dragoesEnemy:
        tiro = Sprite("sprites/personagens/fogo-4 1.png") 
        tiro.y = badDragon[0].y + tiro.height 
        tiro.x = badDragon[0].x
        
        if tiro.y < dragao.y:
            directionBadDragon = "baixo"
        if tiro.y > dragao.y:
            directionBadDragon = "cima"
        tirosBadDragons.append(tiro)
    return directionBadDragon

def movTiroDragaoInimigo(tirosBadDragons,velTiro,janela,directionBadDragon):
    for tiro in tirosBadDragons:
        tiro.x -= velTiro*janela.delta_time()
        if (directionBadDragon == "cima"):
            tiro.y -= velTiro/2*janela.delta_time()
        elif (directionBadDragon == "baixo"):
            tiro.y += velTiro/2*janela.delta_time()
        tiro.draw()
        if (tiro.x > janela.width or tiro.x < 0):
            tirosBadDragons.remove(tiro)

def badDragonsHP(dragoesEnemy):
    for tiro in tiros:
        for i,badDragon in enumerate(dragoesEnemy):
            if (tiro.collided_perfect(badDragon[0])): 
                badDragon = (badDragon[0],badDragon[1]-1)
                if(badDragon[1] <= 0):
                    dragoesEnemy.pop(i)
                    # morreu = pygame.mixer.Sound()
                    # morreu.play

def lastBossPos(janela):
    boss = Sprite("sprites/chefões/chefao_2.png",6)
    boss.set_total_duration(1000)
    boss.set_position(janela.width - boss.width,janela.height - boss.height)
    return boss

def lastBossHP(boss,bossHP,janela):
    for tiro in tiros:
        if tiro.collided_perfect(boss):
            bossHP -= 1
            tiros.remove(tiro)
    desenhaBossHP(bossHP,janela)
    return bossHP

def desenhaBossHP(BossHP,janela):
    vida5Coracoes = Sprite("sprites/vidas/vidascor1.png")
    vida5Coracoes.set_position(janela.width - vida5Coracoes.width, 0)
    vida4_5Coracoes = Sprite("sprites/vidas/vidascor2.png")
    vida4_5Coracoes.set_position(janela.width - vida4_5Coracoes.width, 0)
    vida4Coracoes = Sprite("sprites/vidas/vidascor3.png")
    vida4Coracoes.set_position(janela.width - vida4Coracoes.width, 0)
    vida3_5Coracoes = Sprite("sprites/vidas/vidascor4.png")
    vida3_5Coracoes.set_position(janela.width - vida3_5Coracoes.width, 0)
    vida3Coracoes = Sprite("sprites/vidas/vidascor5.png")
    vida3Coracoes.set_position(janela.width - vida3Coracoes.width, 0)
    vida2_5Coracoes = Sprite("sprites/vidas/vidascor6.png")
    vida2_5Coracoes.set_position(janela.width - vida2_5Coracoes.width, 0)
    vida2Coracoes = Sprite("sprites/vidas/vidascor7.png")
    vida2Coracoes.set_position(janela.width - vida2Coracoes.width, 0)
    vida1_5Coracoes = Sprite("sprites/vidas/vidascor8.png")
    vida1_5Coracoes.set_position(janela.width - vida1_5Coracoes.width, 0)
    vida1Coracoes = Sprite("sprites/vidas/vidascor9.png")
    vida1Coracoes.set_position(janela.width - vida1Coracoes.width, 0)
    vida0_5Coracoes = Sprite("sprites/vidas/vidascor10.png")
    vida0_5Coracoes.set_position(janela.width - vida0_5Coracoes.width, 0)

    if BossHP == 10:
        vida5Coracoes.draw()
    if BossHP == 9:
        vida4_5Coracoes.draw()
    if BossHP == 8:
        vida4Coracoes.draw()
    if BossHP == 7:
        vida3_5Coracoes.draw()
    if BossHP == 6:
        vida3Coracoes.draw()
    if BossHP == 5:
        vida2_5Coracoes.draw()
    if BossHP == 4:
        vida2Coracoes.draw()
    if BossHP == 3:
        vida1_5Coracoes.draw()
    if BossHP == 2:
        vida1Coracoes.draw()
    if BossHP == 1:
        vida0_5Coracoes.draw()
    

def criaTiroChefao(tirosChefao,boss,dragao):
    tiro = Sprite("sprites/personagens/fogo-1 unico.png") 
    
    tiro.y = boss.y + tiro.height
    tiro.x = boss.x
    if tiro.y < dragao.y:
        directionBoss = "baixo"
    if tiro.y > dragao.y:
        directionBoss = "cima"
    tirosChefao.append(tiro)
    return directionBoss

def movTiroChefao(tirosChefao,velTiro,janela,directionBoss):
    for tiro in tirosChefao:
        tiro.x -= velTiro*janela.delta_time()
        if (directionBoss == "cima"):
            tiro.y -= velTiro/2*janela.delta_time()
        elif (directionBoss == "baixo"):
            tiro.y += velTiro/2*janela.delta_time()
        tiro.draw()
        if (tiro.x > janela.width or tiro.x < 0):
            tirosChefao.remove(tiro)

def criaSoldados(vetPlataformas):
    soldados = []
    for i in range(len(vetPlataformas)):
        if(i>0):
            soldadoArmadura = Sprite("sprites/inimigos/soldado1.png",9)
            soldadoDragao = Sprite("sprites/inimigos/soldado3.png",4)
            soldadoArmadura.set_position(vetPlataformas[i].x + vetPlataformas[i].width/4 ,vetPlataformas[i].y - soldadoArmadura.height)
            soldadoDragao.set_position(vetPlataformas[i].x +  vetPlataformas[i].width/2 +20,vetPlataformas[i].y - soldadoDragao.height)
            soldadoArmadura.set_total_duration(1000)
            soldadoDragao.set_total_duration(1000)
            soldados.append(soldadoArmadura)
            soldados.append(soldadoDragao)
    return soldados 

def desenhaSoldados(soldados):
    for soldado in soldados:
        soldado.update()
        soldado.draw()
        
def movSoldados(soldados,velDragao,teclado,janela):
    for soldado in soldados:
        if(teclado.key_pressed("LEFT")):
            soldado.x += velDragao*janela.delta_time()
        elif(teclado.key_pressed("RIGHT")):
            soldado.x -= velDragao*janela.delta_time()
    return soldados

def criaTiroSoldados(tirosSoldados,soldado,dragao):
    tiro = Sprite("sprites/inimigos/ponta_arma.png") 
    tiro.y = soldado.y + tiro.height 
    tiro.x = soldado.x
    if tiro.y < dragao.y:
        direction = "baixo"
    if tiro.y > dragao.y:
        direction = "cima"
    tirosSoldados.append(tiro)
    return direction

def movTiroSoldados(tirosSoldados,velTiro,janela,direction):
    for tiro in tirosSoldados:
        tiro.x -= velTiro*janela.delta_time()
        if (direction == "cima"):
            tiro.y -= velTiro/2*janela.delta_time()
        elif (direction == "baixo"):
            tiro.y += velTiro/2*janela.delta_time()
        tiro.draw()
        if (tiro.x > janela.width or tiro.x < 0):
            tirosSoldados.remove(tiro)
