from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 


def finished(prefDragon):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Você venceu")
    teclado = janela.get_keyboard()

    fundoFinished = GameImage("sprites\icones\img final.jpg")

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    prefDragon.set_position(janela.width/2 - prefDragon.width/2,janela.height/2)
    prefDragon.set_total_duration(1000)


    #Game loop
    while(True):
        fundoFinished.draw()
        if(teclado.key_pressed("ESC")):
            import menu
            menu.gameMenu()
        prefDragon.update()
        prefDragon.draw()
        janela.update()