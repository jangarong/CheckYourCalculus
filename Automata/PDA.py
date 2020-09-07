class PushDown:
    def __init__(self, pda_dict, initial, accept):
        self.pda_dict = pda_dict  # (state1, symbol, stack1): [(state2, stack2)]
        self.initial = initial
        self.accept = accept

    def is_accepting(self, input_string):
        tups = self.transit(self.initial, input_string, [])
        print('all possible outcome = ', tups)
        # all possible outcome in list of tups: [(state, stack), (...)]

        for tup in tups:
            if (tup[0] in self.accept) and (tup[1] == []):
                # end in accpeting state and empty stack
                return True
        return False

    def transit(self, state, str, stack):
        list_of_tups = []  # in the form [(state, stack)]

        # base case: str is empty
        if len(str) == 0:
            list_of_tups.append((state, stack))
            for key in self.pda_dict.keys():
                if (key[0] == state) and (key[1] == ''):
                    for value in self.pda_dict[key]:
                        if (len(key[2]) == 0) and (len(value[1]) == 1):  # e->X
                            list_of_tups.append((value[0], value[1]))
                        elif (len(key[2]) == 0) and (len(value[1]) == 0):  # e->e
                            list_of_tups.append((value[0], []))

        else:
            y = str[:len(str) - 1]  # string before last symbol
            a = str[-1]  # last symbol
            y_list = self.transit(state, y, stack)

            for y_tup in y_list:
                # given state and stack of y, calculate state and stack after adding a
                # then add (new_state, new_stack) to list_of_tups
                list_of_tups = self.update_state_stack(y_tup, a, list_of_tups)

        for sub_tup in list_of_tups:
            list_of_tups = self.update_state_stack(sub_tup, '', list_of_tups)

        return list_of_tups

    def update_state_stack(self, tup, char, list_of_tups):
        for key in self.pda_dict.keys():
            if (key[0] == tup[0]) and (key[1] == char):
                for value in self.pda_dict[key]:
                    if (len(key[2]) == 0) and (len(value[1]) == 1):  # e->X
                        tup_stack_copy = tup[1].copy()
                        tup_stack_copy.append(value[1])
                        list_of_tups.append((value[0], tup_stack_copy))

                    elif (len(key[2]) == 0) and (len(value[1]) == 0):  # e->e
                        list_of_tups.append((value[0], tup[1].copy()))

                    elif (len(key[2]) == 1) and (len(value[1]) == 0) and (len(tup[1]) != 0) and (
                            tup[1][len(tup[1]) - 1] == key[2]):  # X->e
                        tup_stack_copy = tup[1].copy()
                        tup_stack_copy.pop()
                        list_of_tups.append((value[0], tup_stack_copy))

                    elif (len(key[2]) == 1) and (len(value[1]) == 1) and (len(tup[1]) != 0) and (
                            tup[1][len(tup[1]) - 1] == key[2]):  # X->Y
                        tup_stack_copy = tup[1].copy()
                        tup_stack_copy[len(tup[1]) - 1] = value[1]
                        list_of_tups.append((value[0], tup_stack_copy))

        return list_of_tups
