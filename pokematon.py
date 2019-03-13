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
from automata.fa.dfa import DFA

import copy

class AutomatonNotFound(Exception):
    pass

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


def powerset(state):
    """
    give the subset of an undeterministic automaton state
    """
    res =[[]]
    for s in state:
        newsub = [subset + [s] for subset in res]
        res.extend(newsub)
    return res


def convert_to_dfa(automaton):
    """
    Convert an undeterministic automaton to a deterministic one.
    """
    return DFA.from_nfa(automaton)

def get_complementary(automaton):
    temp_complementary = convert_to_dfa(automaton)
    temp_final_state = list(set(complementary.states) - set(complementary.final_states)- set(complementary.initial_states))
    complementary = DFA(
        states=temp_complementary.states,
        input_symbols=temp_complementary.input_symbols,
        transitions=temp_complementary.transitions,
        initial_state=temp_complementary.initial_state,
        final_states=temp_final_state
    )
    return complementary
    
# Louis
def is_intersection_empty(dfa1, dfa2):
    """
    Check wether the intersection of the two automaton is empty or not
    """
    return False

def are_isomorphic(dfa1, dfa2):
    """
    Check if 2 DFA are isomorph
    """
    if len(dfa1.states) != len(dfa2.states):
        return False
    
    sim_states = { dfa1.initial_state: dfa2.initial_state }
    next_states = { dfa1.initial_state }
    explored_states = set()
    
    # Check if transitions are isomorph
    while len(next_states) > 0:
        current_state = next_states.pop()
        current_state2 = sim_states[current_state]
        
        for (label, dst) in dfa1.transitions[current_state].items():
            dst2 = dfa2.transitions[current_state2][label]
            
            if dst in sim_states:
                if dst2 != sim_states[dst]:
                    return False
            else:
                next_states.add(dst)
                sim_states[dst] = dst2
        
        explored_states.add(current_state)
    
    # Check final states
    for state1, state2 in sim_states:
        if (state1 in dfa1.final_states) != (state2 in dfa2.final_states):
            return False
    
    return True
    
def get_minimal_nfa(dfa):
    """
    This is the core function of the project. Returns a NFA with
    the minimal number of states, that corresponds to this DFA.
    """
    for i in range(2, len(dfa.states) + 1):
        for nfa in automatons_of_size(dfa.input_symbols, i):
            test_dfa = convert_to_dfa(nfa)
            min_dfa = test_dfa.minify()
            
            if (dfa == test_dfa):
                return nfa
                
    raise AutomatonNotFound("The minimal automaton was not found. This is probably a bug.")
    