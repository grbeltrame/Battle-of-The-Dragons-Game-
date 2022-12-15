from stringprep import map_table_b2
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 

global velTiro
global delay
global tiros 
velTiro = 600
delay = 0
tiros = []

def criaTiro(tiros,dragao):
    tiro = Sprite("sprites/personagens/fogo-2.png",3) 
    tiro.set_total_duration(1000)
    tiro.y = dragao.y + tiro.height 
    tiro.x = dragao.x*1.5
    tiros.append(tiro)

def movTiro(tiros,velTiro,janela):
    for tiro in tiros:
        tiro.x += velTiro*janela.delta_time()
        tiro.draw()
        if(tiro.x > janela.width):
            tiros.remove(tiro)

def shootFireball(teclado,dragao,janela,delay,soldados):
    if(teclado.key_pressed("Q") and delay == 0 ):
        criaTiro(tiros,dragao)
        delay = 50    
    if(len(tiros)>0):        
        movTiro(tiros,velTiro,janela)
        colisaoTiro(soldados,tiros)
    if(delay>0):
        delay -= 1
    return delay

def colisaoTiro(soldados,tiros):
    for tiro in tiros:
        for i,soldado in enumerate(soldados):    
            if(tiro.collided(soldado)):
                soldados.pop(i)
                # tomou = pygame.mixer.Sound("")
                # tomou.play()
                tiros.remove(tiro)

def movDragao(dragao,janela,teclado): 
    velDragao = 300
    if(teclado.key_pressed("UP")):
        dragao.y -= velDragao*janela.delta_time() 
    elif(teclado.key_pressed("DOWN")):
        dragao.y += velDragao*janela.delta_time() 
    if(teclado.key_pressed("RIGHT")):
        dragao.x += velDragao*janela.delta_time()  
    elif(teclado.key_pressed("LEFT")):
        dragao.x -= velDragao*janela.delta_time() 
    return dragao,velDragao

def movDragaoDinamico(dragao,janela,teclado): 
    velDragao = 300
    if(teclado.key_pressed("UP")):
        dragao.y -= velDragao*janela.delta_time() 
    elif(teclado.key_pressed("DOWN")):
        dragao.y += velDragao*janela.delta_time() 
    return dragao,velDragao
    
def lessHP(dragonHP,enemyTiros,dragao,dano):
    for tiro in enemyTiros:
        if(tiro.collided_perfect(dragao)):
            dragonHP -= dano
            tomei = pygame.mixer.Sound("audio/Medieval Themes (WAV)/tiro do soldado no player.wav")
            tomei.play()
            enemyTiros.remove(tiro)
    return dragonHP
        
def desenhaHP(dragaoHP, modGame):
    vida5Coracoes = Sprite("sprites/vidas/vidascor1.png")
    vida4_5Coracoes = Sprite("sprites/vidas/vidascor2.png")
    vida4Coracoes = Sprite("sprites/vidas/vidascor3.png")
    vida3_5Coracoes = Sprite("sprites/vidas/vidascor4.png")
    vida3Coracoes = Sprite("sprites/vidas/vidascor5.png")
    vida2_5Coracoes = Sprite("sprites/vidas/vidascor6.png")
    vida2Coracoes = Sprite("sprites/vidas/vidascor7.png")
    vida1_5Coracoes = Sprite("sprites/vidas/vidascor8.png")
    vida1Coracoes = Sprite("sprites/vidas/vidascor9.png")
    vida0_5Coracoes = Sprite("sprites/vidas/vidascor10.png")

    if modGame==1:
        if dragaoHP == 10:
            vida5Coracoes.draw()
        if dragaoHP == 9:
            vida4_5Coracoes.draw()
        if dragaoHP == 8:
            vida4Coracoes.draw()
        if dragaoHP == 7:
            vida3_5Coracoes.draw()
        if dragaoHP == 6:
            vida3Coracoes.draw()
        if dragaoHP == 5:
            vida2_5Coracoes.draw()
        if dragaoHP == 4:
            vida2Coracoes.draw()
        if dragaoHP == 3:
            vida1_5Coracoes.draw()
        if dragaoHP == 2:
            vida1Coracoes.draw()
        if dragaoHP == 1:
            vida0_5Coracoes.draw()
    if modGame==2:
        if dragaoHP == 10:
            vida5Coracoes.draw()
        if dragaoHP == 8:
            vida4Coracoes.draw()
        if dragaoHP == 6:
            vida3Coracoes.draw()
        if dragaoHP == 4:
            vida2Coracoes.draw()
        if dragaoHP == 2:
            vida1Coracoes.draw()
    if modGame==4:
        if dragaoHP == 10:
            vida5Coracoes.draw()
        if dragaoHP == 6:
            vida3Coracoes.draw()
        if dragaoHP == 2:
            vida1Coracoes.draw()


def defense(tirosEnemy,dragao,teclado):
    if (teclado.key_pressed("E")):
        rugido = pygame.mixer.Sound("audio/Medieval Themes (WAV)/rugido do player.wav")
        rugido.play()
        for tiro in tirosEnemy:
            if tiro.x >= dragao.x + 100 and (tiro.y <= dragao.y - 100 or tiro.y  >= dragao.y + 100) :
                tirosEnemy.remove(tiro)

