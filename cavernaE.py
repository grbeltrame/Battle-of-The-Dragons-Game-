from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser

def gamePlayCavE(prefDragon,dragaoPrefFlying,delay,flying):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Caverna fase Estática")
    teclado = janela.get_keyboard()

    fundoCavE = GameImage("sprites/caverna-estatico/caverna-estatica.jpg")
    
    #Plataformas interativas
    platform1 = Sprite("sprites/caverna-estatico/Cave -Platform1.png")
    platform1.set_position(1025, 406)
    platform2 = Sprite("sprites/caverna-estatico/Cave -Platform2.png")
    platform2.set_position(499, 391)
    platform3 = Sprite("sprites/caverna-estatico/Cave -Platform3.png")
    platform3.set_position(768, 481)
    platform4 = Sprite("sprites/caverna-estatico/Cave -Platform4.png")
    platform4.set_position(118, 276)

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    prefDragon.set_position(150,janela.height - 50 - prefDragon.height)
    prefDragon.set_total_duration(1000)
    dragaoPrefFlying.set_total_duration(1000)

    #Sprite de controle de que modo o dragão está
    dragao = prefDragon

    #Game loop
    while(True):
        fundoCavE.draw()
        dragao,flying = movimento_dragao.movDragao(dragao,janela,teclado,prefDragon,dragaoPrefFlying,flying) 
        delay = movimento_dragao.shootFireball(teclado,dragao,janela,delay) 
        platform1.draw()
        platform2.draw()
        platform3.draw()
        platform4.draw()     
        dragao.update()
        dragao.draw()
        janela.update()
