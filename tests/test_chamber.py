import unittest
from src.particle import Particle
from src.position import Position
from src.chamber import Chamber
from IPython import embed

class TestChamber(unittest.TestCase):
    def test_chamber_methods(self):
        chamber = Chamber("..RL..")
        self.assertEqual(len(chamber.positions), 6)
        self.assertEqual(chamber.to_string(), "..XX..")
        self.assertEqual(chamber.is_empty(), False)
        chamber_2 = Chamber("....")
        self.assertEqual(chamber_2.to_string(), "....")
        self.assertEqual(chamber_2.is_empty(), True)
        self.assertEqual(chamber.in_bounds(-1), False)
        self.assertEqual(chamber.in_bounds(3), True)
        self.assertEqual(chamber.in_bounds(8), False)

    def test_chamber_animate_frame(self):
        chamber = Chamber("..R.LR.")
        self.assertEqual(chamber.to_string(), "..X.XX.")
        chamber.animate_frame(1)
        self.assertEqual(chamber.to_string(), "...X..X")
        chamber.animate_frame(1)
        self.assertEqual(chamber.to_string(), "..X.X..")
        chamber.animate_frame(1)
        self.assertEqual(chamber.to_string(), ".X...X.")
        chamber.animate_frame(1)
        self.assertEqual(chamber.to_string(), "X.....X")
        chamber.animate_frame(1)
        self.assertEqual(chamber.to_string(), ".......")
        chamber.animate_frame(1)
        self.assertEqual(chamber.to_string(), ".......")

    def test_chamber_animation(self):
        chamber = Chamber("..R.LR.")
        self.assertEqual(chamber.animate(1), ["..X.XX.", "...X..X", "..X.X..", ".X...X.", "X.....X", "......."])
        self.assertEqual(chamber.animate(2), ["..X.XX.", "..X.X..", "X.....X", "......."])
        self.assertEqual(chamber.animate(3), ["..X.XX.", ".X...X.", "......."])
        self.assertEqual(chamber.animate(4), ["..X.XX.", "X.....X", "......."])
        self.assertEqual(chamber.animate(5), ["..X.XX.", "......."])

if __name__=="__main__":
      unittest.main()
