from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao

janela = Window(1280,720)
janela.set_title("Floresta fase Estática")
teclado = janela.get_keyboard()

fundoFloE = GameImage("sprites/floresta-estatico/floresta_estatico.png")
plataforma1 = Sprite("sprites/floresta-estatico/plataforma1.png")
plataforma2 = Sprite("sprites/floresta-estatico/plataforma2.png")
plataforma3 = Sprite("sprites/floresta-estatico/plataforma3.png")

plataforma1.set_position(376, 262)
plataforma2.set_position(672, 383)
plataforma3.set_position(757, 325)
while True:
    fundoFloE.draw()
    plataforma1.draw()
    plataforma2.draw()
    plataforma3.draw()
    janela.update()
