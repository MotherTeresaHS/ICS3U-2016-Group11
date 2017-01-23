# Created by: Amero Defranco
# Created on: January 2016
# Created for: Myself
# This scene shows a main menu screen until a player choses an option,
#   then transitions to the game scene or settings.

from scene import *
from game_scene import *
import sound
import random
import math



class MainMenuScene (Scene):
	def setup(self):
		
		self.background = SpriteNode('./assets/sprites/background3.PNG', size = self.size*2, position = (self.size[0],0), parent = self)
		
		'''---------------------------------------------------------------------------------------------'''
		# main menu #
		
		self.main_menu_node = Node(parent = self.background, position = (-self.size[0], 0))
		
		self.menu_sideframe = SpriteNode('./assets/sprites/menu_sideframe.PNG',size = (self.size[0],self.size[1]), position = (self.size[0]/2,self.size[1]/2), parent = self.main_menu_node)
		
		self.play_button = SpriteNode('./assets/sprites/play.PNG', size = (self.size[0]/3.84, self.size[1]/15.36), position = (self.size[0]/1.25,self.size[1]/2), parent = self.main_menu_node,alpha=0.8)
		
		self.credits_button = SpriteNode('./assets/sprites/credits.PNG', size = (self.size[0]/3.84, self.size[1]/15.36), position = (self.size[0]/1.25,self.size[1]/2.75), parent = self.main_menu_node,alpha=0.8)
		
		self.title = SpriteNode('./assets/sprites/title.PNG', size = (self.size[0]/3, self.size[1]/9), position = (self.size[0]/1.25,self.size[1]/1.5), parent = self.main_menu_node)
		
		self.title_backing = SpriteNode('./assets/sprites/frame.PNG', size = (self.size[0]/2.4, self.size[1]/40), position = (self.size[0]/1.263,self.size[1]/1.65), parent = self.main_menu_node, alpha = 0.5)
		
		'''---------------------------------------------------------------------------------------------'''
		# credits menu #
		
		self.credits_menu_node = Node(parent = self.background, position = (-self.size[0], -self.size[1]))
		
		self.back_to_main_menu_button = SpriteNode('./assets/sprites/back_to_menu.PNG', size = (self.size[0]/3.624, self.size[1]/14.48), position = (self.size[0]/1.2, self.size[1]/1.1), parent = self.credits_menu_node)
		
		self.credits = SpriteNode('./assets/sprites/credits_list.PNG', size = (self.size[0], self.size[1]), position = (self.size[0]/2, self.size[1]/2), parent = self.credits_menu_node)
		
		
		'''---------------------------------------------------------------------------------------------'''
		# settings menu #
		
		self.settings_menu_node = Node(parent = self.background, position = (0, 0))
		
		self.back_to_main_menu_button_two = SpriteNode('./assets/sprites/back_to_menu.PNG', size = (self.size[0]/3.624, self.size[1]/14.48), position = (self.size[0]/1.2, self.size[1]/1.1), parent = self.settings_menu_node)
		
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		
		if self.play_button.frame.contains_point(touch.location) and self.main_menu_node.alpha == 1:
			
			self.present_modal_scene(GameScene())
			
		if self.credits_button.frame.contains_point(touch.location) and self.main_menu_node.alpha == 1:
			
			self.main_menu_node.run_action(Action.fade_to(0,1))
			
			self.background.run_action(Action.move_to(self.size[0],self.size[1],1))
			
			self.credits_menu_node.run_action(Action.fade_to(1,1))
			
		if self.back_to_main_menu_button.frame.contains_point(touch.location) and self.credits_menu_node.alpha == 1:
			
			self.credits_menu_node.run_action(Action.fade_to(0,1))
			self.main_menu_node.run_action(Action.fade_to(1,1))
			self.background.run_action(Action.move_to(self.size[0],0,1))
			
			
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass
