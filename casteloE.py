from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import* 
from PPlay.keyboard import* 
import player
import enemy
import game
import menu

# Adicionar os soldados e o canhão(se a gnt achar o sprite disso), e as plataformas que precisar
# Sinta-se livre pra colocar quantos soldados quiser e onde quiser
 
def gamePlayCasE(dragao,vetorDragoesInimigos,delay,vetPlatCasE,DragaoHP,danoEnemy,modGame):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Castelo fase Estática")
    teclado = janela.get_keyboard()

    fundoCasE = GameImage("sprites/icones/bkg castle.png")

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    dragao.set_position(150,janela.height - 50 - dragao.height)
    dragao.set_total_duration(1000)
    dragaoHitBox = dragao
    
    #Sprite dos inimigos
    soldados=[]
    velTiro = 300
    badDragao = enemy.badDragons(vetorDragoesInimigos,soldados)
    tirosBadDragoes = []
    delayInimDrag = 80

    #Boss
    Boss = enemy.lastBossPos(janela)
    BossHP=10
    tirosBoss = []
    
    #Varivael para controle de musica
    musica = 0
    
    game.imagens(6,janela,teclado)
    
    #Direção do tiro
    direction = ""
    directionBadDrag = ""
    directionBoss = ""
    
    #Game loop
    while(True):
        fundoCasE.draw()
        if musica == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("audio/Medieval Themes (WAV)/fases estaticas.wav")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            musica += 1
        
        for i in range(2):
            vetPlatCasE[i].draw()
            
        dragao,velDragao = player.movDragao(dragao,janela,teclado)
        delay = player.shootFireball(teclado,dragao,janela,delay,soldados) 
        dragaoHitBox.set_position(dragao.x,dragao.y)

        # BadDragoes
        if len(tirosBadDragoes)==0 and delayInimDrag==0:
            for i,badDragao in enumerate(vetorDragoesInimigos):
                if dragaoHitBox.collided_perfect(badDragao[0]):
                    DragaoHP-=1
            directionBadDrag = enemy.criaTiroDragaoInimigo(tirosBadDragoes,vetorDragoesInimigos,dragao)
        if len(tirosBadDragoes)>0: 
            enemy.movTiroDragaoInimigo(tirosBadDragoes,velTiro,janela,directionBadDrag)
            player.defense(tirosBadDragoes,dragao,teclado)
        enemy.badDragonsHP(vetorDragoesInimigos)
        enemy.desenhaInimigo(vetorDragoesInimigos)
        
        # Boss
        if (BossHP>0):
            if len(tirosBoss)==0 and delayInimDrag==0:
                if dragaoHitBox.collided_perfect(Boss):
                    DragaoHP-=1
                directionBoss = enemy.criaTiroChefao(tirosBoss,Boss,dragao)
            if len(tirosBoss)>0:
                enemy.movTiroChefao(tirosBoss,velTiro,janela,directionBoss)
                player.defense(tirosBoss,dragao,teclado)
            BossHP = enemy.lastBossHP(Boss,BossHP,janela)
            Boss.draw()

        if delayInimDrag>0:
            delayInimDrag-=1
        if BossHP<=0:
            passou = pygame.mixer.Sound("audio\Medieval Themes (WAV)\checkpoint alcançado.wav")
            passou.play()
            return game.gamePassed(teclado,janela,6)
        if (DragaoHP<=0):
            perdeu = pygame.mixer.Sound("audio/Medieval Themes (WAV)/perdeu.wav")
            perdeu.play()
            game.gameFail(teclado,janela)
            menu.gameMenu()
            
        DragaoHP = player.lessHP(DragaoHP,tirosBadDragoes,dragaoHitBox,danoEnemy)
        DragaoHP = player.lessHP(DragaoHP,tirosBoss,dragaoHitBox,danoEnemy)

        player.desenhaHP(DragaoHP,modGame)
          
        dragao.update()
        dragao.draw()
        janela.update()