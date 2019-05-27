from itertools import product
import operator

class FibonacciLattice:
    def __init__(self, n, k):
        self.n = n  # colors + 1
        self.k = k  # order
        self.V = list(self.tableaux()) # vertex set
        self.E = {v : list(self.neighbors(v)) for v in self.V} # edge dictionary
        self.components = {color : self.components(color) for color in range(1, n)}

    def is_good(self, v):
        for idx in range(1, len(v)):
            if v[idx] - v[idx - 1] == 1:
                return False

        for idx, coord in enumerate(v):
            if not (idx * self.n < coord <= (1 + idx) * self.n):
                return False

        return True

    def tableaux(self):
        min_tab = list(range(1, self.n * self.k, self.n))
        offsets = product(range(self.n), repeat=self.k)
        for offset in offsets:
            tab = tuple(map(operator.add, min_tab, offset))
            if self.is_good(tab):
                yield tab

    def color(self, tab1, tab2):
        diffs = [z for z in zip(tab1, tab2) if z[0] != z[1]]
        if len(diffs) == 1 and max(diffs[0]) - min(diffs[0]) == 1:
            lower_label = min(diffs[0])

            # The following variables refer to this zero-indexed grid:
            # 1   n-1 1   n-1 (k columns)
            # 2   n-2 2   n-2 ...
            # ... 
            # n-1 1   n-1 1
            # The color is given by the element in column lower_label // n
            # and row lower_label % n.
            col = lower_label // self.n
            row = lower_label - self.n * col
            if col % 2 == 0:
                return row
            else:
                return self.n - row
        return 0

    def neighbors(self, v, color=None):
        """Generate a list of """
        for idx in range(self.k):
            dv = [0] * self.k
            dv[idx] = 1
            for op in (operator.add, operator.sub):
                neighbor = tuple(map(op, v, dv)) 
                if (not color or self.color(v, neighbor) == color) and self.is_good(neighbor):
                    yield neighbor

    def components(self, color):
        if color > self.n - 1:
            return None

        components = []

        for v in self.V:
            for c in components[::-1]:
                if v in c:
                    v_comp = c
                    break
            else:
                v_comp = set([v])
                components.append(v_comp)

            v_comp.update(self.neighbors(v, color))

        return components

    def weight(self, v):
        weight = []
        for color in range(1, self.n):
            comp = [c for c in self.components[color] if v in c][0]
            ranks = [sum(v) for v in comp]
            height = max(ranks) - min(ranks)
            depth = max(ranks) - sum(v)

            weight.append(2 * depth - height)
        return tuple(weight)

    def gen_relations(self, vset, color):
        def vname(v):
            return "v" + "_".join(str(c) for c in v)
        
        def ename(e):
            return "e" +  ""
        
        for v in vset:
            pass
