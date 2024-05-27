# 要先安裝pygame 在終端機輸入 mac :python3 -m pip install -U pygame --user
# windows : py -m pip install -U pygame --user
# 導入函數庫
import pygame
import os
import random
import time
import sys
import csv
# 初始化pygame
def initialize_game():
    pygame.init()

# 顏色
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
SKYBLUE = pygame.Color(0, 127, 255)
# import 圖片檔案
BACKGROUND_LIST = [pygame.image.load(os.path.join("image/background", "3forest.jpg")), pygame.image.load(os.path.join("image/background", "4autumn.jpg"))
                   , pygame.image.load(os.path.join("image/background", "5winter.jpg")), pygame.image.load(os.path.join("image/background", "6city.jpg"))]
CHARACTOR_LIST = [pygame.image.load(os.path.join("image/charactor", "snail-1-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-2-right.png")),]
DAMAGE_LIST = [pygame.image.load(os.path.join("image/charactor", "snail-debuff-1-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-debuff-2-right.png"))]
MUTEKI_LIST =  [pygame.image.load(os.path.join("image/charactor", "snail-invicible-1-right.png")),
                pygame.image.load(os.path.join("image/charactor", "snail-invicible-2-right.png"))]  # 跑步圖片大小 87*94
JUMPING_IMG = pygame.image.load(os.path.join("image/charactor", "snail-jump-right.png"))  # 跳躍圖片大小 87*94
DUCKING_LIST = [pygame.image.load(os.path.join("image/charactor", "snail-hedge-right.png"))]  #  蹲下大小 118*60
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
             pygame.image.load(os.path.join("image/largeobstacle", "obstacle2.png")),
             pygame.image.load(os.path.join("image/largeobstacle", "obstacle3.png"))]
# 小障礙物
SMALLOBSTACLE = [pygame.image.load(os.path.join("image/smallobstacle", "citys.png")),
             pygame.image.load(os.path.join("image/smallobstacle", "obstacle2.png"))]
FLYOBSTACLE = [pygame.image.load(os.path.join("image/flyobstacle", "cityf.png")),
             pygame.image.load(os.path.join("image/flyobstacle", "obstacle2.png"))]
           #  小：68*71 大：99*95 
# 遮蔽視線障礙物
BLUROBSTACLE = [pygame.image.load(os.path.join("image/flyobstacle", "cloud.png"))]
FOG = [pygame.image.load(os.path.join("image/background", "fog.png"))]
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

# 建立視窗(背景長/寬 ＝ 1000/660)
window_height = 650
window_width = 1000
window = pygame.display.set_mode((window_width, window_height))
screen = pygame.display.set_mode((window_width, window_height))
#  難度
EASY = 1
MEDIUM = 2
HARD = 3
game_difficulty = EASY

# 文字處理
class Text:
    def __init__(self, text, size, color, position=(0, 0)):
        self.font = pygame.font.SysFont('freesansbold.ttf', size)  # 字體大小(參數)與字型
        self.surface = self.font.render(text, True, color)  # 印出的字串(參數)與呈現
        self.rect = self.surface.get_rect()  # 文字框起
        self.rect.center = position  # 文字的中心位置(參數)
    def draw(self, screen):
        screen.blit(self.surface, self.rect)
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
        self.image = self.duck_img_list[0]  
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_posduck
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
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
        if user_input[pygame.K_UP] or user_input[pygame.K_SPACE] and not self.ch_jump:
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


    # 目前該做甚麼動作
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
        self.image = self.duck_img_list[0]  
        self.ch_rect = self.image.get_rect()
        self.ch_rect.x = self.x_ch_pos
        self.ch_rect.y = self.y_ch_posduck
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
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


    # 目前該做甚麼動作
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
        self.type = bg  # 三種小仙人掌型態隨機選取一種
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 510 # Y座標位置
class flyobs(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 三種小仙人掌型態隨機選取一種
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 400 # Y座標位置
class largeobs2(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 不同背景不同種類的障礙物
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 200  # Y座標位置
class smallobs2(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 三種小仙人掌型態隨機選取一種
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 210 # Y座標位置
class flyobs2(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 三種小仙人掌型態隨機選取一種
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 100 # Y座標位置
class blurobs(Obstacle):
    def __init__(self, image_list : list):
        self.type = bg  # 三種小仙人掌型態隨機選取一種
        super().__init__(image_list, self.type)  # 繼承障礙物屬性與動作
        self.rect.y = 400 # Y座標位置
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
        self.rect.y = random.randint(150, 310)  # 道具出現的 y 座標
    def update(self):
        self.rect.x -= game_speed  # 道具向左移動的速度
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y)) 
class Coin:
    def __init__(self, image_list: list):
        self.image_list = image_list  # 道具圖片列表
        self.type = 2  # 道具類型，這裡預設為 0
        self.rect = self.image_list[self.type].get_rect()  # 道具的矩形區域
        self.rect.x = window_width  # 道具出現的 x 座標
        self.rect.y = 500 # 道具出現的 y 座標
    def update(self):
        self.rect.x -= game_speed  # 道具向左移動的速度
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))  # 繪製道具
class fog:
    def __init__(self, image_list: list):
        self.image_list = image_list  # 道具圖片列表
        self.type = 0  # 道具類型，這裡預設為 0
        self.rect = self.image_list[self.type].get_rect()  # 道具的矩形區域
        self.rect.x = window_width  # 道具出現的 x 座標
        self.rect.y = 0 # 道具出現的 y 座標
    def update(self):
        self.rect.x -= game_speed  # 道具向左移動的速度
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image_list[self.type], (self.rect.x, self.rect.y))  # 繪製道具


