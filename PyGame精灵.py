#PyGamw 精灵pygame.sprite.Sprite
import pygame,sys
from random import  *
import time
pygame.init()
class Car(pygame.sprite.Sprite):
	id=0
	def __init__(self,filename,initial_position,speed):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(filename)
		self.rect=self.image.get_rect()
		self.rect.topleft=initial_position
		self.speed=speed
		self.id=Car.id
		self.life=0
		Car.id+=1
	def move(self):
		self.rect=self.rect.move(self.speed)
		if self.rect.left<=00 or self.rect.right>=640:
			self.speed[0]*=-1
		if self.rect.top<=0 or self.rect.bottom>=480:
			self.speed[1]*=-1
	@staticmethod
	def distance(item,others):
		for i in others:
			distance=(item.rect.center[0]-i.rect.center[0])**2+(item.rect.center[1]-i.rect.center[1])**2
			if distance<111**2:
				item.speed[0]*=-1
				item.speed[1]*=-1
				return True
width,height=960,480
screen=pygame.display.set_mode([width,height])
screen.fill([0,0,0])
fi='C:/Users/Administrator/PYG02-ball.gif'

#Cargroup=pygame.sprite.Group()
Cargroup=[]
n=2
locationgroup=([0,0],[350,300],[100,200],[44,68])
for i in range(n):
	ball=Car(fi,[randint(0,width-111),randint(0,height-111)],[randint(-10,10),randint(-10,10)])
	while Car.distance(ball,Cargroup):
		ball.rect.topleft=randint(0,width-111),randint(0,height-111)
	Cargroup.append(ball)
	

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
	screen.fill([0,0,0])
	time.sleep(0.04)
	# for i in range(3):
		# for j in range(3):
			# if i!=j:
				# print(i,j)
	#for i in range(len(Cargroup.sprites())):
	# Cargroup.sprites()[0].distance([Cargroup.sprites()[1],Cargroup.sprites()[2]])
	# Cargroup.sprites()[1].distance([Cargroup.sprites()[0],Cargroup.sprites()[2]])
	#Cargroup.sprites()[2].distance([Cargroup.sprites()[1],Cargroup.sprites()[0]])
	# i=0
	for carlist in Cargroup:
		carlist.move()
		screen.blit(carlist.image,carlist.rect)
	for i in range(n):
		item=Cargroup.pop(i)
		#print(item)
		Car.distance(item,Cargroup)
		Cargroup.insert(i,item)

	pygame.display.update()


