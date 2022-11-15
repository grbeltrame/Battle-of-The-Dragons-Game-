from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import*

def scrolling(backg_direita, backg_esquerda, velocidade, janela,teclado):
    if teclado.key_pressed("RIGHT"):
        backg_direita.x -= velocidade * janela.delta_time()
        backg_esquerda.x -= velocidade * janela.delta_time()
        if backg_esquerda.x <= 0:
            backg_direita.x = 0
            backg_esquerda.x = backg_esquerda.width
    if teclado.key_pressed("LEFT"):
        backg_direita.x += velocidade * janela.delta_time()
        backg_esquerda.x += velocidade * janela.delta_time()
        if backg_direita.x >= 0:
            backg_esquerda.x = 0
            backg_direita.x = backg_direita.width
    backg_direita.draw()
    backg_esquerda.draw()
def movimentoplataforma(plataforma,velocidade,janela,teclado):
    if teclado.key_pressed("RIGHT"):
        plataforma.x -= velocidade * janela.delta_time()
    if teclado.key_pressed("LEFT"):
        plataforma.x += velocidade * janela.delta_time()
    plataforma.draw()