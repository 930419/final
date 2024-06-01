# 要先安裝pygame 在終端機輸入 mac :python3 -m pip install -U pygame --user
# windows : py -m pip install -U pygame --user
# 導入函數庫
import pygame
import os
import random
import time
import sys
import csv
# 要先 pip install moviepy
from moviepy.editor import VideoFileClip
    
#  顏色
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BROWN = pygame.Color(40, 33, 22)
SKYBLUE = pygame.Color(0, 127, 255)

#  import 圖片檔案
MENU_BUTTON = [pygame.image.load(os.path.join("image/menu", "button-2.png")),
               pygame.image.load(os.path.join("image/menu/intro", "button_next-2.png")),
               pygame.image.load(os.path.join("image/menu/intro", "button_back-2.png")),
               pygame.image.load(os.path.join("image/menu/intro", "button_start-2.png"))]

INTRODUCTION = [pygame.image.load(os.path.join("image/menu/intro", "intro_single-2.png")),
                pygame.image.load(os.path.join("image/menu/intro", "intro_obstacles-2.png")),
                pygame.image.load(os.path.join("image/menu/intro", "intro_buff-2.png"))]
MENUBG  = pygame.image.load(os.path.join("image/menu/window", "main.png"))

INTRODUCTION2 = [pygame.image.load(os.path.join("image/menu/intro", "intro_Duo-2.png")),
                 pygame.image.load(os.path.join("image/menu/intro", "intro_obstacles-2.png")),
                 pygame.image.load(os.path.join("image/menu/intro", "intro_buff-2.png"))]

BACKGROUND_LIST = [pygame.image.load(os.path.join("image/background", "6city.jpg")),
                   pygame.image.load(os.path.join("image/background", "5winter.jpg")),
                   pygame.image.load(os.path.join("image/background", "4autumn.jpg")),
                   pygame.image.load(os.path.join("image/background", "3forest.jpg"))]

BACKGROUND_LIST_DUO = [pygame.image.load(os.path.join("image/background", "6cityduo.jpg")),
                       pygame.image.load(os.path.join("image/background", "5winterduo.jpg")),
                       pygame.image.load(os.path.join("image/background", "4autumnduo.jpg")),
                       pygame.image.load(os.path.join("image/background", "3forestduo.jpg"))]
CHARACTOR_LIST = [pygame.image.load(os.path.join("image/charactor", "snail-1-right.png")),
                  pygame.image.load(os.path.join("image/charactor", "snail-2-right.png"))]

DAMAGE_LIST = [pygame.image.load(os.path.join("image/charactor", "snail-debuff-1-right.png")),
               pygame.image.load(os.path.join("image/charactor", "snail-debuff-2-right.png"))]

MUTEKI_LIST =  [pygame.image.load(os.path.join("image/charactor", "snail-invicible-1-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-invicible-2-right.png"))]  # 跑步圖片大小 87*94

JUMPING_IMG = [pygame.image.load(os.path.join("image/charactor", "snail-jump-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-invicible-jump-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-debuff-jump-right.png"))]  # 跳躍圖片大小 87*94


DUCKING_LIST = [pygame.image.load(os.path.join("image/charactor", "snail-hedge-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-invicible-hedge-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-debuff-hedge-right.png"))] 


 # 第二隻蝸牛
CHARACTOR_LIST2 = [pygame.image.load(os.path.join("image/charactor/snail2", "snail2-1-right.png")),
                  pygame.image.load(os.path.join("image/charactor/snail2", "snail2-2-right.png"))]

DAMAGE_LIST2 = [pygame.image.load(os.path.join("image/charactor/snail2", "snail2-debuff-1-right.png")),
               pygame.image.load(os.path.join("image/charactor/snail2", "snail2-debuff-2-right.png"))]

MUTEKI_LIST2 =  [pygame.image.load(os.path.join("image/charactor/snail2", "snail2-invicible-1-right.png")),
                pygame.image.load(os.path.join("image/charactor/snail2", "snail2-invicible-2-right.png"))]  # 跑步圖片大小 87*94

JUMPING_IMG2 = [pygame.image.load(os.path.join("image/charactor/snail2", "snail2-jump-right.png")),
                pygame.image.load(os.path.join("image/charactor/snail2", "snail2-invicible-jump-right.png")),
                pygame.image.load(os.path.join("image/charactor/snail2", "snail2-debuff-jump-right.png"))]  # 跳躍圖片大小 87*94

DUCKING_LIST2 = [pygame.image.load(os.path.join("image/charactor/snail2", "snail2-hedge-right.png")),
                pygame.image.load(os.path.join("image/charactor/snail2", "snail2-invicible-hedge-right.png")),
                pygame.image.load(os.path.join("image/charactor/snail2", "snail2-debuff-hedge-right.png"))]  #  蹲下大小 118*60


ITEM = [pygame.image.load(os.path.join("image/item", "1.png")),
        pygame.image.load(os.path.join("image/item", "2.png")),
        pygame.image.load(os.path.join("image/item", "3.png"))]

LIFE_BAR = [pygame.image.load(os.path.join("image/item/life_bar", "Life bar-5-0.png")),
            pygame.image.load(os.path.join("image/item/life_bar", "Life bar-5-1.png")),
            pygame.image.load(os.path.join("image/item/life_bar", "Life bar-5-2.png")),
            pygame.image.load(os.path.join("image/item/life_bar", "Life bar-5-3.png")),
            pygame.image.load(os.path.join("image/item/life_bar", "Life bar-5-4.png")),
            pygame.image.load(os.path.join("image/item/life_bar", "Life bar-5-5.png"))]

#  大障礙物
LARGEOBSTACLE = [pygame.image.load(os.path.join("image/largeobstacle", "cityb.png")),
                 pygame.image.load(os.path.join("image/largeobstacle", "winterb.png")),
                 pygame.image.load(os.path.join("image/largeobstacle", "autumnb.png")),
                 pygame.image.load(os.path.join("image/largeobstacle", "forestb.png"))]
# 小障礙物
SMALLOBSTACLE = [pygame.image.load(os.path.join("image/smallobstacle", "citys.png")),
                 pygame.image.load(os.path.join("image/smallobstacle", "winters.png")),
                 pygame.image.load(os.path.join("image/smallobstacle", "autumns.png")),
                 pygame.image.load(os.path.join("image/smallobstacle", "forests.png"))]

FLYOBSTACLE = [pygame.image.load(os.path.join("image/flyobstacle", "cityf.png")),
               pygame.image.load(os.path.join("image/flyobstacle", "winterf.png")),
               pygame.image.load(os.path.join("image/flyobstacle", "autumnf.png")),
               pygame.image.load(os.path.join("image/flyobstacle", "forestf-2.png"))]

FOG = [pygame.image.load(os.path.join("image/background", "fog1.png"))]
FOG1 = [pygame.image.load(os.path.join("image/flyobstacle", "fog-P2P.png"))]
FOG2 = [pygame.image.load(os.path.join("image/flyobstacle", "fog-P2P.png"))]
BLUROBSTACLE = [pygame.image.load(os.path.join("image/flyobstacle", "cloud.png"))]


# =====

#  是否播過介紹
needintrosingle = True
needintroduo = True


