from io import StringIO
import unittest
import sys
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("New Task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()

        self.assertEqual(len(open_tasks), 3)
        for task in open_tasks:
            self.assertEqual(task.status, "ToDo")

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()

        self.assertEqual(len(done_tasks), 3)
        for task in done_tasks:
            self.assertEqual(task.status, "Done")



if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTaskPool)

    output = StringIO()

    runner = unittest.TextTestRunner(
        stream=output,
        verbosity=2
    )

    result = runner.run(suite)

    if not result.wasSuccessful():
        print(output.getvalue())
        sys.exit(1)

    for line in output.getvalue().splitlines():
        if line.startswith("test_") and line.endswith(" ... ok"):
            test_name = line.split(" ")[0]
            print(f"{test_name} ... ok")
