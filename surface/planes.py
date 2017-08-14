# -* coding: utf-8 -*-
"""Plane (1st order) surfaces."""

from .surfaces import SymbolicSurface


class Plane(SymbolicSurface):
    """Plane surface."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError
