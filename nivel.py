import pygame as pg
from datos import *
from creador_mundo import *
nivel_1 = True
nivel_2 = False
nivel_3 = False
niveles = (nivel_1,nivel_2,nivel_3)
class Juego():
    def __init__(self,lista_eventos,jugador,screen,enemigo):
        self.lista_eventos = lista_eventos
        self.jugador = jugador
        self.screen = screen
        self.enemigo = enemigo
    def update(self,screen=0,tiempo=0):
        for event in self.lista_eventos:
            match event.type:
                
                #SETEO DE TECLAS
                case pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.jugador.mueve_dere = True
                    if event.key == pg.K_LEFT:
                        self.jugador.mueve_izq = True
                    if (event.key == pg.K_e):
                        self.jugador.disparando = True
                        print("Ataco")
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                            juego_ejecutandose,tiempo = pausa(tiempo,screen)
                            return juego_ejecutandose,tiempo
                    #test danio
                    if event.key == pg.K_o:
                        self.jugador.vidas -= 1
                        self.enemigo.vidas -= 1
                        hit_fx.play()
                        print("Auch!")
                    if (event.key == pg.K_UP) and (not self.jugador.cayendo):
                        salto_fx.play()
                        self.jugador.salta = True
                        self.jugador.cayendo = True
        
                case pg.KEYUP:
                    if (event.key == pg.K_UP):
                        self.jugador.cayendo = True
                    if event.key == pg.K_RIGHT:
                        self.jugador.mueve_dere = False
                    if event.key == pg.K_LEFT:
                        self.jugador.mueve_izq = False
                    if event.key == pg.K_e:
                        self.jugador.disparando = False
        if self.jugador.vidas == 3:
            self.screen.blit(vida_img, (0, 0))
            self.screen.blit(vida_img, (60, 0))
            self.screen.blit(vida_img, (120, 0))
        elif self.jugador.vidas == 2:
            self.screen.blit(vida_img, (0, 0))
            self.screen.blit(vida_img, (60, 0))
        elif self.jugador.vidas == 1:
            self.screen.blit(vida_img, (0, 0)) 


