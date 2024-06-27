from abc import ABC, abstractmethod
import type_enforced

class ScrapeFramework(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    # Accesses, formats the club list
    @abstractmethod
    def get_clubs(self, clubs: list[str]):
        raise NotImplementedError("Method not imported")

    # Accesses the events
    @abstractmethod
    def get_events(self, events: list[str]):
        raise NotImplementedError("Method not imported")
    