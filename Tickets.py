tickets = int(input('Введите количество билетов'))
age = [int(input('Введите возраст')) for i in range(1, tickets+1)]
sum = 0
for i in age:
    if 18 <= i < 25:
        sum += 990
    elif i >= 25:
        sum += 1390
if tickets > 3:
    print('За заказ от 3 билетов вам пологается скидка в размере 10%')
    sum *= 0.9
print('Сумма к оплате равна', sum)
