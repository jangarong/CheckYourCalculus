def tautology_contradiction(truth_table: dict) -> str:
    """
    ------------------------------------------------------------------
    normalForms.tautology_contradiction: Determines whether the truth
    table yields a tautology, contradiction, or neither
    ------------------------------------------------------------------
    Parameters:
        truth_table - Dictionary containing the truth table.
    Returns:
        '0' if Contradiction
        '1' if Tautology
        '2' if Neither
    ------------------------------------------------------------------
    """
    all0 = True
    all1 = True
    for key in truth_table:
        if truth_table[key] == '0':
            all1 = False
        else:
            all0 = False
        if not all0 and not all1:
            break

    if all0:
        return '0'
    elif all1:
        return '1'
    return '2'


class NormalForms:
    """
    ------------------------------------------------------------------
    normalForms.NormalForms: Gets CNF and DNF (dependant on TruthTable
    objects).
    ------------------------------------------------------------------
    """

    def dnf(self, predicate: str):
        """
        ------------------------------------------------------------------
        dnf: Gets the dnf of the given predicate.
        ------------------------------------------------------------------
        Parameters:
            predicate: Predicate that we want to turn into a DNF.
        Returns:
            Disjunctive Normal Form of the predicate.
        ------------------------------------------------------------------
        """
        # check whether tautology or contradiction
        truth_table = self.generate_truth_table(predicate)
        tc = tautology_contradiction(truth_table)
        if tc != '2':
            return tc

        var_lst = self.get_vars(predicate)
        res = '('
        for key in truth_table.keys():
            if truth_table[key] == '1':

                # conjoin based on key
                sub_res = '('
                for i in range(len(key)):
                    if key[i] == '0':
                        sub_res += '(\\neg ' + var_lst[i] + ')'
                    else:
                        sub_res += var_lst[i]
                    sub_res += ' \\wedge '
                sub_res = sub_res[:-len(' \\wedge ')] + ')'

                # remove redundant brackets if necessary
                if '\\wedge' not in sub_res:
                    sub_res = sub_res[1:-1]

                # disjunct everything else
                res += sub_res + ' \\vee '

        # if there's only one term, remove redundant brackets
        if res.count('\\wedge') == 1:
            res = res[1:-1]

        if len(res[:-len(' \\vee ')]) > 0:
            return res[:-len(' \\vee ')] + ')'
        else:
            return ''  # None? Or use a contradiction...

    def cnf(self, predicate: str):
        """
        ------------------------------------------------------------------
        cnf: Gets the cnf of the given predicate.
        ------------------------------------------------------------------
        Parameters:
            predicate: Predicate that we want to turn into a CNF.
        Returns:
            Conjunctive Normal Form of the predicate.
        ------------------------------------------------------------------
        """
        # check whether tautology or contradiction
        truth_table = self.generate_truth_table(predicate)
        tc = tautology_contradiction(truth_table)
        if tc != '2':
            return tc

        neg_pre = '(\\neg ' + predicate + ')'
        neg_pre_dnf = self.dnf(neg_pre)
        var_lst = self.get_vars(predicate)
        result = ''

        # apply De Morgan's Law
        i = 0
        while i < len(neg_pre_dnf):
            if neg_pre_dnf.startswith('\\wedge', i):
                result += '\\vee'
                i += len('\\wedge')
            elif neg_pre_dnf.startswith('\\vee', i):
                result += '\\wedge'
                i += len('\\vee')
            elif neg_pre_dnf[i] in var_lst:
                result += '(\\neg ' + neg_pre_dnf[i] + ')'
                i += 1
            else:
                result += neg_pre_dnf[i]
                i += 1

        # apply double negation law
        for var in var_lst:
            result = result.replace('(\\neg(\\neg ' + var + '))', var)

        # if result is just a bracket (usually when it gets simplified to nothing).
        if result == ')':
            return ''  # None? Or use a contradiction or some other method?

        return result
