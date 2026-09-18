"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    if len(product_ids) != len(set(product_ids)):
        return True
    else:
        return False

"""
Solution: I chose to compare the list with a set. Since we are just checking if duplicates are found, comparing the
length of a list to the length of the list as a set allows us to see if there are any duplicates in the list. 
"""

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next
            self.rear = new_node
    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
"""
Solution: I chose a queue since we are dealing with data in a first in, first out capacity. This fits the problem because it is
accepting a list of tasks, adding tasks to the queue, but completing the oldest tasks first. The structure allows for the
"""


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        pass

    def add(self, value):
        pass

    def get_unique_count(self):

        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def main():
    list_1=[10, 20, 30, 20, 40]
    list_2=[1, 2, 3, 4, 5]
    print(has_duplicates(list_1))
    print(has_duplicates(list_2))

main()