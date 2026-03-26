from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Feed", 10, "low")
    
    task.mark_complete()
    
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Leo", "Dog")
    task = Task("Walk", 30, "high")

    pet.add_task(task)

    assert len(pet.tasks) == 1