import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Dev")
owner = st.session_state.owner

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.set_page_config(page_title="PawPal+", page_icon="🐾")

st.title("🐾 PawPal+")

st.subheader(" ➕ Add a Pet")

pet_name = st.text_input("Pet Name")
pet_species = st.text_input("Pet Species")

if st.button("Add Pet"):
    if pet_name and pet_species:
        new_pet = Pet(pet_name, pet_species)
        owner.add_pet(new_pet)
        st.success("Pet added successfully")
    else:
        st.warning("Enter both name and species")

st.subheader("🐾 Your Pets")

if owner.get_pets():
    for pet in owner.get_pets():
        st.write(f"{pet.name} ({pet.species})")
else:
    st.write("No pets yet")

st.subheader("📝 Add Tasks")

task_title = st.text_input("Task Title")
duration = st.number_input("Duration", 1, 240, 20)
priority = st.selectbox("Priority", ["low", "medium", "high"])

if st.button("Add Task"):
    st.session_state.tasks.append({
        "title": task_title,
        "duration_minutes": int(duration),
        "priority": priority
    })
    st.success("Task added")

if st.session_state.tasks:
    st.subheader("Tasks")
    st.table(st.session_state.tasks)
else:
    st.write("No tasks yet")

st.subheader("Generate Schedule")

if st.button("Generate"):

    if not owner.get_pets():
        st.warning("Add a pet first")

    elif not st.session_state.tasks:
        st.warning("Add tasks first")

    else:
        scheduler = Scheduler()
        pet = owner.get_pets()[0]

        for t in st.session_state.tasks:
            task_obj = Task(
                title=t["title"],
                duration_minutes=t["duration_minutes"],
                priority=t["priority"],
                time="09:00",
                pet=pet,
                recurrence="daily"
            )
            scheduler.add_task(task_obj)

        st.subheader("Sorted Schedule")

        sorted_tasks = scheduler.sort_by_time()

        for task in sorted_tasks:
            st.write(f"{task.title} - {task.time}")

        st.subheader("Pending Tasks")

        filtered = scheduler.filter_tasks(completed=False)

        if filtered:
            for task in filtered:
                st.write(f"{task.title} - {task.time}")
        else:
            st.write("All tasks done")

        if sorted_tasks:
            scheduler.mark_task_complete(sorted_tasks[0])
            st.success("Marked first task complete")

        st.subheader("Updated Schedule")

        for task in scheduler.get_schedule():
            status = "Done" if task.completed else "Pending"
            st.write(f"{task.title} - {task.time} ({status})")

        if len(scheduler.get_schedule()) >= 2:
            scheduler.schedule[1].time = scheduler.schedule[0].time

        st.subheader("Conflicts")

        conflicts = scheduler.detect_conflicts()

        if conflicts:
            for c in conflicts:
                st.warning(c)
        else:
            st.write("No conflicts")