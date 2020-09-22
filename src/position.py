class Position(object):
    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def remove_particle(self, particle_index):
        self.particles[particle_index] = None

    def is_empty(self):
        return len(filter(None, self.particles)) == 0

    def reset_just_moved(self):
        for particle in self.particles:
            particle.is_just_moved = False

    def cleanup_after_deleted_particles(self):
        self.particles = filter(None, self.particles)
