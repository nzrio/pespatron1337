class Student:
    """
    Клас, який представляє студента.

    Атрибути:
        name (str): Ім'я студента.
        surname (str): Прізвище студента.
        grade (int): Оцінка студента.
    """

    def __init__(self, name, surname, grade):
        """
        Ініціалізація нового об'єкта класу Student.

        Аргументи:
            name (str): Ім'я студента.
            surname (str): Прізвище студента.
            grade (int): Оцінка студента.
        """
        self.name = name
        self.surname = surname
        self.grade = grade

    def get_full_name(self):
        """Повертає повне ім'я студента (ім'я та прізвище)."""
        return f"{self.name} {self.surname}"

    def is_passing(self):
        """Перевіряє, чи студент складає іспит (оцінка >= 3)."""
        return self.grade >= 3