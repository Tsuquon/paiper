from abc import ABC, abstractmethod

class ScrapeFramework:
    
    @abstractmethod
    def get_clubs(self, clubs):
        raise NotImplementedError("Method not imported")
    
    @abstractmethod
    def process_clubs(self, clubs):
        raise NotImplementedError("Method not imported")
    
    @abstractmethod
    def get_events(self, events):
        raise NotImplementedError("Method not imported")
    
    @abstractmethod
    def process_events(self, events):
        raise NotImplementedError("Method not imported")
    
    @abstractmethod
    def main():
        pass