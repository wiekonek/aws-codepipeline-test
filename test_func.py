#!/usr/bin/env python
import unittest
from app import string_ccat

class Testing(unittest.TestCase):

    def test_concat(self):
        self.assertEqual(string_ccat("o", "la"), "ola")
