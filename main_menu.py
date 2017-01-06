from main_menu_real import *
from scene import *
from star import *
import sound
import random
import math
from time import sleep
from objc_util import *

#main_view = splash_screen.main_view
class MainMenuClass (Scene):
	
	def setup(self):
		self.pressed = False
		self.close = True
		self.newstar = star_class()
		print(self.newstar.get_hydrogen())
		self.sideframe = SpriteNode('./assets/sprites/frame.PNG', size = (self.size[0]/3.5, self.size[1]), alpha = 0.2)
		self.line = SpriteNode('./assets/sprites/line.PNG',parent = self ,size = (self.size[0]/(self.size[0]/2),self.size[1]/(self.size[1]/2)), position = (self.size[0]/3,self.size[1]/3), z_position = 9.0)
		
		self.ui_curve = SpriteNode('./assets/sprites/ui_bubbles.PNG',parent=self,size = self.size, position  = self.size/2, z_position = 4.0, alpha = 0)
		self.ui_curve.rotation = 3.14159
		
		self.button_one = SpriteNode('./assets/sprites/statistics_button.PNG',parent=self,size = (self.size[0]/8.5, self.size[0]/8.5), position  = (self.size[0]/1.9, self.size[1]/1.75), z_position = 5.0, alpha = 0)
		self.line.rotation = 5.49779
		self.line.anchor_point = (0,0)
		#self.button_one = SpriteNode('./assets/sprites/button3.PNG',parent=self,size = (250,60), position = (self.size[0]/2.00,self.size[1]/2+15), z_position = 5.0, alpha = 0)
		
		self.button_two = SpriteNode('./assets/sprites/button3.PNG',parent=self,size = (250,60), position = (self.size[0]/1.84,self.size[1]/2.75+15), z_position = 5.0, alpha = 0)
		
		self.button_three = SpriteNode('./assets/sprites/button3.PNG',parent=self,size = (250,60), position = (self.size[0]/1.85,self.size[1]/4.5+15), z_position = 5.0, alpha = 0)
		
		self.button = SpriteNode('./assets/sprites/fire.PNG', parent=self, size = (235,262), position = (self.size[0]/3.6 - 4,self.size[1]/3+15) , z_position = 2, alpha=0.01)
		
		self.settings_node = Node(parent=self, position = (-self.sideframe.size[0]/2, self.size[1]/2), z_position = 6.0)
		self.settings_node.add_child(self.sideframe)
		SpriteNode('./assets/sprites/IMG_2640.PNG', size = self.size, position=self.size/2, parent=self, z_position = 1)
		hydrogen = list(str(self.newstar.get_hydrogen()/10**29))
		hydrogen.insert(1, ".")
		total_hydrogen = ''
		for i in hydrogen:
			total_hydrogen = total_hydrogen + i
		self.hydrogen = LabelNode(parent=self.settings_node, text = 'Hydrogen = ' + total_hydrogen  + ' Nonillion', )
		
		self.hydrogen.size = (self.sideframe.size[0], self.sideframe.size[1]/20)
		with open('./assets/shaders/SimplexNoise.fsh') as f:
			src = f.read()
			shader = Shader(src)
			
		self.sprite = SpriteNode('./assets/sprites/SimplexNoiseGradient.PNG', size=self.size, position=self.size/2, parent=self, z_position = 0)
		
		self.sprite.shader = shader
		
	def did_change_size(self):
		pass
	
	def update(self):
		pass
		
	def touch_began(self, touch):
		
		if self.button_one.frame.contains_point(touch.location) and self.button_one.alpha == 1.0:
			
			if self.settings_node.position[0] < self.sideframe.size[0]/2 and self.settings_node.position[0] > -self.sideframe.size[0]/2 :
				pass
			elif self.settings_node.position[0] == -self.sideframe.size[0]/2:
				self.settings_node.run_action(Action.move_by(self.sideframe.size[0], 0, 0.5))
				self.close = True
			elif self.settings_node.position[0] == self.sideframe.size[0]/2:
				self.settings_node.run_action(Action.move_by(-self.sideframe.size[0], 0, 0.5))
				
				
		if self.button.frame.contains_point(touch.location) or self.close == True:
				if self.pressed == False:
					#self.ui_curve.run_action(Action.fade_to(1, 1))
					#self.button_three.run_action(Action.fade_to(1, 1))
					#self.button_two.run_action(Action.fade_to(1, 1))
					self.line.run_action((Action.scale_y_to(self.size[0]/10, 1)))
					self.button_one.run_action(Action.fade_to(1, 1))
					self.pressed = True
				else:
					self.ui_curve.run_action(Action.fade_to(0, 1))
					self.button_three.run_action(Action.fade_to(0, 1))
					self.button_two.run_action(Action.fade_to(0, 1))
					self.button_one.run_action(Action.fade_to(0, 1))
					self.pressed = False
					self.close = False
					
					
				
		if self.button_one.frame.contains_point(touch.location):
			#self.dismiss_modal_scene()
			pass

	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass
		
	
