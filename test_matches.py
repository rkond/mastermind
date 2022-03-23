from unittest import TestCase

from mastermind import get_matches


class TestMatches(TestCase):
    def test_matches_without_repeats(self) -> None:
        self.assertEqual((4, 0), get_matches(['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D']))
        self.assertEqual((2, 2), get_matches(['A', 'B', 'C', 'D'], ['A', 'B', 'D', 'C']))
        self.assertEqual((0, 4), get_matches(['A', 'B', 'C', 'D'], ['B', 'A', 'D', 'C']))
        self.assertEqual((0, 3), get_matches(['A', 'B', 'C', 'D'], ['B', 'A', 'D', 'E']))

    def test_matches_with_repeats(self) -> None:
        self.assertEqual((4, 0), get_matches(['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A']))
        self.assertEqual((3, 0), get_matches(['A', 'A', 'B', 'B'], ['A', 'A', 'A', 'B']))
        self.assertEqual((1, 2), get_matches(['A', 'A', 'C', 'D'], ['C', 'A', 'A', 'E']))
        self.assertEqual((0, 3), get_matches(['A', 'A', 'C', 'D'], ['C', 'C', 'A', 'A']))