#  標題目錄
def menu():
    global game_difficulty
    global game_mode

    text_position = (600, window_height // 2) # 螢幕中心
    run = True
    while run :
        window.fill(WHITE)
        window.blit(BACKGROUND_LIST[0], (0, 0))
        start_text = Text("Choose the Game mode", 40, BLACK, text_position)
        start_text.draw(window)
        # 繪製人數選擇區域
        single_button_rect = pygame.Rect(100, 200, 200, 50)
        Duo_button_rect = pygame.Rect(100, 400, 200, 50)

        pygame.draw.rect(window, BLACK, single_button_rect, 2)
        pygame.draw.rect(window, BLACK, Duo_button_rect, 2)
        # 繪製難度選擇按鈕及最高分的文本
        Single_text = Text("Single", 30, BLACK, (200, 225))
        
        Duo_text = Text("Duo", 30, BLACK, (200, 425))
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
                        mainDuo()

 
    pygame.quit()
    sys.exit()
def difficulty():
    global game_difficulty
    text_position = (600, window_height // 2) # 螢幕中心
    run = True
    while run :
        window.fill(WHITE)
        window.blit(BACKGROUND_LIST[0], (0, 0))
        start_text = Text("Choose the Game Difficulty", 40, BLACK, text_position)
        start_text.draw(window)

        # 繪製難度選擇按鈕及框框
        easy_button_rect = pygame.Rect(100, 200, 200, 50)
        medium_button_rect = pygame.Rect(100, 300, 200, 50)
        hard_button_rect = pygame.Rect(100, 400, 200, 50)

        pygame.draw.rect(window, BLACK, easy_button_rect, 2)
        pygame.draw.rect(window, BLACK, medium_button_rect, 2)
        pygame.draw.rect(window, BLACK, hard_button_rect, 2)

        # 繪製難度選擇按鈕及最高分的文本
        easy_text = Text("EASY", 30, BLACK, (200, 225))
        medium_text = Text("MEDIUM", 30, BLACK, (200, 325))
        hard_text = Text("HARD", 30, BLACK, (200, 425))
        
        # 顯示各關目前最高分
        easy_score_list = load_sorted_score_list("1.csv")
        if len(easy_score_list) > 0:
            easy_highest_name = easy_score_list[0][0]
            easy_highest_score = easy_score_list[0][1]
            easy_highest_score_text = Text(f"Highest Score: {easy_highest_name} {easy_highest_score}",30, BLACK, (200, 185))
        else:
            easy_highest_score_text = Text(f"Highest Score: no record", 30, BLACK, (200, 185))
        medium_score_list = load_sorted_score_list("2.csv")
        if len(medium_score_list) > 0:
            medium_highest_name = medium_score_list[0][0]
            medium_highest_score = medium_score_list[0][1]
            medium_highest_score_text = Text(f"Highest Score: {medium_highest_name} {medium_highest_score}",30, BLACK, (200, 285))
        else:
            medium_highest_score_text = Text(f"Highest Score: no record", 30, BLACK, (200, 285))
        hard_score_list = load_sorted_score_list("3.txt")
        if len(hard_score_list) > 0:
            hard_highest_name = hard_score_list[0][0]
            hard_highest_score = hard_score_list[0][1]
            hard_highest_score_text = Text(f"Highest Score: {hard_highest_name} {hard_highest_score}",30, BLACK, (200, 385))
        else:
            hard_highest_score_text = Text(f"Highest Score: no record", 30, BLACK, (200, 385))
        
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
                        mainsingle()
                    elif medium_button_rect.collidepoint(mouse_pos):
                        game_difficulty = MEDIUM
                        mainsingle()
                    elif hard_button_rect.collidepoint(mouse_pos):
                        game_difficulty = HARD
                        mainsingle()
# 主程式
def mainsingle():
    global game_speed
    global jump_val
    global points
    global bg
    clock = pygame.time.Clock()
    points = 0
    oripoint = 0
    bg = 0
    player = Charactor1()
    obstacles = []
    run = True
    x_bg_pos, y_bg_pos = 0, 0
    x_heart, y_heart = 33, 50
    items = []
    countdown = 3
    paused = False
    restart = False
    exit = False
    
    while countdown > 0:
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
        player.draw(window)
        count_text = Text(f"{countdown}", 300, BLACK, (485, 300))
        count_text.draw(window)
        pygame.display.update()
        time.sleep(1)
        countdown -= 1
#  難度調整
    if game_difficulty == EASY:
        game_speed = 7
        life = 5
    elif game_difficulty == MEDIUM:
        game_speed = 10
        life = 4
    elif game_difficulty == HARD:
        game_speed = 13
        life = 3
    
 #  開始迴圈
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    if paused:
                        countdown = 3
                        while countdown > 0:
                            window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
                            window.blit(BACKGROUND_LIST[bg], (x_bg_pos + window_width, y_bg_pos))
                            player.draw(window)
                            count_text = Text(f"{countdown}", 300, BLACK, (485, 300))
                            count_text.draw(window)
                            pygame.display.update()
                            time.sleep(1)
                            countdown -= 1
                    paused = not paused
                elif event.key == pygame.K_r and paused:
                    restart = True
                    initialize_game()
                elif event.key == pygame.K_e and paused:
                    exit = True
        if restart:
            mainsingle()
        if exit:
            break
        if paused:
            image = pygame.image.load(os.path.join("image/window", "paused_window.png"))
            window.blit(image, (200,150))
            continue_text = Text("press k again to continue", 50, BLACK, (500, 230))
            restart_text = Text("press r to restart", 50, BLACK, (500, 330))
            exit_text =  Text("press e to exit", 50, BLACK, (500, 430))
            continue_text.draw(window)
            restart_text.draw(window)
            exit_text.draw(window)
            pygame.display.update()
            continue

#  背景移動
        x_bg_pos -= game_speed 
        if oripoint % 3200 == 0 and points != 0: 
            bg = (bg + 1) % len(BACKGROUND_LIST)
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos + window_width, y_bg_pos))

        if x_bg_pos <= -window_width:
            window.blit(BACKGROUND_LIST[bg], (x_bg_pos + window_width, y_bg_pos))
            x_bg_pos = 0
