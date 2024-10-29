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
data = pd.DataFrame(columns=['SIZE', 'PRICE', 'WEIGHT'])
for cargo in flights['CARGO'].unique():
    siz = flights[flights['CARGO'] == cargo].shape[0]
    price = flights[flights['CARGO'] == cargo].loc[:, 'PRICE'].sum()
    weight = flights[flights['CARGO'] == cargo].loc[:, 'WEIGHT'].sum()
    data._set_value(index=cargo, col='SIZE', value=siz)
    data._set_value(index=cargo, col='PRICE', value=price)
    data._set_value(index=cargo, col='WEIGHT', value=weight)
print(data)
print(data.index)
for yi in ['SIZE', 'PRICE', 'WEIGHT']:
    data.plot.pie(y=yi, labels=data.index, autopct=lambda pct: func(pct, data.loc[:, yi]), startangle=300,
                  fontsize=10, title=yi)
plt.show()

info = pd.read_excel('students_info.xlsx').dropna()
results = pd.read_html('results_ejudge.html')[0]
info.columns = ['User', 'group_faculty', 'group_out']
data = pd.merge(results, info, on='User')

for groups in [data.loc[:, 'group_faculty'], data.loc[:, 'group_out']]:
    average_group = []
    for group in groups:
        a = [group, round(
            data[groups == group].loc[:, 'Solved'].sum() / data[groups == group].loc[:,
                                                                          'User'].size, 2)]
        if a not in average_group:
            average_group.append(a)
    x = [i[0] for i in average_group]
    y = [i[1] for i in average_group]
    plt.bar(x, y)
    plt.grid()
    plt.xlabel('groups')
    plt.ylabel('average solved')
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], ha='center')
    plt.show()

best = data[(data['G'] > 10) | (data['H'] > 10)].loc[:, ['User', 'group_faculty', 'group_out']].reset_index()
print(best)
