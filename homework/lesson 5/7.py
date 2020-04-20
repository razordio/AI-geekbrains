import json

firm_dict = {}
all_profit = 0
firms = 0
with open("file_for_7.txt", 'r') as f_obj:
    for line in f_obj:
        firms += 1
        firm_list = line.split()
        firm_profit = int(firm_list[2]) - int(firm_list[3])
        print(firm_list[0], firm_profit)
        firm_dict[firm_list[0]] = firm_profit
        if firm_profit <= 0:
            continue
        else:
            all_profit += firm_profit
average_profit = all_profit / firms
profit_dict = {"average profit": average_profit}
end_list = list()
end_list.append(firm_dict)
end_list.append(profit_dict)

with open("my_file.json", "w") as write_f:
    json.dump(end_list, write_f)
