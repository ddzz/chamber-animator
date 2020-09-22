from particle import Particle
from position import Position

class Chamber(object):
    def __init__(self, initial_positions):
        self.initial_positions = initial_positions
        self.set_initial_positions()

    def animate_frame(self, speed):
        for position_index, position in enumerate(self.positions):
            for particle_index, particle in enumerate(position.particles):
                if particle.is_just_moved:
                    continue

                position.remove_particle(particle_index)

                new_position = (position_index - speed) if particle.direction == "L" else (position_index + speed)

                if self.in_bounds(new_position):
                    new_particle = Particle(particle.direction)
                    self.positions[new_position].add_particle(new_particle)
                    new_particle.is_just_moved = True
            position.cleanup_after_deleted_particles()
        self.reset_just_moved()

    def animate(self, speed):
        output = []
        output.append(self.to_string())
        while not self.is_empty():
            self.animate_frame(speed)
            output.append(self.to_string())
        self.set_initial_positions()
        return output

    def to_string(self):
        str_list = []
        for position in self.positions:
            str_list.append(".") if position.is_empty() else str_list.append("X")
        return "".join(str_list)

    def is_empty(self):
        return all(position.is_empty() for position in self.positions)

    def in_bounds(self, index):
        return index >= 0 and index < len(self.positions)

    def reset_just_moved(self):
        map(lambda position: position.reset_just_moved(), self.positions)

    def set_initial_positions(self):
        self.positions = []
        for direction in list(self.initial_positions):
            position = Position()
            if direction != ".":
                particle = Particle(direction)
                position.add_particle(particle)
            self.positions.append(position)
