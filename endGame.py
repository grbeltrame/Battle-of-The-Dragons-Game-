from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import menu

def finished(prefDragon):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Você venceu")
    teclado = janela.get_keyboard()

    fundoFinished = GameImage("sprites\icones\img final.jpg")

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    prefDragon.set_position(janela.width/2 - prefDragon.width/2,janela.height/2)
    prefDragon.set_total_duration(1000)

    #Varivael para controle de musica
    musica = 0

    #Game loop
    while(True):
        if musica == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("audio/Medieval Themes (WAV)/Game-Of-Thrones-Funk-251.wav")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            musica += 1
        fundoFinished.draw()
        if(teclado.key_pressed("ESC")):
            menu.gameMenu()
        prefDragon.update()
        prefDragon.draw()
        janela.update()