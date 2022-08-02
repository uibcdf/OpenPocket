import numpy as np
from scipy.spatial import Voronoi
from scipy.spatial.distance import euclidean

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

            # Checking if the argument points fulfills requirements

            if isinstance(points, (list, tuple)):
                points = np.array(points)
            elif isinstance(points, np.ndarray):
                pass
            else:
                raise ValueError("The argument points needs to be a numpy array with shape (n_points, 3)")

            if (len(points.shape)!=2) and (points.shape[1]!=3):
                raise ValueError("The argument points needs to be a numpy array with shape (n_points, 3)")

            # Saving attributes points and n_points

            self.points = points
            self.n_points = points.shape[0]

            # Voronoi class to build the alpha-spheres

            voronoi = Voronoi(self.points)

            # The alpha-spheres centers are the voronoi vertices

            self.centers = voronoi.vertices
            self.n_alpha_spheres = self.centers.shape[0]

            # Let's compute the 4 atoms' sets in contact with each alpha-sphere

            self.points_of_alpha_sphere = [[] for ii in range(self.n_alpha_spheres)]

            n_regions = len(voronoi.regions)
            region_point={voronoi.point_region[ii]:ii for ii in range(self.n_points)}

            for region_index in range(n_regions):
                region=voronoi.regions[region_index]
                if len(region)>0:
                    point_index=region_point[region_index]
                    for vertex_index in region:
                        if vertex_index != -1:
                            self.points_of_alpha_sphere[vertex_index].append(point_index)

            for ii in range(self.n_alpha_spheres):
                self.points_of_alpha_sphere[ii] = sorted(self.points_of_alpha_sphere[ii])


            # Let's finally compute the radius of each alpha-sphere

            self.radii = []

            for ii in range(self.n_alpha_spheres):
                radius = euclidean(self.centers[ii], self.points[self.points_of_alpha_sphere[ii][0]])
                self.radii.append(radius)

