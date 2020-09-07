from Automata.DFSA import Deterministic

#use dictionary to describe DFSA
#use tuple as key of dic

#accept: {|x|>=2, x start and end with 0}
d = Deterministic({('q0', '0'): 'q1',
                   ('q1', '0'): 'q2',
                   ('q1', '1'): 'q3',
                   ('q2', '0'): 'q2',
                   ('q2', '1'): 'q3',
                   ('q3', '0'): 'q2',
                   ('q3', '1'): 'q3'}, 'q0', ['q2'])

# print(d.is_accepting('')) #false
# print(d.is_accepting('0')) #false
# print(d.is_accepting('1')) #false
# print(d.is_accepting('00')) #true
print(d.is_accepting('0111010')) #true
# print(d.is_accepting('100011')) #false