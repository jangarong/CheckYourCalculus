from Automata.NFSA import NonDeterministic

n = NonDeterministic({('q0', '0'): ['q1'],
                      ('q1', '0'): ['q1', 'q2'],
                      ('q1', '1'): ['q1'],
                      ('q2', ''): ['q0', 'q1']}, 'q0', ['q2'])

# print(n.is_accepting('010')) #true
# print(n.is_accepting('001')) #false

n2 = NonDeterministic({('q0', '5'): ['q1'],
                       ('q0', '7'): ['q2'],
                       ('q0', ''): ['q2'],
                       ('q1', ''): ['q3'],
                       ('q2', ''): ['q3'],
                       ('q3', '5'): ['q4'],
                       ('q4', '7'): ['q3'],
                       ('q4', ''): ['q3']
                       }, 'q0', ['q3'])

print(n2.is_accepting(''))  # true
print(n2.is_accepting('55'))  # true
print(n2.is_accepting('75757557'))  # true
print(n2.is_accepting('555775'))  # false
