"""Implements diamond/crossing relations for Fibonacci lattices.
"""
from itertools import product
from functools import lru_cache
import operator

import networkx as nx

class FibonacciLattice(nx.Graph):
    """Fibonacci lattice class.

    A Fibonacci lattice is a subset of [1, ..., k]
    """
    def __init__(self, scale, order):
        super().__init__()

        self.scale = scale
        self.order = order

        self.add_nodes_from(self.tableaux())
        # TODO This edge generation process can be sped up by turning it around
        # that is, only check the possible adjacent labels and see if they're valid
        for node1 in self.nodes():
            for node2 in self.nodes():
                if self.adjacent(node1, node2):
                    self.add_edge(node1, node2,
                                  color=self.color(node1, node2))

    def color(self, node1, node2):
        """Return the color the edge between _node1_ and _node2_
        should have, or None if they are nonadjacent.
        """
        if not self.adjacent(node1, node2):
            return None

        diffs = [(comp1, comp2) for comp1, comp2 in zip(node1, node2) if comp1 != comp2][0]
        lower_label = min(diffs)

        # The following variables refer to this zero-indexed grid:
        # 1   n-1 1   n-1 (k columns)
        # 2   n-2 2   n-2 ...
        # ...
        # n-1 1   n-1 1
        # The color is given by the element in column lower_label // n
        # and row lower_label % n.
        col = lower_label // self.scale
        row = lower_label - self.scale * col
        if col % 2 == 0:
            return row
        return self.scale - row

    @staticmethod
    def adjacent(node1, node2):
        """Check if _node1_ and _node2_ are adjacent.
        """
        differences = 0
        for comp1, comp2 in zip(node1, node2):
            if comp1 != comp2:
                differences += 1
                if int(abs(comp1 - comp2)) != 1:
                    return False

        return differences == 1

    def is_good(self, tableau):
        """Check if _tableau_ is a valid vertex label for this lattice.
        """
        for idx in range(1, len(tableau)):
            if tableau[idx] - tableau[idx - 1] == 1:
                return False

        for idx, coord in enumerate(tableau):
            if not idx * self.scale < coord <= (1 + idx) * self.scale:
                return False

        return True

    @staticmethod
    def satisfies_crossing_relation(node):
        pass

    def component(self, node, color):
        """Return the _color_-component in which _node_ lies.
        """
        component = set()
        frontier = set(node)

        while frontier:
            next_frontier = set()
            for fnode in frontier:
                component.add(fnode)

                for fneighbor in self.neighbors(fnode):
                    if fneighbor not in component:
                        if self[fnode][fneighbor]['color'] == color:
                            next_frontier.add(fneighbor)
            frontier = next_frontier

        return frozenset(component)


    def tableaux(self):
        """Return all valid tableaux for this lattice.
        """
        min_tab = list(range(1, self.scale * self.order, self.scale))
        offsets = product(range(self.scale), repeat=self.order)
        for offset in offsets:
            tab = tuple(map(operator.add, min_tab, offset))
            if self.is_good(tab):
                yield tab

    def solve(self):
        """Attempt to find a solution for the diamond and crossing relations.

        Until the lattice is solved or there is a deadlock, repeat:
        Step 1a: Check components for solubility (cis-color propagation)
        Step 1b: Check vertices for soluble crossing relations (trans-color propagation)
        """
        components = []
        for color in range(1, self.scale):
            components[color] = set()
            for node in self.nodes():
                if not any(node in component for component in components):
                    components[color].add(self.component(node, color))

    @staticmethod
    def solve_component_lm3(component):
        """Return a dictionary {edge: weight} satisfying the diamond and/or
        crossing relations for this component, or None if there is no such
        solution.

        These solutions are limited to those components appearing in Fibonacci
        lattices of order 3. I have not yet proven that this list is
        exhaustive, but I have no reason to believe that any more components
        appear.

        Components are identified by their spectrum. I suspect but have not
        proven that no isospectral components appear.

        This should really be refactored off to a subclass, but I'm going to
        wait until that's actually necessary.
        """
        # A: (a, b, a, b).

        # A2: g = (3 - a)/(1 + a),
        # (a, 3-a, 1+a, ag), (ag, 1+g, 3-g, g).
        # a != -1.
         
