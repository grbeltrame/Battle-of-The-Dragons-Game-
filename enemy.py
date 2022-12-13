from PPlay.gameimage import* 
from PPlay.window import *
from PPlay.sprite import *

# tirosSoldados = []

# def badDragons():
#     criar e movimentar os dragoes pelo mapa 


# def lastBossPos(janela):
#     boss = Sprite("sprites/chefões/chefao_2.png",6)
#     boss.set_total_duration(1000)
#     boss.x = janela.width - boss.width 
#     boss.y = janela.height - boss.height
#     return boss


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

# def criaTiroSoldados(tirosSoldados,soldado):
#     tiro = Sprite("sprites/inimigos/ponta_arma.png") 
#     tiro.y = soldado.y + tiro.height 
#     tiro.x = soldado.x*1.5
#     tirosSoldados.append(tiro)

# def movTiroSoldados(tirosSoldados,velTiro,janela):
#     for tiro in tirosSoldados:
#         tiro.x -= velTiro*janela.delta_time()
#         tiro.draw()
#         if(tiro.x > janela.width):
#             tirosSoldados.remove(tiro)

# def shootArma(teclado,dragao,janela,delay,soldados):
    # IA para atirar no dragao
