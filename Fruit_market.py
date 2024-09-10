def display_fruit_list():
    print('Fruit List')
    print('Index\t|Name\t|Stock\t|Price')
    for indeks_show,(key_show, value_show) in enumerate(fruit_dict.items()):
        print(f"{indeks_show}\t|{key_show}\t|{value_show['stock']}\t|{value_show['price']}")

def add_fruit_list():
    fruit_new = input('Enter fruit name: ').capitalize()
    stock_new = int(input('Enter fruit stock: '))
    price_new = int(input('Enter the price of fruit: '))

    if fruit_new in fruit_dict:
        fruit_dict[fruit_new]['stock'] += stock_new
        print(f'{stock_new} units of {fruit_new} added. New stock: {fruit_dict[fruit_new]["stock"]}')
    else:
        fruit_dict[fruit_new] = {'stock': stock_new, 'price': price_new}
        print(f'{fruit_new} added to the list with {stock_new} stock.')

    #fruit_dict[fruit_new.capitalize()]={'stock':stock_new,'price':price_new}
    display_fruit_list()

def remove_fruit_list():
    display_fruit_list()
            
    del_fruit = int(input('Enter the index of the fruit you want to delete: '))

    while del_fruit>len(keys)-1 or del_fruit<0:
        print('The index is not available')
        del_fruit = int(input('Enter the index of the fruit you want to delete: '))

    del fruit_dict[keys[del_fruit]]

    display_fruit_list()

def buy_fruit_list():
    while True:
        display_fruit_list()
        indeks_buy = int(input('Enter the index of the fruit you want to buy: '))
        qty_buy = int(input('Enter the amount you want to buy: '))

        if qty_buy>fruit_dict[keys[indeks_buy]]['stock']:
            print(f"Not enough stock, {keys[indeks_buy]} stock only {fruit_dict[keys[indeks_buy]]['stock']} left")

        else:
            if keys[indeks_buy] in user_purc:
                user_purc[keys[indeks_buy]] += qty_buy
            else:
                user_purc[keys[indeks_buy]] = qty_buy

            fruit_dict[keys[indeks_buy]]['stock'] -= qty_buy

        chart_content()

        if continue_shopping()==0:
            shopping_details()
            break
            

def chart_content():
    print(f"Chart_Contents:")
    print(f"Name\t|Qty\t|Price")
    for key_purc, value_purc in user_purc.items():
        price_purc = fruit_dict[key_purc]['price']
        print(f"{key_purc}\t|{value_purc}\t|{price_purc}")
    print()
    
def continue_shopping():
    while True:
        purc_dec = input('Want to buy another one? (yes/no)= ')
        if purc_dec.lower()=='yes':
            return 1
        elif purc_dec.lower()=='no':
            return 0
        else:
            print("Invalid input, please answer with 'yes' or 'no'.")

def shopping_details():
    Total = 0
    print(f'\nShopping Details: ')
    print(f"Name\t|Qty\t|Price\t|Total")
    for key_purc, value_purc in user_purc.items():
        price_purc = fruit_dict[key_purc]['price']
        total_price = value_purc*price_purc
        Total += total_price
        print(f"{key_purc}\t|{value_purc}\t|{price_purc}\t|{total_price}")
    print(f"Total Payable = {Total}")

    money = int(input('Enter the amount of money: '))
    while money<Total:
        print(f'Your money is less than {Total-money}')
        money = int(input('Enter the amount of money: '))
    print(f'Thank You')
    if money>Total:
        print(f'\nYour money back: {money-Total}')


    #No.3
fruit_dict={
    'Apple':{
        'stock':20,
        'price':10000, 
    },
    'Orange':{
        'stock':15,
        'price':15000, 
    },
    'Grape':{
        'stock':25,
        'price': 20000, 
    }
}

user_purc = {}
while True:
    keys = list(fruit_dict.keys())

    print('Welcome to the Fruit Market')
    print('\nMenu List:')
    print('1. Displays a list of fruits\n'
        '2. Add fruit\n'
        '3. Remove fruit\n'
        '4. Buy fruit\n'
        '5. Exit Program')
    
    menu = int(input('Enter the menu number you want to run: '))
    if menu == 1:
        display_fruit_list()

    elif menu==2:
        add_fruit_list()
            
    elif menu==3:
        remove_fruit_list()

    elif menu==4:
        buy_fruit_list()

    elif menu==5:
        break
    else:
        print('Invalid option. Please select a number from the menu.')
    print()


