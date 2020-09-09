from typing import List, Tuple, Dict


class NonDeterministic:
    """
    ------------------------------------------------------------------
    Automata.NFSA: NonDeterministic
    ------------------------------------------------------------------
    """

    def __init__(self, nfsa_dict: Dict[Tuple[str, str], List[str]],
                 initial: str, accept: List[str]):
        self.nfsa_dict = nfsa_dict  # in the form (q0, str):[q0, q1]
        self.initial = initial
        self.accept = accept

    def is_accepting(self, input_string: str):
        result = self.transit(self.initial, input_string)
        print('possible state = ', result)

        # if there's intersection between result and accept, return True
        for s in result:
            if s in self.accept:
                return True
        return False

    def transit(self, state: str, s: str):
        result = []
        if len(s) == 0:
            result.append(state)
            if (state, '') in self.nfsa_dict:
                result.extend(self.nfsa_dict[(state, '')])
            return result

        y = s[:len(s) - 1]  # string before last symbol
        a = s[-1]  # last symbol

        possible_y_state = self.transit(state, y)  # all possible state before reading the last symbol

        for sub_y_state in possible_y_state:
            if (sub_y_state, a) in self.nfsa_dict:
                result.extend(self.nfsa_dict[(sub_y_state, a)])

        for sub_result in result:
            if (sub_result, '') in self.nfsa_dict:
                result.extend(self.nfsa_dict[(sub_result, '')])

        return result
