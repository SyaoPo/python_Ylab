from typing import Union
from heroes import Superman, SuperHero, Chuck_Noris
from places import Kostroma, Tokyo
from media import TV

def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    TV(hero, place).create_news()


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(Chuck_Noris(), Tokyo())
