class Grammar:
    """
    ------------------------------------------------------------------
    CFG.Grammar: Grammar
    ------------------------------------------------------------------
    """

    def is_accepting_recursive(self, input_string, curr_production):
        print('\"'+input_string+'\"')
        self.index_stack.append(['|', None, None])  # to keep track of depth
        for terminal in self.cfg_dict[curr_production]:
            if terminal == input_string:
                return True
            else:

                # iterate through the terminal
                string_i = 0
                terminal_i = 0
                valid = True
                while terminal_i < len(terminal):

                    print(string_i, terminal_i, terminal, self.index_stack, '"'+
                          input_string[string_i:]+'"', '"'+terminal[terminal_i:]+'"')

                    # if it's a symbol
                    if terminal[terminal_i] in self.cfg_dict.keys():

                        # add to stack only if we've never seen this before
                        if (self.index_stack[len(self.index_stack) - 1][1] is None or
                                self.index_stack[len(self.index_stack) - 1][1] != string_i):
                            self.index_stack.append([0, string_i, terminal_i])

                        # take the rest of the substring and reduce it until we get correct indices
                        inner_res = False
                        while (string_i + self.index_stack[len(self.index_stack) - 1][0] <=
                               len(input_string) and not inner_res):

                            # reduce substring
                            self.index_stack[len(self.index_stack) - 1][0] -= 1

                            # check if this substring is valid
                            inner_res = (self.is_accepting_recursive(
                                input_string
                                [string_i:self.index_stack[len(self.index_stack) - 1][0]],
                                terminal[terminal_i]))

                            # remove depth stack
                            self.index_stack.pop(len(self.index_stack) - 1)

                        # none of the combinations work at this stage
                        if (string_i + self.index_stack[len(self.index_stack) - 1][0] >
                                len(input_string)):

                            # pop this stack
                            self.index_stack.pop(len(self.index_stack) - 1)

                            # check if this depth's stack is empty.
                            if self.index_stack[len(self.index_stack) - 1][0] == '|':
                                print('NO MATCH => BREAK')
                                valid = False
                                break

                            # go back to the last point
                            else:
                                print('NO MATCH => BACKTRACK')
                                string_i = self.index_stack[len(self.index_stack) - 1][1]
                                terminal_i = self.index_stack[len(self.index_stack) - 1][2]

                        # move to next character
                        else:
                            print('ACCEPTED')
                            string_i = (self.index_stack[len(self.index_stack) - 1][0] +
                                        len(input_string))
                            terminal_i += 1

                    # if they don't match up
                    elif terminal[terminal_i] != input_string[string_i]:

                        # check if this depth's stack is empty.
                        if self.index_stack[len(self.index_stack) - 1][0] == '|':
                            print('MISMATCH => BREAK')
                            valid = False
                            break

                        # go back to the last point
                        else:
                            print('MISMATCH => BACKTRACK')
                            string_i = self.index_stack[len(self.index_stack) - 1][1]
                            terminal_i = self.index_stack[len(self.index_stack) - 1][2]

                    else:
                        string_i += 1
                        terminal_i += 1

                # ends are met, and all is valid
                if (valid and terminal != '' and terminal_i == len(terminal)
                        and string_i == len(input_string)):
                    print(string_i, terminal_i, terminal, self.index_stack, '"' +
                          input_string[string_i:] + '"', '"' + terminal[terminal_i:] + '"')
                    return True
                # else:
                #     if self.index_stack[len(self.index_stack) - 1][0] != '|':
                #         self.index_stack.pop(len(self.index_stack) - 1)

        return False

    def is_accepting(self, input_string):

        # check if the string does not contain CFG symbols
        for key in self.cfg_dict.keys():
            if key in input_string:
                return False

        # use backtracking to determine whether this string gets accepted or not.
        res = self.is_accepting_recursive(input_string, 'S')
        self.index_stack = []
        return res

    def __init__(self, cfg_dict):
        """
        ------------------------------------------------------------------
        __init__: Initializes CFG via Python dictionary.
        ------------------------------------------------------------------
        Parameters:
            cfg_dict: Dictionary that contains the grammar of the CFG.
                Example: {'S': ['', '1', '0', '1S1', '0S0']}
        ------------------------------------------------------------------
        """
        self.cfg_dict = cfg_dict
        self.index_stack = []


