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

def trocaDragao(atual,novo):
    dragao = novo
    dragao.x = atual.x
    dragao.y = atual.y
    return dragao

def criaTiro(tiros,dragao):
    tiro = Sprite("sprites/personagens/fogo-2.png",4) 
    tiro.set_total_duration(1000)
    tiro.y = dragao.y - tiro.height/2
    tiro.x = dragao.x*1.5
    tiros.append(tiro)

def movTiro(tiros,velTiro,janela):
    for tiro in tiros:
        tiro.x += velTiro*janela.delta_time()
        tiro.y -= velTiro*janela.delta_time()
        tiro.draw()
        if(tiro.y < 0 - tiro.height):
            tiros.remove(tiro)
def shootFireball(teclado,dragao,janela):
    delay = 20
    criaTiro(tiros,dragao)     
    if(len(tiros)>0):        
        movTiro(tiros,velTiro,janela)
    if(delay>0):
        delay -= 1

def movDragao(atual,janela,teclado,dragaoPrefStand,dragaoPrefFlying): 
    dragao = atual
    velDragao = 300
    if(teclado.key_pressed("X")):
        dragao = trocaDragao(dragao,dragaoPrefFlying)
    if(teclado.key_pressed("left_shift")) :
        dragao = trocaDragao(dragao,dragaoPrefStand)
    # if(teclado.key_pressed("SPACE")):
    #     inserir forma dele pular
    if(teclado.key_pressed("RIGHT")):
        dragao.x += velDragao*janela.delta_time()  
    if(teclado.key_pressed("LEFT")):
        dragao.x -= velDragao*janela.delta_time() 
    if(teclado.key_pressed("UP")):
        dragao.y -= velDragao*janela.delta_time() 
    if(teclado.key_pressed("DOWN")):
        dragao.y += velDragao*janela.delta_time() 
    if(teclado.key_pressed("F") ):
        shootFireball(teclado,dragao,janela)
    return dragao



# def colisaoDragao(plataforma,soldado,dragao):
#     estudar as colisoes de acordo com as plataformas, soldados e tiros de outros dragoes

# def lessHP(dragonHP,enemyTiros,dragao,dano,modGame):
#     for tiro in enemyTiros:
        # if(tiro.collided(dragao)):
        #     dragonHP -= dano*modGame
        # alterar barra de hp
        # return dragonHP


# def gameOver(dragonHP):
#     if(dragonHP == 0):
        # mensagem e som dizendo que o jogador perdeu


