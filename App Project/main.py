# Created by: Amero Defranco
# Created on: January 2016
# Created for: Myself
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from splash_screen import *
from scene import *
import ui

main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = SplashScene()
main_view.present(hide_title_bar = True, animated = False)