# 暫停文字提示
        pause_text = Text("press k to pause", 30, BLACK, (890, 20))
        pause_text.draw(window)
#  生命值 

        if life == 5:
            window.blit(LIFE_BAR[5], (x_heart, y_heart))
        elif life == 4:
            window.blit(LIFE_BAR[4], (x_heart, y_heart))
        elif life == 3:
            window.blit(LIFE_BAR[3], (x_heart, y_heart))
        elif life == 2:
            window.blit(LIFE_BAR[2], (x_heart, y_heart))
        elif life == 1:
            window.blit(LIFE_BAR[1], (x_heart, y_heart))
        elif life == 0:
            window.blit(LIFE_BAR[0], (x_heart, y_heart))
            run = False
#  分數計算
        oripoint +=1
        if oripoint % 2 == 0:
            points += 1
        score_position = (80, 20)
        score = Text("Points: " + str(points), 30, BLACK, score_position)
        score.draw(window)
        if points % 400 == 0 and game_speed <= 40:
            game_speed += 1
#  角色操作
        user_input = pygame.key.get_pressed()  # 接收玩家指令
        player.update(user_input)  # 依據玩家指令更新恐龍的動作
        player.draw(window)  
#  障礙物
        if len(obstacles) == 0:  # 生成障礙物
            rand = random.randint(0, 6)
            if rand == 0 or rand == 1:
                obstacles.append(smallobs(SMALLOBSTACLE))
                obstacletype = 0
            elif rand == 2 or rand == 3:
                obstacles.append(largeobs(LARGEOBSTACLE))
                obstacletype = 0
            elif rand == 4 or rand == 5:
                obstacles.append(flyobs(FLYOBSTACLE))
                obstacletype = 0
            else:
                obstacles.append(blurobs(BLUROBSTACLE))
                obstacletype = 1

        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw(window)
            if player.ch_rect.colliderect(obstacle.rect): 
                if player.is_takingdamage() or player.is_invincible():
                    continue
                elif obstacletype == 1:
                    fog(FOG).draw(window)
                    fog(FOG).update()
                    obstacles.remove(obstacle)
                else:
                    life -= 1
                    player.take_damage()

            if obstacle.rect.x < -obstacle.rect.width:
                obstacles.remove(obstacle)
