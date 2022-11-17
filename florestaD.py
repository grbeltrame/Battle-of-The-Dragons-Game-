from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao
import background_dinamico

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser

def gamePlayFlorD(prefDragon,dragaoPrefFlying,vetorDragoesInimigos,delay,flying,vetPlatFlorD):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Caverna fase Estática")
    teclado = janela.get_keyboard()

    fundoCasD_1 = GameImage("sprites/floresta-dinamico/floresta_dinamico.png")
    fundoCasD_2 = GameImage("sprites/floresta-dinamico/floresta_dinamico.png")
    
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
        for i in range(11):
            background_dinamico.movimentoplataforma(vetPlatFlorD[i], speed,janela,teclado)
    
        dragao,flying = movimento_dragao.movDragao(dragao,janela,teclado,prefDragon,dragaoPrefFlying,flying) 

        delay = movimento_dragao.shootFireball(teclado,dragao,janela,delay)      
        dragao.update()
        dragao.draw()
        janela.update()
