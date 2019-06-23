import pygame

# create area to text be drawn
def text_objects(text, font):
    color = (130,210,180)
    # create a invisible block to the text appear
    text_block = font.render(text, True, color)
    # return this block and its dimensions
    return text_block, text_block.get_rect()


# makes the text appear in the screen
def message_display(text, bkgd):
    # message position
    x, y = (bkgd.width/2),(bkgd.height/3)
    font_size = 75
    font_style = 'linuxbiolinumo'


    text_obj = pygame.font.SysFont(font_style, font_size)
    text_surf, text_pos = text_objects(text, text_obj)
    # centralize the message within the 'invisible box'
    text_pos.center = (x, y)

    # put this text in the screen
    bkgd.display.blit(text_surf, text_pos)
    # update here due to a time.freeze in the main.py
    pygame.display.update()
