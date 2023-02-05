from abc import ABC, abstractmethod


class abstract_tfstate(ABC):

    def __init__(self, path_input):
        self.tfstates = dict() # filled by the `_get` method
        self.mapping = dict() # filled by the `_get` method
        self.path_input = path_input
        self._get()

    @abstractmethod
    def _get(self):
        pass
