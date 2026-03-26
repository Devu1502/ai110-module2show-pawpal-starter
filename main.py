from pawpal_system import Task, Pet, Owner, Scheduler

def main():
    """Run a demo of the PawPal scheduling system with sample pets and tasks."""
    owner = Owner("Dev")

    dog = Pet("Blu", "Dog")
    cat = Pet("Kiko", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()

    # Create Tasks (OUT OF ORDER)
    task1 = Task("Morning Walk", 30, "high", "12:00", dog, recurrence="daily")
    task2 = Task("Feed Breakfast", 10, "medium", "09:00", dog)
    task3 = Task("Vet Appointment", 60, "high", "15:00", cat)
    task4 = Task("Evening Walk", 20, "medium", "12:00", dog)

    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)
    scheduler.add_task(task4)

    # ✅ SORT
    print("\nSorted by Time:\n")
    sorted_tasks = scheduler.sort_by_time()
    for task in sorted_tasks:
        print(f"{task.title} - {task.time}")

    # ✅ FILTER BY PET
    print("\nTasks for Blu:\n")
    dog_tasks = scheduler.filter_tasks(pet_name="Blu")
    for task in dog_tasks:
        print(f"{task.title} - {task.time}")

    # ✅ RECURRING TASK TEST
    scheduler.mark_task_complete(task1)

    print("\nAfter Completing Recurring Task:\n")
    for task in scheduler.get_schedule():
        status = "Completed" if task.completed else "Pending"
        print(f"{task.title} - {task.time} ({status})")

    # ✅ CONFLICT DETECTION
    print("\nChecking for Conflicts:\n")
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for c in conflicts:
            print(c)
    else:
        print("No conflicts found.")


if __name__ == "__main__":
    main()