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

    assert alphaspheres.n_alpha_spheres == 4

    centers = ([[ 6.5 ,  1.5 , -0.5 ],
                [-0.25, -0.75,  1.75],
                [ 0.5 ,  1.5 , -0.5 ],
                [-1.5 ,  0.5 ,  0.5 ]])

    assert np.allclose(centers, alphaspheres.centers)

    radius_all = ([6.68954408, 1.92028644, 1.6583124 , 1.6583124 ])
    
    assert np.allclose(radius_all, alphaspheres.radii)

    points_of_alpha_sphere = ([[1, 2, 3, 4],
                               [2, 3, 4, 5],
                               [0, 1, 3, 4],
                               [0, 3, 4, 5]])

    assert np.allclose(points_of_alpha_sphere, alphaspheres.points_of_alpha_sphere)

    merged_selected_point_indices = [0, 2, 3, 4, 5]

    assert np.allclose(merged_selected_point_indices, alphaspheres.get_points_of_alpha_spheres([1,3]))

    alphaspheres.remove_big_alpha_spheres(5.0)
    
    assert alphaspheres.n_alpha_spheres == 3

    remaining_no_big_radius = ([1.92028644, 1.6583124 , 1.6583124 ])
    
    assert np.allclose(remaining_no_big_radius, alphaspheres.radii)

    remaining_no_big_centers = ([[-0.25, -0.75,  1.75],
                                [ 0.5 ,  1.5 , -0.5 ],
                                [-1.5 ,  0.5 ,  0.5 ]])

    assert np.allclose(remaining_no_big_centers, alphaspheres.centers)

    alphaspheres.remove_small_alpha_spheres(1.66) 

    assert alphaspheres.n_alpha_spheres == 1

    remaining_no_small_radius = ([1.92028644])

    assert np.allclose(remaining_no_small_radius, alphaspheres.radii)

    remaining_no_small_centers= ([[-0.25, -0.75,  1.75]])

    assert np.allclose(remaining_no_small_centers, alphaspheres.centers)
