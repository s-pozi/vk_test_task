import pytest


class TestTask:
    def test_dict_add(self):
        """
        Проверка добавления ключа/значения в словарь
        """
        test_dict = {}
        add_key = "key"
        add_value = "value"
        test_dict[add_key] = add_value
        assert add_key in test_dict and test_dict[add_key] == add_value

    @pytest.mark.parametrize("key", [2, 4, 6, 8, 10])
    def test_dict_even_keys(self, key):
        """Проверяем, что ключ является четным числом"""
        assert key % 2 == 0

    def test_dict_get_nonexistent_key(self):
        """Проверка получения по несуществующему ключу"""
        test_dict = {'key': 'value'}
        assert test_dict.get('nonexistent_key') is None

    def test_set_add(self):
        """Проверяем что добавленное значение существует в множестве"""
        add_value = 'test'
        test_set = set()
        test_set.add(add_value)
        assert add_value in test_set

    @pytest.mark.parametrize("element,set,expected", [
        (1, {1, 2, 3}, True),  # Элемент присутствует в множестве
        (4, {1, 2, 3}, False),  # Элемент отсутствует в множестве
    ])
    def test_element_existence_in_set(self, element, set, expected):
        """Параметризованная проверка наличия значения во множестве"""
        assert (element in set) == expected

    def test_set_remove_nonexistent_element(self):
        """Проверка удаления несуществующего элемента, ожидается KeyError"""
        test_set = {1, 2, 3}
        element_to_remove = 4

        with pytest.raises(KeyError):
            test_set.remove(element_to_remove)












