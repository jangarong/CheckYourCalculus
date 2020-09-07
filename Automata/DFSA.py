from typing import Tuple, Dict, List


class Deterministic:
    """
    ------------------------------------------------------------------
    Automata.DFSA: DFSA
    ------------------------------------------------------------------
    """

    def __init__(self, dfsa_dict: Dict[Tuple[str, str], str],
                 initial: str, accept: List[str]):
        """
        ------------------------------------------------------------------
        __init__: Initializes DFSA via Python dictionary.
        ------------------------------------------------------------------
        Parameters:
            dfsa_dict: Dictionary that contains the transition function of DFSA
                Example: {('q0', '1'): 'q1', ('q1', '0'): 'q0'}
        ------------------------------------------------------------------
        """
        self.dfsa_dict = dfsa_dict  # in the form (q0, str):q1
        self.dfsa_dict[('dead', '0')] = 'dead'  # add dead state
        self.dfsa_dict[('dead', '1')] = 'dead'

        self.initial = initial  # string of initial state
        self.accept = accept  # array of str of accepting state

    def transit(self, state: str, s: str):
        # input is empty string
        if len(s) == 0:
            return state

        y = s[:len(s) - 1]  # state before last symbol
        a = s[-1]  # last symbol

        y_state = (self.transit(state, y), a)
        print('step', len(y), ': current string = ', y,
              ', current state = ', y_state[0])

        if y_state in self.dfsa_dict:
            return self.dfsa_dict[y_state]

        return self.dfsa_dict[('dead', a)]

    def is_accepting(self, input_string: str):
        result = self.transit(self.initial, input_string)
        print('step', len(input_string), ': current string = ',
              input_string, ', current state = ', result)

        return result in self.accept

    def give_examples(self):
        # give concrete examples that are accepted by DFSA
        # not finished

        result = []

        for accepted in self.accept:
            s = ''
            target_state = accepted
            for key in self.dfsa_dict.keys():
                if self.dfsa_dict[key] == target_state:
                    s = self.dfsa_dict[key][1] + s
                    target_state = self.dfsa_dict[key][0]
                # to be completed

        if s not in result:
            result.append(str)
        return result
