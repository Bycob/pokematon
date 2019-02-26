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

from automaton import machines

def automatons_of_size(alphabet, size):
    """
    Iterate through all undeterministic automaton of given size with the given
    alphabet (using yield)
    """
    pass
    
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
    
def is_intersection_empty(dfa1, dfa2):
    """
    Check wether the intersection of the two automaton is empty or not
    """
    return False
    