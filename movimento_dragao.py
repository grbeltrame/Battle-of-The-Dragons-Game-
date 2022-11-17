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

def shootFireball(teclado,dragao,janela,delay):
    if(teclado.key_pressed("F") and delay == 0 ):
        criaTiro(tiros,dragao)
        delay = 50    
    if(len(tiros)>0):        
        movTiro(tiros,velTiro,janela)
    if(delay>0):
        delay -= 1
    return delay

def movDragao(atual,janela,teclado,dragaoPrefStand,dragaoPrefFlying,flying): 
    dragao = atual
    velDragao = 300
    if(teclado.key_pressed("X")):
        dragao = trocaDragao(dragao,dragaoPrefFlying)
        flying = True
    if(teclado.key_pressed("left_shift")) :
        dragao = trocaDragao(dragao,dragaoPrefStand)
        flying = False
    if(flying == True):
        if(teclado.key_pressed("UP")):
            dragao.y -= velDragao*janela.delta_time() 
        if(teclado.key_pressed("DOWN")):
            dragao.y += velDragao*janela.delta_time() 
    # if(teclado.key_pressed("SPACE")):
    #     inserir forma dele pular
    if(teclado.key_pressed("RIGHT")):
        dragao.x += velDragao*janela.delta_time()  
    if(teclado.key_pressed("LEFT")):
        dragao.x -= velDragao*janela.delta_time() 
    return dragao,flying,velDragao

def movDragaoDinamico(atual,janela,teclado,dragaoPrefStand,dragaoPrefFlying,flying): 
    dragao = atual
    velDragao = 300
    if(teclado.key_pressed("X")):
        dragao = trocaDragao(dragao,dragaoPrefFlying)
        flying = True
    if(teclado.key_pressed("left_shift")) :
        dragao = trocaDragao(dragao,dragaoPrefStand)
        flying = False
    if(flying == True):
        if(teclado.key_pressed("UP")):
            dragao.y -= velDragao*janela.delta_time() 
        if(teclado.key_pressed("DOWN")):
            dragao.y += velDragao*janela.delta_time()
    # else: 
    # if(teclado.key_pressed("SPACE")):
    #     inserir forma dele pular
    return dragao,flying,velDragao

def colisaoDragao(vetPlataformas,dragao,velDragao,janela):
    for plataforma in vetPlataformas:
        if dragao.collided_perfect(plataforma):
            if(dragao.x + dragao.width >= plataforma.x):
                dragao.x -= velDragao*janela.delta_time()
            elif(dragao.x  <= plataforma.x + plataforma.width):
                dragao.x += velDragao*janela.delta_time()
            if(dragao.y + dragao.height >= plataforma.y):
                dragao.y -= velDragao*janela.delta_time()
            elif(dragao.y  <= plataforma.y + plataforma.height):
                dragao.y += velDragao*janela.delta_time()
    return velDragao,dragao

def colisaoDragaoDinamico(vetPlataformas,dragao,velDragao,janela,background1,background2):
    for plataforma in vetPlataformas:
        if dragao.collided_perfect(plataforma):
            if(dragao.x + dragao.width >= plataforma.x):
                background1.x -= velDragao*janela.delta_time()
                background2.x -= velDragao*janela.delta_time()
            elif(dragao.x  <= plataforma.x + plataforma.width):
                background1.x += velDragao*janela.delta_time()
                background2.x += velDragao*janela.delta_time()
            if(dragao.y + dragao.height >= plataforma.y):
                dragao.y -= velDragao*janela.delta_time()
            elif(dragao.y  <= plataforma.y + plataforma.height):
                dragao.y += velDragao*janela.delta_time()
    return velDragao,dragao,background1,background2
    
# def lessHP(dragonHP,enemyTiros,dragao,dano):
#     for tiro in enemyTiros:
        # if(tiro.collided(dragao)):
        #     dragonHP -= dano
        # alterar barra de hp
        # return dragonHP



