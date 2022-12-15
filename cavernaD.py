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

def gamePlayCavD(dragao,delay,vetPlatCavD,DragaoHP,danoEnemy,modGame,init):
    #Define dimensão da janela e teclado
    janela = Window(1280,720)
    janela.set_title("Caverna fase Dinamica")
    teclado = janela.get_keyboard()

    fundoCavD_1 = GameImage("sprites/caverna-dinamico/fundocavernad.jpg")

    #Define dragão de acordo com o selecionado e com a movimentação e posiciona no inicio do jogo
    dragao.set_position(150,janela.height - dragao.height -200)
    dragao.set_total_duration(1000)
    dragaoHitBox = dragao
    
    #Sprite dos inimigos
    soldados = enemy.criaSoldados(vetPlatCavD)
    tirosSoldados = []
    velTiro = 300
    delayInim = 120
    
    #Varivael para controle de musica
    musica = 0

    #mensagem explicativa
    game.imagens(1,janela,teclado)
    checkpoint = Sprite("sprites/vidas/flag.png")
    parou=False
    
    #Direção do tiro
    direction = ""
    
    #Game loop
    while(True):
        fundoCavD_1.draw()
        if musica == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("audio/Medieval Themes (WAV)/fases dinamicas.wav")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            musica += 1
        dragao,velDragao = player.movDragaoDinamico(dragao,janela,teclado)
        if (fundoCavD_1.x >= -2556):
            background_dinamico.scrolling(fundoCavD_1,velDragao,janela,teclado)
            enemy.movSoldados(soldados,velDragao,teclado,janela)
            for i in range(13):
                background_dinamico.movimentoplataforma(vetPlatCavD[i],velDragao,janela,teclado)
        else:
            checkpoint,init = game.inCheckpoint(checkpoint,init,janela.width-200,467-checkpoint.height)
            parou=True
            if(teclado.key_pressed("RIGHT") and dragao.x < janela.width - dragao.width):
                dragao.x += velDragao*janela.delta_time()  
            elif(teclado.key_pressed("LEFT") and dragao.x > 0):
                dragao.x -= velDragao*janela.delta_time() 
        for i in range(13):
            vetPlatCavD[i].draw()
        
        delay = player.shootFireball(teclado,dragao,janela,delay,soldados) 
        dragaoHitBox.x = dragao.x
        dragaoHitBox.y = dragao.y 
        if len(tirosSoldados)==0 and delayInim==0:
            for i,soldado in enumerate(soldados):
                if dragaoHitBox.collided_perfect(soldado):
                    DragaoHP-=1
                direction = enemy.criaTiroSoldados(tirosSoldados,soldado,dragao) 

        if len(tirosSoldados)>0:
            enemy.movTiroSoldados(tirosSoldados,velTiro,janela,direction)
        if delayInim>0:
            delayInim-=1
        enemy.desenhaSoldados(soldados)
        
        if (parou==True and dragaoHitBox.collided_perfect(checkpoint)):
            chegou = pygame.mixer.Sound("audio/Medieval Themes (WAV)/checkpoint alcançado.wav")
            chegou.play()
            return game.gamePassed(teclado,janela,1)
        if (DragaoHP<=0):
            perdeu = pygame.mixer.Sound("audio/Medieval Themes (WAV)/perdeu.wav")
            perdeu.play()
            game.gameFail(teclado,janela)
            menu.gameMenu()
            
        DragaoHP = player.lessHP(DragaoHP,tirosSoldados,dragaoHitBox,danoEnemy)
        player.desenhaHP(DragaoHP,modGame)
        
        dragao.update()
        dragao.draw()
        janela.update()
