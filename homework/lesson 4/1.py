from sys import argv

sname, hours, basic_pay, add_cash = argv

hours = float(hours)
basic_pay = float(basic_pay)
add_cash = float(add_cash)

main_money = hours * basic_pay
sum_cash = main_money + add_cash

print(sum_cash)