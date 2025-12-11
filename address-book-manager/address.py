"""
Модуль Address для представления адресной информации.
"""

class Address:
    """
    Класс для хранения деталей адреса.
    
    Атрибуты:
        street (str): Название улицы.
        city (str): Название города.
        zip_code (str): Почтовый индекс.
    """
    
    def __init__(self, street: str, city: str, zip_code: str):
        """
        Инициализация нового адреса.
        """
        if not all([isinstance(arg, str) for arg in [street, city, zip_code]]):
            raise TypeError("Все аргументы адреса должны быть строками.")
        
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    # Геттеры
    def get_full_address(self) -> str:
        """Возвращает полный адрес в формате: Улица, Город, Индекс."""
        return f"{self.__street}, {self.__city}, {self.__zip_code}"

    # Сеттеры для возможности редактирования
    def set_street(self, street: str):
        """Устанавливает новое значение улицы."""
        self.__street = street

    def set_city(self, city: str):
        """Устанавливает новое значение города."""
        self.__city = city

    def set_zip_code(self, zip_code: str):
        """Устанавливает новое значение почтового индекса."""
        self.__zip_code = zip_code

    def __str__(self):
        """Возвращает строковое представление объекта Address."""
        return self.get_full_address()
