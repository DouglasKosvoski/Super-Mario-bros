import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, (130,210,180))
    return textSurface, textSurface.get_rect()

def message_display(text, bkgd):
    largeText = pygame.font.SysFont('linuxbiolinumo', 75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((bkgd.width/2),(bkgd.height/2.5))
    bkgd.display.blit(TextSurf, TextRect)
    pygame.display.update()
