import sympy as sm


class Proof:
    """
    ------------------------------------------------------------------
    SqueezeTheorem.Proof: Proof structure for Squeeze Theorem Proofs.
    Goal: the limit of both sides need to equal each other.
    ------------------------------------------------------------------
    """

    def pop(self):
        """
        ------------------------------------------------------------------
        pop: Removes last equation.
        ------------------------------------------------------------------
        Returns:
            Equation that was removed.
        ------------------------------------------------------------------
        """
        if self.equations:
            return self.equations.pop(len(self.equations) - 1)
        else:
            print("No equations to remove!")
            return None

    def eval(self):
        """
        ------------------------------------------------------------------
        eval: Applies squeeze theorem if possible.
        ------------------------------------------------------------------
        """
        if self.equations:
            l1 = sm.limit(self.equations[len(self.equations) - 1][0], sm.Symbol('x'), self.x0,
                          dir=self.direction)
            l3 = sm.limit(self.equations[len(self.equations) - 1][2], sm.Symbol('x'), self.x0,
                          dir=self.direction)
            if l1 == l3:
                self.finish = True
                self.limit = l1
        else:
            print("Cannot apply squeeze theorem. Limits are not the same/no equations in list.")

    def insert(self, f1, f2, f3):
        """
        ------------------------------------------------------------------
        insert: Inserts valid inequality.
        ------------------------------------------------------------------
        Parameters:
            f1: Left hand side expression
            f2: Center expression.
            f3: Right hand expression.
        ------------------------------------------------------------------
        """
        # sub actual xs
        local_f1 = f1.subs({'x': self.x})
        local_f2 = f2.subs({'x': self.x})
        local_f3 = f3.subs({'x': self.x})

        # check if their solution is over the reals
        s1 = sm.solveset(local_f1 <= local_f2, self.x, domain=sm.S.Reals)
        s2 = sm.solveset(local_f2 <= local_f3, self.x, domain=sm.S.Reals)
        if s1 == s2 and s1 == sm.S.Reals and not self.finish:
            self.equations.append((local_f1, local_f2, local_f3))
        else:
            print("Not a valid inequality!")

    def __init__(self, fx, x0, direction="+-"):
        """
        ------------------------------------------------------------------
        __init__: Initializes Squeeze Theorem proof structure.
        ------------------------------------------------------------------
        Parameters:
            fx: The given function we're taking the limit of.
            x0: What x is approaching.
            direction: In which direction x is approaching.
        ------------------------------------------------------------------
        """

        # store equations in a list and make parameters public variables
        self.equations = []
        self.direction = direction
        self.x0 = x0
        self.fx = fx
        self.finish = False
        self.limit = 0
        self.x = sm.Symbol("x", real=True)
