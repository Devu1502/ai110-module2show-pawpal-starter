from dataclasses import dataclass, field
from typing import List


# -------- Task --------
@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str  # "low", "medium", "high"


# -------- Pet --------
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass

    def get_tasks(self) -> List[Task]:
        pass


# -------- Owner --------
@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def get_pets(self) -> List[Pet]:
        pass


# -------- Scheduler --------
class Scheduler:
    def __init__(self):
        self.schedule: List[Task] = []

    def add_task(self, task: Task):
        pass

    def sort_by_priority(self) -> List[Task]:
        pass

    def get_schedule(self) -> List[Task]:
        pass