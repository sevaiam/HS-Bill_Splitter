# write your code here
from random import choice
my_friends = int(input('Enter the number of friends joining (including you):'))
my_friends_dic = {}
print()
if my_friends <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(my_friends):
        new_friend = input()
        my_friends_dic.setdefault(new_friend, 0)
    print()
    bill_total = float(input('Enter the total bill value:'))


    print()
    get_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    print()
    if get_lucky == 'Yes':
        lucky = choice(list(my_friends_dic.keys()))
        print(lucky, 'is the lucky one!')
        bill_split = bill_total / (len(my_friends_dic) - 1)
        for key in my_friends_dic:
            if key != lucky:
                my_friends_dic[key] = round(bill_split, 2)
    else:
        print('No one is going to be lucky')
        bill_split = bill_total / len(my_friends_dic)
        for key in my_friends_dic:
            my_friends_dic[key] = round(bill_split, 2)
    print(my_friends_dic)

