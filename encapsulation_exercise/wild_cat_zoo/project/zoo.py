from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary_worker = 0
        for worker in self.workers:
            total_salary_worker += worker.salary
        if self.__budget >= total_salary_worker:
            self.__budget -= total_salary_worker
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_cost = 0
        for animal in self.animals:
            total_cost += animal.money_for_care

        if self.__budget >= total_cost:
            self.__budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(repr(animal))
        result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        result.extend(lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        vet = []
        caretaker = []
        keeper = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keeper.append(repr(worker))
            elif worker.__class__.__name__ == "Vet":
                vet.append(repr(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretaker.append(repr(worker))

        result = [f"You have {len(self.workers)} workers", f"----- {len(keeper)} Keepers:"]
        result.extend(keeper)
        result.append(f"----- {len(caretaker)} Caretakers:")
        result.extend(caretaker)
        result.append(f"----- {len(vet)} Vets:")
        result.extend(vet)

        return "\n".join(result)
