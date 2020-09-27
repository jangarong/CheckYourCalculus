class LESymbol:
    """
    ------------------------------------------------------------------
    LESymbol: CDT for symbol operations.
    ------------------------------------------------------------------
    """

    def __init__(self, char: str, order: int, truth_table: dict):
        self.order = order
        self.truth_table = truth_table
        self.char = char
        if len(truth_table.keys()) > 4:
            print("Symbols that take more than 2 variables have not"
                  "been implemented yet for Truth Tables.")

        # note to self: should display an error if the char is ' ', '(' or ')'

