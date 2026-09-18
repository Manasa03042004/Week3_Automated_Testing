# Test Case Documentation

## 1. Introduction

This document describes the automated test cases developed for the Task Manager Python module.

The test suite was created using the pytest framework. The tests verify normal functionality, edge cases, invalid inputs, exception handling, and an integrated task-management workflow.

A total of 25 automated test cases are included.

---

## 2. Test Cases

| Test Case | Functionality Tested | Purpose |
|---|---|---|
| test_add_task | Add task | Verifies that a valid task is created correctly. |
| test_add_multiple_tasks | Multiple tasks | Checks whether multiple tasks can be stored. |
| test_add_task_removes_extra_spaces | Input cleaning | Verifies that unnecessary spaces are removed. |
| test_add_empty_task | Validation | Ensures empty task titles are rejected. |
| test_add_whitespace_task | Validation | Ensures titles containing only spaces are rejected. |
| test_add_duplicate_task | Duplicate prevention | Checks that duplicate tasks are not allowed. |
| test_duplicate_task_is_case_insensitive | Duplicate prevention | Ensures duplicate detection ignores letter case. |
| test_get_task | Retrieve task | Verifies that an existing task can be retrieved. |
| test_get_nonexistent_task | Error handling | Checks that an invalid task ID raises an error. |
| test_update_task | Update functionality | Verifies that an existing task can be updated. |
| test_update_task_with_empty_title | Validation | Ensures an empty updated title is rejected. |
| test_update_nonexistent_task | Error handling | Checks invalid task IDs during update operations. |
| test_complete_task | Completion | Verifies that a task can be marked as completed. |
| test_complete_nonexistent_task | Error handling | Checks completion of a nonexistent task. |
| test_remove_task | Remove functionality | Verifies that an existing task can be removed. |
| test_remove_nonexistent_task | Error handling | Checks removal of a nonexistent task. |
| test_search_tasks | Search functionality | Verifies that tasks can be searched using keywords. |
| test_search_is_case_insensitive | Search | Ensures searches work regardless of letter case. |
| test_search_empty_keyword | Edge case | Checks behavior when an empty keyword is provided. |
| test_search_no_matching_task | Search | Verifies that an empty result is returned when no task matches. |
| test_get_pending_tasks | Status filtering | Checks retrieval of pending tasks. |
| test_get_completed_tasks | Status filtering | Checks retrieval of completed tasks. |
| test_statistics_with_no_tasks | Statistics | Verifies statistics when there are no tasks. |
| test_statistics | Statistics | Checks total, completed, and pending task counts. |
| test_complete_task_workflow | Integration | Tests a complete workflow from adding to completing and searching a task. |

---

## 3. Testing Categories

### Unit Testing

The majority of the test cases are unit tests. Each test checks a specific method of the TaskManager class independently.

Examples include:

- Adding a task
- Updating a task
- Removing a task
- Completing a task
- Searching tasks
- Calculating statistics

### Edge Case Testing

Edge cases are tested to ensure that unusual inputs are handled safely.

Examples include:

- Empty task titles
- Whitespace-only titles
- Empty search keywords
- Nonexistent task IDs
- Duplicate task titles

### Error Testing

The test suite verifies that invalid operations raise the expected `ValueError` exception.

This prevents invalid data from being silently accepted by the application.

### Integration Testing

The `test_complete_task_workflow` test checks multiple operations together.

The workflow is:

1. Add a task.
2. Update the task.
3. Complete the task.
4. Search for the task.
5. Verify task statistics.

This ensures that different parts of the module work correctly together.

---

## 4. Testing Methodology

The project follows a TDD-style testing approach.

The general process was:

1. Identify the required functionality.
2. Define expected behavior.
3. Create automated test cases.
4. Implement the corresponding functionality.
5. Run the tests.
6. Identify and correct issues.
7. Run the complete test suite again.
8. Review the implementation for clarity and maintainability.

The final test execution completed successfully with all 25 tests passing.

---

## 5. Test Result

The complete test suite was executed using:

```text
python -m pytest -v
```

Final result:

```text
25 passed in 0.13s
```

Therefore, all implemented test cases passed successfully.
