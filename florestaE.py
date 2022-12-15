from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import player
import background_dinamico
import enemy
import game
import menu

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser

def gamePlayFlorE(dragao,vetorDragoesInimigos,delay,vetPlatFlorE,DragaoHP,danoEnemy,modGame):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Last Fase")
    teclado = janela.get_keyboard()

    fundoFlorE = GameImage("sprites/icones/bkg forest.png")
   

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    dragao.set_position(150,janela.height - 50 - dragao.height)
    dragao.set_total_duration(1000)
    dragaoHitBox = dragao
    
    #Sprite dos inimigos
    soldados = enemy.criaSoldados(vetPlatFlorE)
    tirosSoldados = []
    velTiro = 300
    delayInim = 120
    badDragao = enemy.badDragons(vetorDragoesInimigos,soldados)
    tirosBadDragoes = []
    delayInimDrag = 120
    
    #Varivael para controle de musica
    musica = 0
    
    game.imagens(4,janela,teclado)
    
    #Direção do tiro
    direction = ""
    directionBadDrag = ""
    
    #Game loop
    while(True):
        fundoFlorE.draw()
        if musica == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("audio/Medieval Themes (WAV)/fases estaticas.wav")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            musica += 1
        
        for i in range(3):
            vetPlatFlorE[i].draw()
            
        dragao,velDragao = player.movDragao(dragao,janela,teclado)
        delay = player.shootFireball(teclado,dragao,janela,delay,soldados)
        dragaoHitBox.set_position(dragao.x,dragao.y)
        if len(tirosSoldados)==0 and delayInim==0:
            for i,soldado in enumerate(soldados):
                if dragaoHitBox.collided_perfect(soldado):
                    DragaoHP-=1
                direction = enemy.criaTiroSoldados(tirosSoldados,soldado,dragao) 

        if len(tirosSoldados)>0:
            enemy.movTiroSoldados(tirosSoldados,velTiro,janela,direction)
            player.defense(tirosSoldados,dragao,teclado)
        if delayInim>0:
            delayInim-=1
        enemy.desenhaSoldados(soldados)

        # BadDragoes
        if len(tirosBadDragoes)==0 and delayInimDrag==0:
            for i,badDragao in enumerate(vetorDragoesInimigos):
                if dragaoHitBox.collided_perfect(badDragao[0]):
                    DragaoHP-=1
            directionBadDrag = enemy.criaTiroDragaoInimigo(tirosBadDragoes,vetorDragoesInimigos,dragao)
        if len(tirosBadDragoes)>0:
            enemy.movTiroDragaoInimigo(tirosBadDragoes,velTiro,janela,directionBadDrag)
            player.defense(tirosBadDragoes,dragao,teclado)
            
        if delayInimDrag>0:
            delayInimDrag-=1
        enemy.badDragonsHP(vetorDragoesInimigos)
        enemy.desenhaInimigo(vetorDragoesInimigos)
        
        if len(soldados)==0:
            passou = pygame.mixer.Sound("audio\Medieval Themes (WAV)\checkpoint alcançado.wav")
            passou.play()
            return game.gamePassed(teclado,janela,4)
        if (DragaoHP<=0):
            perdeu = pygame.mixer.Sound("audio/Medieval Themes (WAV)/perdeu.wav")
            perdeu.play()
            game.gameFail(teclado,janela)
            menu.gameMenu()
            
        DragaoHP = player.lessHP(DragaoHP,tirosSoldados,dragaoHitBox,danoEnemy)
        DragaoHP = player.lessHP(DragaoHP,tirosBadDragoes,dragaoHitBox,danoEnemy)

        player.desenhaHP(DragaoHP,modGame)
          
        dragao.update()
        dragao.draw()
        janela.update()

