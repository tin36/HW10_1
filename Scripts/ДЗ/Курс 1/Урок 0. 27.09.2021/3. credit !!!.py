salary = 80000  # Зарплата
procent = 0.2
duty = 200000  # Долг

pay = salary * procent  # Выплата
mduty = 0

while duty >= 0:
  duty = duty - pay
  mduty += 1
  lduty = duty - abs(duty)
  md = lduty
  print('%s-й месяц, выплата %s рублей, остаток %s рублей' % (mduty, round(pay), duty))
    
  if pay > duty:
    klm = abs(duty)
    mduty += 1
    print('%s-й месяц, выплата %s рублей, остаток %s рублей' % (mduty, round(klm), md))

  
  if abs(duty) < pay:
    break