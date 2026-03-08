### Test_1 
Перевірка старту

**hello**
Порожня книга

**all**
Очікування: No contacts found.

**Додати контакт (1 телефон)**
add John 1234567890
Очікування: Contact added.

**Показати всі**
all
Очікування: John: 1234567890

**Додати ще один телефон тому ж контакту**
add John 0987654321
Очікування: Contact updated.

**Показати телефони контакту**
phone John
Очікування: 1234567890; 0987654321

**Змінити телефон (старий → новий)**
change John 1234567890 1111111111
Очікування: Contact updated.

**Перевірити, що змінилось**
phone John
Очікування: 1111111111; 0987654321

**Негативний тест: змінити неіснуючий старий телефон**
change John 0000000000 2222222222
Очікування: Old phone not found.

**Вихід**
exit


### Test_2 birthday
Тест-команди для Birthday

- add John 1234567890
- add-birthday John 05.03.1990 → має повернути "Birthday added."
- show-birthday John → має показати 05.03.1990
- birthdays → або список, або "No birthdays in the next 7 days."

### Final test

В CLI прогнати:

- add John 1234567890
- add John 0987654321
- phone John
- change John 1234567890 1111111111
- add-birthday John 05.03.1990
- show-birthday John
- birthdays

exit