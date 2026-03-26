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

**b. Tradeoffs**

The scheduler uses a simple conflict detection strategy that only checks if two tasks have the exact same time. This makes the system easy to implement and understand, but it does not detect overlapping tasks based on duration. This tradeoff is reasonable because it keeps the system simple while still providing useful feedback to the user.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**b. Test plan**

I focused on testing both normal functionality and edge cases across the scheduler system:
Recurring Tasks
Ensure new tasks are created when recurring tasks are completed
Verify behavior for daily, weekly, and non-recurring tasks
Handle repeated completion of the same task
Conflict Detection
Detect tasks scheduled at the same time
Ensure multiple conflicts are correctly identified
Verify no false conflicts when tasks do not overlap
Sorting
Verify tasks are sorted correctly by time
Handle identical timestamps and invalid priority values
Ensure sorting works on empty schedules
Filtering
Filter tasks by pet name and completion status
Handle non-existent pets and empty results
Ensure filtering does not modify the original schedule
Data Integrity
Validate task time format
Ensure tasks are associated with the correct pet
Handle duplicate pet names safely

**b. What you tested**

The test suite verifies the core functionality of the PawPal+ system:
Sorting: Ensures tasks are ordered correctly by time
Recurrence Logic: Confirms recurring tasks generate new tasks when completed
Conflict Detection: Detects tasks scheduled at the same time
Task Completion: Verifies tasks are marked as completed correctly
Pet-Task Assignment: Ensures tasks are properly linked to pets

**b. Confidence**

(4/5)
The system performs reliably for core features such as scheduling, sorting, recurrence, and conflict detection.
Some limitations remain, such as recurrence not fully accounting for date differences and conflict detection only checking exact time matches.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the system by supporting full date and time tracking instead of just time, and detecting overlapping tasks based on duration instead of only exact matches. I would also improve the user interface to allow users to input task times directly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

