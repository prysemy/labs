## Эпизод 1.
В наши руки попали данные о платежах некоторой глубоко законспирированной организации.
Судя по всему, поля в данных следует воспринимать предельно просто: CONTRACTOR - кому платёж, STATUS - статус операции, SUM - сумма операции. 

### Задача 1: найти 3 самых крупных платежа из реально проведённых (статус OK).
```Python
import pandas as pd

transactions = pd.read_csv('transactions.csv', delimiter=',')
transactions = transactions.drop(transactions[transactions['STATUS'] != 'OK'].index)
contractor = list(transactions['CONTRACTOR'])
sums = list(transactions['SUM'])
print('Самые крупные платежи:', *sorted(sums, reverse=True)[:3])
```

Вывод программы:
```
Самые крупные платежи: 100500 1000 999
```

### Задача 2: определить полную сумму реально проведённых платежей в адрес Umbrella, Inc.
```Python
sum_to_um = 0
for c in contractor:
    if c == 'Umbrella, Inc':
        sum_to_um += int(sums[contractor.index(c)])
print('Полная сумма, отправленная Umbrella, Inc:', sum_to_um)
```

Вывод программы:
```
Полная сумма, отправленная Umbrella, Inc: 1286220
```
