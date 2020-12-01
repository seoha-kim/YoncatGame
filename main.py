from intro import Intro
from map import Map
from interaction import Interaction

import pygame
from pygame.locals import *
import sys




if __name__ == "__main__":
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('연냥이를 부탁해!')
    pygame.display.set_icon(pygame.image.load('images/999_ect/game_icon.png'))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        intro = Intro()
        intro.opening_movie()
        intro.notice_box()
        pygame.time.delay(1000)
        intro.start_button()

        intro.choice_screen()
        character = intro.character

        map_ = Map(character)
        map_.character_move()
        map_.interaction_start()

        interaction = Interaction()
        interaction.basic_show()
        interaction.chat_show()
        interaction.interaction_choice()

        pygame.quit()
        sys.exit()
