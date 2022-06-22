import abc


class AbstractDao(abc.ABC):
    @abc.abstractmethod
    def add(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abc.abstractmethod
    def find(self, search_params):
        raise NotImplementedError