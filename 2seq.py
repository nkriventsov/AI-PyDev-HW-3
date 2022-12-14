# 5. (МОДУЛЬ 2) создать модуль 2seq.py. Задание:
# Пользователь вводит любые цифры через запятую
# Сохранить цифры в список
# Получить новый список в котором будут только уникальные элементы исходного
# (уникальным считается символ, который встречается в исходном списке только 1 раз)
# Вывести новый список на экран
# Порядок цифр в новом списке не важен
# Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
# Результат: 2, 4, 6, 9
#______________________________________________________________________________________

new_list = list(set(input('Введите любые цифры через запятую: ').split(',')))
print(new_list)

#______________________________________________________________________________________
# (Дополнительно*) Предусмотреть что пользователь может использовать один из 3-х разделителей:
# запятую, точку с запятой, слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя
#______________________________________________________________________________________

separators = set(',;/')
new_set = set()
eligible_chars_set = separators | set('0123456789')
while len(separators & new_set) > 1 \
        or len(separators - new_set) == len(separators) \
        or len(new_set - eligible_chars_set) > 0:
    if len(separators & new_set) > 1 \
            or len(new_set - eligible_chars_set) > 0:
        print('Используйте \033[4mтолько один\033[0m из 3-х разделителей!')
    new_set = set(input('Введите любые цифры через один из 3-х разделителей ("," или ";" или "/"): '))
uniq_list = list(new_set-separators)
print(uniq_list)
