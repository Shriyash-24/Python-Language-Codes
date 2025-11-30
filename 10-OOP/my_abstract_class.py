# We need to derive Shape class from ABC module. Abstract Base Class (ABC).

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


