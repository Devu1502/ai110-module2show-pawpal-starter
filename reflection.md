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

**a. What you tested**

I tested sorting by adding tasks in random order and checking if they were displayed correctly. I tested filtering by showing tasks for a specific pet and by completion status. I tested recurring tasks by marking a task as complete and verifying that a new task was automatically created. I also tested conflict detection by creating two tasks at the same time and confirming that a warning was displayed.

**b. Confidence**

I am confident that the scheduler works correctly for the main features such as sorting, filtering, recurring tasks, and conflict detection. If I had more time, I would test edge cases such as invalid time formats, multiple overlapping tasks, and handling large numbers of tasks.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the system by supporting full date and time tracking instead of just time, and detecting overlapping tasks based on duration instead of only exact matches. I would also improve the user interface to allow users to input task times directly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

