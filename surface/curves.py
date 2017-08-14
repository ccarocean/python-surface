# -* coding: utf-8 -*-


class Curve(object):
    """Base class for all xy curves."""

    def __init__(self):
        raise NotImplementedError


class SymbolicCurve(Curve):
    """A curve defined symbolically."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError


class NumericCurve(Curve):
    """A curve defined numerically."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError
