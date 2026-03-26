import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Dev")
owner = st.session_state.owner

st.write("Number of pets:", len(owner.get_pets()))

st.subheader("➕ Add a Pet")

pet_name = st.text_input("Pet Name")
pet_species = st.text_input("Pet Species")

if st.button("Add Pet"):
    if pet_name and pet_species:
        new_pet = Pet(pet_name, pet_species)
        owner.add_pet(new_pet)
        st.success(f"{pet_name} added successfully!")
    else:
        st.warning("Please enter both name and species.")

st.subheader("🐾 Your Pets")

for pet in owner.get_pets():
    st.write(f"- {pet.name} ({pet.species})")

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    if not owner.get_pets():
        st.warning("Please add at least one pet.")
    elif not st.session_state.tasks:
        st.warning("Please add at least one task.")
    else:
        scheduler = Scheduler()

        # Use first pet for simplicity
        pet = owner.get_pets()[0]

        # Convert UI tasks → Task objects
        for t in st.session_state.tasks:
            task_obj = Task(
                title=t["title"],
                duration_minutes=t["duration_minutes"],
                priority=t["priority"],
                time="09:00",   # default time (since UI doesn’t collect time yet)
                pet=pet,
                recurrence="daily"  # demo recurring
            )
            scheduler.add_task(task_obj)

        # ✅ SORT
        sorted_tasks = scheduler.sort_by_time()

        st.subheader("📅 Sorted Schedule")
        for task in sorted_tasks:
            st.write(f"{task.title} - {task.time} ({task.priority})")

        # ✅ FILTER (example: show only pending)
        filtered = scheduler.filter_tasks(completed=False)

        st.subheader("🔍 Pending Tasks")
        for task in filtered:
            st.write(f"{task.title} - {task.time}")

        # ✅ MARK ONE COMPLETE (demo recurrence)
        if sorted_tasks:
            scheduler.mark_task_complete(sorted_tasks[0])

        st.subheader("🔁 After Recurring Update")
        for task in scheduler.get_schedule():
            status = "✅" if task.completed else "⏳"
            st.write(f"{task.title} - {task.time} {status}")

        # ✅ CONFLICT DETECTION (force conflict for demo)
        if len(scheduler.get_schedule()) >= 2:
            scheduler.schedule[1].time = scheduler.schedule[0].time

        conflicts = scheduler.detect_conflicts()

        st.subheader("⚠️ Conflict Detection")
        if conflicts:
            for c in conflicts:
                st.warning(c)
        else:
            st.success("No conflicts found.")
