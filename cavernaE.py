from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser
global dragaoPrefStand
global dragaoPrefFlying
def gamePlayCavE(prefDragon,dragaoPrefFlying):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Caverna fase Estática")
    teclado = janela.get_keyboard()

    fundoCavE = GameImage("sprites/caverna-estatico/caverna-estatica.jpg")

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    dragaoPrefStand = prefDragon
    dragaoPrefStand.set_position(150,janela.height - 50 - dragaoPrefStand.height)
    dragaoPrefStand.set_total_duration(1000)
    dragaoPrefFlying.set_total_duration(1000)

    #Sprite de controle de que modo o dragão está
    dragao = dragaoPrefStand

    #Game loop
    while(True):
        fundoCavE.draw()
        if(teclado.key_pressed("SPACE")):
            dragao = movimento_dragao.trocaDragao(dragao,dragaoPrefFlying)
        if(teclado.key_pressed("left_shift")) :
            dragao = movimento_dragao.trocaDragao(dragao,dragaoPrefStand)       
        dragao.update()
        dragao.draw()
        janela.update()