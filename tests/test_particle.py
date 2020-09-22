import unittest
from src.particle import Particle

class TestParticle(unittest.TestCase):
    def test_particle_creation(self):
        particle = Particle("L")
        self.assertEqual(particle.type, "L")
        self.assertEqual(particle.is_just_moved, False)

if __name__=='__main__':
      unittest.main()