#  道具
        random_item = random.randint(0, 1)
    # 在遊戲迴圈中生成道具
        if len(items) == 0 and random.randint(0, 1000) < 2 and random_item == 0:  # 機率2%
            items.append(Heart(ITEM))
            itemtype = 0  # 加入新的道具到道具列表中
        elif len(items) == 0 and random.randint(0, 1000) < 10 and random_item == 1:  # 機率1%
            items.append(star(ITEM))  # 加入新的道具到道具列表中
            itemtype = 1
    # 在遊戲迴圈中更新和繪製道具
        for item in items:
            item.update()
            if item.rect.colliderect(obstacle.rect) == False:
                item.draw(window)
            else:
                items.remove(item)

    # 檢測角色和道具的碰撞
            if player.ch_rect.colliderect(item.rect) and itemtype == 0:
                if life < 5:
                    life += 1  # 增加生命值
                items.remove(item)  # 移除已經碰撞的道具
            elif player.ch_rect.colliderect(item.rect) and itemtype == 1:
                player.muteki_time()
                items.remove(item) 
            if item.rect.x < -item.rect.width:
                items.remove(item)
          # coin main


        pygame.display.update()

        clock.tick(60)

    gameover()
def mainDuo():
    global game_speed
    global jump_val
    global points
    global bg
    global winner
    mid = (window_width//2, window_height//2)
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
    x_heart2, y_heart2 = 33, 50
    x_heart1, y_heart1 = 33, 375
    items1 = []
    items2 = []
    countdown = 3
    restart = False
    paused = False
    exit = False
    pygame.draw.line(window, BLACK, (0, 325), (1000, 325), 3)


    while countdown > 0:
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
        player1.draw(window)
        player2.draw(window)
        count_text = Text(f"{countdown}", 300, BLACK, (485, 300))
        count_text.draw(window)
        pygame.display.update()
        time.sleep(1)
        countdown -= 1
#  難度調整
    if game_difficulty == EASY:
        game_speed = 7
        life1 = 5
        life2 = 5
    
   
    
 #  開始迴圈
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    if paused:
                        countdown = 3
                        while countdown > 0:
                            window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
                            window.blit(BACKGROUND_LIST[bg], (x_bg_pos + window_width, y_bg_pos))
                            player1.draw(window)
                            player2.draw(window)
                            count_text = Text(f"{countdown}", 300, BLACK, (485, 300))
                            count_text.draw(window)
                            pygame.display.update()
                            time.sleep(1)
                            countdown -= 1
                    paused = not paused
                elif event.key == pygame.K_r and paused:
                    restart = True
                    initialize_game()
                elif event.key == pygame.K_e and paused:
                    exit = True
        if restart:
            mainDuo()
        if exit:
            winner = 0
            break
        if paused:
            image = pygame.image.load(os.path.join("image/window", "paused_window.png"))
            window.blit(image, (200,150))
            continue_text = Text("press k again to continue", 50, BLACK, (500, 230))
            restart_text = Text("press r to restart", 50, BLACK, (500, 330))
            exit_text =  Text("press e to exit", 50, BLACK, (500, 430))
            continue_text.draw(window)
            restart_text.draw(window)
            exit_text.draw(window)
            pygame.display.update()
            continue
#  背景移動
        x_bg_pos -= game_speed 
        if oripoint % 3200 == 0 and points != 0: 
            bg = (bg + 1) % len(BACKGROUND_LIST)
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos, y_bg_pos))
        window.blit(BACKGROUND_LIST[bg], (x_bg_pos + window_width, y_bg_pos))
        pygame.draw.line(window, BLACK, (0, 325), (1000, 325), 4)

        if x_bg_pos <= -window_width:
            window.blit(BACKGROUND_LIST[bg], (x_bg_pos + window_width, y_bg_pos))
            x_bg_pos = 0
            
