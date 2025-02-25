import pickle
from datetime import datetime


class Animal:
    def __init__(self, name: str, age: int, kind: str):
        self.name = name
        self.age = age
        self.kind = kind

    def make_sound(self):
        print('Животное издает звук')

    def eat(self):
        print(f'{self.name} кушает')


class Bird(Animal):
    def __init__(self, name: str, age: int, kind: str,
                 ability_to_sing: bool = False, is_fly: bool = True):
        super().__init__(name, age, kind)
        self.ability_to_sing = ability_to_sing
        self.is_fly = is_fly

    def make_sound(self):
        if self.ability_to_sing:
            print(f'{self.name} красиво поет')
        else:
            print(f'{self.name} кряхтит')

    def fly(self):
        if self.is_fly:
            print(f'{self.name} летит')
        else:
            print(f"{self.name} не умеет летать")


class Mammal(Animal):
    def __init__(self, name: str, age: int, kind: str,
                 dangerous: bool = False):
        super().__init__(name, age, kind)
        self.dangerous = dangerous

    def make_sound(self):
        if self.dangerous:
            print(f'{self.name} рычит')
        else:
            print(f'{self.name} издает звук')

    def run(self):
        if self.dangerous:
            self.make_sound()
            print(f'И гонится за дичью')
        else:
            print(f'{self.name} убегает от хищника')


class Reptile(Animal):
    def __init__(self, name: str, age: int, kind: str):
        super().__init__(name, age, kind)

    def make_sound(self):
        print(f'{self.name} шипит')

    def crawl(self):
        print(f'{self.name} крадется')


class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hire_date = datetime.now()


class Veterinarian(Employee):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def heal_animal(self, animal: Animal):
        print(f'{self.name} лечит {animal.name}')


class ZooKeeper(Employee):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def feed_animal(self, animal: Animal):
        print(f'{self.name} кормит {animal.name}')


class Zoo:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.animals = []
        self.employees = []

    def add_animal(self, class_name, parameters):
        animal = class_name(*parameters)
        self.animals.append(animal)

    def add_employee(self, class_name, name, age):
        employee = class_name(name, age)
        self.employees.append(employee)

    def animal_sounds(self):
        for animal in self.animals:
            animal.make_sound()

    def save_state(self, filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_state(cls, filename: str):
        with open(filename, 'rb') as f:
            return pickle.load(f)


# Пример использования
if __name__ == "__main__":
    # Создание зоопарка
    my_zoo = Zoo("Дикий мир", "ул. Зоологическая, 1")

    # Добавление животных
    my_zoo.add_animal(Bird,{'name':"Кеша", 'age': 2, 'kind': "Попугай",  'ability_to_sing':True})
    my_zoo.add_animal(Mammal,{"name":"Барсик", 'age':5, 'kind': "Тигр", 'dangerous':True})
    my_zoo.add_animal(Reptile,{"name":"Гена", 'age':10, "kind": "Крокодил"})

    # Добавление сотрудников
    my_zoo.add_employee(ZooKeeper, "Иван Иванов", 30)
    my_zoo.add_employee(Veterinarian,"Мария Иванова", 28)

    # Демонстрация полиморфизма
    print("\nЗвуки животных:")
    my_zoo.animal_sounds()

    # Работа сотрудников
    keeper = my_zoo.employees[0]
    vet = my_zoo.employees[1]
    keeper.feed_animal(my_zoo.animals[0])
    vet.heal_animal(my_zoo.animals[1])

    # Сохранение состояния
    my_zoo.save_state("zoo_state.pkl")
    print('Запись в файл')


    # Загрузка состояния
    loaded_zoo = Zoo.load_state("zoo_state.pkl")
    print("\nПосле загрузки:")
    loaded_zoo.animal_sounds()