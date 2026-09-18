class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        if any(task["title"].lower() == title.strip().lower()
               for task in self.tasks):
            raise ValueError("Task already exists")

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        return task

    def remove_task(self, task_id):
        task = self._find_task(task_id)
        self.tasks.remove(task)
        return True

    def update_task(self, task_id, new_title):
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty")

        task = self._find_task(task_id)
        task["title"] = new_title.strip()
        return task

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        task["completed"] = True
        return task

    def get_task(self, task_id):
        return self._find_task(task_id)

    def search_tasks(self, keyword):
        if not keyword or not keyword.strip():
            return []

        keyword = keyword.strip().lower()

        return [
            task for task in self.tasks
            if keyword in task["title"].lower()
        ]

    def get_tasks_by_status(self, completed):
        return [
            task for task in self.tasks
            if task["completed"] == completed
        ]

    def get_statistics(self):
        total = len(self.tasks)
        completed = sum(task["completed"] for task in self.tasks)
        pending = total - completed

        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }

    def _find_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task

        raise ValueError("Task not found")
