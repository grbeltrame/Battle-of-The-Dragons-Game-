from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *

# def badDragons():
#     criar e movimentar os dragoes pelo mapa 


# def lastBossMov():
#     movimentação do ultimo chefão

# def lastBossHP():
#     controla vida do ultimo chefão

def criaSoldados(vetPlataformas):
    soldados = []
    for i in range(len(vetPlataformas)):
        if(i>0):
            soldadoArmadura = Sprite("sprites/inimigos/soldado1.png",9)
            soldadoDragao = Sprite("sprites/inimigos/soldado3.png",4)
            soldadoArmadura.set_position(vetPlataformas[i].x + vetPlataformas[i].width/4 ,vetPlataformas[i].y - soldadoArmadura.height)
            soldadoDragao.set_position(vetPlataformas[i].x +  vetPlataformas[i].width/2 +20,vetPlataformas[i].y - soldadoDragao.height)
            soldadoArmadura.set_total_duration(1000)
            soldadoDragao.set_total_duration(1000)
            soldados.append(soldadoArmadura)
            soldados.append(soldadoDragao)
    return soldados 

def desenhaSoldados(soldados):
    for soldado in soldados:
        soldado.update()
        soldado.draw()

def movSoldados(soldados,velDragao,teclado,janela):
    for soldado in soldados:
        if(teclado.key_pressed("LEFT")):
            soldado.x += velDragao*janela.delta_time()
        elif(teclado.key_pressed("RIGHT")):
            soldado.x -= velDragao*janela.delta_time()
    return soldados