# 暫停文字提示
        pause_text = Text("press k to pause", 30, BLACK, (890, 20))
        pause_text.draw(window) 
#  生命值 

        if life1 == 5:
            window.blit(LIFE_BAR[5], (x_heart1, y_heart1))
        elif life1 == 4:
            window.blit(LIFE_BAR[4], (x_heart1, y_heart1))
        elif life1 == 3:
            window.blit(LIFE_BAR[3], (x_heart1, y_heart1))
        elif life1 == 2:
            window.blit(LIFE_BAR[2], (x_heart1, y_heart1))
        elif life1 == 1:
            window.blit(LIFE_BAR[1], (x_heart1, y_heart1))
        elif life1 == 0:
            window.blit(LIFE_BAR[0], (x_heart1, y_heart1))
            winner = 2
            run = False

        if life2 == 5:
            window.blit(LIFE_BAR[5], (x_heart2, y_heart2))
        elif life2 == 4:
            window.blit(LIFE_BAR[4], (x_heart2, y_heart2))
        elif life2 == 3:
            window.blit(LIFE_BAR[3], (x_heart2, y_heart2))
        elif life2 == 2:
            window.blit(LIFE_BAR[2], (x_heart2, y_heart2))
        elif life2 == 1:
            window.blit(LIFE_BAR[1], (x_heart2, y_heart2))
        elif life2 == 0:
            window.blit(LIFE_BAR[0], (x_heart2, y_heart2))
            winner = 1
            run = False

        
#  分數計算
        oripoint +=1
        if oripoint % 2 == 0:
            points += 1
        score_position = (80, 20)
        score = Text("Points: " + str(points), 30, BLACK, score_position)
        score.draw(window)
        if points % 200 == 0 and game_speed <= 40:
            game_speed += 1
#  角色操作
        user_input = pygame.key.get_pressed()  # 接收玩家指令
        player1.update(user_input)  # 依據玩家指令更新的動作
        player1.draw(window)  
        user_input = pygame.key.get_pressed()  # 接收玩家指令
        player2.update(user_input)  # 依據玩家指令更新的動作
        player2.draw(window)  
#  障礙物
        if len(obstacles1) == 0:  # 生成障礙物
            rand = random.randint(0, 2)
            if rand == 0:
                obstacles1.append(smallobs(SMALLOBSTACLE))
            elif rand == 1:
                obstacles1.append(largeobs(LARGEOBSTACLE))
            elif rand == 2:
                obstacles1.append(flyobs(FLYOBSTACLE))

        for obstacle in obstacles1:
            obstacle.update()
            obstacle.draw(window)
            if player1.ch_rect.colliderect(obstacle.rect): 
                if player1.is_invincible() or player1.is_takingdamage():
                    continue
                else:
                    life1 -= 1
                    player1.take_damage()

            if obstacle.rect.x < -obstacle.rect.width:
                obstacles1.remove(obstacle)

        if len(obstacles2) == 0:  # 生成障礙物
            rand = random.randint(0, 2)
            if rand == 0:
                obstacles2.append(smallobs2(SMALLOBSTACLE))
            elif rand == 1:
                obstacles2.append(largeobs2(LARGEOBSTACLE))
            elif rand == 2:
                obstacles2.append(flyobs2(FLYOBSTACLE))

        for obstacle in obstacles2:
            obstacle.update()
            obstacle.draw(window)
            if player2.ch_rect.colliderect(obstacle.rect): 
                if player2.is_invincible() or player2.is_takingdamage():
                    continue
                else:
                    life2 -= 1
                    player2.take_damage()

            if obstacle.rect.x < -obstacle.rect.width:
                obstacles2.remove(obstacle)
