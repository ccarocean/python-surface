# -* coding: utf-8 -*-


class Surface(object):
    """Base class for all surfaces."""

    def __init__(self):
        raise NotImplementedError

    def contour(self, z=0):
        """Contour of surface in the xy (or any parallel) plane.

        Parameters
        ----------
        z : float
            The z-level of the plane the contour is taken at.

        Returns
        -------
        :
            A contour line or lines, type and format are dependent on the
            subclass.

        """
        raise NotImplementedError


class SymbolicSurface(Surface):
    """A surface defined symbolically."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError

    def contour(self, z=0):
        """Contour of surface in the xy (or any parallel) plane.

        Parameters
        ----------
        z : float
            The z-level of the plane the contour is taken at.

        Returns
        -------
        : surface.
            A symbolic
            A contour line or lines, type and format are dependent on the
            subclass.

        """
        raise NotImplementedError


class NumericSurface(Surface):
    """A surface defined numerically."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class UnstructuredSurface(NumericSurface):
    """A surface with no structure."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class CurvilinearSurface(NumericSurface):
    """A surface on a curvilinear grid."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class RectilinearSurface(CurvilinearSurface):
    """A surface on a rectilinear grid."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class UniformSurface(RectilinearSurface):
    """A surface on a uniform (possibly Cartesian) grid."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError
