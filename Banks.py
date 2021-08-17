per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите желаемую сумму вклада'))/100
deposit = list(per_cent.values())
for i in range(len(deposit)):
    deposit[i] *= money
print(deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))