from abc import ABC, abstractmethod
import type_enforced

class ScrapeFramework(ABC):
    
    @type_enforced.Enforcer
    @abstractmethod
    def get_clubs(self, clubs: list[str]):
        raise NotImplementedError("Method not imported")
    
    @type_enforced.Enforcer
    @abstractmethod
    def process_clubs(self, clubs: list[str]):
        raise NotImplementedError("Method not imported")

    # need event_name, club_name, start_date, end_date, price, description
    @type_enforced.Enforcer
    @abstractmethod
    def get_events(self, events: list[str]):
        raise NotImplementedError("Method not imported")
    
    @type_enforced.Enforcer
    @abstractmethod
    def process_events(self, events: list[str]):
        raise NotImplementedError("Method not imported")
    
    @abstractmethod
    def main():
        pass