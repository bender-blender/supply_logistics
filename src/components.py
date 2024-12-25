from abc import ABC, abstractmethod


class IStorage(ABC):
    """Хранилище

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def func(self):
        """Вывод содержимого

        Args:
            product (str): _description_
        """
        pass


class Box(IStorage):
    """Коробка

    Args:
        IStorage (_type_): _description_
    """
    def __init__(self, name: str, capacity:list):
        self.name = name
        self.capacity = capacity
    
    def func(self):
        return self.capacity


class Container(IStorage):
    """Контейнер

    Args:
        IStorage (_type_): _description_
    """
    def __init__(self):
        self.capacity = [] # Вместимость
    
    def add(self, object: IStorage):
        """Добавить в контейнер

        Args:
            object (IStorage): _description_
        """
        self.capacity.append(object)
    
    def remove(self, object: IStorage):
        """Удалить из контейнера

        Args:
            object (IStorage): _description_
        """
        self.capacity.remove(object)
    
    def func(self):
        result = [leaf.func() for leaf in self.capacity]
        return f"Контейнер\n{result}"


