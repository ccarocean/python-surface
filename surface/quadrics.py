# -* coding: utf-8 -*-
"""Quadric elements.

This is subset of quadrics, it is only those that can be solved for a single
real value of z.
"""

from .surfaces import SymbolicSurface


class Quadric(SymbolicSurface):
    """Base class of all quadrics.

    Quadrics are defined by a function of x and y that produces a single
    z-value, that is they must pass the vertical line test.
    """

    def __init__(self):
        self._classified = False

    def translate(self, dx=0, dy=0, dz=0):
        """Translated the quadric.

        Parameters
        ----------
        dx : float
            Distance to translated quadric in x direction.
        dy : float
            Distance to translated quadric in y direction.
        dz : float
            Distance to translated quadric in z direction.

        """
        raise NotImplementedError

    def rotate(self, theta):
        """Rotate the quadric about the z axis.

        Parameters
        ----------
        theta : float
            Angle in degrees to rotate the quadric about the z-axis.

        """
        raise NotImplementedError

    def contour(self, z=0):
        """Contour of quadric in the xy (or any parallel) plane.

        Parameters
        ----------
        z : float
            The z-level of the plane the contour is taken at.

        Returns
        -------
        : surface.conic.Conic
            The conic of the projection or None if the plane at the given `z`
            level does not intersect the quadric.

        """
        raise NotImplementedError

    def classify(self):
        """Try to classify the quadric and return a specific quadric object.

        Returns
        -------
        : Quadric
            A more specific quadric if possible, otherwise `self` is returned.
        """
        raise NotImplementedError

    @property
    def classified(self):
        return self._classified


class EllipticParaboloid(Quadric):
    """An elliptic paraboloid, translated in (x,y,z), and rotated about z."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class CircularParaboloid(EllipticParaboloid):
    """A circular paraboloid, translated in (x,y,z)."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class HyperbolicParaboloid(Quadric):
    """A hyperbolic paraboloid, translated in (x,y,z), and rotated about z.

    This is also known as a saddle.
    """

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class ParabolicCylinder(Quadric):
    """A parabolic cylinder, translated in (x, y, z), and rotated about z."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError
