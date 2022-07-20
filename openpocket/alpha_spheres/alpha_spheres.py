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

            ### To be added by Juan Carlos ###

            pass # remove this line

