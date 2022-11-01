from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser
 

#Define dimensão da janela e teclado
janela = Window(1280,720)
janela.set_title("Caverna fase Estática")
teclado = janela.get_keyboard()

fundoCavE = GameImage("sprites/caverna-estatico/caverna-estatica.jpg")

#Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
dragaoStand = Sprite("sprites/personagens/azul-1.png",4)
dragaoFlying = Sprite("sprites/personagens/azul-2.png",4)
dragaoStand.set_position(150,janela.height - 50 - dragaoStand.height)
dragaoStand.set_total_duration(1000)
dragaoFlying.set_total_duration(1000)

#Sprite de controle de que modo o dragão está
dragao = dragaoStand

#Game loop
while(True):
    fundoCavE.draw()
    if(teclado.key_pressed("SPACE")):
        dragao = movimento_dragao.trocaDragao(dragao,dragaoFlying)
    if(teclado.key_pressed("left_shift")) :
        dragao = movimento_dragao.trocaDragao(dragao,dragaoStand)       
    dragao.update()
    dragao.draw()
    janela.update()