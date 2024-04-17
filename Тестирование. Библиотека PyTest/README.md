# Тестирование. Библиотека PyTest

## Задача 1. 

Ознакомьтесь с программой **Task Manager**, которая предназначена для управления задачами.

```python
import datetime


class Task:
    def __init__(self, description, priority=1, deadline=None):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def set_deadline(self, deadline):
        self.deadline = deadline

    def __str__(self):
        status = "Completed" if self.is_completed else "Not Completed"
        deadline_info = f"Deadline: {self.deadline}" if self.deadline else "No Deadline"
        return f"Description: {self.description}\nPriority: {self.priority}\nStatus: {status}\n{deadline_info}\n"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def update_task(self, task, new_description):
        if task in self.tasks:
            task.description = new_description

    def sort_by_priority(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

    def filter_by_status(self, completed=False):
        return [task for task in self.tasks if task.is_completed == completed]


# Пример использования
if __name__ == "__main__":
    task_list = TaskList()

    task1 = Task("Write report", priority=2)
    task_list.add_task(task1)
    task2 = Task("Buy groceries", priority=1)
    task_list.add_task(task2)
    task3 = Task("Call client", priority=3, deadline=datetime.datetime(2023, 10, 1))
    task_list.add_task(task3)

    task_list.sort_by_priority()

    print("All Tasks:")
    for task in task_list.tasks:
        print(task)

    task2.mark_completed()

    completed_tasks = task_list.filter_by_status(completed=True)
    print("Completed Tasks:")
    for task in completed_tasks:
        print(task)

    print("Updated Task List:")
    for task in task_list.tasks:
        print(task)
```

Проведите тестирование для алгоритма, используемого в системе управления задачами.

Требования к тестам:

1. **Тест инициализации задачи `test_task_initialization`**:
    - Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры `sample_task`.
    - Убедиться, что приоритет равен `1`, дедлайн не установлен и задача не помечена как завершенная.
    
2. **Тест отметки задачи как выполненной `test_mark_completed`**:
    - Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры `sample_task`.
    - Вызвать метод `mark_completed()` для того, чтобы отметить задачу как выполненную.
    - Убедиться, что статус выполнения изменился на "Выполнено".
  
3. **Тест установки дедлайна для задачи `test_set_deadline`:**
    - Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры `sample_task`.
    - Установить `deadline` для задачи, используя модуль `datetime`.
    - Установить дедлайн для задачи с использованием метода `set_deadline()` и передать в него созданный объект дедлайна `deadline`.
    - Проверить, что дедлайн задачи `sample_task` теперь соответствует установленному дедлайну `deadline`.

    
4. **Тест строкового представления задачи `test_task_string_representation`**:
    - Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры `sample_task`.
    - Убедиться, что строковое представление задачи `str(sample_task)` соответствует ожидаемому формату, который создается на основе атрибутов задачи:
    ```
    "Description: [описание]      
     Priority: 1 
     Status: Not Completed
     No Deadline"
    ```
    
5. **Тест инициализации списка задач `test_tasklist_initialization`**:
    - Создать пустой список задач `TaskList`.
    - Убедиться, что список задач пуст.
    
6. **Тест добавления задачи в список `test_add_task`**:
    - С помощью метода `add_task()` добавить задачу `sample_task` с заданным описанием "Sample Task" в список задач `task_list`.
    - Убедиться, что список содержит одну задачу.
    - Убедиться, что  `sample_task` находится в списке задач.
    
7. **Тест удаления задач из списка `test_remove_task`**:
    - Добавить задачу с описанием, полученным из параметризованной фикстуры `sample_task`, в список задач `task_list`.
    - Вызвать метод `remove_task()` для удаления задачи `sample_task` из списка.
    - Убедиться, что после удаления задачи, количество задач в списке `task_list` уменьшилось на 1.
    - Также убедиться, что удаленная задача `sample_task` больше не присутствует в списке задач `task_list`.
    
8. **Тест сортировки задач по приоритету `test_sort_by_priority`:**
    - Добавить в список задач `task_list`  две задачи `task1` и `task2` с разными приоритетами.
    - Вызвать метод `sort_by_priority()` для сортировки задач в списке `task_list`.
    - Убедиться, что задачи в списке расположены в порядке убывания приоритета. Чем больше значение, тем выше приоритет задачи.
    
9. **Тест фильтрации задач по статусу выполнения `test_filter_by_status`:**
    - Добавить в список задач `task_list`  две задачи `task1` и `task2`. Одну из задач пометить как выполненная.
    - Выполнить фильтрацию задач по статусу выполнения "Выполнено".
    - Убедиться, что в результирующем списке содержится только выполненная задача.
    
   
