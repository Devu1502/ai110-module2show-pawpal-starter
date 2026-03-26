import unittest
from pawpal_system import Pet, Task, Scheduler


class TestPawPal(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()
        self.pet = Pet("Buddy", "Dog")

    # ✅ Sorting Test
    def test_sorting_by_time(self):
        task1 = Task("Feed", 30, "high", "10:00", self.pet)
        task2 = Task("Walk", 20, "medium", "08:00", self.pet)
        task3 = Task("Vet", 60, "low", "09:00", self.pet)

        self.scheduler.add_task(task1)
        self.scheduler.add_task(task2)
        self.scheduler.add_task(task3)

        sorted_tasks = self.scheduler.sort_by_time()
        times = [task.time for task in sorted_tasks]

        self.assertEqual(times, ["08:00", "09:00", "10:00"])

    # 🔁 Recurrence Test
    def test_daily_recurrence(self):
        task = Task("Feed", 30, "high", "09:00", self.pet, recurrence="daily")

        self.scheduler.add_task(task)

        # ✅ Correct method
        self.scheduler.mark_task_complete(task)

        tasks = self.scheduler.get_schedule()

        self.assertEqual(len(tasks), 2)
        self.assertFalse(tasks[1].completed)

    # ⚠️ Conflict Detection Test
    def test_conflict_detection(self):
        task1 = Task("Feed", 30, "high", "09:00", self.pet)
        task2 = Task("Walk", 20, "medium", "09:00", self.pet)

        self.scheduler.add_task(task1)
        self.scheduler.add_task(task2)

        conflicts = self.scheduler.detect_conflicts()

        self.assertTrue(len(conflicts) > 0)

    # ✅ Task Completion Test
    def test_task_completion(self):
        task = Task("Feed", 30, "high", "10:00", self.pet)

        task.mark_complete()  # ✅ correct usage

        self.assertTrue(task.completed)

    # 🐾 Add Task to Pet Test
    def test_add_task_to_pet(self):
        pet = Pet("Leo", "Dog")
        task = Task("Walk", 20, "high", "10:00", pet)

        pet.add_task(task)

        self.assertEqual(len(pet.tasks), 1)


if __name__ == "__main__":
    unittest.main()