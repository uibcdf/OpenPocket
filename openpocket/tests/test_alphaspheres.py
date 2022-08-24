"""
Unit to test the AlphaSpheres class
"""

import openpocket as opoc
import pytest
import numpy as np

def test_alphaspheres_original_points():

    points = ([[-1.,  2.,  0.],
               [ 0.,  2.,  1.],
               [ 1., -2.,  1.],
               [ 0.,  1.,  1.],
               [ 0.,  0.,  0.],
               [-1., -1.,  0.]])

    alphaspheres = opoc.alpha_spheres.AlphaSpheres(points)

    assert np.allclose(points, alphaspheres.points)

    assert alphaspheres.n_points == 6