***Примечание**: используйте параметризованную фикстуру **sample_task**, которая создает экземпляр `Task` с разными описаниями задач (например, "Sample Task 1" и "Sample Task 2").*

*А также используйте фикстуру **task_list**, которая создает экземпляр класса `TaskList`. Это позволит создавать новые списки задач для каждого теста. Таким образом, мы обеспечиваем изоляцию между тестами и удостоверяемся, что каждый тест не зависит от состояния других тестов. Это важно для корректного тестирования функциональности.*


## Задача 2. 

Ознакомьтесь с программой **Watering System**, которая предназначена для управления системой полива почвы.

```python
class WateringSystem:
    def __init__(self):
        self.water_level = 2000  # Начальный уровень воды в системе
        self.is_watering = False  # Флаг, указывающий, идет ли полив в данный момент
        self.areas = {}  # Возможные участки для полива

    @property
    def water_level(self):
        return self._water_level

    @water_level.setter
    def water_level(self, value):
        self._water_level = value

    @property
    def is_watering(self):
        return self._is_watering

    @is_watering.setter
    def is_watering(self, value):
        self._is_watering = value

    def get_water_level(self):
        print(f"Current water level in the system: {self.water_level} мл \n")

    def add_water(self, amount):
        self.water_level += amount

    def add_area(self, area, initial_moisture):
        if area not in self.areas:
            self.areas[area] = {
                "soil_moisture": initial_moisture,  # Уровень влажности почвы на участке
                "spray_water": 0,  # Скорость подачи воды
            }
        else:
            print(f"An area named {area} already exists in the system.")

    def check_soil_moisture(self, area_name=None):
        if area_name is not None:
            if area_name in self.areas:
                moisture = self.areas[area_name]["soil_moisture"]
                print(f"Moisture level for area {area_name}: {moisture}%.")
            else:
                print(f"An area named {area_name} already exists in the system.")
        else:
            for area, data in self.areas.items():
                moisture = data["soil_moisture"]
                print(f"Moisture level for area {area_name}: {moisture}%.")

    def water_area(self, area, duration):
        if area in self.areas:
            if self.is_watering:
                print(
                    "Watering is already in progress. Wait for the current watering to complete."
                )
                return  # Останавливаем выполнение метода
            print(f"Watering of the {area} has been started.")
            self.is_watering = True  
            water_needed = (
                duration * self.areas[area]["spray_water"]
            )  # Вычисляем необходимое количество воды
            if self.water_level >= water_needed:
                if self.areas[area]["soil_moisture"] < 100:
                    # Если уровень влажности на участке не достиг 100%
                    self.water_level -= water_needed
                    new_soil_moisture = self.areas[area]["soil_moisture"] + (
                        duration * 5
                    )
                    self.areas[area]["soil_moisture"] = min(
                        new_soil_moisture, 100
                    )  # Ограничиваем влажность до 100%
                else:
                    print(
                        f"Zone {area} already has maximum moisture (100%) and does not require watering."
                    )
            else:
                print(f"Not enough water to spray the area {area}")
            print(f"The watering of the {area} has been completed.")
            self.is_watering = False  

    def water_spray_supply(self, area, spray_water):
        if area in self.areas:
            self.areas[area]["spray_water"] = spray_water
        else:
            print(
                f"Area named {area} does not exist in the system. Please add a site using add_area."
            )


if __name__ == "__main__":
    system = WateringSystem()

    system.get_water_level()

    system.add_area("Garden", 30)
    system.check_soil_moisture("Garden")
    system.water_spray_supply("Garden", 10)
    system.water_area("Garden", 30)
    system.check_soil_moisture("Garden")

    system.get_water_level()

    system.add_area("Flowerbed", 25)
    system.check_soil_moisture("Flowerbed")
    system.water_spray_supply("Flowerbed", 8)
    system.water_area("Flowerbed", 20)
    system.check_soil_moisture("Flowerbed")

    system.get_water_level()
```

Проведите тестирование для алгоритма, используемого в системе полива.

Требования к тестам:

1. **Тест на начальный уровень влажности участка `test_initial_soil_moisture`**:
   - Создать экземпляр системы автоматического полива с заданным участком `Garden` и начальным уровнем влажности 30% с помощью фикстуры `watering_system`.
   - Проверить, что начальный уровень влажности участка `Garden` равен 30%.

