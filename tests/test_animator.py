import unittest

from src.particle import Particle
from src.position import Position
from src.chamber import Chamber
from src.animator import Animator

class TestAnimator(unittest.TestCase):
    def test_animation_cases(self):
        animator = Animator()
        self.assertEqual(animator.animate(2, "..R...."), ("..X....\n"
                                                            "....X..\n"
                                                            "......X\n"
                                                            "......."))
        animator = Animator()
        self.assertEqual(animator.animate(3, "RR..LRL"), ("XX..XXX\n"
                                                            ".X.XX..\n"
                                                            "X.....X\n"
                                                            "......."))
        animator = Animator()
        self.assertEqual(animator.animate(2, "LRLR.LRLR"), ("XXXX.XXXX\n"
                                                            "X..X.X..X\n"
                                                            ".X.X.X.X.\n"
                                                            ".X.....X.\n"
                                                            "........."))
        animator = Animator()
        self.assertEqual(animator.animate(10, "RLRLRLRLRL"), ("XXXXXXXXXX\n"
                                                                ".........."))
        animator = Animator()
        self.assertEqual(animator.animate(1, "..."), "...")

        animator = Animator()
        self.assertEqual(animator.animate(1, "LRRL.LR.LRR.R.LRRL."), ("XXXX.XX.XXX.X.XXXX.\n"
                                                                        "..XXX..X..XX.X..XX.\n"
                                                                        ".X.XX.X.X..XX.XX.XX\n"
                                                                        "X.X.XX...X.XXXXX..X\n"
                                                                        ".X..XXX...X..XX.X..\n"
                                                                        "X..X..XX.X.XX.XX.X.\n"
                                                                        "..X....XX..XX..XX.X\n"
                                                                        ".X.....XXXX..X..XX.\n"
                                                                        "X.....X..XX...X..XX\n"
                                                                        ".....X..X.XX...X..X\n"
                                                                        "....X..X...XX...X..\n"
                                                                        "...X..X.....XX...X.\n"
                                                                        "..X..X.......XX...X\n"
                                                                        ".X..X.........XX...\n"
                                                                        "X..X...........XX..\n"
                                                                        "..X.............XX.\n"
                                                                        ".X...............XX\n"
                                                                        "X.................X\n"
                                                                        "..................."))

    def test_input_validation(self):
        animator = Animator()
        self.assertRaises(ValueError, lambda: animator.animate(-2, "..R."))
        self.assertRaises(ValueError, lambda: animator.animate(0, "..R."))
        self.assertRaises(ValueError, lambda: animator.animate(2, ".a...RL."))

if __name__== '__main__':
    unittest.main()
