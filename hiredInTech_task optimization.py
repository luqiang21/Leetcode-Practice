"""
A worker has a set of N tasks to complete. For each task the worker knows the
time in minutes it will take to complete. This is dependent on the difficulty of
the task. So, a task with difficulty D takes D minutes to complete. The worker
has a limited amount of time T during which he wants to complete as many tasks as possible.

As mentioned above the tasks have different difficulty and when switching from
one task to another with difficulties D1 and D2, the worker needs |D1 - D2|
minutes to prepare for working on the next task.

The number of tasks N is in the range [1, 10,000]. The total time T is in the
range [0, 200,000,000]. The task difficulties are integer numbers in the range [1, 10,000].

You need to write a function, which computes the maximum number of tasks that
can be completed within the given time T. The function accepts as arguments the
 number N and T and a list of the task difficulties. It must return one integer
 - the maximum number of tasks that can be completed within the given time limit.

Here is an example test case.

SAMPLE INPUT

5 65
24 23 22 10 20
SAMPLE OUTPUT

3
All five tasks cannot be completed within the allowed 65 minutes, but it is
possible to accomplish three tasks, for example tasks 4, 5, 3 if completed in this order.
"""

from tools import timing

@timing
def maximum_completed_tasks(n, t, task_difficulties):
    # Write your code here


    tasks = sorted(task_difficulties)
    if tasks[0] > t:
        return 0

    amount = tasks[0]
    for i in range(1, n):
        amount += tasks[i]*2 - tasks[i-1]
        if amount > t:
            return i
    return n
n = 5
t = 65
task_difficulties = [24, 23, 22, 10, 20]
print(maximum_completed_tasks(n, t, task_difficulties))
assert maximum_completed_tasks(n, t, task_difficulties) == 3
