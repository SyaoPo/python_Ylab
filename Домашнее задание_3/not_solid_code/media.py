from abc import abstractmethod


class Media(ABC):
    def __init__(self, hero, place):
        self.place = place
        self.hero = hero

    @abstractmethod
    def create_news(self):
        pass


class TV(Media):
    def create_news(self, name_hero: str, place: Place):
        print(f'{self.name}: {name_hero} saved the {place.place_name}!')


