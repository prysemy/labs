import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

transactions = pd.read_csv('transactions.csv', delimiter=',')
print(transactions[transactions['STATUS'] == 'OK'].sort_values(by='SUM').drop_duplicates('SUM').loc[:, 'SUM'][-3:])
print(transactions[transactions['STATUS'] == 'OK'][transactions['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum())


def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"


flights = pd.read_csv('flights.csv', delimiter=',')
s = flights.groupby(flights.loc[:, 'CARGO'], as_index=False).size().loc[:, 'size']
siz = [s[0], s[1], s[2]]
flights.groupby(flights.loc[:, 'CARGO'], as_index=False).size().plot.pie(y='size',
                                                                         labels=flights.loc[:,
                                                                                'CARGO'].drop_duplicates(),
                                                                         autopct=lambda pct: func(pct, siz),
                                                                         startangle=300, fontsize=13,
                                                                         title='Количество перелетов')
plt.savefig('pd1_1.png')
plt.show()
price_Jumbo = flights[flights['CARGO'] == 'Jumbo'].loc[:, 'PRICE'].sum()
price_Medium = flights[flights['CARGO'] == 'Medium'].loc[:, 'PRICE'].sum()
price_Numble = flights[flights['CARGO'] == 'Nimble'].loc[:, 'PRICE'].sum()
pric = [price_Jumbo, price_Medium, price_Numble]
pd.DataFrame({'PRICES': [price_Jumbo, price_Medium, price_Numble]}).plot.pie(y='PRICES',
                                                                             labels=flights.loc[:,
                                                                                    'CARGO'].drop_duplicates(),
                                                                             autopct=lambda pct: func(pct, pric),
                                                                             startangle=300,
                                                                             fontsize=11,
                                                                             title='Стоимость')
plt.savefig('pd1_2.png')
plt.show()
weight_Jumbo = flights[flights['CARGO'] == 'Jumbo'].loc[:, 'WEIGHT'].sum()
weight_Medium = flights[flights['CARGO'] == 'Medium'].loc[:, 'WEIGHT'].sum()
weight_Numble = flights[flights['CARGO'] == 'Nimble'].loc[:, 'WEIGHT'].sum()
weig = [weight_Jumbo, weight_Medium, weight_Numble]
pd.DataFrame({'WEIGHTS': [weight_Jumbo, weight_Medium, weight_Numble]}).plot.pie(y='WEIGHTS',
                                                                                 labels=flights.loc[:,
                                                                                        'CARGO'].drop_duplicates(),
                                                                                 autopct=lambda pct: func(pct, weig),
                                                                                 startangle=30,
                                                                                 fontsize=13,
                                                                                 title='Вес')
plt.savefig('pd1_3.png')
plt.show()

info = pd.read_excel('students_info.xlsx').dropna()
results = pd.read_html('results_ejudge.html')[0]
info.columns = ['User', 'group_faculty', 'group_out']
data = pd.merge(results, info, on='User')

average_group = []
average_inf = []
for group in data.loc[:, 'group_faculty']:
    a = [group,
         round(data[data['group_faculty'] == group].loc[:, 'Solved'].sum() / data[data['group_faculty'] == group].loc[:,
                                                                             'User'].size, 2)]
    if a not in average_group:
        average_group.append(a)
for group in data.loc[:, 'group_out']:
    a = [group, round(
        data[data['group_out'] == group].loc[:, 'Solved'].sum() / data[data['group_out'] == group].loc[:, 'User'].size,
        2)]
    if a not in average_inf:
        average_inf.append(a)
x1 = [i[0] for i in average_group]
y1 = [i[1] for i in average_group]
plt.bar(x1, y1)
plt.grid()
plt.xlabel('group_faculty')
plt.ylabel('average solved')
for i in range(len(x1)):
    plt.text(x1[i], y1[i], y1[i], ha='center')
plt.savefig('pd3_1.png')
plt.show()
x2 = [i[0] for i in average_inf]
y2 = [i[1] for i in average_inf]
plt.bar(x2, y2)
plt.grid()
plt.xlabel('group_out')
plt.ylabel('average solved')
for i in range(len(x2)):
    plt.text(x2[i], y2[i], y2[i], ha='center')
plt.savefig('pd3_2.png')
plt.show()

best = data[(data['G'] > 10) | (data['H'] > 10)].loc[:, ['User', 'group_faculty', 'group_out']].reset_index()
print(best)
