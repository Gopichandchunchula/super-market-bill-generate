from datetime import datetime

print("Welcome to Godavari Supermarket!")

name = input('Enter Your Name: ')

# List of items
lists = '''
Rice        RS 30/kg
Sugar       RS 40/kg
Salt        RS 25/kg
Oil         RS 60/kg
Paneer      RS 90/kg
Colgate     RS 55/each
Idly Powder RS 44/kg
Horlicks    RS 20/each
'''

# Item dictionary with prices
items = {
    'rice': 30,
    'sugar': 40,
    'salt': 25,
    'oil': 60,
    'paneer': 90,
    'colgate': 55,
    'idly powder': 44,
    'horlicks': 20
}

# Variables for billing
price = 0
pricelist = []
totalprice = 0
ilist = []
qlist = []
plist = []

# Display item list if user requests
option = int(input('For list of items, press 1: '))
if option == 1:
    print(lists)

# Main shopping loop
while True:
    inpl = int(input('If you want to buy, press 1; to exit, press 2: '))
    if inpl == 2:
        break
    if inpl == 1:
        item = input('Enter your item: ').lower()  # Convert to lowercase for consistency
        quantity = int(input('Enter quantity: '))
        if item in items.keys():
            price = quantity * items[item]
            pricelist.append((item, quantity, price))  # Append only item, quantity, and price
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
        else:
            print('Sorry, the item you entered is not available in our market.')
    else:
        print('You entered an invalid number. Please try again.')

# Ask user if they want to generate a bill
inp = input('Can I bill the items? (yes or no): ').lower()
if inp == 'yes' and totalprice > 0:
    gst = (totalprice * 5) / 100
    finalamount = gst + totalprice
    print(30 * '=', 'Hyderabad Supermarket', 30 * '=')
    print(40 * ' ', 'Hyderabad')
    print('Name:', name, 30 * ' ', 'Date:', datetime.now())
    print(30 * '=')
    print('S.No', 8 * ' ', 'Item', 15 * ' ', 'Quantity', 8 * ' ', 'Price')
    for i, (item, quantity, price) in enumerate(pricelist, start=1):
        print(f'{i:<5} {item:<20} {quantity:<15} Rs {price:<10}')
    print(30 * '_')
    print(f'Total Amount: {totalprice:>50}')
    print(f'GST (5%): {gst:>57}')
    print(f'Final Amount: {finalamount:>50}')
    print(30 * '_')
    print(25 * ' ', 'Thanks for visiting!')
else:
    print('No items were billed. Thank you for visiting!')













                
            

