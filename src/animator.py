import re
from chamber import Chamber

class Animator(object):
    def __init__(self):
        pass

    def animate(self, speed, init):
        self.validate_input(speed, init)
        self.chamber = Chamber(init)
        return "\n".join(self.chamber.animate(int(speed)))

    def validate_input(self, speed, init):
        if int(speed) < 1 or int(speed) > 10:
            raise ValueError("Invalid speed entered.")
        if re.search(r"^[\.RL]+$", init) is None:
            raise ValueError("Invalid initial positions entered.")
        if len(init) > 50:
            raise ValueError("Initial positions string too long.")
