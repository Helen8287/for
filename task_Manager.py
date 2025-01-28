#Менеджер задач

#Задача: Создай класс Task, который позволяет управлять задачами
# (делами). У задачи должны быть атрибуты: описание задачи, срок
# выполнения и статус (выполнено/не выполнено). Реализуй функцию
# для добавления задач, отметки выполненных задач и вывода списка
# текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline=None):
        self.description = description  # Описание задачи
        self.deadline = deadline  # Срок выполнения
        self.status = "не выполнено"  # Статус задачи (по умолчанию "не выполнено")

class TaskManager:
    def __init__(self):
        self.tasks = []  # Список для хранения всех задач

    def add_task(self, description, deadline=None):
        new_task = Task(description, deadline)  # Создаем новую задачу
        self.tasks.append(new_task)  # Добавляем задачу в список

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description and task.status == "не выполнено":
                task.status = "выполнено"  # Меняем статус задачи на "выполнено"
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена или уже выполнена.")

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "не выполнено"]
        return current_tasks

    def get_all_tasks(self):
        return self.tasks

# Создаем менеджер задач
manager = TaskManager()

# Функция для добавления задачи
def add_task_from_input():
    description = input("Введите описание задачи: ")
    deadline = input("Введите срок выполнения задачи (например, 2025-10-05): ")
    manager.add_task(description, deadline)
    print(f"Задача '{description}' добавлена.")

# Функция для отметки задачи как выполненной
def mark_task_completed_from_input():
    description = input("Введите описание задачи, которую хотите отметить как выполненную: ")
    manager.mark_task_completed(description)

# Функция для вывода текущих задач
def print_current_tasks():
    current_tasks = manager.get_current_tasks()
    if current_tasks:
        print("Текущие задачи:")
        for task in current_tasks:
            print(f"Описание: {task.description} | Срок: {task.deadline} | Статус: {task.status}")
    else:
        print("Нет текущих задач.")

def print_all_tasks():
    all_tasks = manager.get_all_tasks()
    if all_tasks:
        print("Все задачи:")
        for task in all_tasks:
            print(f"Описание: {task.description} | Срок: {task.deadline} | Статус: {task.status}")
    else:
        print("Нет задач.")

# Основной цикл программы
while True:
    print("\nМенеджер задач")
    print("1. Добавить задачу")
    print("2. Отметить задачу как выполненную")
    print("3. Показать текущие задачи")
    print("4. Показать все задачи")
    print("5. Выйти")
    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        add_task_from_input()
    elif choice == "2":
        mark_task_completed_from_input()
    elif choice == "3":
        print_current_tasks()
    elif choice == "4":
        print_all_tasks()
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")



