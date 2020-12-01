import sys, time
import pygame
from pygame.locals import *
import pyganim


class Map:
    def __init__(self, character):
        self.character = character
        if self.character == "male":
            self.front_standing = pygame.image.load('images/3_map_obj/characters/male/male_front.png')
            self.back_standing = pygame.image.load('images/3_map_obj/characters/male/male_back.png')
            self.left_standing = pygame.image.load('images/3_map_obj/characters/male/male_left.png')
            self.right_standing = pygame.image.load('images/3_map_obj/characters/male/male_right.png')

        elif self.character == "female":
            self.front_standing = pygame.image.load('images/3_map_obj/characters/female/female_front.png')
            self.back_standing = pygame.image.load('images/3_map_obj/characters/female/female_back.png')
            self.left_standing = pygame.image.load('images/3_map_obj/characters/female/female_left.png')
            self.right_standing = pygame.image.load('images/3_map_obj/characters/female/female_right.png')

        self.player_width, self.player_height = self.front_standing.get_size()
        self.animation_objs = {}
        self.move_conductor = None

        self.window_width, self.window_height = 1340, 720
        self.window_surface = pygame.display.set_mode((self.window_width, self.window_height))

        self.obj_list = {}
        self.map1, self.map1_x, self.map1_y = 'images/3_map_obj/map_1.png', 0, 0
        self.map2, self.map2_x, self.map2_y = 'images/3_map_obj/map_2.png', 0, 0

        self.catbook, self.catbook_x, self.catbook_y = 'images/3_map_obj/book.png', 2, 19
        self.shop, self.shop_x, self.shop_y = 'images/3_map_obj/shop.png', 100, 31
        self.inventory, self.inventory_x, self.inventory_y = 'images/3_map_obj/inventory.png', 157, 19
        self.coin, self.coin_x, self.coin_y = 'images/3_map_obj/coin.png', 1065, 34
        self.minimap, self.minimap_x, self.minimap_y = 'images/3_map_obj/minimap.png', 1234, 20

        self.cat, self.cat_x, self.cat_y = 'images/3_map_obj/cat/full/kakku.png', 860, 154
        self.mark, self.mark_x, self.mark_y = 'images/3_map_obj/mark.png', 874, 90
        self.chat, self.chat_x, self.chat_y = 'images/3_map_obj/chat_kakku.png', 170, 497

        self.character_x = 0; self.character_y = 320

    def background_music(self, mp3_file='sounds/map_bgm.ogg'):
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def character_animation(self):
        animation_types = 'back_walk front_walk left_walk right_walk'.split()
        for animType in animation_types:
            images = [('images/3_map_obj/characters/%s/%s_%s_%s.png' % (
                    self.character, self.character, animType, str(num).rjust(3, '0')), 100)
                for num in range(2)]
            self.animation_objs[animType] = pyganim.PygAnimation(images)
        self.move_conductor = pyganim.PygConductor(self.animation_objs)

    def map1_basic_show(self):
        self.obj_list['background'] = pygame.image.load(self.map1), (self.map1_x, self.map1_y)
        self.obj_list['catbook'] = pygame.image.load(self.catbook), (self.catbook_x, self.catbook_y)
        self.obj_list['shop'] = pygame.image.load(self.shop), (self.shop_x, self.shop_y)
        self.obj_list['inventory'] = pygame.image.load(self.inventory), (self.inventory_x, self.inventory_y)
        self.obj_list['coin'] = pygame.image.load(self.coin), (self.coin_x, self.coin_y)
        self.obj_list['minimap'] = pygame.image.load(self.minimap), (self.minimap_x, self.minimap_y)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))

    def map2_basic_show(self):
        self.obj_list = {}
        self.obj_list['background'] = pygame.image.load(self.map2), (self.map2_x, self.map2_y)
        self.obj_list['catbook'] = pygame.image.load(self.catbook), (self.catbook_x, self.catbook_y)
        self.obj_list['shop'] = pygame.image.load(self.shop), (self.shop_x, self.shop_y)
        self.obj_list['inventory'] = pygame.image.load(self.inventory), (self.inventory_x, self.inventory_y)
        self.obj_list['coin'] = pygame.image.load(self.coin), (self.coin_x, self.coin_y)
        self.obj_list['minimap'] = pygame.image.load(self.minimap), (self.minimap_x, self.minimap_y)
        self.obj_list['cat'] = pygame.image.load(self.cat), (self.cat_x, self.cat_y)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))

    def remove_obj(self, obj_name):
        del self.obj_list[obj_name]
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

    def interaction_start(self):
        self.obj_list['mark'] = pygame.image.load(self.mark), (self.mark_x, self.mark_y)
        self.obj_list['character'] = self.back_standing, (self.character_x, self.character_y)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
        pygame.time.wait(500)
        self.obj_list['chat'] = pygame.image.load(self.chat), (self.chat_x, self.chat_y)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
        pygame.time.wait(1000)
        self.remove_obj('chat')
        time.sleep(1.5)

    def character_move(self):
        self.character_animation()
        self.background_music()

        UP = 'up'; DOWN = 'down'; LEFT = 'left'; RIGHT = 'right'
        moveUp = moveDown = moveLeft = moveRight = False
        direction = RIGHT; walk_rate = 18

        main_clock = pygame.time.Clock()
        no_event = True; map1 = True
        while no_event:
            if map1 == True:
                self.map1_basic_show()
            else:
                self.map2_basic_show()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    elif event.key == K_UP:
                        moveUp = True
                        moveDown = False
                        if not moveLeft and not moveRight:
                            direction = UP

                    elif event.key == K_DOWN:
                        moveDown = True
                        moveUp = False
                        if not moveLeft and not moveRight:
                            direction = DOWN

                    elif event.key == K_LEFT:
                        moveLeft = True
                        moveRight = False
                        if not moveUp and not moveDown:
                            direction = LEFT

                    elif event.key == K_RIGHT:
                        moveRight = True
                        moveLeft = False
                        if not moveUp and not moveDown:
                            direction = RIGHT

                elif event.type == KEYUP:
                    if event.key == K_UP:
                        moveUp = False
                        if moveLeft:
                            direction = LEFT
                        if moveRight:
                            direction = RIGHT

                    elif event.key == K_DOWN:
                        moveDown = False
                        if moveLeft:
                            direction = LEFT
                        if moveRight:
                            direction = RIGHT

                    elif event.key == K_LEFT:
                        moveLeft = False
                        if moveUp:
                            direction = UP
                        if moveDown:
                            direction = DOWN

                    elif event.key == K_RIGHT:
                        moveRight = False
                        if moveUp:
                            direction = UP
                        if moveDown:
                            direction = DOWN

            # draw the correct walking sprite from the animation object
            if moveUp or moveDown or moveLeft or moveRight:
                self.move_conductor.play()
                if direction == UP:
                    self.animation_objs['back_walk'].blit(self.window_surface, (self.character_x, self.character_y))
                elif direction == DOWN:
                    self.animation_objs['front_walk'].blit(self.window_surface, (self.character_x, self.character_y))
                elif direction == LEFT:
                    self.animation_objs['left_walk'].blit(self.window_surface, (self.character_x, self.character_y))
                elif direction == RIGHT:
                    self.animation_objs['right_walk'].blit(self.window_surface, (self.character_x, self.character_y))

                if moveUp:
                    self.character_y -= walk_rate
                if moveDown:
                    self.character_y += walk_rate
                if moveLeft:
                    self.character_x -= walk_rate
                if moveRight:
                    self.character_x += walk_rate

            # standing still
            else:
                self.move_conductor.stop()
                if direction == UP:
                    self.window_surface.blit(self.back_standing, (self.character_x, self.character_y))
                elif direction == DOWN:
                    self.window_surface.blit(self.front_standing, (self.character_x, self.character_y))
                elif direction == LEFT:
                    self.window_surface.blit(self.left_standing, (self.character_x, self.character_y))
                elif direction == RIGHT:
                    self.window_surface.blit(self.right_standing, (self.character_x, self.character_y))

            pygame.display.update()
            # need modifying - move room
            if self.character_x < 0:
                self.character_x, self.character_y = 1285, 320
                self.remove_obj('cat')
                self.map1_basic_show()
                map1 = True

            if self.character_x > self.window_width:
                self.character_x, self.character_y = 10, 320
                self.map2_basic_show()
                map1 = False

            if self.character_y < 0:
                self.character_y = 0

            if self.character_y > self.window_height - self.player_height:
                self.character_y = self.window_height - self.player_height

            if (845 <= self.character_x <= 920) and (self.character_y <= 186) and (direction == UP):
                no_event = False

            pygame.time.delay(10)

            pygame.display.update()
            main_clock.tick(30)
