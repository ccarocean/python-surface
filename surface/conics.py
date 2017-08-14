# -* coding: utf-8 -*-
"""Conic sections.

"""

from .curves import SymbolicCurve


class Conic(SymbolicCurve):
    """Base class of all conics.

    Conics are defined by a relation between x and y in the xy plane.
    """

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Point(Conic):
    """A point in the xy plane."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Line(Conic):
    """A line in the xy plane."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class DoubleLine(Conic):
    """A double line in the xy plane."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Ellipse(Conic):
    """An ellipse in the xy plane."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError

class Circle(Ellipse):
    """A circle in the xy plane."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Parabola(Conic):
    """A parabola in the xy plane."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Hyperbola(Conic):
    """A hyperbola in the xy plane."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError
