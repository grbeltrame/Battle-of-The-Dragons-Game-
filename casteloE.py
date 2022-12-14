from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import movimento_dragao

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser
 
def gamePlayCasE(prefDragon,dragaoPrefFlying,vetorDragoesInimigos,delay,flying,vetPlatCasE):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Caverna fase Estática")
    teclado = janela.get_keyboard()

    fundoCasE = GameImage("sprites/icones/bkg castle.png")

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    prefDragon.set_position(150,janela.height - 50 - prefDragon.height)
    prefDragon.set_total_duration(1000)
    dragaoPrefFlying.set_total_duration(1000)

    #Sprite de controle de que modo o dragão está
    dragao = prefDragon

   #Varivael para controle de musica
    musica = 0
    
    #Game loop
    while(True):
        if musica == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("audio/Medieval Themes (WAV)/fases estaticas.wav")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            musica += 1
        fundoCasE.draw()
        dragao,flying = movimento_dragao.movDragao(dragao,janela,teclado,prefDragon,dragaoPrefFlying,flying) 

        delay = movimento_dragao.shootFireball(teclado,dragao,janela,delay)      
        dragao.update()
        dragao.draw()
        janela.update()
