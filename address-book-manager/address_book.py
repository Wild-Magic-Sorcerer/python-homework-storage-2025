"""
Модуль AddressBook для управления коллекцией контактов.
Предоставляет функциональность для добавления, удаления, поиска и экспорта.
"""

import json
from typing import List, Optional
from .contact import Contact # Импорт Contact

class AddressBook:
    """
    Класс-контейнер для хранения и управления коллекцией объектов Contact.
    
    Атрибуты:
        contacts (List[Contact]): Список объектов Contact.
    """
    
    def __init__(self):
        """
        Инициализация пустой адресной книги.
        """
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact):
        """
        Добавляет новый контакт в адресную книгу.
        """
        if not isinstance(contact, Contact):
            raise TypeError("Можно добавлять только экземпляры класса Contact.")
        self.contacts.append(contact)
        print(f"Контакт '{contact.get_name()}' добавлен.")

    def delete_contact(self, name_or_phone: str) -> bool:
        """
        Удаляет контакт по имени или телефону.
        Возвращает True при успешном удалении, иначе False.
        """
        initial_count = len(self.contacts)
        self.contacts = [
            c for c in self.contacts 
            if c.get_name() != name_or_phone and c.get_phone() != name_or_phone
        ]
        if len(self.contacts) < initial_count:
            print(f"Контакт по запросу '{name_or_phone}' удален.")
            return True
        else:
            print(f"Контакт по запросу '{name_or_phone}' не найден.")
            return False

    def find_contact(self, query: str) -> List[Contact]:
        """
        Поиск контактов по имени или телефону (частичное совпадение).
        """
        query = query.lower()
        results = [
            c for c in self.contacts 
            if query in c.get_name().lower() or query in c.get_phone()
        ]
        return results

    def edit_contact(self, name_or_phone: str, new_data: dict) -> bool:
        """
        Находит контакт и редактирует его данные.
        'new_data' - словарь с полями для обновления.
        """
        for contact in self.contacts:
            if contact.get_name() == name_or_phone or contact.get_phone() == name_or_phone:
                if 'name' in new_data:
                    contact.set_name(new_data['name'])
                if 'phone' in new_data:
                    contact.set_phone(new_data['phone'])
                if 'email' in new_data:
                    contact.set_email(new_data['email'])
                
                # Редактирование адреса
                addr_data = new_data.get('address', {})
                address_obj = contact.get_address()
                if 'street' in addr_data:
                    address_obj.set_street(addr_data['street'])
                if 'city' in addr_data:
                    address_obj.set_city(addr_data['city'])
                if 'zip_code' in addr_data:
                    address_obj.set_zip_code(addr_data['zip_code'])
                    
                print(f"Контакт '{name_or_phone}' успешно отредактирован.")
                return True
        print(f"Контакт '{name_or_phone}' для редактирования не найден.")
        return False
    
    def export_to_json(self, filename: str = "address_book_export.json"):
        """
        Экспортирует все контакты в JSON файл.
        """
        data = []
        for contact in self.contacts:
            data.append({
                "name": contact.get_name(),
                "phone": contact.get_phone(),
                "email": contact.get_email(),
                "address": {
                    "street": contact.get_address().get_full_address().split(',')[0].strip(), # Простой парсинг
                    "city": contact.get_address().get_full_address().split(',')[1].strip(),
                    "zip_code": contact.get_address().get_full_address().split(',')[2].strip()
                }
            })
            
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Контакты успешно экспортированы в файл: {filename}")
        except IOError as e:
            print(f"Ошибка при экспорте в файл: {e}")

    def __str__(self):
        """Возвращает строковое представление всей адресной книги."""
        if not self.contacts:
            return "Адресная книга пуста."
        return "\n---\n".join([str(c) for c in self.contacts])
