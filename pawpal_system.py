from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta

# Task
@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    time: str
    pet: "Pet"
    completed: bool = False
    recurrence: str = "none"

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


# Pet
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Assign a task to this pet and add it to the pet's task list."""
        task.pet = self
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet's task list if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        """Return the list of all tasks assigned to this pet."""
        return self.tasks


# Owner
@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from this owner's list if it exists."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self) -> List[Pet]:
        """Return the list of all pets owned by this owner."""
        return self.pets


# Scheduler
class Scheduler:
    def __init__(self):
        """Set up the scheduler with an empty task list."""
        self.schedule: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the scheduler's task list."""
        self.schedule.append(task)

    def get_schedule(self) -> List[Task]:
        """Return all tasks currently in the schedule."""
        return self.schedule

    # ✅ SORTING
    def sort_by_time(self, tasks=None):
        """
        Sort tasks by their scheduled time (earliest first).

        Args:
            tasks: A list of tasks to sort. Uses the full schedule if not provided.

        Returns:
            A new sorted list of Task objects ordered by time.
        """
        tasks = tasks if tasks else self.schedule
        return sorted(tasks, key=lambda t: datetime.strptime(t.time, "%H:%M"))

    def sort_by_priority(self):
        """
        Sort all scheduled tasks by priority (high → medium → low).

        Returns:
            A new sorted list of Task objects ordered by priority level.
        """
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(self.schedule, key=lambda t: priority_order.get(t.priority, 4))

    # ✅ FILTERING
    def filter_tasks(self, tasks=None, pet_name=None, completed=None):
        """
        Filter tasks by pet name and/or completion status.

        Args:
            tasks: List of tasks to filter. Uses the full schedule if not provided.
            pet_name: If given, only return tasks belonging to this pet.
            completed: If True/False, only return tasks with that completion status.

        Returns:
            A list of Task objects that match all provided filters.
        """
        tasks = tasks if tasks else self.schedule
        return [
            task for task in tasks
            if (pet_name is None or task.pet.name == pet_name)
            and (completed is None or task.completed == completed)
        ]

    # ✅ RECURRING TASKS
    def mark_task_complete(self, task: Task):
        """
        Mark a task as done and, if it recurs, schedule the next occurrence.

        Args:
            task: The Task to mark complete. If recurrence is 'daily' or 'weekly',
                  a new copy of the task is added to the schedule.
        """
        task.completed = True

        if task.recurrence == "daily":
            next_time = (
                datetime.strptime(task.time, "%H:%M") + timedelta(days=1)
            ).strftime("%H:%M")

        elif task.recurrence == "weekly":
            next_time = (
                datetime.strptime(task.time, "%H:%M") + timedelta(weeks=1)
            ).strftime("%H:%M")

        else:
            return

        # Create new task
        new_task = Task(
            title=task.title,
            duration_minutes=task.duration_minutes,
            priority=task.priority,
            time=task.time,  
            pet=task.pet,
            recurrence=task.recurrence
        )

        self.add_task(new_task)

    # ✅ CONFLICT DETECTION
    def detect_conflicts(self):
        """
        Find tasks that are scheduled at the exact same time.

        Returns:
            A list of warning strings describing each conflicting pair of tasks.
            Returns an empty list if there are no conflicts.
        """
        conflicts = []
        seen = set()

        sorted_tasks = sorted(self.schedule, key=lambda t: t.time)

        for i in range(len(sorted_tasks) - 1):
            t1 = sorted_tasks[i]
            t2 = sorted_tasks[i + 1]

            if t1.time == t2.time:
                pair = tuple(sorted([t1.title, t2.title]))

                if pair not in seen:
                    seen.add(pair)
                    conflicts.append(
                        f"⚠️ Conflict: '{t1.title}' and '{t2.title}' at {t1.time}"
                    )

        return conflicts