# =====

#  建立視窗(背景長/寬 ＝ 1000/660)
window_height = 650
window_width = 1000
window = pygame.display.set_mode((window_width, window_height))
screen = pygame.display.set_mode((window_width, window_height))


# =====

#  難度
EASY = 1
MEDIUM = 2
HARD = 3
game_difficulty = EASY


# =====

#  文字大小
TITLE = 48
HEADING = 32
SUBHEADING = 28
BODY = 24


#  像素文字
class Text:
    def __init__(self, text, size, color, position=(0, 0)):
        self.font = pygame.font.Font('fonts/PixelEmulator.ttf', size)  # 字體大小(參數)與字型
        self.surface = self.font.render(text, True, color)  # 印出的字串(參數)與呈現
        self.rect = self.surface.get_rect()  # 文字框起
        self.rect.center = position  # 文字的中心位置(參數)
    def draw(self, screen):
        screen.blit(self.surface, self.rect)


#  一般文字        
class Text_body:
    def __init__(self, text, size, color, position=(0, 0)):
        self.font = pygame.font.Font('fonts/AgencyFB-Bold.ttf', size)  # 字體大小(參數)與字型
        self.surface = self.font.render(text, True, color)  # 印出的字串(參數)與呈現
        self.rect = self.surface.get_rect()  # 文字框起
        self.rect.center = position  # 文字的中心位置(參數)
    def draw(self, screen):
        screen.blit(self.surface, self.rect)


# =====

