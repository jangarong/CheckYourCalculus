class Deterministic:
    """
    ------------------------------------------------------------------
    Automata.DFSA: DFSA
    ------------------------------------------------------------------
    """
    def __init__(self, dfsa_dict, initial, accept):
        """
        ------------------------------------------------------------------
        __init__: Initializes DFSA via Python dictionary.
        ------------------------------------------------------------------
        Parameters:
            dfsa_dict: Dictionary that contains the transition functon of DFSA
                Example: {('q0', '1'): 'q1', ('q1', '0'): 'q0'}
        ------------------------------------------------------------------
        """
        self.dfsa_dict = dfsa_dict  # in the form (q0, str):q1
        self.dfsa_dict[('dead', '0')] = 'dead';  # add dead state
        self.dfsa_dict[('dead', '1')] = 'dead';

        self.initial = initial  # string of initial state
        self.accept = accept  # array of str of accepting state

    def transit(self, state, str):
        # input is empty string
        if len(str) == 0:
            return state

        y = str[:len(str) - 1] #state before last symbol
        a = str[-1] # last symbol

        y_state = (self.transit(state, y), a)
        print('step', len(y), ': current string = ', y,
              ', current state = ', y_state[0])

        if y_state in self.dfsa_dict:
            return self.dfsa_dict[y_state]

        return self.dfsa_dict[('dead', a)]

    def is_accepting(self, input_string):
        result = self.transit(self.initial, input_string)
        print('step', len(input_string), ': current string = ',
              input_string, ', current state = ', result)

        return result in self.accept

    def give_examples(self):
        # give concrete examples that are accepted by DFSA
        # not finished

        result = [];

        for accepted in self.accept:
            str = ''
            target_state = accepted
            for key in self.dfsa_dict.keys():
                if self.dfsa_dict[key] == target_state:
                    str = self.dfsa_dict[key][1] + str
                    target_state = self.dfsa_dict[key][0]
                # to be completed

        if str not in result:
            result.append(str)
        return result
