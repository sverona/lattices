from typing import List

class Vertex:
    """Generic vertex class for lattices.
    """
    def __init__(self, name: str):
        self.name = name

    def diamonds(self, color: int) -> List[List[Vertex]]:
        """Return all diamonds this vertex is part of.
        A diamond is a sublattice [A, B, C, D] with A > B > D,
        A > C > D, B incomparable with C.
        """
        pass

    def satisfies_diamond_relations(self, color: int) -> bool:
        """Check the diamond relations for this vertex in the appropriate
        color component.
        """

    def satisfies_crossing_relations(self, color: int) -> bool:
        """Check the crossing relations for this vertex in the appropriate
        color component.
        """

class Edge:
    """Generic edge class for lattices.
    """
    def __init__(self):
        pass

class Lattice:
    def __init__(self, vertices: List[Vertex]):
        self.vertices = vertices
