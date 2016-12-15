import splash_screen
from scene import *
import sound
import random
import math
from time import sleep
from objc_util import *

#main_view = splash_screen.main_view
class MainMenuClass (Scene):
	
	def setup(self):
		self.sideframe = SpriteNode('./assets/sprites/frame.PNG', parent=self, size = (self.size[0]/4, self.size[1]), position =(0,self.size[1]/2), z_position = 3.0, alpha = 0.2)
		
		self.sideframe.position = (-1*(self.sideframe.size.x/2 + self.sideframe.position.x), self.sideframe.position[1])
		
		self.button = SpriteNode('./assets/sprites/fire.PNG', parent=self, size = (235,262), position = (self.size[0]/3.6 - 4,self.size[1]/3+15) , z_position = 2, alpha=0.01)
		SpriteNode('./assets/sprites/IMG_2640.PNG', size = self.size, position=self.size/2, parent=self, z_position = 1)
		with open('./assets/shaders/SimplexNoise.fsh') as f:
			src = f.read()
			shader = Shader(src)
		self.sprite = SpriteNode('./assets/sprites/SimplexNoiseGradient.PNG', size=self.size, position=self.size/2, parent=self, z_position = 0)
		self.sprite.shader = shader
	def did_change_size(self):
		self.sprite.size = self.size
		self.sprite.position = self.size/2
	
	def update(self):
		pass
	def touch_began(self, touch):
		if self.button.frame.contains_point(touch.location):
			if self.sideframe.position[0] != self.sideframe.size[0]/2:
				self.sideframe.run_action(Action.move_by(self.sideframe.size[0], 0, 0.5))
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass
