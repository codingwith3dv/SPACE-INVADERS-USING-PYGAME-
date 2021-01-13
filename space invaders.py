# part 10 in space invaders using pygame
# by CODING WITH 3DV
# some cool levels including boss fight 
# Pydroid 3
import pygame
import math
pygame.init()

w = pygame.display.set_mode((200,200))
clock = pygame.time.Clock()

player_image =  pygame.image.load("/storage/emulated/0/Download/player.png")
player_image = pygame.transform.scale(player_image,(100,100)) 

myfont = pygame.font.Font("/storage/emulated/0/CODING/Fonts/times new roman bold.ttf", 50)  

current_players_score = 0

def score(scr):
	current_score = myfont.render("Score: " + str(scr) , True, (225,225,0)) 
	w.blit(current_score,[0,0]) 
	
def play_sound():
	pygame.mixer.init()
	pygame.mixer.music.load("/storage/emulated/0/CODING/Sounds/shoot_sound.wav") 
	pygame.mixer.music.play()

class BulletClass(pygame.sprite.Sprite):
	def __init__(self, x, y, w, h):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.image = pygame.Surface([w,h])
		self.image.fill((225,0,0))
		self.rect = self.image.get_rect()
		
class EnemyClass(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([25,25])
		self.image.fill((255,255,255)) 
		self. rect = self.image.get_rect()
		
	def update(self):
		self.rect.y += 1
	
BulletObj = BulletClass(100,100,10,20)
	
EnemyGroup = pygame.sprite.Group() 
for row in range(1):
	for column in range(1,6):
		EnemyObj = EnemyClass()
		EnemyObj.rect.x = 200 + (50*column)
		EnemyObj.rect.y = 50 + (50 * row) 
		EnemyGroup.add(EnemyObj) 
		
EnemyGroup1 = pygame.sprite.Group() 
for row1 in range(1,3):
	for column1 in range(1,6):
		EnemyObj1 = EnemyClass()
		EnemyObj1.rect.x = 200 + (50*column1)
		EnemyObj1.rect.y = 50 + (50 * row1) 
		EnemyGroup1.add(EnemyObj1)  
		
EnemyGroup2 = pygame.sprite.Group() 
for row2 in range(1,4):
	for column2 in range(1,6):
		EnemyObj2 = EnemyClass()
		EnemyObj2.rect.x = 200 + (50*column2)
		EnemyObj2.rect.y = 50 + (50 * row2) 
		EnemyGroup2.add(EnemyObj2)  
		
EnemyGroup3 = pygame.sprite.Group() 
for row3 in range(1,5):
	for column3 in range(1,6):
		EnemyObj3 = EnemyClass()
		EnemyObj3.rect.x = 200 + (50*column3)
		EnemyObj3.rect.y = 50 + (50 * row3) 
		EnemyGroup3.add(EnemyObj3) 
		
EnemyGroup4 = pygame.sprite.Group() 
for row4 in range(1,6):
	for column4 in range(1,6):
		EnemyObj4 = EnemyClass()
		EnemyObj4.rect.x = 200 + (50*column4)
		EnemyObj4.rect.y = 50 + (50 * row4) 
		EnemyGroup4.add(EnemyObj4) 
		
BossImage = pygame.transform.scale(pygame.image.load('/storage/emulated/0/Download/boss1.png') , (200,200)) 

class BossClass(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = BossImage 
			self.rect = self.image.get_rect() 
			self.rect.y = 0
			self.rect.x = 250
			self.visible = True
		def update(self):
			self.rect.y += 1 
			
class BossBulletClass(pygame.sprite.Sprite):
		def __init__(self, x1, y1):
			self.x = x1
			self.y = y1
			self.bullet_speed = 35
		def draw(self):
			pygame.draw.rect(w, (225,225,0), (self.x, self.y, 10,20))
			self.y += self.bullet_speed
			
BossGroup = pygame.sprite.Group()
BossObj = BossClass()
BossGroup.add(BossObj)
		
BulletGroup = pygame.sprite.Group() 
BulletObj = BulletClass(100,100,10,20)
BulletGroup.add(BulletObj) 

BossBulletObj = BossBulletClass(250,0) 

boss_health = 20

while True:
	w.fill((0,0,0)) 

	x, y = pygame.mouse.get_pos()   
	x1 = x - 50
	y1 = y - 250 
	
	score(current_players_score)
	
	BulletGroup.draw(w)
	EnemyGroup.draw(w) 
	

	BulletObj.rect.y -= 20
	for invaders in EnemyGroup:
		invaders.update() 
		if(invaders.rect.y > 950 - 25):
					exit()
		if pygame.sprite.spritecollide(invaders,BulletGroup,False):
			invaders.kill() 
			play_sound()
			BulletObj.rect. y = y1
			BulletObj.rect. x = x1 + 45  
			current_players_score+=1
			
		distance=math.hypot(invaders.rect.x-x1,invaders.rect.y-y1)
		if distance<40:
			exit() 
			
	if current_players_score >= 5:
		EnemyGroup1.draw(w) 
		for invaders in EnemyGroup1:
			invaders.update() 
			if(invaders.rect.y > 950 - 25):
					exit() 
			if pygame.sprite.spritecollide(invaders,BulletGroup,False): 
				invaders.kill() 
				play_sound()
				BulletObj.rect. y = y1
				BulletObj.rect. x = x1 + 45  
				current_players_score+=1
			
			distance=math.hypot(invaders.rect.x-x1,invaders.rect.y-y1)
			if distance<40:
				exit()   
				
	if current_players_score >= 15:
		EnemyGroup2.draw(w) 
		for invaders in EnemyGroup2:
			invaders.update() 
			if(invaders.rect.y > 950 - 25):
					exit() 
			if pygame.sprite.spritecollide(invaders,BulletGroup,False): 
				invaders.kill() 
				play_sound()
				BulletObj.rect. y = y1
				BulletObj.rect. x = x1 + 45  
				current_players_score+=1
			
			distance=math.hypot(invaders.rect.x-x1,invaders.rect.y-y1)
			if distance<40:
				exit()   
				
	if current_players_score >= 30:
		EnemyGroup3.draw(w) 
		for invaders in EnemyGroup3:
			invaders.update() 
			if(invaders.rect.y > 950 - 25):
					exit() 
			if pygame.sprite.spritecollide(invaders,BulletGroup,False): 
				invaders.kill() 
				play_sound()
				BulletObj.rect. y = y1
				BulletObj.rect. x = x1 + 45  
				current_players_score+=1
			
			distance=math.hypot(invaders.rect.x-x1,invaders.rect.y-y1)
			if distance<40:
				exit()  
				
	if current_players_score >= 50:
		EnemyGroup4.draw(w) 
		for invaders in EnemyGroup4:
			invaders.update() 
			if(invaders.rect.y > 950 - 25):
					exit() 
			if pygame.sprite.spritecollide(invaders,BulletGroup,False): 
				invaders.kill() 
				play_sound()
				BulletObj.rect. y = y1
				BulletObj.rect. x = x1 + 45  
				current_players_score+=1
			
			distance=math.hypot(invaders.rect.x-x1,invaders.rect.y-y1)
			if distance<40:
				exit()   
				
	if current_players_score >= 75 and BossObj.visible == True:
		BossGroup.draw(w)
		BossGroup.update()
		BossBulletObj.draw() 
		if BossBulletObj.y > 1280:
			print('>')
			BossBulletObj = BossBulletClass(BossObj.rect.x + 100,BossObj.rect.y + 200) 
		if pygame.sprite.spritecollide(BossObj,BulletGroup,False):
			boss_health -= 0.5
			if(boss_health <= 0):
				BossObj.visible = False
			play_sound()
			BulletObj.rect. y = y1
			BulletObj.rect. x = x1 + 45  
			current_players_score+=1
				
		pygame.draw.rect(w,(225,0,0), (BossObj.rect.x - 100,BossObj.rect.y,25,200)) 	
		pygame.draw.rect(w,(0,225,0), (BossObj.rect.x - 100,BossObj.rect.y, 25,200-(10*(20-boss_health))))

	if BulletObj. rect.y <= 0:
		BulletObj.rect. y = y1
		BulletObj.rect. x = x1 + 45

	w.blit(player_image,(x1,y1))
	pygame.draw.line(w, (225,0,0), (0,950), (720, 950),5)
	
	clock.tick(60)
	pygame.display.update()