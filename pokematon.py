"""

Copyright (C) 2019 Louis Jean, Maxence Hanin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Algorithm details

- Iterate through every possible undeterministic automaton, beginning
with the minimal number of states.
- For each undeterministic automaton :
    - Transform it to a deterministic one
    - Take the complementary automaton
    - Check that its language does not intersects with the initial deterministic
    automaton. If it is the case, then we found our minimal-sized automaton !
    
"""

from automata.fa.nfa import NFA

import copy

def create_nfa(size, alphabet={}):
    states = set()
    transitions = {}
    
    for i in range(size):
        states.add(str(i))
        transitions[str(i)] = {}
        
        for symbol in alphabet:
            transitions[str(i)][symbol] = set()
    
    return NFA(
        states=states,
        input_symbols=alphabet,
        transitions=transitions,
        initial_state="0",
        final_states=set()
    )

# Louis
def automatons_of_size(alphabet, size):
    """
    Iterate through all undeterministic automaton of given size with the given
    alphabet (using yield)
    """

    def possible_transitions(automaton, src_state, dst_state, symbols):
        if len(symbols) == 0:
            yield automaton
        else:
            symbol = symbols.pop()
            
            clone = copy.deepcopy(automaton)
            clone.transitions[str(src_state)][symbol].add(str(dst_state))
            
            for processed in [automaton, clone]: 
                for result in possible_transitions(processed, src_state, dst_state, symbols.copy()):
                    yield result

    def possible_graphs(automaton, src_state, dst_state):
        if dst_state >= size:
            src_state += 1
            dst_state = 0
        
        if src_state >= size:
            yield automaton
        else:
            for transition in possible_transitions(automaton, src_state, dst_state, alphabet.copy()):
                for full_graph in possible_graphs(transition, src_state, dst_state + 1):
                    yield full_graph

    for first_terminal in range(0, size):
        for start_state in {0, first_terminal}:
            automaton = create_nfa(size, alphabet)

            for i_state in range(first_terminal, size):
                automaton.final_states.add(str(i_state))

            automaton.initial_state = str(start_state)
            
            for possible_graph in possible_graphs(automaton, 0, 0):
                yield possible_graph


def convert_to_dfa(automaton):
    """
    Convert an undeterministic automaton to a deterministic one.
    """
    pass
    
def get_complementary(automaton):
    """
    Get the complementary automaton of this one
    """
    pass
    
# Louis
def is_intersection_empty(dfa1, dfa2):
    """
    Check wether the intersection of the two automaton is empty or not
    """
    return False
    