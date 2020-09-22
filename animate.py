import sys

from src.animator import Animator

speed = sys.argv[1]
init = sys.argv[2]
animator = Animator()
print animator.animate(speed, init)