2. **Тест на добавление воды в систему `test_add_water`**:
   - Создать экземпляр системы автоматического полива с начальным уровнем воды 2000 мл с помощью фикстуры `watering_system`.
   - Вызвать метод `add_water` с параметром 500 для добавления 500 мл воды.
   - Проверить, что уровень воды в системе стал равен 2500 мл.

3. **Тест на добавление уже существующего участка `test_add_existing_area`**:
   - Создать экземпляр системы автоматического полива с заданным участком `Garden` и начальным уровнем влажности 30% с помощью фикстуры `watering_system`.
   - Вызвать метод `add_area` с параметром `Garden` и новым начальным уровнем влажности 50.
   - Проверить, что метод `add_area` не изменил начальный уровень влажности участка `Garden` (остался 30%).

4. **Тест на добавление нового участка `test_add_new_area`**:
   - Создать экземпляр системы автоматического полива с пустым списком участков с помощью фикстуры `watering_system`.
   - Вызвать метод `add_area` с параметром `Lawn` и начальным уровнем влажности 40.
   - Проверить, что участок `Lawn` добавлен в систему.

5. **Тест для проверки подачи воды `test_water_spray_supply`**:
   - Создать экземпляр системы автоматического полива с заданным участком `Garden` и начальным уровнем влажности 30% с помощью фикстуры `watering_system`.
   - Вызвать метод `test_water_spray_supply` с параметрами `Garden` и скоростью подачи воды 15.
   - Проверить, что скорость подачи воды для участка `Garden` стала равной 15.

6. **Тест для проверки уровня влажности после полива `test_water_area`**:
   - Создать экземпляр системы автоматического полива с заданными участками с помощью фикстуры `watering_system`.
   - Параметры теста: `area` (участок для полива), `duration` (продолжительность полива в минутах) и `expected_moisture` (ожидаемый уровень влажности после полива).
   - Вызвать метод `water_area` с заданными параметрами.
   - Проверить, что уровень влажности на участке после полива соответствует ожидаемому.

7. **Тест на полив при нехватке воды `test_water_area_not_enough_water`**:
   - Создать экземпляр системы автоматического полива с начальным уровнем воды 0 мл с помощью фикстуры `watering_system`.
   - Вызвать метод `water_area` с параметрами `Garden` (участок для полива) и `duration` (продолжительность полива в минутах) 30.
   - Проверить, что метод `water_area` возвращает None, так как не хватает воды для полива.

8. **Тест на полив при максимальной влажности `test_max_soil_moisture`**:
   - Создать экземпляр системы автоматического полива с заданным участком `Garden` и максимальным уровнем влажности 100% с помощью фикстуры `watering_system`.
   - Вызвать метод `water_area` с параметрами `Garden` и `duration` 30.
   - Проверить, что метод `water_area` не выполнил полива, так как уровень влажности уже максимальный.

9. **Тест для проверки влажности почвы после длительного полива `test_soil_moisture_after_long_watering`**:
   - Создать экземпляр системы автоматического полива с заданным участком `Garden` и начальным уровнем влажности 30% с помощью фикстуры `watering_system`.
   - Вызвать метод `water_area` с параметрами `Garden` и `duration` 60 (продолжительность полива в минутах).
   - Проверить, что после длительного полива уровень влажности на участке `Garden` стал максимальным (100%).
   
10. **Тест на проверку влажности почвы после полива `test_soil_moisture_after_watering`**:
    - Создать экземпляр системы автоматического полива с заданным участком `Garden` и начальным уровнем влажности 30% с помощью фикстуры `watering_system`.
    - Вызвать метод `water_area` с параметрами `Garden` и `duration` 30 (продолжительность полива в минутах).
    - Проверить, что после полива уровень влажности на участке `Garden` стал максимальным (100%).
   
***Примечание**: используйте параметризованную фикстуру **watering_system**, которая создает экземпляр класса `WateringSystem` и настраивает его с определенными участками для полива и расписанием. А именно:* 

*1) Добавляет участок `Garden` с начальным уровнем влажности 30%, и устанавливает скорость подачи воды 10.*

*2) Добавляет участок `Flowerbed` с начальным уровнем влажности 25%, и устанавливает скорость подачи воды 8.*

*А также используйте фикстуру, которая определяет разные сценари полива и ожидаемые результаты. Это позволит создавать новые списки задач для каждого теста. Таким образом, мы обеспечиваем изоляцию между тестами и удостоверяемся, что каждый тест не зависит от состояния других тестов. Это важно для корректного тестирования функциональности.*
