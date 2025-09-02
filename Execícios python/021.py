import pygame
pygame.init()
pygame.mixer.music.load("Execícios python/021.mp3")
pygame.mixer.music.play()
input("Digite qualquer coisa para parar a música: ")
pygame.event.wait()