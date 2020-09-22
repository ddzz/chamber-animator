import unittest
from src.position import Position
from src.particle import Particle

class TestPosition(unittest.TestCase):
    def test_position_is_empty(self):
        position = Position()
        self.assertEqual(position.particles, [])
        self.assertEqual(position.is_empty(), True)
        particle = Particle("L")
        position.add_particle(particle)
        self.assertEqual(position.is_empty(), False)
        self.assertEqual(position.particles, [particle])

    def test_remove_particle(self):
        position = Position()
        particle = Particle("R")
        position.add_particle(particle)
        position.remove_particle(0)
        self.assertEqual(position.is_empty(), True)

    def test_reset_just_moved(self):
        position = Position()
        particle = Particle("R")
        position.add_particle(particle)
        position.particles[0].is_just_moved = True
        position.reset_just_moved()
        self.assertEqual(position.particles[0].is_just_moved, False)

if __name__== '__main__':
    unittest.main()
