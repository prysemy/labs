### Эпизод 1.
В наши руки попали данные о платежах некоторой глубоко законспирированной организации.
Судя по всему, поля в данных следует воспринимать предельно просто: CONTRACTOR - кому платёж, STATUS - статус операции, SUM - сумма операции. 

## Задача 1: найти 3 самых крупных платежа из реально проведённых (статус OK).
```Python
import pandas as pd

transactions = pd.read_csv('transactions.csv', delimiter=',')
transactions = transactions.drop(transactions[transactions['STATUS'] != 'OK'].index)
contractor = list(transactions['CONTRACTOR'])
sums = list(transactions['SUM'])
print('Самые крупные платежи: ', *sorted(sums, reverse=True)[:3])
```
