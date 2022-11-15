from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao
import background_dinamico

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser

def gamePlayFlorD(prefDragon,dragaoPrefFlying,vetorDragoesInimigos,delay,flying):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Caverna fase Estática")
    teclado = janela.get_keyboard()

    fundoCasD_1 = GameImage("sprites/floresta-dinamico/floresta_dinamico.png")
    fundoCasD_2 = GameImage("sprites/floresta-dinamico/floresta_dinamico.png")
    plataforma_1 = Sprite("sprites/floresta-dinamico/plataforma_flo1.png", 1)
    plataforma_2 = Sprite("sprites/floresta-dinamico/plataforma_flo2.png", 1)
    plataforma_3 = Sprite("sprites/floresta-dinamico/plataforma_flo3.png", 1)
    plataforma_4 = Sprite("sprites/floresta-dinamico/plataforma_flo4.png", 1)
    plataforma_5 = Sprite("sprites/floresta-dinamico/plataforma_flo4.png", 1)
    plataforma_6 = Sprite("sprites/floresta-dinamico/plataforma_flo5.png", 1)
    plataforma_7 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    plataforma_8 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    plataforma_9 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    plataforma_10 = Sprite("sprites/floresta-dinamico/plataforma_flo6.png", 1)
    plataforma_11 = Sprite("sprites/floresta-dinamico/plataforma_flo7.png", 1)

    plataforma_1.set_position(0, 358)
    plataforma_2.set_position(1281, 658)
    plataforma_3.set_position(1845, 512)
    plataforma_4.set_position(1349, 304)
    plataforma_5.set_position(1634, 458)
    plataforma_6.set_position(2546, 628)
    plataforma_7.set_position(2855, 493)
    plataforma_8.set_position(3154, 283)
    plataforma_9.set_position(3419, 581)
    plataforma_10.set_position(3676, 380)
    plataforma_11.set_position(3844, 523)
    speed = 300

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    prefDragon.set_position(150,janela.height - 50 - prefDragon.height)
    prefDragon.set_total_duration(1000)
    dragaoPrefFlying.set_total_duration(1000)

    #Sprite de controle de que modo o dragão está
    dragao = prefDragon

    #Game loop
    while(True):
        background_dinamico.scrolling(fundoCasD_1,fundoCasD_2,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_1, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_2, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_3, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_4, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_5, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_6, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_7, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_8, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_9, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_10, speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma_11, speed,janela,teclado)
        dragao,flying = movimento_dragao.movDragao(dragao,janela,teclado,prefDragon,dragaoPrefFlying,flying) 
        delay = movimento_dragao.shootFireball(teclado,dragao,janela,delay)      
        dragao.update()
        dragao.draw()
        janela.update()
