import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from scipy.spatial.distance import euclidean as distance

class AlphaSpheres():

    """Set of alpha-spheres

    Object with a set of alpha-spheres and its main attributes such as radius and contacted points

    Attributes
    ----------
    points : ndarray (shape=[n_points,3], dtype=float)
        Array of coordinates in space of all points used to generate the set of alpha-spheres.
    n_points: int
        Number of points in space to generate the set of alpha-spheres.
    centers: ndarray (shape=[n_alpha_spheres,3], dtype=float)
        Centers of alpha-spheres.
    radii: ndarray (shape=[n_alpha_spheres], dtype=float)
        Array with the radii of alpha-spheres.
    points_of_alpha_sphere: ndarray (shape=[n_alpha_spheres, 4], dtype=int)
        Indices of points in the surface of each alpha-sphere.
    n_alpha_spheres: int
        Number of alpha-spheres in the set.

    """

    def __init__(self, points=None):

        """Creating a new instance of AlphaSpheres

        With an array of three dimensional positions (`points`) the resultant set of alpha-spheres is returned
        as a class AlphaSpheres.

        Parameters
        ----------
        points: ndarray (shape=[n_points,3], dtype=float)
            Array with the three dimensional coordinates of the input points.

        Examples
        --------

        See Also
        --------

        Notes
        -----

        """

        self.points=None
        self.n_points=None
        self.centers=None
        self.points_of_alpha_sphere=None
        self.radii=None
        self.n_alpha_spheres=None

        if points is not None:
            try:
                isinstance(points,(np.ndarray)):
                points.shape[1] == 3 

            except (TypeError,Exception) as e:
                print(e)
                print("the input object must be a three dimensional array")
            else:
                self.points=points # a way to store the input instance, giving that it has the right attributes
                vor = Voronoi(points, incremental=False)
### How could make this works? I want those two exception work in order to catch those very exception and print the several message warning                
    def n_points(self):
        if n_points is not None:
            try:
                points()
            except Exception as e:
                print(e)
            else:
                return self.n_points = vor.npoints

    def centers(self):
        if centers is not None:
            try:
                points()
            except Exception as e:
                print(e)
            else:
                return self.centers = vor.vertices

    def points_of_alpha_sphere(self):
        if points_of_alpha_sphere is not None:
            try:
                points()
            except Exception as e:
                print(e)
            else:
                n_vertices = vor.vertices.shape[0]
                n_regions = len(vor.regions)
                n_points = vor.npoints # The number of original centers
#               n_points= self.n_points  # recalling the above method
#               n_points= n_points()  # Try another way to recall the same method defined previously
                points_of_vertex = [[] for ii in range(n_vertices)]
                region_point={vor.point_region[ii]:ii for ii in range(n_points)}

                for region_index in range(n_regions):
                    region=vor.regions[region_index]
                    if len(region)>0:
                        point_index=region_point[region_index]
                        for vertex_index in region:
                            if vertex_index != -1:
                                points_of_vertex[vertex_index].append(point_index)
                return self.points_of_alpha_sphere = points_of_vertex 
    def radii(self):
        if radii is not None:
            try:
                points()
            except Exception as e:
                print(e)
            else:
                n_alpha_circles = n_vertices
                alpha_circle_centers = vor.vertices
                alpha_circle_radius = [distance(vor.vertices[ii], points[points_of_vertex[ii][0]]) for ii in range(n_vertices)]
                return self.radii = alpha_circle_radius 
    def n_alpha_spheres(self):
        if n_alpha_spheres is not None:
            try:
                points()
            except Exception as e:
                print(e)
            else:
                n_alpha_spheres = vor.vertices.shape[0]
                return self.n_alpha_spheres = n_alpha_spheres 
