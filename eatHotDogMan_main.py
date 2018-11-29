import pygame
from eatHotDogman import *
class PlayHotDogMan(object):
    def __init__(self):
        #添加游戏背景音乐
        filename = './resource/mp3/bg.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(1)
        #1.创建游戏窗口
        # set_mode(resolution=(0,0),flags=0,depth=0)
        # resolution 指定游戏窗口的大小,默认窗口和屏幕大小一致,flags:屏幕附加选项,如全屏,默认不需要传递,depth:颜色的位数,默认自动匹配
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 创建游戏窗口,480 * 700 像素的大小
        # pygame.rect用来描述矩形区域,Rect(x,y,width,height),该方法不需要init()方法初始化,就能直接使用
        # Rect的size属性返回一个元组,第一个为宽,第二个为高

        # 设置窗体名字
        pygame.display.set_caption("Design by Sweet")

        #2.创建游戏时钟
        self.clock = pygame.time.Clock()

        #3.调用私有方法创建精灵和精灵组的创建
        self.__create_sprites()

        #设置定时器事件,--创建敌机--1s一个
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#1000为毫秒
        #自动发射热狗,500毫秒一个
        pygame.time.set_timer(FIRE_HOTDOG_EVENT,1000)
    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg = Background("./resource/img/bg.jpg")
        bg_copy = Background("./resource/img/bg_copy.jpg")
        bg_copy.rect.y = -bg_copy.rect.height#第二张背景图在第一张的正上方
        self.back_group = pygame.sprite.Group(bg,bg_copy)

        #创建勇士的精灵组
        self.man_group = pygame.sprite.Group()

        #创建热狗机的精灵和精灵组
        self.Machine = hotGogMachine()
        self.Machine_group = pygame.sprite.Group(self.Machine)

    def start_game(self):
        while True:
            #1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #2.事件监听
            self.__event_handler__()
            #3.碰撞检测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()
            pass
    #事件监听方法
    def __event_handler__(self):
        for event in pygame.event.get():  # 返回值为列表
            # 判断事件类型是否是退出
            if event.type == pygame.QUIT:
                print("游戏退出")
                # quit 卸载所有游戏模块
                pygame.quit()
                # exit 直接退出系统,终止程序的执行
                exit();
            elif event.type == CREATE_ENEMY_EVENT:
                #1.创建勇士精灵
                Man = HotdogMan()
                #2.添加精灵到精灵组
                self.man_group.add(Man)
            elif event.type == FIRE_HOTDOG_EVENT:
                self.Machine.fire_hotDog()

            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
               # print("向右") 不能识别连续按键
        #使用键盘提供的方法获取键盘的按键--返回值为元组
        key_pressed = pygame.key.get_pressed()
        #判断元组中对应按键的索引值,值为1表示安下,支持持续按键
        if key_pressed[pygame.K_a]:#a键左移
            self.Machine.speed = -5
        elif key_pressed[pygame.K_d]:#d键右移
            self.Machine.speed = 5
        elif key_pressed[pygame.K_w]:  # d键上移
            #self.Machine.speed = 5
            print("d键安下")
        elif key_pressed[pygame.K_s]:  # s键下移
            print("s键安下")
            #self.Machine.speed = 5
        else:#其他键无反应
            self.Machine.speed = 0
    #碰撞检测方法
    def __check_collide(self):
        #1.面包击退勇士
        pygame.sprite.groupcollide(self.Machine.Breads,self.man_group,True,True)
        #2.勇士撞毁热狗机
        #enem = pygame.sprite.spritecollide(self.Machine,self.man_group,True,True)
        #if len(enem) > 0:
           # self.Machine.kill()
            #PlayHotDogMan.__game_over()
    #更新/绘制精灵组方法
    def __update_sprites(self):
        #更新屏幕背景
        self.back_group.update()
        #绘制屏幕背景
        self.back_group.draw(self.screen)
        #更新勇士
        self.man_group.update()
        #绘制勇士
        self.man_group.draw(self.screen)
        #更新热狗机
        self.Machine_group.update()
        #绘制热狗机
        self.Machine_group.draw(self.screen)
        #更新面包精灵
        self.Machine.Breads.update()
        #绘制面包精灵组
        self.Machine.Breads.draw(self.screen)
    @staticmethod
    def __game_over():
        print("game over")
        exit()

if __name__ == '__main__':
    game = PlayHotDogMan()
    game.start_game()