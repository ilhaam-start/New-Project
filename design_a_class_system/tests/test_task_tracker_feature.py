"""
When I add multiple tasks and I don't mark any complete
#all_incomplete lists them out in the order they were added
"""
# task_list = TaskList()
# task_1 = Task("Walk the dog")
# task_2 = Task("Walk the cat")
# task_3 = Task("Walk the monkey")
# task_list.add(task_1)
# task_list.add(task_2)
# task_list.add(task_3)
# task_list.all_incomplete() == [task_1, task_2, task_3]

"""
When I add multiple tasks and I mark one complete
#all_incomplete lists the incomplete tasks only
"""
# task_list = TaskList()
# task_1 = Task("Walk the dog")
# task_2 = Task("Walk the cat")
# task_3 = Task("Walk the monkey")
# task_list.add(task_1)
# task_list.add(task_2)
# task_list.add(task_3)
# task_2.mark_complete()
# task_list.all_incomplete() == [task_1, task_3]

"""
When I add multiple tasks and I mark one complete
#all_complete lists the complete tasks only
"""
# task_list = TaskList()
# task_1 = Task("Walk the dog")
# task_2 = Task("Walk the cat")
# task_3 = Task("Walk the monkey")
# task_list.add(task_1)
# task_list.add(task_2)
# task_list.add(task_3)
# task_2.mark_complete()
# task_list.all_incomplete() == [task_2]