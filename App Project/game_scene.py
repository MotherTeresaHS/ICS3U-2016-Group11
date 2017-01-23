# Created by: Amero Defranco
# Created on: January 2016
# Created for: Myself
# This scene is the game scene

from main_menu import *
from scene import *
from time import sleep
from objc_util import *
import sound

class GameScene (Scene):
	
	def setup(self):
		# This scene contains all the game components
		self.highscore = 0
		self.old_highscore = self.highscore
		
		self.planet = SpriteNode('./assets/sprites/planet.PNG',parent = self,size = ( self.size[0]/6.82,  self.size[1]/5.12 ), position = (self.size[0]/2 + self.size[0]/4, self.size[1]/2 + self.size[1]/4),z_position = 5.0)
		
		self.pause_button = SpriteNode('./assets/sprites/pause_button.PNG', parent=self, size = (self.size[0]/10.24,self.size[1]/7.68), position = (self.size[0]/10,self.size[1]),z_position=5.0)
		
		self.button = SpriteNode('./assets/sprites/hydrogen_button.PNG', parent=self,size = (self.size[0]/8.5, self.size[0]/8.5), position  = (self.size[0]/1.9, self.size[1]/1.75), z_position = 5.0)
		
		self.pause_button.position = (0 + self.pause_button.size.x/2, self.size[1] - self.pause_button.size.y/2)
				
		SpriteNode('./assets/sprites/IMG_2640.PNG', size = self.size, position = self.size/2, parent = self, z_position = 1)
		
		self.highscore_label = LabelNode(z_position = 4.0, parent = self,position = (self.size[0]/2 + self.size[0]/4, 0 + self.size[1]/10), size = self.size/10, text = ('Highscore: ' + str(self.highscore)))
		
		self.coin = SpriteNode('./assets/sprites/coin.PNG', position = (self.size[0]/2 + self.size[0]/4,self.size[1]/2), size = (self.size[0]/50,self.size[1]/50), parent = self, z_position = 4.0)
		
		with open('./assets/shaders/SimplexNoise.fsh') as shade:
			src = shade.read()
			shader = Shader(src)
			
		self.sprite = SpriteNode('./assets/sprites/SimplexNoiseGradient.PNG', size = self.size, position= self.size/2, parent = self, z_position = 0)
		
		self.sprite.shader = shader
		
		
	def did_change_size(self):
		pass
	
	def update(self):
		
		if self.old_highscore != self.highscore:
			
			self.highscore_label.text = 'Highscore: ' + str(self.highscore)
			self.old_highscore = self.highscore
			
		if self.planet.frame.contains_point(self.coin.position):
			
			self.highscore += 1
			sound.play_effect('./assets/sounds/coin.caf')
			sound.set_volume(1000.0)
		
	def touch_began(self, touch):
		
		if self.button.frame.contains_point(touch.location) and self.planet.position[1] != self.size[1]/2 - self.size[1]/4:
			
			self.planet.run_action(Action.move_to(self.planet.position[0],self.size[1]/2 - self.size[1]/4))
			
		elif self.planet.position[1] == self.size[1]/2 - self.size[1]/4:
			self.planet.run_action(Action.move_to(self.planet.position[0],self.size[1]/2 + self.size[1]/4))
			
		if self.pause_button.frame.contains_point(touch.location):
			self.dismiss_modal_scene()
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

