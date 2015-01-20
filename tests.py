import pytest
import unittest
from maximum_pit_depth import (get_maximum_pit_depth, _get_pit_depths,
                               _is_pit, _is_consecutively_ch, _get_depth)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ARR0 = [0, 1, 3, -2, 0, 1, 0, -3, 2, 3]

    def tearDown(self):
        pass

    def test_get_maximum_pit_depth(self):
        assert get_maximum_pit_depth(self.ARR0) == 4


    def test_get_pit_depths(self):
        assert _get_pit_depths([0, 1, 3, -2, 0]) == [2]


    def test_is_pit(self):
        assert _is_pit(self.ARR0, 0, 2, 3) == False
        assert _is_pit(self.ARR0, 2, 3, 4) == True
        assert _is_pit(self.ARR0, 2, 3, 5) == True
        assert _is_pit(self.ARR0, 5, 7, 8) == True


    def test_is_consecutively_ch(self):
        assert _is_consecutively_ch("incr", self.ARR0, 0, 2) == True

    def test_get_depth(self):
        assert _get_depth((3, -2, 0)) == 2



if __name__ == "__main__":
    unittest.main()
