salary = 80000 #Зарплата
procent = 0.2
duty = 200000 #Долг

pay = (salary*procent) #Выплата
mduty = 0

for i in range(1, 111):
   
    print('%s-й месяц, выплата %s, остаток %s' % (i, round(pay), duty))
    duty = duty - pay

    if duty < -10000:

      break