from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import*
import movimento_dragao
import background_dinamico

global dragaoPrefStand
global dragaoPrefFlying

def gamePlayCasD(prefDragon,dragaoPrefFlying):
    janela = Window(1280,720)
    janela.set_title("Castelo Fase Dinamica")
    teclado = janela.get_keyboard()
    fundoCasD_1 = GameImage("sprites/castelo-dinamico/background2.png")
    fundoCasD_2 = GameImage("sprites/castelo-dinamico/background2.png")
    speed = 300
    dragaoPrefStand = prefDragon
    dragaoPrefStand.set_position(150,janela.height - 50 - dragaoPrefStand.height)
    dragaoPrefStand.set_total_duration(1000)
    dragaoPrefFlying.set_total_duration(1000)
    dragao = dragaoPrefStand
    while True:
        background_dinamico.scrolling(fundoCasD_1,fundoCasD_2,speed,janela,teclado)
        dragao = movimento_dragao.movDragao(dragao,janela,teclado,dragaoPrefStand,dragaoPrefFlying)
        dragao.update()
        dragao.draw()
        janela.update()
