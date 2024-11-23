
class TK_41:
    """Тестовий клас, зараз реалізуємо опис студента
    
    ---

    surname : str
        Прізвище студента
    
    """
    var_lover_case = "Це проста класова змінна"
    COLLEGE_NAME = "Це подібне до константи в клосі, але ми можемо її перезаписати"
    _protected_var = 1
    __private_var = 2

    total_students = 0
    total_marks = 0

    def __init__(self, surname:str, name, mark:int, group=None):
        """
        Ініціалізуємо обєкт
        - в середині конструктора створюються атрибути
        """
        print("Викликаємо __init__")
        self.__surname = surname #  private Це приватні атрибути, вони не висвічуються назовні
        self.__name = name
        self.mark = mark # public публічний атрибук
        self.group = group
        self._age = None # (protected) захищений атрибут
        self._scholarship = 0

        self.var_lover_case = "Перазаписали класові змінну"
        TK_41.total_students += 1
        TK_41.total_marks += mark


    def __del__(self):
        print("Відрахували студента")
        TK_41.total_students -= 1

    @property
    def college_raiting(self):
        return TK_41.total_marks / TK_41.total_students

    @property
    def name(self):
        """Ця властивість є закритою, її можна читати але не можна змінювати
        """
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def say_hello(self):
        a = 1 + 2
        return f"Привіт {a}"
    
    def __repr__(self):
        return "Представлення обєкту Студент, його задають: TK_41(surname, name, mark)"
    
    def __len__(self):
        return len(self.surname)
    
    def fucntion_in_class(self):
        """Це вже метод згідно термінології, і він публічний
        """
        return "Ми викликали публічний метод"

    def _protected_method_in_class(self):
        """Це захищений метод
        """
        self.__this_is_private()
        return "Ми доступаємось до захищеного методу"
    
    def __this_is_private(self):
        print("Це приватний метод!")

    def calculate_scholarship_after_session(self, raiting: int):
        if raiting == 5:
            self._scholarship = "1800 грн"
            return "Присвоєно підвищену стипундію"
        if raiting == 4:
            self._scholarship = "1400 грн"
            return "Присвоєно звичайну стипундію"
        self._scholarship = 0
        return "Рейтинг занизький для стипендії"
    
    def panishment(self):
        return "Ми прийшли додому і мама нас насварила за погані оцінки"
    
    @staticmethod
    def hobbi(h=None):
        """в таких методах нема вказівника на обєкт
        """
        if h:
            print(f"В мене зявилось хоббі {h}")
        else:
            print("На жаль в мене немає Хаббі")
    
    @classmethod
    def create_from_surname_name(cls, full_name:str):
        """ альтернативний конструктор, створюємо обєкт з повного імені
        розчеплюємо повне імя на частинки Прізкище та Імя
        """
        surname, name = full_name.split(" ")
        return cls(surname, name, 0)
    
    @classmethod
    def create_from_name_surname(cls, full_name:str):
        """ альтернативний конструктор, створюємо обєкт з повного імені
        розчеплюємо повне імя на частинки Прізкище та Імя
        """
        name, surname = full_name.split(" ")
        return cls(surname, name, 0)


def function_in_module():
    """Це просто функція (згідно загальної термінології)
    """
    pass