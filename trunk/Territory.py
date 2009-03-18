#Copyright 2009 Brian Meeker
#
#This file is part of pyFish.
#
#pyFish is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#pyFish is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with pyFish.  If not, see <http://www.gnu.org/licenses/>.

class Territory:
    
    def __init__(self, name, neighbors, owner, armies):
        assert isinstance(name, str)
        self._name = name
        self._owner = owner
        self._neighbors = neighbors
        assert armies > 0, "A territory must have at least 1 army"
        self._armies = armies
        
    @property
    def name(self):
        return self._name
    
    @property
    def neighbors(self):
        return self._neighbors
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner
    
    @property
    def armies(self):
        return self._armies
    
    @armies.setter
    def armies(self, armies):
        assert armies > 0, "A territory must have at least 1 army"
        self._armies = armies