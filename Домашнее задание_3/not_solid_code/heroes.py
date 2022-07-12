from antagonistfinder import AntagonistFinder
from abc import ABC, abstractmethod

        
class Fire_a_gun(self):
    def attack(self):
        print('PIU PIU')


class Incinerate_with_lasers:
    def ultimate(self):
        print('Wzzzuuuup!')


class Roundhouse_kick:
    def attack(self):
        print('Bump')


class Superman_attack:
    def attack(self):
        print("Kick")
   
class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)
        
        @abstractmethod
    def attack(self):
        pass

    def ultimate(self):
        pass
    
class Superman(Superman_attack, Incinerate_with_lasers, SuperHero):
    def __init__(self):
        super(Superman, self).__init__("Clark Kent", True)
        

class Chuck_Noris(Fire_a_gun, SuperHero):
    def __init__(self):
        super(Chuck_Noris, self).__init__("Chuck Noris", False)
    def create_news(self, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')

   