#  角色處理
class Charactor1:
    x_ch_pos = 80
    y_ch_pos = 480
    y_ch_posduck = 510
    jump_val = 7
    invincible_timer1 = 0
    take_damagetimer1 = 0
    
    def __init__(self):
         # 定義變數
        self.ch_duck = False
        self.ch_run = True
        self.ch_jump = False
        self.step_index = 0  # 腳步動畫
        self.fall = self.jump_val  # fall:高度變化幅度
        # 圖片
        self.duck_img_list = DUCKING_LIST
        self.run_img_list = CHARACTOR_LIST
        self.jump_img = JUMPING_IMG
        self.damage_img_list = DAMAGE_LIST
        self.muteki_img_list = MUTEKI_LIST
        self.image = self.run_img_list[0]  
        # 把角色框列
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.invincible_timer1 = 0
        self.take_damagetimer1 = 0

    def run(self):
        self.image = self.run_img_list[self.step_index // 5]  # 依 step_index 跑步圖片，每五個step_index換一張圖
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.step_index += 1

    def duck(self):
        duck_sound = pygame.mixer.Sound(os.path.join("music/sounds", "duck.wav"))
        pygame.mixer.Channel(0).play(duck_sound)
        if self.invincible_timer1 > 0:
            self.image = self.duck_img_list[1]
        elif self.invincible_timer1 <= 0 and self.take_damagetimer1 > 0:
            self.image = self.duck_img_list[2]
        else:
            self.image = self.duck_img_list[0]  
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_posduck
        self.step_index += 1

    def jump(self):
        jump_sound = pygame.mixer.Sound(os.path.join("music/sounds", "jump.wav"))
        pygame.mixer.Channel(1).play(jump_sound)
        if self.invincible_timer1 > 0:
            self.image = self.jump_img[1]
        elif self.invincible_timer1 <= 0 and self.take_damagetimer1 > 0:
            self.image = self.jump_img[2]
        else:
            self.image = self.jump_img[0]
        if self.ch_jump:
            self.ch_rect.y -= self.fall * 4  
            self.fall -= 0.5  
        if self.fall <= - self.jump_val:
            self.ch_jump = False
            self.fall = self.jump_val
            
    def damage(self):
        self.image = self.damage_img_list[(self.step_index // 5)-1]  # 依 step_index 跑步圖片，每五個step_index換一張圖
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.step_index += 1
        
    def muteki(self):
        self.image = self.muteki_img_list[(self.step_index // 5)-1]  # 依 step_index 跑步圖片，每五個step_index換一張圖
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.step_index += 1
        
    def take_damage(self):  # 不會連續扣血
        if self.take_damagetimer1 <= 0:  # 如果不在無敵時間內
            self.take_damagetimer1 = 30
            
    def muteki_time(self): # 無敵星星
        if self.invincible_timer1 <= 0:  # 如果不在無敵時間內
            self.invincible_timer1 = 300

    def update(self, user_input):
        if user_input[pygame.K_UP] or user_input[pygame.K_SPACE] and self.ch_jump == False:
            self.ch_duck = False
            self.ch_run = False
            self.ch_jump = True
        elif user_input[pygame.K_DOWN] and not self.ch_jump:
            self.ch_duck = True
            self.ch_run = False
            self.ch_jump = False

        elif not (self.ch_jump or user_input[pygame.K_DOWN]):
            self.ch_duck = False
            self.ch_run = True
            self.ch_jump = False
        if self.ch_duck:
            self.duck()
        if self.ch_run:
            if self.invincible_timer1 > 0:
                self.muteki()
            elif self.invincible_timer1 <= 0 and self.take_damagetimer1 > 0:
                self.damage()
            elif self.invincible_timer1 <= 0 and self.take_damagetimer1 <= 0:
                self.run()
        if self.ch_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0
        if self.invincible_timer1 > 0:
            self.invincible_timer1 -= 1
        if self.take_damagetimer1 > 0:
            self.take_damagetimer1 -= 1
            
    def is_invincible(self):
        return self.invincible_timer1 > 0
        
    def is_takingdamage(self):
        return self.take_damagetimer1 > 0
        
    def draw(self, screen):
        screen.blit(self.image, (self.ch_rect.x, self.ch_rect.y))


class Charactor2:
    invincible_timer2 = 0
    take_damagetimer2 = 0
    x_ch_pos = 80
    y_ch_pos = 200
    y_ch_posduck = 230
    jump_val = 7
    
    def __init__(self):
         # 定義變數
        self.ch_duck = False
        self.ch_run = True
        self.ch_jump = False
        self.step_index = 0  # 腳步動畫
        self.fall = self.jump_val  # fall:高度變化幅度

        # 圖片
        self.duck_img_list = DUCKING_LIST2
        self.run_img_list = CHARACTOR_LIST2
        self.jump_img = JUMPING_IMG2
        self.damage_img_list = DAMAGE_LIST2
        self.muteki_img_list = MUTEKI_LIST2
        self.image = self.run_img_list[0]  

        # 把角色框列
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.invincible_timer1 = 0
        self.take_damagetimer1 = 0

    def run(self):
        self.image = self.run_img_list[self.step_index // 5]  # 依 step_index 跑步圖片，每五個step_index換一張圖
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.step_index += 1

    def duck(self):
        duck_sound = pygame.mixer.Sound(os.path.join("music/sounds", "duck.wav"))
        pygame.mixer.Channel(0).play(duck_sound)
        if self.invincible_timer2 > 0:
            self.image = self.duck_img_list[1]
        elif self.invincible_timer2 <= 0 and self.take_damagetimer2 > 0:
            self.image = self.duck_img_list[2]
        else:
            self.image = self.duck_img_list[0] 
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_posduck
        self.step_index += 1

    def jump(self):
        jump_sound = pygame.mixer.Sound(os.path.join("music/sounds", "jump.wav"))
        pygame.mixer.Channel(1).play(jump_sound)
        if self.invincible_timer2 > 0:
            self.image = self.jump_img[1]
        elif self.invincible_timer2 <= 0 and self.take_damagetimer2 > 0:
            self.image = self.jump_img[2]
        else:
            self.image = self.jump_img[0]
        if self.ch_jump:
            self.ch_rect.y -= self.fall * 4  
            self.fall -= 0.5  
        if self.fall <= - self.jump_val:
            self.ch_jump = False
            self.fall = self.jump_val
            
    def damage(self):
        self.image = self.damage_img_list[(self.step_index // 5)-1]  # 依 step_index 跑步圖片，每五個step_index換一張圖
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.step_index += 1
        
    def muteki(self):
        self.image = self.muteki_img_list[(self.step_index // 5)-1]  # 依 step_index 跑步圖片，每五個step_index換一張圖
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_pos
        self.step_index += 1
        
    def take_damage(self):  # 不會連續扣血
        if self.take_damagetimer2 <= 0:  # 如果不在無敵時間內
            self.take_damagetimer2 = 30
            
    def muteki_time(self): # 無敵星星
        if self.invincible_timer2 <= 0:  # 如果不在無敵時間內
            self.invincible_timer2 = 300

    def update(self, user_input):
        if user_input[pygame.K_w]  and not self.ch_jump:
            self.ch_duck = False
            self.ch_run = False
            self.ch_jump = True
        elif user_input[pygame.K_s] and not self.ch_jump:
            self.ch_duck = True
            self.ch_run = False
            self.ch_jump = False
        elif not (self.ch_jump or user_input[pygame.K_s]):
            self.ch_duck = False
            self.ch_run = True
            self.ch_jump = False
        if self.ch_duck:
            self.duck()
        if self.ch_run:
            if self.invincible_timer2 > 0:
                self.muteki()
            elif self.invincible_timer2 <= 0 and self.take_damagetimer2 > 0:
                self.damage()
            elif self.invincible_timer2 <= 0 and self.take_damagetimer2 <= 0:
                self.run()
        if self.ch_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0
        if self.invincible_timer2> 0:
            self.invincible_timer2 -= 1
        if self.take_damagetimer2 > 0:
            self.take_damagetimer2 -= 1
            
    def is_invincible(self):
        return self.invincible_timer2 > 0
        
    def is_takingdamage(self):
        return self.take_damagetimer2 > 0
        
    def draw(self, screen):
        screen.blit(self.image, (self.ch_rect.x, self.ch_rect.y))


# =====

#  障礙物處理
class Obstacle:
    def __init__(self, imageList : list, typeObject : int):
        self.image_list = imageList  # 以變數儲存障礙物類型
        self.type = typeObject  # 以變數儲存障礙物樣貌
        self.rect = self.image_list[self.type].get_rect()  # 將障礙物框起
        self.rect.x = window_width  # 障礙物X座標位置
    def update(self):
        self.rect.x -= game_speed
    def draw(self, screen : pygame.surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))


class largeobs(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 不同背景不同種類的障礙物
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 500  # Y座標位置


class smallobs(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 不同背景不同種類的障礙物
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 510 # Y座標位置


class flyobs(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 415 # Y座標位置


class largeobs2(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 不同背景不同種類的障礙物
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 200  # Y座標位置


class smallobs2(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 210 # Y座標位置


class flyobs2(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 三種小仙人掌型態隨機選取一種
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 170 # Y座標位置


class blurobs:
    def __init__(self, imageList : list):
        self.image_list = imageList  # 以變數儲存障礙物類型
        self.type = 0  # 以變數儲存障礙物樣貌
        self.rect = self.image_list[self.type].get_rect()  # 將障礙物框起
        self.rect.x = window_width  # 障礙物X座標位置
        self.rect.y = 400 
        
    def update(self):
        self.rect.x -= game_speed
        
    def draw(self, screen : pygame.surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))


class blurobs2(Obstacle):
    def __init__(self, imageList : list):
        self.image_list = imageList  # 以變數儲存障礙物類型
        self.type = 0  # 以變數儲存障礙物樣貌
        self.rect = self.image_list[self.type].get_rect()  # 將障礙物框起
        self.rect.x = window_width  # 障礙物X座標位置
        self.rect.y = 200 
        
    def update(self):
        self.rect.x -= game_speed
        
    def draw(self, screen : pygame.surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))


# =====

#  道具處理
class Heart:
    def __init__(self, image_list: list):
        self.image_list = image_list  # 道具圖片列表
        self.type = 0  # 道具類型，這裡預設為 0
        self.rect = self.image_list[self.type].get_rect()  # 道具的矩形區域
        self.rect.x = window_width  # 道具出現的 x 座標
        self.rect.y = random.randint(330, 500)  # 道具出現的 y 座標
        
    def update(self):
        self.rect.x -= game_speed  # 道具向左移動的速度
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))  # 繪製道具


class star:
    def __init__(self, image_list: list):
        self.image_list = image_list  # 道具圖片列表
        self.type = 2  # 道具類型，這裡預設為 0
        self.rect = self.image_list[self.type].get_rect()  # 道具的矩形區域
        self.rect.x = window_width  # 道具出現的 x 座標
        self.rect.y = random.randint(330, 500)  # 道具出現的 y 座標
        
    def update(self):
        self.rect.x -= game_speed  # 道具向左移動的速度
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))  # 繪製道具


class Heart2:
    def __init__(self, image_list: list):
        self.image_list = image_list  # 道具圖片列表
        self.type = 0  # 道具類型，這裡預設為 0
        self.rect = self.image_list[self.type].get_rect()  # 道具的矩形區域
        self.rect.x = window_width  # 道具出現的 x 座標
        self.rect.y = random.randint(150, 320)  # 道具出現的 y 座標
        
    def update(self):
        self.rect.x -= game_speed  # 道具向左移動的速度
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))  # 繪製道具


class star2:
    def __init__(self, image_list: list):
        self.image_list = image_list  # 道具圖片列表
        self.type = 2  # 道具類型，這裡預設為 0
        self.rect = self.image_list[self.type].get_rect()  # 道具的矩形區域
        self.rect.x = window_width  # 道具出現的 x 座標
        self.rect.y = random.randint(150, 280)  # 道具出現的 y 座標
        
    def update(self):
        self.rect.x -= game_speed  # 道具向左移動的速度
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y)) 


# =====

# 特殊情況
class Fog:
    def __init__(self):
        self.image_list = FOG  # 道具圖片列表
        self.type = 0  # 道具類型，這裡預設為 0
        self.rect = self.image_list[0].get_rect()  # 道具的矩形區域
        self.rect.x = 0  # 道具出現的 x 座標
        self.rect.y = 0 # 道具出現的 y 座標
        self.fog_timer = 0
        
    def startfog(self):
        if self.fog_timer != 180:
            self.fog_timer = 180
            
    def isfog(self):
        return self.fog_timer > 0
        
    def update(self):

        self.fog_timer -= 1
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))  # 繪製道具


class Fog1:
    def __init__(self):
        self.image_list = FOG1 # 道具圖片列表
        self.type = 0  # 道具類型，這裡預設為 0
        self.rect = self.image_list[0].get_rect()  # 道具的矩形區域
        self.rect.x = 500  # 道具出現的 x 座標
        self.rect.y = 490 # 道具出現的 y 座標
        self.fog_timer = 0
        
    def startfog(self):
        if self.fog_timer != 180:
            self.fog_timer = 180
            
    def isfog(self):
        return self.fog_timer > 0
        
    def update(self):

        self.fog_timer -= 1
    
    # 繪製道具    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (0, 0)) # 霧的大小已經調成符合單人視窗了 


class Fog2:
    def __init__(self):
        self.image_list = FOG2  # 道具圖片列表
        self.type = 0  # 道具類型，這裡預設為 0
        self.rect = self.image_list[0].get_rect()  # 道具的矩形區域
        self.rect.x = 500  # 道具出現的 x 座標
        self.rect.y = 163 # 道具出現的 y 座標
        self.fog_timer = 0
        
    def startfog(self):
        if self.fog_timer != 180:
            self.fog_timer = 180
            
    def isfog(self):
        return self.fog_timer > 0
        
    def update(self):

        self.fog_timer -= 1

    # 繪製道具
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (0, window_height // 2))


class LifeBar:
    def __init__(self, max_life, x, y):
        self.max_life = max_life
        self.current_life = max_life
        self.x = x
        self.y = y

    def draw(self, window, life_bar_images):
        window.blit(life_bar_images[self.current_life], (self.x, self.y))

    def take_damage(self, amount=1):
        self.current_life = max(0, self.current_life - amount)

    def heal(self, amount=1):
        self.current_life = min(self.max_life, self.current_life + amount)

    def is_alive(self):
        return self.current_life > 0

    def reset(self):
        self.current_life = self.max_life


# =====

#  初始化pygame
def initialize_game(): 
    pygame.init()


#  讀取背景音樂
def load_bg_music(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)


#  讀取分數
def load_sorted_score_list(which_score):
    score_list = list()
    score_file_path = os.path.join("score", which_score)
    if os.path.exists(score_file_path):
        with open(score_file_path, newline='', encoding='utf-8-sig') as score_file:
            try:
                rows = csv.reader(score_file)
                for row in rows:
                    score_list.append([row[0], int(row[1])])
                score_list.sort(key = lambda x:x[1], reverse=True)
            except:
                pass
        score_file.close()
    return score_list


#  起始頁面
def startpage():

    global game_difficulty
    global game_mode
    global TITLE, HEADING, BODY

    intro_anime = VideoFileClip(os.path.join("anime", "intro_anime.mp4"))
    intro_anime.preview()

    text_position1 = (650, (window_height//2) - 50)  # Choose The
    text_position2 = (650, (window_height//2) + 50)  # Game Difficulty
    """
    run = True
    while run :
        window.blit(BACKGROUND_LIST[0], (0, 0))

        start_text_0 = Text("Press Enter To Start", TITLE, BLACK, (500, 450))
        start_text_0.draw(window)
        for event in pygame.event.get():
            if event.type == (pygame.QUIT or pygame.K_ESCAPE):
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu()
    """
    menu()
    pygame.display.update()


# 單雙人選擇目錄
def menu():
    global needintrosingle
    global needintroduo
    global game_difficulty
    global game_mode
    global TITLE, HEADING, BODY

    text_position1 = (650, (window_height//2) - 50)  # Choose The
    text_position2 = (650, (window_height//2) + 50)  # Game Difficulty

    load_bg_music(os.path.join("music", "bg_music_in_menu.ogg"))
    pygame.mixer.music.play(-1)  # menu background music

    run = True
    
    while run :
        window.blit(MENUBG, (0, 0))
        start_text_L1 = Text("Choose The", TITLE, BLACK, text_position1)
        start_text_L2 = Text("Game Mode", TITLE, BLACK, text_position2)
        resource_text = Text_body("Background music: Music Atelier Amacha", BODY, BROWN, (180, 25))
        start_text_L1.draw(window), start_text_L2.draw(window)
        # 設置人數選擇按鈕的背景
        single_button_rect = MENU_BUTTON[0].get_rect(topleft=(100, 200))
        Duo_button_rect = MENU_BUTTON[0].get_rect(topleft=(100, 400))

        window.blit(MENU_BUTTON[0], single_button_rect.topleft)
        window.blit(MENU_BUTTON[0], Duo_button_rect.topleft)
        
        # 繪製難度選擇按鈕及最高分的文本
        Single_text = Text("Single", HEADING, BROWN, (200, 225))
        resource_text.draw(window)
        Duo_text = Text("Duo", HEADING, BROWN, (200, 425))
        Single_text.draw(window)
        Duo_text.draw(window)



        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == (pygame.QUIT or pygame.K_ESCAPE):
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左鍵點擊
                    mouse_pos = pygame.mouse.get_pos()
                    if single_button_rect.collidepoint(mouse_pos):
                        game_mode = 1
                        difficulty()
                    elif Duo_button_rect.collidepoint(mouse_pos):
                        game_mode = 2
                        game_difficulty = EASY
                        if needintroduo == True:
                            needintroduo = False
                            introduo()
                        else:
                            mainDuo()
    pygame.quit()
    sys.exit()  


# =====

# 遊戲介紹 
def introsingle():
    run = True
    n = 1
    while run:
        if n == 0:
            n = 1
        elif n == 1:
            window.blit(INTRODUCTION[n - 1], (0, 0))  # 第一個畫面部顯示back button
            next_button_rect = MENU_BUTTON[1].get_rect(topleft=(800, 575))
            window.blit(MENU_BUTTON[1], next_button_rect.topleft)
        elif n < len(INTRODUCTION):
            window.blit(INTRODUCTION[n - 1], (0, 0))  # 顯示當前介紹畫面
            next_button_rect = MENU_BUTTON[1].get_rect(topleft=(800, 575))
            back_button_rect = MENU_BUTTON[2].get_rect(topleft=(100, 575))
            window.blit(MENU_BUTTON[1], next_button_rect.topleft)
            window.blit(MENU_BUTTON[2], back_button_rect.topleft)
        else:
            window.blit(INTRODUCTION[-1], (0, 0))  # 如果 n 等於長度，顯示最後一個畫面
            next_button_rect = MENU_BUTTON[3].get_rect(topleft=(800, 575))
            back_button_rect = MENU_BUTTON[2].get_rect(topleft=(100, 575))
            window.blit(MENU_BUTTON[3], next_button_rect.topleft)
            window.blit(MENU_BUTTON[2], back_button_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if next_button_rect.collidepoint(mouse_pos):
                    if n < len(INTRODUCTION):
                        n += 1
                    else:
                        mainsingle()
                elif n != 1 and back_button_rect.collidepoint(mouse_pos) and n > 0:
                    n -= 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if n < len(INTRODUCTION):
                        n += 1
                    else:
                        mainsingle()
                elif event.key == pygame.K_LEFT and n > 0:
                    n -= 1

        pygame.display.update()
    
            
    pygame.quit()
    sys.exit()


def introduo():
    run = True
    n = 1
    while run:
        if n == 0:
            n = 1
        elif n == 1:
            window.blit(INTRODUCTION2[n - 1], (0, 0))  # 第一個畫面不顯示back button
            next_button_rect = MENU_BUTTON[1].get_rect(topleft=(800, 575))
            window.blit(MENU_BUTTON[1], next_button_rect.topleft)
        elif n < len(INTRODUCTION2):
            window.blit(INTRODUCTION2[n - 1], (0, 0))  # 顯示當前介紹畫面
            next_button_rect = MENU_BUTTON[1].get_rect(topleft=(800, 575))
            back_button_rect = MENU_BUTTON[2].get_rect(topleft=(100, 575))
            window.blit(MENU_BUTTON[1], next_button_rect.topleft)
            window.blit(MENU_BUTTON[2], back_button_rect.topleft)
        else:
            window.blit(INTRODUCTION2[-1], (0, 0))  # 如果 n 等於長度，顯示最後一個畫面
            next_button_rect = MENU_BUTTON[3].get_rect(topleft=(800, 575))
            back_button_rect = MENU_BUTTON[2].get_rect(topleft=(100, 575))
            window.blit(MENU_BUTTON[3], next_button_rect.topleft)
            window.blit(MENU_BUTTON[2], back_button_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if next_button_rect.collidepoint(mouse_pos):
                    if n < len(INTRODUCTION2):
                        n += 1
                    else:
                        mainDuo()
                elif n != 1 and back_button_rect.collidepoint(mouse_pos) and n > 0:
                    n -= 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if n < len(INTRODUCTION2):
                        n += 1
                    else:
                        mainDuo()
                elif event.key == pygame.K_LEFT and n > 0:
                    n -= 1

        pygame.display.update()
    

    pygame.quit()
    sys.exit()


def difficulty():
    global game_difficulty
    global TITLE, HEADING, BODY
    global needintrosingle
    
    text_position1 = (650, (window_height//2) - 50)  # For "Choose The"
    text_position2 = (650, (window_height//2) + 50)  # For "Game Difficulty"
    
    run = True
    
    while run :
        window.fill(WHITE)
        window.blit(MENUBG, (0, 0))
        start_text_L1 = Text("Choose The", TITLE, BLACK, text_position1)
        start_text_L2 = Text("Game Difficulty", TITLE, BLACK, text_position2)
        start_text_L1.draw(window), start_text_L2.draw(window)

        # 繪製難度選擇按鈕及框框
        easy_button_rect = MENU_BUTTON[0].get_rect(topleft=(100, 200))
        medium_button_rect = MENU_BUTTON[0].get_rect(topleft=(100, 300))
        hard_button_rect = MENU_BUTTON[0].get_rect(topleft=(100, 400))

        window.blit(MENU_BUTTON[0], easy_button_rect.topleft)
        window.blit(MENU_BUTTON[0], medium_button_rect.topleft)
        window.blit(MENU_BUTTON[0], hard_button_rect.topleft)

        # 繪製難度選擇按鈕及最高分的文本
        easy_text = Text("EASY", HEADING, BROWN, (200, 225))
        medium_text = Text("MEDIUM", HEADING, BROWN, (200, 325))
        hard_text = Text("HARD", HEADING, BROWN, (200, 425))
        
        # 顯示各關目前最高分
        easy_score_list = load_sorted_score_list("1.csv")
        if len(easy_score_list) > 0:
            easy_highest_name = easy_score_list[0][0]
            easy_highest_score = easy_score_list[0][1]
            easy_highest_score_text = Text_body(f"Highest Score: {easy_highest_name} {easy_highest_score}",BODY, BLACK, (200, 185))
        else:
            easy_highest_score_text = Text_body(f"Highest Score: no record", BODY, BLACK, (200, 185))
        medium_score_list = load_sorted_score_list("2.csv")
        if len(medium_score_list) > 0:
            medium_highest_name = medium_score_list[0][0]
            medium_highest_score = medium_score_list[0][1]
            medium_highest_score_text = Text_body(f"Highest Score: {medium_highest_name} {medium_highest_score}",BODY, BLACK, (200, 285))
        else:
            medium_highest_score_text = Text_body(f"Highest Score: no record", BODY, BLACK, (200, 285))
        hard_score_list = load_sorted_score_list("3.csv")
        if len(hard_score_list) > 0:
            hard_highest_name = hard_score_list[0][0]
            hard_highest_score = hard_score_list[0][1]
            hard_highest_score_text = Text_body(f"Highest Score: {hard_highest_name} {hard_highest_score}",BODY, BLACK, (200, 385))
        else:
            hard_highest_score_text = Text_body(f"Highest Score: no record", BODY, BLACK, (200, 385))
        
        easy_text.draw(window)
        medium_text.draw(window)
        hard_text.draw(window)
        easy_highest_score_text.draw(window)
        medium_highest_score_text.draw(window)
        hard_highest_score_text.draw(window)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == (pygame.QUIT or pygame.K_ESCAPE):
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左鍵點擊
                    mouse_pos = pygame.mouse.get_pos()
                    if easy_button_rect.collidepoint(mouse_pos):
                        game_difficulty = EASY
                        if needintrosingle == True:
                            needintrosingle = False
                            introsingle()
                        else:
                            mainsingle()
                    elif medium_button_rect.collidepoint(mouse_pos):
                        game_difficulty = MEDIUM
                        if needintrosingle == True:
                            needintrosingle = False
                            introsingle()
                        else:
                            mainsingle()
                    elif hard_button_rect.collidepoint(mouse_pos):
                        game_difficulty = HARD
                        if needintrosingle == True:
                            needintrosingle = False
                            introsingle()
                        else:
                            mainsingle()
    pygame.quit()
    sys.exit()


def countdown_timer(window, player, bg, x_bg_pos, y_bg_pos, countdown_time=3):
    countdown = countdown_time
    count_down_sound = pygame.mixer.Sound(os.path.join("music/sounds", "count_down.wav"))
    
    while countdown > 0:
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
        player.draw(window)
        pygame.mixer.Channel(2).play(count_down_sound)
        count_text = Text(f"{countdown}", 300, BLACK, (485, 300))
        count_text.draw(window)
        pygame.display.update()
        time.sleep(1)
        countdown -= 1


def pause_game(window, player, bg, x_bg_pos, y_bg_pos):
    image = [pygame.image.load(os.path.join("image/window", "paused_window-2.png")),
             pygame.image.load(os.path.join("image/window", "paused_button-2.png"))]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False, True  # run, restart, exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    return True, False, False
                elif event.key == pygame.K_r:
                    return False, True, False
                elif event.key == pygame.K_e:
                    return False, False, True

        window.blit(image[0], (200, 150))
        paused_button_rect1 = image[1].get_rect(topleft=(280, 198))
        paused_button_rect2 = image[1].get_rect(topleft=(280, 296))
        paused_button_rect3 = image[1].get_rect(topleft=(280, 396))
        window.blit(image[1], paused_button_rect1.topleft)
        window.blit(image[1], paused_button_rect2.topleft)
        window.blit(image[1], paused_button_rect3.topleft)

        continue_text = Text_body("Press k again to continue", TITLE, BLACK, (500, 230))
        restart_text = Text_body("Press r to restart", TITLE, BLACK, (500, 330))
        exit_text = Text_body("Press e to exit", TITLE, BLACK, (500, 430))
        continue_text.draw(window)
        restart_text.draw(window)
        exit_text.draw(window)
        pygame.display.update()


def mainsingle():
    global game_speed, jump_val, points, bg
    
    clock = pygame.time.Clock()
    points = 0
    oripoint = 0
    bg = 0
    player = Charactor1()
    obstacles = []
    blurs = []
    run = True
    x_bg_pos, y_bg_pos = 0, 0
    x_heart, y_heart = 33, 50
    fog = Fog()
    items = []
    paused = False
    restart = False
    exit = False
    itemtype = 0
    count_down_sound = pygame.mixer.Sound(os.path.join("music/sounds", "count_down.wav"))
    small_obstacle_sound = pygame.mixer.Sound(os.path.join("music/sounds", "small.wav"))
    large_obstacle_sound = pygame.mixer.Sound(os.path.join("music/sounds", "big.wav"))
    fly_obstacle_sound = pygame.mixer.Sound(os.path.join("music/sounds", "fly.wav"))
    star_sound = pygame.mixer.Sound(os.path.join("music/sounds", "star.wav"))
    heart_sound = pygame.mixer.Sound(os.path.join("music/sounds", "heart.wav"))
    fog_sound = pygame.mixer.Sound(os.path.join("music/sounds", "blur.wav"))

    if game_difficulty == EASY:
        game_speed = 7
        life_bar = LifeBar(5, x_heart, y_heart)
    elif game_difficulty == MEDIUM:
        game_speed = 10
        life_bar = LifeBar(4, x_heart, y_heart)
    elif game_difficulty == HARD:
        game_speed = 13
        life_bar = LifeBar(3, x_heart, y_heart)

    countdown_timer(window, player, bg, x_bg_pos, y_bg_pos)

    load_bg_music(os.path.join("music", "bg_music_in_game.ogg"))
    pygame.mixer.music.play(-1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    paused, restart, exit = pause_game(window, player, bg, x_bg_pos, y_bg_pos)
                    if restart:
                        mainsingle()
                        return
                    if exit:
                        run = False
                        break

        if not run:
            break

        x_bg_pos -= game_speed
        if oripoint % 800 == 0 and points != 0:
            bg = (bg + 1) % len(BACKGROUND_LIST)
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos + window_width, y_bg_pos))

        if x_bg_pos <= -window_width:
            x_bg_pos = 0

        pause_text = Text_body("press k to pause", SUBHEADING, BLACK, (900, 25))
        pause_text.draw(window)

        life_bar.draw(window, LIFE_BAR)

        if not life_bar.is_alive():
            run = False

        oripoint += 1
        if oripoint % 2 == 0:
            points += 1
        score_position = (115, 25)
        score = Text("Points: " + str(points), SUBHEADING, BLACK, score_position)
        score.draw(window)
        if points % 400 == 0 and game_speed <= 40:
            game_speed += 1

        user_input = pygame.key.get_pressed()
        player.update(user_input)
        player.draw(window)
        
        random_item = random.randint(0, 1)
        if len(items) == 0 and random.randint(0, 1000) < 2 and random_item == 0:
            items.append(Heart(ITEM))
            itemtype = 0
        elif len(items) == 0 and random.randint(0, 1000) < 10 and random_item == 1:
            items.append(star(ITEM))
            itemtype = 1

        for item in items:
            item.update()
            if not item.rect.colliderect(obstacle.rect):
                item.draw(window)
            else:
                items.remove(item)

            if player.ch_rect.colliderect(item.rect):
                if itemtype == 0:
                    life_bar.heal()
                    pygame.mixer.Channel(5).play(heart_sound)
                elif itemtype == 1:
                    pygame.mixer.Channel(6).play(star_sound)
                    player.muteki_time()
                items.remove(item)
            if item.rect.x < -item.rect.width:
                items.remove(item)
                         
        if len(obstacles) == 0:
            rand = random.randint(0, 5)
            if rand == 0 or rand == 1:
                obstacles.append(smallobs(SMALLOBSTACLE))
            elif rand == 2 or rand == 3:
                obstacles.append(largeobs(LARGEOBSTACLE))
            elif rand == 4 or rand == 5:
                obstacles.append(flyobs(FLYOBSTACLE))
        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw(window)
            if player.ch_rect.colliderect(obstacle.rect):
                if player.is_takingdamage() or player.is_invincible():
                    continue
                else:
                    life_bar.take_damage()
                    pygame.mixer.Channel(4).play(large_obstacle_sound)
                    player.take_damage()
            if obstacle.rect.x < -obstacle.rect.width:
                obstacles.remove(obstacle)

        if len(blurs) == 0:
            randfog = random.randint(0, 1000)
            if randfog < 1:
                blurs.append(blurobs(BLUROBSTACLE))
        for blur in blurs:
            blur.update()
            blur.draw(window)
            if blur.rect.colliderect(obstacle.rect):
                blurs.remove(blur)
            if player.ch_rect.colliderect(blur.rect):
                if player.is_takingdamage() or player.is_invincible():
                    continue
                else:
                    pygame.mixer.Channel(3).play(fog_sound)
                    fog.startfog()
                    blurs.remove(blur)
            if blur.rect.x < -blur.rect.width:
                blurs.remove(blur)
        
        
        fog.update()
        if fog.isfog():
            fog.draw(window)


        pygame.display.update()
        clock.tick(60)

    gameover()


def mainDuo():
    global game_speed, points, bg, winner, TITLE, SUBHEADING
    winner = 0
    
    clock = pygame.time.Clock()
    points = 0
    oripoint = 0
    bg = 0
    player1 = Charactor1()
    player2 = Charactor2()
    obstacles1 = []
    obstacles2 = []
    run = True
    x_bg_pos, y_bg_pos = 0, 0
    blurs1 = []
    blurs2 = []
    items1 = []
    items2 = []
    restart = False
    paused = False
    exit = False
    pygame.draw.line(window, BLACK, (0, 325), (1000, 325), 3)
    fog1 = Fog2()
    fog2 = Fog1()

    count_down_sound = pygame.mixer.Sound(os.path.join("music/sounds", "count_down.wav"))
    small_obstacle_sound = pygame.mixer.Sound(os.path.join("music/sounds", "small.wav"))
    large_obstacle_sound = pygame.mixer.Sound(os.path.join("music/sounds", "big.wav"))
    fly_obstacle_sound = pygame.mixer.Sound(os.path.join("music/sounds", "fly.wav"))
    star_sound = pygame.mixer.Sound(os.path.join("music/sounds", "star.wav"))
    heart_sound = pygame.mixer.Sound(os.path.join("music/sounds", "heart.wav"))
    fog_sound = pygame.mixer.Sound(os.path.join("music/sounds", "blur.wav"))
    pygame.mixer.set_num_channels(12)
    if game_difficulty == EASY:
        game_speed = 7
        life_bar1 = LifeBar(5, 33, 340)
        life_bar2 = LifeBar(5, 33, 50)

    countdown_timer(window, player1, bg, x_bg_pos, y_bg_pos)

    load_bg_music(os.path.join("music", "bg_music_in_game.ogg"))
    pygame.mixer.music.play(-1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    paused, restart, exit = pause_game(window, player1, bg, x_bg_pos, y_bg_pos)
                    if restart:
                        mainDuo()
                        return
                    if exit:
                        run = False
                        break

        if not run:
            break

        x_bg_pos -= game_speed
        if oripoint % 3200 == 0 and points != 0:
            bg = (bg + 1) % len(BACKGROUND_LIST_DUO)
        window.blit(BACKGROUND_LIST_DUO[bg], (x_bg_pos, y_bg_pos))
        window.blit(BACKGROUND_LIST_DUO[bg], (x_bg_pos + window_width, y_bg_pos))
        pygame.draw.line(window, BLACK, (0, 325), (1000, 325), 4)
        p1 = Text_body("1P", TITLE, BLACK, (50, 110))
        p2 = Text_body("2P", TITLE, BLACK, (50, 400))
        p1.draw(window)
        p2.draw(window)
        if x_bg_pos <= -window_width:
            window.blit(BACKGROUND_LIST_DUO[bg], (x_bg_pos + window_width, y_bg_pos))
            x_bg_pos = 0

        pause_text = Text_body("press k to pause", SUBHEADING, BLACK, (900, 25))
        pause_text.draw(window)

        life_bar1.draw(window, LIFE_BAR)
        life_bar2.draw(window, LIFE_BAR)

        if not life_bar1.is_alive():
            winner = 2
            run = False

        if not life_bar2.is_alive():
            winner = 1
            run = False

        oripoint += 1
        if oripoint % 2 == 0:
            points += 1
        score_position = (115, 25)
        score = Text("Points: " + str(points), SUBHEADING, BLACK, score_position)
        score.draw(window)
        if points % 200 == 0 and game_speed <= 40:
            game_speed += 1

        user_input = pygame.key.get_pressed()
        player1.update(user_input)
        player1.draw(window)
        player2.update(user_input)
        player2.draw(window)

        if len(obstacles1) == 0:
            rand1 = random.randint(0, 5)
            if rand1 in [0, 1]:
                obstacles1.append(smallobs(SMALLOBSTACLE))
            elif rand1 in [2, 3]:
                obstacles1.append(largeobs(LARGEOBSTACLE))
            else:
                obstacles1.append(flyobs(FLYOBSTACLE))

        for obstacle in obstacles1:
            obstacle.update()
            obstacle.draw(window)
            if player1.ch_rect.colliderect(obstacle.rect):
                if not (player1.is_takingdamage() or player1.is_invincible()):
                    pygame.mixer.Channel(4).play(large_obstacle_sound)
                    life_bar1.take_damage()
                    player1.take_damage()
            if obstacle.rect.x < -obstacle.rect.width:
                obstacles1.remove(obstacle)

        if len(blurs1) == 0:
            if random.randint(0, 1000) < 2:
                blurs1.append(blurobs(BLUROBSTACLE))
        for blur in blurs1:
            blur.update()
            blur.draw(window)
            if player1.ch_rect.colliderect(blur.rect):
                pygame.mixer.Channel(3).play(fog_sound)
                fog1.startfog()
                blurs1.remove(blur)
            if blur.rect.x < -blur.rect.width:
                blurs1.remove(blur)
        fog1.update()
        if fog1.isfog():
            fog1.draw(window)

        if len(obstacles2) == 0:
            rand2 = random.randint(0, 5)
            if rand2 in [0, 1]:
                obstacles2.append(smallobs2(SMALLOBSTACLE))
            elif rand2 in [2, 3]:
                obstacles2.append(largeobs2(LARGEOBSTACLE))
            else:
                obstacles2.append(flyobs2(FLYOBSTACLE))

        for obstacle in obstacles2:
            obstacle.update()
            obstacle.draw(window)
            if player2.ch_rect.colliderect(obstacle.rect):
                if not (player2.is_takingdamage() or player2.is_invincible()):
                    pygame.mixer.Channel(8).play(large_obstacle_sound)
                    life_bar2.take_damage()
                    player2.take_damage()
            if obstacle.rect.x < -obstacle.rect.width:
                obstacles2.remove(obstacle)

        if len(blurs2) == 0:
            if random.randint(0, 1000) < 2:
                blurs2.append(blurobs2(BLUROBSTACLE))
        for blur in blurs2:
            blur.update()
            blur.draw(window)
            if player2.ch_rect.colliderect(blur.rect):
                pygame.mixer.Channel(7).play(fog_sound)
                fog2.startfog()
                blurs2.remove(blur)
            if blur.rect.x < -blur.rect.width:
                blurs2.remove(blur)
        fog2.update()
        if fog2.isfog():
            fog2.draw(window)

        if len(items1) == 0:
            if random.randint(0, 1000) < 2:
                items1.append(Heart(ITEM))
            elif random.randint(0, 1000) < 10:
                items1.append(star(ITEM))
        for item in items1:
            item.update()
            item.draw(window)
            if player1.ch_rect.colliderect(item.rect):
                if isinstance(item, Heart):
                    pygame.mixer.Channel(9).play(heart_sound)
                    life_bar1.heal()
                else:
                    pygame.mixer.Channel(10).play(star_sound)
                    player1.muteki_time()
                items1.remove(item)
            if item.rect.x < -item.rect.width:
                items1.remove(item)

        if len(items2) == 0:
            if random.randint(0, 1000) < 2:
                items2.append(Heart2(ITEM))
            elif random.randint(0, 1000) < 10:
                items2.append(star2(ITEM))
        for item in items2:
            item.update()
            item.draw(window)
            if player2.ch_rect.colliderect(item.rect):
                if isinstance(item, Heart2):
                    pygame.mixer.Channel(5).play(heart_sound)
                    life_bar2.heal()
                else:
                    pygame.mixer.Channel(6).play(star_sound)
                    player2.muteki_time()
                items2.remove(item)
            if item.rect.x < -item.rect.width:
                items2.remove(item)

        pygame.display.update()
        clock.tick(60)

    gameover()


# =====

def enter_your_name(enter_name_text, enter_rect):
    global TITLE, HEADING
    
    name = str()
    entering = False
    finish_enter = False
    x_pos = window_width // 2 - 70
    y_pos = window_height // 2 + 10
    active = True
    cursor_timer = pygame.time.get_ticks()
    name_font = pygame.font.Font('Fonts/AgencyFB-Bold.ttf', TITLE)
    name_surface = name_font.render(name, True, BLACK)
    name_rect = name_surface.get_rect()
    name_rect.bottomleft = (x_pos, y_pos - 10)
    cursor_x, cursor_y = name_rect.topright
    
    while not finish_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左鍵點擊
                    mouse_pos = pygame.mouse.get_pos()
                    if enter_rect.collidepoint(mouse_pos):
                        entering = True
                    else:
                        entering = False
            if entering:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        finish_enter = True
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
        window.fill(WHITE)
        
        finish_text = Text_body("Press Enter when finish entering", HEADING, BLACK, (window_width // 2, window_height // 2 + 50))
        finish_text.draw(window)
        enter_name_text.draw(window)
        pygame.draw.rect(window, WHITE, enter_rect, 2)
        name_surface = name_font.render(name, True, BLACK)
        name_rect = name_surface.get_rect()
        name_rect.bottomleft = (x_pos, y_pos - 10)
        window.blit(name_surface, name_rect)
        cursor_x, cursor_y = name_rect.topright
        current_time = pygame.time.get_ticks()
        if current_time - cursor_timer > 500:  # 每500毫秒切換一次
            active = not active
            cursor_timer = current_time
        if active and entering:
            pygame.draw.line(window, SKYBLUE, (cursor_x, cursor_y + 7), ( cursor_x, cursor_y + 47), 2)
        pygame.display.update()
    return name


# =====

def show_rank(score_list, y_already):
    global TITLE, HEADING, BODY
    
    image = pygame.image.load(os.path.join("image/window", "rank_board-2.png"))

    x_pos = window_width // 2 - 50
    y_pos = 109
    name_font = pygame.font.Font('Fonts/AgencyFB-Bold.ttf', SUBHEADING)
    window.blit(image, (0, 0))
    score_range = int()
    if len(score_list) > 10:
        score_range = 10
    else:
        score_range = len(score_list)
    for i in range(score_range):
        record = f"{score_list[i][0]} {score_list[i][1]}"
        record_surface = name_font.render(record, True, BROWN)
        record_rect = record_surface.get_rect()
        record_rect.bottomleft = (x_pos, y_pos)
        window.blit(record_surface, record_rect)
        y_pos += 54
    n_text_row1 = Text_body("Press Tab again", SUBHEADING, BROWN, (910, 30))
    n_text_row2 = Text_body("to go back", SUBHEADING, BROWN, (935, 70))
    n_text_row1.draw(window), n_text_row2.draw(window)
    pygame.display.update()  
    leave_rank = False
    
    while not leave_rank:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    window.fill(WHITE)
                    if y_already:
                        score_recorded_text = Text("Score recorded!", 80, BLACK, (window_width // 2, window_height // 2 - 100))
                        score_text = Text(f"Your score: {points}", TITLE, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
                        tab_or_n_text = Text_body("Press n to leave / Press Tab to check ranks / Press r to restart", BODY, BLACK, (window_width // 2, window_height // 2 + 50))
                        score_recorded_text.draw(window)
                        score_text.draw(window)
                        tab_or_n_text.draw(window)
                    else:
                        game_over_text = Text("Game Over", 80, BLACK, (window_width // 2, window_height // 2 - 100))  # 顯示 "Game Over" 文字
                        score_text = Text(f"Your score: {points}", TITLE, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
                        record_or_not_text = Text_body("Do you want to record your score?", TITLE, BLACK, (window_width // 2, window_height // 2 + 90))
                        y_or_n_or_tab_text = Text_body("Press y to record / Press n to leave / Press Tab to check ranks / Press r to restart", BODY, BLACK, (window_width // 2, window_height // 2 + 150))
                        game_over_text.draw(window)
                        score_text.draw(window)
                        record_or_not_text.draw(window)
                        y_or_n_or_tab_text.draw(window)
                    pygame.display.update()
                    leave_rank = True
                    break


# =====

def gameover():
    window.fill(WHITE)  # 用白色填充整個視窗
    pygame.mixer.music.stop()
    if game_mode == 1:
        game_over_text = Text("Game Over", 80, BLACK, (window_width // 2, window_height // 2 - 100))  # 顯示 "Game Over" 文字
        score_text = Text(f"Your score: {points}", TITLE, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
        record_or_not_text = Text_body("Do you want to record your score?", TITLE, BLACK, (window_width // 2, window_height // 2 + 90))
        y_or_n_or_tab_text = Text_body("Press y to record / Press n to leave / Press Tab to check ranks / Press r to restart", BODY, BLACK, (window_width // 2, window_height // 2 + 150))
        game_over_text.draw(window)
        score_text.draw(window)
        record_or_not_text.draw(window)
        y_or_n_or_tab_text.draw(window)
        y_already = False
        pygame.display.update()
        score_list = load_sorted_score_list(f"{game_difficulty}.csv")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:  # 如果玩家按下 n 鍵
                        menu()
                    elif event.key == pygame.K_y:  # 如果玩家按下 y 鍵
                        y_already = True
                        window.fill(WHITE)
                        enter_name_text = Text_body("Enter your name: _______________________", TITLE, BLACK, (window_width // 2, window_height // 2 - 30))
                        enter_name_text.draw(window)
                        enter_rect = pygame.Rect(window_width // 2 - 80, window_height // 2 - 50, 450, 47)
                        pygame.draw.rect(window, WHITE, enter_rect, 2)
                        pygame.display.update()
                        name = enter_your_name(enter_name_text, enter_rect)
                        already_record = False
                        already_record_index = int()
                        for i in range(len(score_list)):
                            if score_list[i][0] == name:
                                already_record = True
                                already_record_index = i
                                break
                        if already_record:
                            if points > score_list[already_record_index][1]:
                                score_list[already_record_index][1] = points
                        else:
                            score_list.append([name, points])
                        score_list.sort(key = lambda x:x[1], reverse=True)
                        with open(os.path.join("score", f"{game_difficulty}.csv"), "w", newline="", encoding="utf-8-sig") as file:
                            writer = csv.writer(file)
                            writer.writerows(score_list)
                        file.close()  # 存入分數
                        window.fill(WHITE)
                        score_recorded_text = Text("Score recorded!", 80, BLACK, (window_width // 2, window_height // 2 - 100))
                        score_text = Text(f"Your score: {points}", TITLE, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
                        tab_or_n_text = Text_body("Press n to leave / Press Tab to check ranks / Press r to restart", BODY, BLACK, (window_width // 2, window_height // 2 + 50))
                        score_recorded_text.draw(window)
                        score_text.draw(window)
                        tab_or_n_text.draw(window)
                        pygame.display.update()
                    elif event.key == pygame.K_TAB:
                        show_rank(score_list, y_already)
                    elif event.key == pygame.K_r:
                        mainsingle()

    elif game_mode == 2:
        game_over_text = Text("Game Over", 80, BLACK, (window_width // 2, window_height // 2 - 100))  # 顯示 "Game Over" 文字
        if winner == 1:
            winner_text = Text("winner is 2P", TITLE, BLACK, (window_width // 2, window_height // 2))
        elif winner == 2:  
            winner_text = Text("winner is 1P", TITLE, BLACK, (window_width // 2, window_height // 2))
        elif winner == 0:  
            winner_text = Text("draw", TITLE, BLACK, (window_width // 2, window_height // 2))
    
        continue_text = Text("Press Enter to Continue / Press r to restart", 24, BLACK, (window_width // 2, window_height // 2 + 100))  # 提示玩家按 Enter 鍵繼續
        game_over_text.draw(window)
        winner_text.draw(window)
        continue_text.draw(window)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # 如果玩家按下 Enter 鍵
                        menu()
                    elif event.key == pygame.K_r:
                        mainDuo()


# =====

# 執行程式碼
if __name__ == "__main__":
    initialize_game()
    startpage()
