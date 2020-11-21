from abc import ABC, abstractmethod


class Watcher(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def run(self):
        pass
