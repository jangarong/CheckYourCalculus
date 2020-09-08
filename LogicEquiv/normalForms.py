

class NormalForms:
    """
    ------------------------------------------------------------------
    normalForms.NormalForms: Gets CNF and DNF (dependant on TruthTable
    objects).
    ------------------------------------------------------------------
    """

    def dnf(self, predicate: str):
        truth_table = self.generate_truth_table(predicate)
        var_lst = self.get_vars(predicate)
        res = '('
        for key in truth_table.keys():
            if truth_table[key] == '1':

                # conjoin based on key
                sub_res = '('
                for i in range(len(key)):
                    if key[i] == '0':
                        sub_res += '(\\neg' + var_lst[i] + ')'
                    else:
                        sub_res += var_lst[i]
                    sub_res += ' \\wedge '
                sub_res = sub_res[:-len(' \\wedge ')] + ')'

                # remove redundant brackets if necessary
                if '\\wedge' not in sub_res:
                    sub_res = sub_res[1:-1]

                # disjunct everything else
                res += sub_res + ' \\vee '

        if len(res) > 0:
            return res[:-len(' \\vee ')] + ')'
        else:
            return ''   # None exist?
