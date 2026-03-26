from pawpal_system import Task, Pet, Owner, Scheduler


def main():
    # Create Owner
    owner = Owner("Sree")

    # Create Pets
    dog = Pet("Leo", "Dog")
    cat = Pet("Milo", "Cat")

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create Tasks
    task1 = Task("Morning Walk", 30, "high")
    task2 = Task("Feed Breakfast", 10, "medium")
    task3 = Task("Vet Appointment", 60, "high")

    # Assign tasks to pets
    dog.add_task(task1)
    dog.add_task(task2)
    cat.add_task(task3)

    # Create Scheduler
    scheduler = Scheduler()

    # Add all tasks to scheduler
    for pet in owner.get_pets():
        for task in pet.get_tasks():
            scheduler.add_task(task)

    # Sort tasks
    sorted_tasks = scheduler.sort_by_priority()

    # Print Schedule (clean format)
    print("\nToday's Schedule \n")

    for i, task in enumerate(sorted_tasks, start=1):
        print(f"{i}. {task.title}")
        print(f"   Duration: {task.duration_minutes} mins")
        print(f"   Priority: {task.priority.capitalize()}")
        print("-" * 30)


if __name__ == "__main__":
    main()