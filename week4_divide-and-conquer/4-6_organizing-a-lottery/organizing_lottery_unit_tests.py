import unittest
from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, -3, -1], [5, 2, 10], [1, 6])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        return True
        #

    def test_large(self):
        return True
        #


if __name__ == '__main__':
    unittest.main()
