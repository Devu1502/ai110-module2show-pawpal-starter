# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The three core actions a user should be able to perform are:
1. Add and manage pets in the system.
2. Create and manage pet care tasks such as feeding, walking, and medication.
3. Generate and view a daily schedule based on task priority and duration.

The system has four main classes:
1. Owner – stores information about the user and manages their pets.
2. Pet – represents a pet and stores its care tasks.
3. Task – represents an activity such as feeding, walking.
4. Scheduler – organizes tasks into a daily schedule based on priority and constraints.

**b. Design changes**

The design was slightly updated after reviewing it.

The Scheduler class was made clearer so that it only organizes tasks and does not own them.

Also, task priority was changed to use simple labels like "low", "medium", and "high" instead of numbers to match the user interface.

These changes made the system easier to understand and use.

More advanced improvements such as linking tasks back to pets or adding unique identifiers were considered, but were not implemented to keep the design simple for this project.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers time and priority as the main constraints. Tasks are sorted by time so they appear in the correct order, and priority is used to rank tasks when needed. I chose time as the most important constraint because a schedule should follow a clear timeline. Priority is secondary and helps organize tasks when multiple tasks exist.
The sorting is implemented using Python’s built-in sorted function with datetime parsing, which ensures tasks are ordered correctly by time.

**b. Tradeoffs**

The scheduler uses a simple conflict detection strategy that only checks if two tasks have the exact same time. This makes the system easy to implement and understand, but it does not detect overlapping tasks based on duration. This tradeoff is reasonable because it keeps the system simple while still providing useful feedback to the user.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools mainly for debugging, writing tests, and improving my design. I asked questions like how to test sorting, how to handle recurring tasks, and what edge cases I should consider. AI also helped me generate test cases and fix errors when my code was not working.
The most helpful prompts were asking for test plans and asking why certain errors were happening, because it helped me understand my own code better.
This helped me not only fix issues but also understand why the system behaves the way it does.

**b. Judgment and verification**

One moment where I did not accept AI suggestions directly was when the test code used the wrong method for marking tasks complete. AI suggested calling task.mark_complete(self.scheduler), but in my actual code the correct method was scheduler.mark_task_complete(task).
I verified this by checking my pawpal_system.py file and comparing it with the test. This helped me fix the tests correctly and understand how my system actually works.

---

## 4. Testing and Verification

**a. Test plan**

I focused on testing both normal functionality and edge cases across the scheduler system:
** Recurring Tasks **
- Ensure new tasks are created when recurring tasks are completed
- Verify behavior for daily, weekly, and non-recurring tasks
- Handle repeated completion of the same task

** Conflict Detection **
- Detect tasks scheduled at the same time
- Ensure multiple conflicts are correctly identified
- Verify no false conflicts when tasks do not overlap

** Sorting **
- Verify tasks are sorted correctly by time
- Handle identical timestamps and invalid priority values
- Ensure sorting works on empty schedules

** Filtering **
- Filter tasks by pet name and completion status
- Handle non-existent pets and empty results
- Ensure filtering does not modify the original schedule

** Data Integrity **
- Validate task time format
- Ensure tasks are associated with the correct pet
- Handle duplicate pet names safely

**b. What you tested**

I tested the core functionality of the system by checking sorting, recurring tasks, and conflict detection. I verified that tasks are ordered correctly, new tasks are created for recurring events, and conflicts are detected when tasks have the same time. I also checked that tasks are correctly linked to pets.

**c. Confidence**

(4/5)
The system performs reliably for core features such as scheduling, sorting, recurrence, and conflict detection.
Some limitations remain, such as recurrence not fully accounting for date differences and conflict detection only checking exact time matches.

---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is getting the full system working together, including sorting, filtering, recurring tasks, and conflict detection and also seeing the website come together and using it. I was also able to successfully write tests and fix multiple errors, which helped me confirm that the system works correctly.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the system by supporting full date and time tracking instead of just time, and detecting overlapping tasks based on duration instead of only exact matches. I would also improve the user interface to allow users to input task times directly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned is that designing a system step by step is very important. Starting with a clear structure (UML) made it easier to build the code. I also learned that AI is helpful, but you still need to verify everything yourself and make sure it matches your actual implementation.
