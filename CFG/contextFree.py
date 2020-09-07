class Grammar:
    def __init__(self, cfg_dict, start):
        self.cfg_dict = cfg_dict  # {var: [str+var+str, str]}
        self.start = start
        self.max_depth = self.get_max_depth()

    def is_accepting(self, input_string):
        # first initialize the input_string into a string that contains a variable
        # for every possible string, check if some sub string can be replaced by other variable
        # repeat this until only get the start variable

        init_list = self.initialize(input_string)
        for init in init_list:
            result = self.production(init)
            if result:
                return True
        return False

    def initialize(self, str):
        # return list of str where sub str is replaced by a variable
        # example: 101 -> [S01, 1S1, 10S] if S->0,1,1S1,0S0
        result_list = []

        keys = self.cfg_dict.keys()
        for key in keys:
            for value in self.cfg_dict[key]:  # traverse every value in dict
                for sub_key in keys:
                    if value.find(sub_key) == -1:
                        # a string without variable
                        if value == '':
                            # empty str, insert the variable everywhere
                            for i in range(len(str) + 1):
                                result = str[0: i] + key + str[i:]
                                result_list.append(result)
                        else:
                            # non-empty value, find value in str, replace by key
                            for i in range(len(str)):
                                if str.startswith(value, i):
                                    result = self.replace(str, i, value, key)
                                    result_list.append(result)
        return result_list

    def replace(self, str, i, substr, target):
        # replace substr by target (in the i th position at str)
        # example: replace('012345', 2, '234', 'A') -> '01A5'
        if (str[i: i + len(substr)] != substr):
            # debug message
            print("Substr not start at i th position")
            print("slice = ", str[i: i + len(substr)], "  sub str = ", substr)
            return;

        return str[:i] + target + str[i + len(substr):]

    def get_max_depth(self):
        # max of a variable appears in value
        max_count = 1
        keys = self.cfg_dict.keys()
        for key in keys:
            for value in self.cfg_dict[key]:  # traverse every value in dict
                count = 0
                for sub_key in keys:
                    count += value.count(sub_key)
                if count > max_count:
                    max_count = count
        return max_count

    def get_num_var(self, str):
        count = 0
        keys = self.cfg_dict.keys()
        for sub_key in keys:
            count += str.count(sub_key)

        return count

    def production(self, str):
        # if str is not start variable and can't be replaced anymore, return false
        # rerun initialize if there are more than one sub str to be replaced by variable
        # count the number of variables in str, run only if < max_depth

        if self.get_num_var(str) > self.max_depth:
            return False

        # base case: if str is start variable, return true
        if str == self.start:
            return True

        keys = self.cfg_dict.keys()
        for key in keys:
            for value in self.cfg_dict[key]:  # traverse every value in dict
                for i in range(len(str)):
                    if str.startswith(value, i) and value != '':
                        replaced_str = self.replace(str, i, value, key)
                        replaced_result = self.production(replaced_str)
                        if replaced_result:
                            return True

        re_init_list = self.initialize(str)
        for re_init in re_init_list:
            return self.production(re_init)

        return False
