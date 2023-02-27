import unittest
import os

from composer import get_words_from_text, make_graph, compose, main
from contextlib import redirect_stdout


class TestMarkovChain(unittest.TestCase):

    def setUp(self):
        self.words = get_words_from_text("texts/alice_in_wonderland.txt")

    def test_get_words_from_text(self):
        words = get_words_from_text("texts/alice_in_wonderland.txt")
        self.assertIsInstance(words, list)
        self.assertEqual(len(words), 3000)

    def test_make_graph(self):
        g = make_graph(self.words)
        self.assertEqual(len(g.vertices), 772)

    def test_compose(self):
        g = make_graph(self.words)
        composition = compose(g, self.words, 5)
        self.assertIsInstance(composition, str)
        self.assertGreater(len(composition), 0)

    def test_main(self):
        # Test the main function without actually printing the output to the console
        with open(os.devnull, "w") as f:
            with redirect_stdout(f):
                main()
