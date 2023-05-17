from consolemenu import *
from consolemenu.items import *
from task_list import *

menu = ConsoleMenu("Your TO-DO List ", "This is the list of your planned tasks. Feel free to add or remove tasks as you wish.")

add_tasks_submenu = ConsoleMenu("Add task submenu", "This is the add task submenu.")
add_task = CommandItem("Add task", addTask)
add_tasks_submenu.append_item(add_task)
add_tasks_submenu_item = SubmenuItem("Add taks", add_tasks_submenu, menu=menu)

mark_as_complete_submenu = ConsoleMenu("Mark as complete submenu", "This is the mark as complete submenu.")
mark_as_complete = FunctionItem("Mark tasks as complete", markAsComplete)
mark_as_complete_submenu.append_item(mark_as_complete)
mark_as_complete_submenu_item = SubmenuItem("Mark as complete", mark_as_complete_submenu, menu=menu)

remove_tasks_submenu = ConsoleMenu("Remove task submenu", "This is the remove task submenu.")
remove_tasks = FunctionItem("Remove tasks", removeTask)
remove_tasks_submenu.append_item(remove_tasks)
remove_tasks_submenu_item = SubmenuItem("Remove taks", remove_tasks_submenu, menu=menu)

view_tasks_submenu = ConsoleMenu("View task submenu", "This is the view task submenu.")
view_tasks = FunctionItem("View taks", viewTasks)
view_tasks_submenu.append_item(view_tasks)
view_tasks_submenu_item = SubmenuItem("View taks", view_tasks_submenu, menu=menu)

menu.append_item(add_tasks_submenu_item)
menu.append_item(mark_as_complete_submenu_item)
menu.append_item(remove_tasks_submenu_item)
menu.append_item(view_tasks)

menu.show()


