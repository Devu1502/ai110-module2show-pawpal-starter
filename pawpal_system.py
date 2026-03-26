from dataclasses import dataclass, field
from typing import List


# Task
@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str  # "low", "medium", "high"


# Pet
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks


# Owner
@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self) -> List[Pet]:
        return self.pets


# Scheduler
class Scheduler:
    def __init__(self):
        self.schedule: List[Task] = []

    def add_task(self, task: Task):
        self.schedule.append(task)

    def sort_by_priority(self) -> List[Task]:
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(self.schedule, key=lambda t: priority_order.get(t.priority, 4))

    def get_schedule(self) -> List[Task]:
        return self.schedule