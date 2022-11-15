from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *
import cavernaD
import cavernaE
import florestaD
import florestaE
import casteloD
import casteloE
import endGame

def game(prefDragon,dragaoPrefFlying,cenario,vetorDragoesInimigos):
    delay = 50 
    flying = False
    #Chamando as fases
    if(cenario == 1):
        cavernaD.gamePlayCavD(prefDragon,dragaoPrefFlying,delay,flying)
    if(cenario == 2):
        cavernaE.gamePlayCavE(prefDragon,dragaoPrefFlying,delay,flying)
    if(cenario == 3):
        florestaD.gamePlayFlorD(prefDragon,dragaoPrefFlying,vetorDragoesInimigos,delay,flying)
    if(cenario == 4):
        florestaE.gamePlayFlorE(prefDragon,dragaoPrefFlying,vetorDragoesInimigos,delay,flying)
    if(cenario == 5):
        casteloD.gamePlayCasD(prefDragon,dragaoPrefFlying,vetorDragoesInimigos,delay,flying)
    if(cenario == 6):
        casteloE.gamePlayCasE(prefDragon,dragaoPrefFlying,vetorDragoesInimigos,delay,flying)
    if(cenario == 7):
        endGame.finished(prefDragon,dragaoPrefFlying)

    

