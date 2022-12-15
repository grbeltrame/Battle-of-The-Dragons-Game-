from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import*

def scrolling(backg_1, velocidade, janela,teclado):
    if teclado.key_pressed("RIGHT"):
        backg_1.x -= velocidade * janela.delta_time()     
    elif teclado.key_pressed("LEFT"):
        backg_1.x += velocidade * janela.delta_time()
def movimentoplataforma(plataforma,velocidade,janela,teclado):
    if teclado.key_pressed("RIGHT"):
        plataforma.x -= velocidade * janela.delta_time()
    elif teclado.key_pressed("LEFT"):
        plataforma.x += velocidade * janela.delta_time()