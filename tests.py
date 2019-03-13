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

"""


from unittest import TestCase
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
import pokematon as pkm

def create_test_dfa():
    """
    Create a Deterministic Finite Automaton for testing purpose.
    
    Returns: a DFA that can be used for tests
    """
    dfa = DFA(
        states={'q0', 'q1', 'q2'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q0', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q1'}
        },
        initial_state='q0',
        final_states={'q1'}
    )
    return dfa
    
def print_automaton(automaton):
    print("states: ", automaton.states)
    print("final states:", automaton.final_states)
    print("transitions: ", automaton.transitions, "\n")
    

class PokematonTest(TestCase):
    def setUp(self):
        pass
        
    def test_automatons_of_size(self):
        c = 0
        for automaton in pkm.automatons_of_size({'a', 'b'}, 2):
            c += 1
            # print_automaton(automaton)
            self.assertTrue(automaton.validate())
        
        self.assertEqual(c, 768)
    
    def test_are_isomorphic(self):
        dfa = DFA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'0', '1'},
            transitions={
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q0', '1': 'q2'},
                'q2': {'0': 'q2', '1': 'q1'}
            },
            initial_state='q0',
            final_states={'q1'}
        )
        
        dfac = DFA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'0', '1'},
            transitions={
                'q0': {'0': 'q0', '1': 'q2'},
                'q1': {'0': 'q1', '1': 'q2'},
                'q2': {'0': 'q0', '1': 'q1'}
            },
            initial_state='q0',
            final_states={'q2'}
        )
        
        self.assertTrue(pkm.are_isomorphic(dfa, dfac))
        
    def test_are_not_isomorphic_wrong_transition(self):
        dfa = DFA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'0', '1'},
            transitions={
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q0', '1': 'q2'},
                'q2': {'0': 'q2', '1': 'q1'}
            },
            initial_state='q0',
            final_states={'q1'}
        )
        
        dfae = DFA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'0', '1'},
            transitions={
                'q0': {'0': 'q0', '1': 'q2'},
                'q1': {'0': 'q1', '1': 'q2'},
                'q2': {'0': 'q0', '1': 'q2'}
            },
            initial_state='q0',
            final_states={'q2'}
        )
        
        self.assertFalse(pkm.are_isomorphic(dfa, dfae))
    
    def test_are_not_isomorphic_useless_state(self):
        dfa = DFA(
            states={'q0', 'q1', 'q2', 'q3'},
            input_symbols={'0', '1'},
            transitions={
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q0', '1': 'q2'},
                'q2': {'0': 'q2', '1': 'q1'},
                'q3': {'0': 'q2', '1': 'q1'}
            },
            initial_state='q0',
            final_states={'q1'}
        )
        
        dfae = DFA(
            states={'q0', 'q1', 'q2', 'q3'},
            input_symbols={'0', '1'},
            transitions={
                'q0': {'0': 'q0', '1': 'q2'},
                'q1': {'0': 'q1', '1': 'q2'},
                'q2': {'0': 'q0', '1': 'q1'},
                'q3': {'0': 'q2', '1': 'q1'}
            },
            initial_state='q0',
            final_states={'q2'}
        )
        
        self.assertFalse(pkm.are_isomorphic(dfa, dfae))
        
    def test_minimal_nfa(self):
        pass # pkm.get_minimal_nfa(create_test_dfa())
        