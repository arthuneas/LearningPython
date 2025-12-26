import pygame

pygame.init()

pygame.mixer.music.load("C:/Users/arthur.almeida/Downloads/clarinet.wav")
pygame.mixer.music.play()
pygame.event.wait()