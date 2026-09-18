# Week 3 - Automated Testing for Python Applications

## 1. Project Title

Task Manager - Automated Testing Project

## 2. Objective

The objective of this project is to develop a moderately complex Python module and create a comprehensive automated test suite for it.

The project demonstrates unit testing, integration testing, edge-case testing, exception handling, and test documentation using the pytest framework.

---

## 3. Project Description

The Task Manager is a simple Python module that allows users to manage tasks.

The module provides functionality to:

- Add new tasks
- Retrieve existing tasks
- Update task titles
- Complete tasks
- Remove tasks
- Search for tasks
- Filter tasks based on completion status
- Calculate task statistics

The module is designed using a class-based structure so that individual functions can be tested independently.

---

## 4. Technologies Used

- Python 3.14
- pytest 9.1.1
- Visual Studio Code
- PowerShell

---

## 5. Project Structure

```text
Week3_Automated_Testing/
│
├── app/
│   ├── __init__.py
│   └── task_manager.py
│
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py
│
├── README.md
├── test_cases.md
├── requirements.txt
└── run_tests.bat
```

### File Description

**app/task_manager.py**

Contains the TaskManager class and all task management functionality.

**tests/test_task_manager.py**

Contains the automated pytest test cases.

**test_cases.md**

Documents the purpose and functionality covered by each test case.

**requirements.txt**

Contains the required Python testing dependency.

**run_tests.bat**

Provides a simple way to execute the complete test suite on Windows.

**README.md**

Contains project information, installation instructions, testing methodology, and execution instructions.

---

## 6. Features of the Module

### Add Task

A valid task can be added to the task manager.

The module automatically assigns a unique task ID and sets the task status to pending.

### Update Task

An existing task title can be modified.

### Complete Task

A pending task can be marked as completed.

### Remove Task

An existing task can be removed from the task manager.

### Search Tasks

Tasks can be searched using a keyword.

The search is case-insensitive.

### Filter Tasks

Tasks can be filtered based on whether they are completed or pending.

### Task Statistics

The module calculates:

- Total number of tasks
- Number of completed tasks
- Number of pending tasks

### Input Validation

The module rejects:

- Empty task titles
- Whitespace-only task titles
- Duplicate task titles

Invalid task IDs also generate appropriate errors.

---

## 7. Testing Framework

The project uses **pytest** as the automated testing framework.

pytest was selected because it provides a simple syntax for writing tests, supports fixtures, provides clear test results, and makes it easy to test exceptions.

---

## 8. Testing Methodology

The project uses a test-after-development approach with a TDD-style refinement process.

The initial module functionality was implemented first. Automated tests were then developed to verify each requirement.

The testing process was:

1. Identify the required functionality.
2. Implement the Task Manager module.
3. Develop tests for individual functions.
4. Add tests for invalid inputs and edge cases.
5. Add exception-handling tests.
6. Add an integration test for a complete workflow.
7. Run the complete test suite.
8. Review the implementation and test coverage.
9. Confirm that all tests pass successfully.

This approach helped identify potential failures and verify that changes did not break existing functionality.

---

## 9. Test Coverage

The automated test suite contains **25 test cases**.

The tests cover:

- Task creation
- Multiple task creation
- Input cleaning
- Empty input validation
- Whitespace validation
- Duplicate task prevention
- Case-insensitive duplicate detection
- Task retrieval
- Invalid task retrieval
- Task updating
- Invalid task updates
- Task completion
- Invalid task completion
- Task removal
- Invalid task removal
- Task searching
- Case-insensitive searching
- Empty search input
- Search with no matching results
- Pending task filtering
- Completed task filtering
- Empty task statistics
- Task statistics calculation
- Complete task workflow integration

Detailed information about each test case is available in `test_cases.md`.

---

## 10. Edge Cases Tested

The test suite includes several edge cases to improve reliability.

Examples include:

- Adding an empty task
- Adding a whitespace-only task
- Adding duplicate tasks
- Adding duplicate tasks with different letter cases
- Searching with an empty keyword
- Searching for a task that does not exist
- Accessing an invalid task ID
- Updating an invalid task
- Removing an invalid task
- Completing an invalid task
- Calculating statistics when no tasks exist

---

## 11. Exception Testing

The module uses `ValueError` for invalid operations.

pytest's `raises()` feature is used to verify that the expected exception is generated.

Example:

```python
with pytest.raises(ValueError):
    manager.add_task("")
```

This verifies that the application does not silently accept invalid task data.

---

## 12. Integration Testing

The project contains an integration test called:

```text
test_complete_task_workflow
```

This test combines multiple operations into one workflow.

The workflow is:

```text
Add Task
   ↓
Update Task
   ↓
Complete Task
   ↓
Search Task
   ↓
Check Statistics
```

The test verifies that these operations work correctly together.

---

## 13. Installation Instructions

### Step 1: Open the project folder

Open PowerShell in:

```text
C:Week3_Automated_Testing
```

### Step 2: Install the required dependency

Run:

```powershell
python -m pip install -r requirements.txt
```

### Step 3: Verify pytest

Run:

```powershell
python -m pytest --version
```

---

## 14. Running the Tests

To run all automated tests, use:

```powershell
python -m pytest -v
```

The `-v` option provides detailed information about each test.

Alternatively, on Windows, the test suite can be started using:

```text
run_tests.bat
```

---

## 15. Expected Test Result

The complete test suite contains 25 tests.

A successful execution produces:

```text
25 passed
```

The final test execution completed successfully with all 25 tests passing.

---

## 16. Code Quality and Maintainability

The module uses a class-based design to keep related functionality together.

The code is divided into small methods, with each method performing a specific operation.

The test suite uses a pytest fixture to create a fresh TaskManager instance for each test.

This prevents data from one test from affecting another test.

The tests are grouped according to functionality, making the test suite easier to read and maintain.

---

## 17. Refactoring and Review

After implementing the functionality and tests, the code was reviewed for clarity and maintainability.

The implementation uses separate methods for adding, updating, completing, removing, searching, filtering, and calculating statistics.

The tests were also organized into logical sections so that failures can be identified easily.

The final test suite was executed after the review to ensure that the changes did not break existing functionality.

---

## 18. Final Validation

The project was tested in a clean project environment using the required Python dependencies.

The final command used was:

```powershell
python -m pytest -v
```

Result:

```text
25 passed
```

This confirms that all implemented automated tests passed successfully.

---

## 19. Conclusion

This project demonstrates the development and automated testing of a Python application.

The test suite covers normal operations, edge cases, invalid inputs, exception handling, and integration between multiple functions.

The project also provides documentation explaining the test cases, testing methodology, installation process, and test execution procedure.

The final project is self-contained and does not require any external datasets or proprietary resources.