#  道具
        random_item1 = random.randint(0, 1)
    # 在遊戲迴圈中生成道具
        if len(items1) == 0 and random.randint(0, 1000) < 2 and random_item1 == 0:  # 機率2%
            items1.append(Heart(ITEM))
            itemtype1 = 0  # 加入新的道具到道具列表中
        elif len(items1) == 0 and random.randint(0, 1000) < 10 and random_item1 == 1:  # 機率1%
            items1.append(star(ITEM)) 
            itemtype1 = 1 # 加入新的道具到道具列表中


    # 在遊戲迴圈中更新和繪製道具
        for item in items1:
            item.update()
            if item.rect.colliderect(obstacle.rect) == False:
                item.draw(window)
            else:
                items1.remove(item)

    # 檢測角色和道具的碰撞
            if player1.ch_rect.colliderect(item.rect) and itemtype1 == 0:
                if life1 < 5:
                    life1 += 1  # 增加生命值
                items1.remove(item)  # 移除已經碰撞的道具
            elif player1.ch_rect.colliderect(item.rect) and itemtype1 == 1:
                player1.muteki_time()
                items1.remove(item) 
            if item.rect.x < -item.rect.width:
                items1.remove(item)
# 玩家二在遊戲迴圈中生成道具
        random_item2 = random.randint(0, 1)
        if len(items2) == 0 and random.randint(0, 1000) < 2 and random_item2 == 0:  # 機率2%
            items2.append(Heart2(ITEM))
            itemtype2 = 0  # 加入新的道具到道具列表中
        elif len(items2) == 0 and random.randint(0, 1000) < 10 and random_item2 == 1:  # 機率1%
            items2.append(star2(ITEM))
            itemtype2 = 1  # 加入新的道具到道具列表中


    # 在遊戲迴圈中更新和繪製道具
        for item in items2:
            item.update()
            if item.rect.colliderect(obstacle.rect) == False:
                item.draw(window)
            else:
                items2.remove(item)

    # 檢測角色和道具的碰撞
            if player2.ch_rect.colliderect(item.rect) and itemtype2 == 0:
                if life2 < 5:
                    life2 += 1  # 增加生命值
                items2.remove(item)  # 移除已經碰撞的道具
            elif player2.ch_rect.colliderect(item.rect) and itemtype2 == 1:
                player2.muteki_time()
                items2.remove(item) 
            if item.rect.x < -item.rect.width:
                items2.remove(item)
          # coin main


        pygame.display.update()

        clock.tick(60)

    gameover()

