from stringprep import map_table_b2
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 

def trocaDragao(atual,novo):
    dragao = novo
    dragao.x = atual.x
    dragao.y = atual.y
    return dragao

def movDragao(atual,janela,teclado):
    dragao = atual
    velDragao = 300
    # if(teclado.key_pressed("SPACE")):
    #     dragao = movimento_dragao.trocaDragao(dragao,dragaoFlying)
    # if(teclado.key_pressed("left_shift")) :
    #     dragao = movimento_dragao.trocaDragao(dragao,dragaoStand)
    if(teclado.key_pressed("RIGHT")):
        dragao.x += velDragao*janela.delta_time()  
    if(teclado.key_pressed("LEFT")):
        dragao.x -= velDragao*janela.delta_time() 
    if(teclado.key_pressed("UP")):
        dragao.y -= velDragao*janela.delta_time() 
    if(teclado.key_pressed("DOWN")):
        dragao.y += velDragao*janela.delta_time() 
    return dragao

def criaTiro(tiros,dragao):
    tiro = Sprite("sprites/dificuldade.png") #mudar para foguinhos depois que tiver o sprite 
    tiro.y = dragao.y - tiro.height/2
    tiro.x = dragao.x
    tiros.append(tiro)

def movTiro(tiros,velTiro,janela):
    for tiro in tiros:
        tiro.y -= velTiro*janela.delta_time()
        tiro.draw()
        if(tiro.y < 0 - tiro.height):
            tiros.remove(tiro)

# def colisaoDragao(plataforma,soldado,dragao):
#     estudar as colisoes de acordo com as plataformas, soldados e tiros de outros dragoes:

# def badDragons():
#     criar e movimentar os dragoes pelo mapa 

# def movSoldados():
#     movimento dos soldados e dos tiros dos soldados contra o dragao, preferencialmente por IA 
