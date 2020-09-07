from Automata.PDA import PushDown


p2 = PushDown({('q0', '0', ''): [('q0', 'X'), ('q1', '')],
              ('q0', '1', ''): [('q0', 'Y'), ('q1', '')],
              ('q0', '', ''): [('q1', '')],
              ('q1', '0', 'X'): [('q1', '')],
              ('q1', '1', 'Y'): [('q1', '')]
              }, 'q0', ['q1'])

# accept palidrome
print(p2.is_accepting(''))
print(p2.is_accepting('0'))
print(p2.is_accepting('11'))
print(p2.is_accepting('1000110001'))
print(p2.is_accepting('101101101'))
print(p2.is_accepting('1011011011'))