def enter_your_name(enter_name_text, enter_rect):
    name = str()
    entering = False
    finish_enter = False
    x_pos = window_width // 2 - 70
    y_pos = window_height // 2
    active = True
    cursor_timer = pygame.time.get_ticks()
    name_font = pygame.font.SysFont('freesansbold.ttf', 30)
    name_surface = name_font.render(name, True, BLACK)
    name_rect = name_surface.get_rect()
    name_rect.bottomleft = (x_pos, y_pos + 10)
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
        finish_text = Text("Press Enter when finish entering", 30, BLACK, (window_width // 2, window_height // 2 + 50))
        finish_text.draw(window)
        enter_name_text.draw(window)
        pygame.draw.rect(window, WHITE, enter_rect, 2)
        name_surface = name_font.render(name, True, BLACK)
        name_rect = name_surface.get_rect()
        name_rect.bottomleft = (x_pos, y_pos + 10)
        window.blit(name_surface, name_rect)
        cursor_x, cursor_y = name_rect.topright
        current_time = pygame.time.get_ticks()
        if current_time - cursor_timer > 500:  # 每500毫秒切換一次
            active = not active
            cursor_timer = current_time
        if active and entering:
            pygame.draw.line(window, SKYBLUE, (cursor_x + 2, cursor_y), ( cursor_x + 2, cursor_y + 20), 2)
        pygame.display.update()
    return name

def show_rank(score_list, y_already):
    x_pos = 50
    y_pos = 70
    name_font = pygame.font.SysFont('freesansbold.ttf', 30)
    window.fill(WHITE)
    for i in range(len(score_list)):
        record = f"{i + 1}: {score_list[i][0]} {score_list[i][1]}"
        record_surface = name_font.render(record, True, BLACK)
        record_rect = record_surface.get_rect()
        record_rect.topleft = (x_pos, y_pos)
        window.blit(record_surface, record_rect)
        y_pos += 40
        if (i + 1) % 14 == 0:
            x_pos += 250
            y_pos = 70
    n_text = Text("Press Tab again to go back", 30, BLACK, (820, 20))
    n_text.draw(window)
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
                        score_text = Text(f"Your score: {points}", 40, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
                        tab_or_n_text = Text("Press n to leave / Press Tab to check ranks", 30, BLACK, (window_width // 2, window_height // 2 + 50))
                        score_recorded_text.draw(window)
                        score_text.draw(window)
                        tab_or_n_text.draw(window)
                    else:
                        game_over_text = Text("Game Over", 80, BLACK, (window_width // 2, window_height // 2 - 100))  # 顯示 "Game Over" 文字
                        score_text = Text(f"Your score: {points}", 40, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
                        record_or_not_text = Text("Do you want to record your score?", 40, BLACK, (window_width // 2, window_height // 2 + 50))
                        y_or_n_or_tab_text = Text("Press y to record / Press n to leave / Press Tab to check ranks", 30, BLACK, (window_width // 2, window_height // 2 + 90))
                        game_over_text.draw(window)
                        score_text.draw(window)
                        record_or_not_text.draw(window)
                        y_or_n_or_tab_text.draw(window)
                    pygame.display.update()
                    leave_rank = True
                    break
    
def gameover():
    window.fill(WHITE)  # 用白色填充整個視窗
    if game_mode == 1:
        game_over_text = Text("Game Over", 80, BLACK, (window_width // 2, window_height // 2 - 100))  # 顯示 "Game Over" 文字
        score_text = Text(f"Your score: {points}", 40, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
        record_or_not_text = Text("Do you want to record your score?", 40, BLACK, (window_width // 2, window_height // 2 + 50))
        y_or_n_or_tab_text = Text("Press y to record / Press n to leave / Press Tab to check ranks", 30, BLACK, (window_width // 2, window_height // 2 + 90))
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
                        enter_name_text = Text("Enter your name: ______________________________", 30, BLACK, (window_width // 2, window_height // 2))
                        enter_name_text.draw(window)
                        enter_rect = pygame.Rect(window_width // 2 - 80, window_height // 2 - 20, 335, 40)
                        pygame.draw.rect(window, WHITE, enter_rect, 2)
                        pygame.draw.line(window, SKYBLUE, (window_width // 2 - 70, window_height // 2 + 10), (window_width // 2 - 70, window_height // 2 - 10), 2)
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
                        score_text = Text(f"Your score: {points}", 40, BLACK, (window_width // 2, window_height // 2))  # 顯示分數
                        tab_or_n_text = Text("Press n to leave / Press Tab to check ranks", 30, BLACK, (window_width // 2, window_height // 2 + 50))
                        score_recorded_text.draw(window)
                        score_text.draw(window)
                        tab_or_n_text.draw(window)
                        pygame.display.update()
                    elif event.key == pygame.K_TAB:
                        show_rank(score_list, y_already)

    elif game_mode == 2:
        game_over_text = Text("Game Over", 80, BLACK, (window_width // 2, window_height // 2 - 100))  # 顯示 "Game Over" 文字
        if winner == 1:
            winner_text = Text("winner is 1P", 40, BLACK, (window_width // 2, window_height // 2))
        elif winner == 2:  
            winner_text = Text("winner is 2P", 40, BLACK, (window_width // 2, window_height // 2))
        elif winner == 0:  
            winner_text = Text("draw", 40, BLACK, (window_width // 2, window_height // 2))
    
        continue_text = Text("Press Enter to Continue", 30, BLACK, (window_width // 2, window_height // 2 + 100))  # 提示玩家按 Enter 鍵繼續
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

# 執行程式碼
if __name__ == "__main__":
    initialize_game()
    menu()
