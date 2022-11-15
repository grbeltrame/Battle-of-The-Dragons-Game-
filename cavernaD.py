from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao
import background_dinamico

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser

def gamePlayCavD(prefDragon,dragaoPrefFlying,delay,flying):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Caverna fase Estática")
    teclado = janela.get_keyboard()

    fundoCavD_1 = GameImage("sprites/caverna-dinamico/fundocavernad.jpg")
    fundoCavD_2 = GameImage("sprites/caverna-dinamico/fundocavernad.jpg")
    plataforma1= Sprite("sprites/caverna-dinamico/plataforma_cav2.png",1)
    plataforma2= Sprite("sprites/caverna-dinamico/plataforma_cav3.png",1)
    plataforma3= Sprite("sprites/caverna-dinamico/plataforma_cav4.png",1)
    plataforma4= Sprite("sprites/caverna-dinamico/plataforma_cav1.png",1)
    plataforma5= Sprite("sprites/caverna-dinamico/plataforma_cav5.png",1)
    plataforma6= Sprite("sprites/caverna-dinamico/plataforma_cav3.png",1)
    plataforma7= Sprite("sprites/caverna-dinamico/plataforma_cav4.png",1)
    plataforma8= Sprite("sprites/caverna-dinamico/plataforma_cav6.png",1)
    plataforma9= Sprite("sprites/caverna-dinamico/plataforma_cav5.png",1)
    plataforma10= Sprite("sprites/caverna-dinamico/plataforma_cav5.png",1)
    plataforma11= Sprite("sprites/caverna-dinamico/plataforma_cav3.png",1)
    plataforma12= Sprite("sprites/caverna-dinamico/plataforma_cav4.png",1)
    plataforma13= Sprite("sprites/caverna-dinamico/plataforma_cav7.png",1)

    

    plataforma1.set_position(0, 568)
    plataforma2.set_position(342, 325)
    plataforma3.set_position(710, 478)
    plataforma4.set_position(1030, 325)
    plataforma5.set_position(1509, 574)
    plataforma6.set_position(1847, 416)
    plataforma7.set_position(2314, 298)
    plataforma8.set_position(2002, 528)
    plataforma9.set_position(2395, 574)
    plataforma10.set_position(2902, 571)
    plataforma11.set_position(2813, 300)
    plataforma12.set_position(3208, 441)
    plataforma13.set_position(3468, 449)

    speed = 300

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    prefDragon.set_position(150,janela.height - 50 - prefDragon.height)
    prefDragon.set_total_duration(1000)
    dragaoPrefFlying.set_total_duration(1000)

    #Sprite de controle de que modo o dragão está
    dragao = prefDragon

    #Game loop
    while(True):
        background_dinamico.scrolling(fundoCavD_1,fundoCavD_2,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma1,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma2,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma3,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma4,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma5,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma6,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma7,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma9,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma8,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma10,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma11,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma12,speed,janela,teclado)
        background_dinamico.movimentoplataforma(plataforma13,speed,janela,teclado)

        dragao,flying = movimento_dragao.movDragao(dragao,janela,teclado,prefDragon,dragaoPrefFlying,flying) 
  
        delay = movimento_dragao.shootFireball(teclado,dragao,janela,delay)     
        dragao.update()
        dragao.draw()
        janela.update()
