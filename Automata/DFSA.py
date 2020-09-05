class Deterministic:
    def __init__(self, dfsa_dict, initial, accept):
        """
        ------------------------------------------------------------------
        __init__: Initializes DFSA via Python dictionary.
        ------------------------------------------------------------------
        Parameters:
            dfsa_dict: Dictionary that contains the transition functon of DFSA
                Example:
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

        y = str[:len(str) - 1]
        a = str[-1]

        if (self.transit(state, y), a) in self.dfsa_dict:
            return self.dfsa_dict[(self.transit(state, y), a)]

        return self.dfsa_dict[('dead', a)]

    def is_accepting(self, input_string):

        return self.transit(self.initial, input_string) in self.accept
