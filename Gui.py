import pygame
import sys
from pygame.locals import *
import numpy as np

escala = 5
LEFT = 1
RIGHT = 3

color = np.zeros((20,3))
color[0]  = (255,255,255)	#blanco
color[1]  = (255,255,0)		#amarillo
color[2]  = (34,113,179)	#azul
color[3]  = (87,166,57)		#verde
color[4]  = (213,48,50)		#rojo
color[5]  = (99,58,52)		#cafe
color[6]  = (215,45,109)	#magenta
color[7]  = (255,117,20)	#naranja
color[8]  = (127,181,181)	#turquesa
color[9]  = (234,137,154)	#rosa
color[10] = (40,114,51)		#esmeralda
color[11] = (1,93,82)		#opalo
color[12] = (0,247,0)		#verde brillante
color[13] = (244,169,0)		#melon
color[14] = (71,64,46)		#oliva
color[15] = (37,109,123)	#agua
color[16] = (194,176,120)	#beige
color[17] = (110,28,52)		#brudeos
color[18] = (125,132,113)	#gris cemento
color[19] = (10,10,10)		#negro
ventana = pygame.display.set_mode((90*escala, 90*escala))

class GUI:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic-Tac-Toe")
        ventana.fill(color[0])
        grosor = 2
        pygame.draw.line(ventana, color[19],(30*escala,0),(30*escala,90*escala),grosor)
        pygame.draw.line(ventana, color[19],(60*escala,0),(60*escala,90*escala),grosor)
        pygame.draw.line(ventana, color[19],(0,30*escala),(90*escala,30*escala),grosor)
        pygame.draw.line(ventana, color[19],(0,60*escala),(90*escala,60*escala),grosor)

    def wait(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                arr = [[1,2,3],[4,5,6],[7,8,9]]
                pos = pygame.mouse.get_pos()
                posx, posy = pos
                posx = int(posx / (30*escala))
                posy = int(posy / (30*escala))
                a = arr[posy][posx] -1
                return a
            pygame.display.update()

    def show(self,board):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20*escala)
        posiciones = [(10,10),(40,10),(70,10),(10,40),(40,40),(70,40),(10,70),(40,70),(70,70)]
        indice = 0
        for i in posiciones:
            element = (i[0]*escala,i[1]*escala)
            posiciones[indice] = element
            indice = indice +1

        indice = 0
        for element in board:
            if element == 'X':
                color_text = color[3]
            elif element == 'O':
                color_text = color[4]
            else:
                color_text = color[19]
            textsurface = myfont.render(element, False, color_text)
            ventana.blit(textsurface, posiciones[indice])
            indice = indice +1
        pygame.display.update()