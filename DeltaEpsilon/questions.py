import random
import function_generator as fg
from DeltaEpsilon.proof import DeltaEpsilonProof


def question():
    """
    ------------------------------------------------------------------
    Delta.Epsilon.question: Creates a Delta Epsilon proof where you
    have to prove the limit of the randomized function.
    ------------------------------------------------------------------
    Returns:
        DeltaEpsilon proof that is ready for solving.
    ------------------------------------------------------------------
    """
    fx = [fg.get_polynomial(random.randint(0, 3)),
          fg.get_rational(random.randint(0, 2), random.randint(1, 2))][random.randint(0, 1)]
    x0 = random.randint(-10, 10)
    proof = DeltaEpsilonProof(fx, x0)
    return proof
