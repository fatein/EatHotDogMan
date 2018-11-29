import random
import pygame
#设置屏幕大小常量
SCREEN_RECT = pygame.Rect(0,0,480,700)#矩阵对象
#设置刷新的帧率
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#热狗机发射面包
FIRE_HOTDOG_EVENT = pygame.USEREVENT +1
#
#精灵类
#注意:当继承的类不是基类(object)时,一定要调用下父类的init方法,让父类中init的代码能够正常执行
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		#调用父类的方法
		super().__init__()
		#定义对象的属性
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()#返回精灵图片的大小
		self.speed = speed
	def update(self):#重写父类的update
		#精灵在背景垂直方向上移动
		self.rect.y += self.speed


class Background(GameSprite):#游戏背景精灵

	def update(self):
		#1.调用父类的垂直移动方法
		super().update()
		#2.判断是背景否移出屏幕
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height


class HotdogMan(GameSprite):#吃热狗的勇士
	def __init__(self):
		#1.调用父类方法,创建勇士精灵,同时指定勇士图片
		super().__init__("./resource/img/wang.png")
		#2.指定勇士的初始随机速度
		self.speed = random.randint(0,5)
		#3.指定勇士的初始随机位置,bottom属性让勇士的缓缓进入屏幕,竖直方向
		self.rect.bottom = 0
		#3.1 水平方向的随机
		max_x = SCREEN_RECT.width-self.rect.width
		self.rect.x = random.randint(0,max_x)
		pass
	def update(self):
		#1.调用父类方法,保持垂直方向的飞行
		super().update()
		#2.判断是否飞出屏幕,若是删除该对象
		if self.rect.y >= SCREEN_RECT.height:
			#kill方法可以将精灵从所有精灵组中移除,精灵就会被自动销毁
			self.kill()
	def __del__(self):
		pass


class hotGogMachine(GameSprite):
	#热狗机
	def __init__(self):
		#1.调用父类方法,设置图片和速度,默认是不会移动的需要用户控制才会移动
		super().__init__("./resource/img/hotDogMachine.png",0)
		#2.设置热狗机的初始位置(距底部120px,在x轴的中间
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom-80
		#3.创建子弹的精灵组
		self.Breads = pygame.sprite.Group()
	def update(self):

		#热狗机在水平方向移动
		self.rect.x += self.speed
		#判断热狗机不能离开屏幕
		if self.rect.x < 0 :
			self.rect.x = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		##热狗机在竖直方向移动
		#self.rect.y = -self.speed
	#热狗机发射面包
	def fire_hotDog(self):
			#1.创建子弹精灵
			bread = Bread()
			#2.设置精灵位置
			bread.rect.bottom = self.rect.y + 30
			bread.rect.centerx = self.rect.centerx
			#3.将精灵添加到精灵组
			self.Breads.add(bread)
class Bread(GameSprite):#面包为子弹
	def __init__(self):
		#调用父类方法设置子弹图片,设置初始子弹速度
		super().__init__("./resource/img/zidan.png",-2)
	def update(self):
		#调用父类方法,让子弹垂直飞行
		super().update()
		#判断子弹是否飞出屏幕
		if self.rect.bottom < 0:
			self.kill()



