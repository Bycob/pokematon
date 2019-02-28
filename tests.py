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
import pokematon as pkm

def create_test_dfa():
    """
    Create a Deterministic Finite Automaton for testing purpose.
    
    Returns: a tuple (dfa, alphabet)
    """
    
    dfa = machines.FiniteMachine()
    dfa.add_state("1")
    dfa.add_state("2")
    dfa.add_state("3");
    dfa.add_state("4");
    dfa.add_state("5", terminal=True);
    dfa.add_state("6", terminal=True);
    
    dfa.add_transition("1", "2", "a")
    dfa.add_transition("1", "3", "b")
    
    # TODO end
    return dfa, ['a', 'b', 'c']
    
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
            automaton.validate()
        
        self.assertEqual(c, 768)
    