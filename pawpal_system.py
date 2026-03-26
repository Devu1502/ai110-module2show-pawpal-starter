from dataclasses import dataclass, field
from typing import List


# Task
@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

# Pet
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to the pet."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from the pet if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for the pet."""
        return self.tasks


# Owner
@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
         """Remove a pet from the owner if it exists."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self) -> List[Pet]:
        """Return all pets owned by the owner."""
        return self.pets


# Scheduler
class Scheduler:
    def __init__(self):
        self.schedule: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the schedule."""
        self.schedule.append(task)

    def sort_by_priority(self) -> List[Task]:
        """Return tasks sorted by priority."""
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(self.schedule, key=lambda t: priority_order.get(t.priority, 4))

    def get_schedule(self) -> List[Task]:
        """Return the full task schedule."""
        return self.schedule