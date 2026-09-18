import pytest
from app.task_manager import TaskManager


@pytest.fixture
def manager():
    return TaskManager()


# -------------------------
# ADD TASK TESTS
# -------------------------

def test_add_task(manager):
    task = manager.add_task("Learn Python")

    assert task["id"] == 1
    assert task["title"] == "Learn Python"
    assert task["completed"] is False


def test_add_multiple_tasks(manager):
    manager.add_task("Learn Python")
    manager.add_task("Write Tests")

    assert len(manager.tasks) == 2


def test_add_task_removes_extra_spaces(manager):
    task = manager.add_task("  Learn Python  ")

    assert task["title"] == "Learn Python"


def test_add_empty_task(manager):
    with pytest.raises(ValueError):
        manager.add_task("")


def test_add_whitespace_task(manager):
    with pytest.raises(ValueError):
        manager.add_task("   ")


def test_add_duplicate_task(manager):
    manager.add_task("Learn Python")

    with pytest.raises(ValueError):
        manager.add_task("Learn Python")


def test_duplicate_task_is_case_insensitive(manager):
    manager.add_task("Learn Python")

    with pytest.raises(ValueError):
        manager.add_task("learn python")


# -------------------------
# GET TASK TESTS
# -------------------------

def test_get_task(manager):
    manager.add_task("Learn Python")

    task = manager.get_task(1)

    assert task["title"] == "Learn Python"


def test_get_nonexistent_task(manager):
    with pytest.raises(ValueError):
        manager.get_task(999)


# -------------------------
# UPDATE TASK TESTS
# -------------------------

def test_update_task(manager):
    manager.add_task("Learn Python")

    task = manager.update_task(1, "Learn Advanced Python")

    assert task["title"] == "Learn Advanced Python"


def test_update_task_with_empty_title(manager):
    manager.add_task("Learn Python")

    with pytest.raises(ValueError):
        manager.update_task(1, "")


def test_update_nonexistent_task(manager):
    with pytest.raises(ValueError):
        manager.update_task(999, "New Task")


# -------------------------
# COMPLETE TASK TESTS
# -------------------------

def test_complete_task(manager):
    manager.add_task("Learn Python")

    task = manager.complete_task(1)

    assert task["completed"] is True


def test_complete_nonexistent_task(manager):
    with pytest.raises(ValueError):
        manager.complete_task(999)


# -------------------------
# REMOVE TASK TESTS
# -------------------------

def test_remove_task(manager):
    manager.add_task("Learn Python")

    result = manager.remove_task(1)

    assert result is True
    assert len(manager.tasks) == 0


def test_remove_nonexistent_task(manager):
    with pytest.raises(ValueError):
        manager.remove_task(999)


# -------------------------
# SEARCH TESTS
# -------------------------

def test_search_tasks(manager):
    manager.add_task("Learn Python")
    manager.add_task("Learn Java")
    manager.add_task("Write Report")

    results = manager.search_tasks("Learn")

    assert len(results) == 2


def test_search_is_case_insensitive(manager):
    manager.add_task("Learn Python")

    results = manager.search_tasks("python")

    assert len(results) == 1


def test_search_empty_keyword(manager):
    manager.add_task("Learn Python")

    results = manager.search_tasks("")

    assert results == []


def test_search_no_matching_task(manager):
    manager.add_task("Learn Python")

    results = manager.search_tasks("Database")

    assert results == []


# -------------------------
# STATUS FILTER TESTS
# -------------------------

def test_get_pending_tasks(manager):
    manager.add_task("Learn Python")
    manager.add_task("Write Tests")

    pending = manager.get_tasks_by_status(False)

    assert len(pending) == 2


def test_get_completed_tasks(manager):
    manager.add_task("Learn Python")
    manager.add_task("Write Tests")

    manager.complete_task(1)

    completed = manager.get_tasks_by_status(True)

    assert len(completed) == 1
    assert completed[0]["title"] == "Learn Python"


# -------------------------
# STATISTICS TESTS
# -------------------------

def test_statistics_with_no_tasks(manager):
    statistics = manager.get_statistics()

    assert statistics == {
        "total": 0,
        "completed": 0,
        "pending": 0
    }


def test_statistics(manager):
    manager.add_task("Learn Python")
    manager.add_task("Write Tests")
    manager.add_task("Prepare Report")

    manager.complete_task(1)
    manager.complete_task(2)

    statistics = manager.get_statistics()

    assert statistics["total"] == 3
    assert statistics["completed"] == 2
    assert statistics["pending"] == 1


# -------------------------
# INTEGRATION TEST
# -------------------------

def test_complete_task_workflow(manager):
    # Add a task
    task = manager.add_task("Complete Week 3 Task")

    assert task["completed"] is False

    # Update the task
    manager.update_task(1, "Complete Week 3 Automated Testing Task")

    # Complete the task
    manager.complete_task(1)

    # Search for the task
    results = manager.search_tasks("Automated Testing")

    assert len(results) == 1
    assert results[0]["completed"] is True

    # Check statistics
    statistics = manager.get_statistics()

    assert statistics["total"] == 1
    assert statistics["completed"] == 1
    assert statistics["pending"] == 0
