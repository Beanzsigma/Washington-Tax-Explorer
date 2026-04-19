continue_calculating = True
while continue_calculating:
    useramount = input('What is your amount: ')
    try:
        amount = float(useramount)
        if amount <= 0:
            print('Please enter a positive amount.')
            continue
    except ValueError:
        print('Please enter a valid number.')
        continue
    print('Calculating tax and total price...')
    washington_tax_rate = 0.065
    user_change_tax_rate = input('Washington tax rate = 6.5%. Do you want to change the tax rate? (yes/no): ')
    if user_change_tax_rate.lower() in ['yes', 'y']:
        new_tax_rate = input('Enter the new tax rate (as a decimal, e.g., 0.07 for 7%): ')
        try:
            washington_tax_rate = float(new_tax_rate)
            print(f'Tax rate updated to {washington_tax_rate:.2%}')
        except ValueError:
            print('Invalid input for tax rate. Using default tax rate of 6.5%.')
    tax = amount * washington_tax_rate
    tax = round(tax, 2) 
    totalprice = amount + tax 
    totalprice = round(totalprice, 2)
    print('Your total price will be: ')
    print(f'${totalprice:.2f}')
    print('With a tax amount of: ')
    print(f'${tax:.2f}')
    
    user_continue = input('Do you want to calculate another amount? (yes/no): ')
    if user_continue.lower() not in ['yes', 'y']:
        continue_calculating = False