from DeltaEpsilon.questions import question
from DeltaEpsilon.proof import Proof
from DeltaEpsilon.parsing import latex_to_limit


def delta_epsilon_ui(proof):
    """
    ------------------------------------------------------------------
    delta_epsilon_ui: Console UI for delta epsilon proofs.
    ------------------------------------------------------------------
    Parameters:
        proof: The DeltaEpsilonProof object initialized beforehand.
    ------------------------------------------------------------------
    """
    while True:
        choice = input("Please select an option:\n"
                       "1. Insert equation\n"
                       "2. Bound delta/N by a constant\n"
                       "3. Insert equation to bound delta/N\n"
                       "4. Choose delta/N\n"
                       "5. Print all\n"
                       "6. Go Back\n")

        if choice == str(1):
            proof.insert(input("Type in your LaTeX equation.\n"))
        elif choice == str(2):
            proof.insert_bound_equation(input("Type in the constant you want to bound delta or N "
                                              "with.\n"))
        elif choice == str(3):
            proof.insert_bound_equation(input("Type in your LaTeX equation.\n"))
        elif choice == str(4):
            proof.choose_delta("Type in what delta/N is.\n")
        elif choice == str(5):
            proof.print_all()
        elif choice == str(6):
            return


def choice_1():
    """
    ------------------------------------------------------------------
    choice_1: Console UI for choice 1 (for Delta Epsilon proofs)
    ------------------------------------------------------------------
    """
    while True:
        choice = input("Please select an option:\n"
                       "1. Input your own LaTeX limit and prove it.\n"
                       "2. Generate a random Delta Epsilon question and prove it.\n"
                       "3. Go Back.\n")

        if choice == str(1):
            p = Proof(*latex_to_limit(input("Type in your LaTeX limit.\n")))
            delta_epsilon_ui(p)

        elif choice == str(2):
            p = question()
            delta_epsilon_ui(p)

        elif choice == str(3):
            return


def main_ui():
    """
    ------------------------------------------------------------------
    main_ui: Console UI for CheckYourCalculus
    ------------------------------------------------------------------
    """
    while True:
        choice = input("Please select an option:\n"
                       "1. Delta Epsilon Proofs.\n"
                       "2. Exit.\n")
        if choice == str(1):
            choice_1()
        elif choice == str(2):
            return


main_ui()
