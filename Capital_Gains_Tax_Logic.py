def parse_currency(value: str) -> float:
    cleaned = value.strip().replace(',', '').replace('$', '')
    return float(cleaned)


def parse_tax_rate(value: str) -> float:
    cleaned = value.strip().replace('%', '')
    rate = float(cleaned)
    if rate > 1:
        rate /= 100
    return rate


def calculate_capital_gains_tax(amount: float, rate: float = 0.07) -> float:
    if amount <= 250000:
        return 0.0
    return round(amount * rate, 2)


def main() -> None:
    continue_calculating = True

    while continue_calculating:
        user_input = input('Enter the amount of capital gains: ')
        try:
            amount = parse_currency(user_input)
            if amount <= 0:
                print('Please enter a positive amount.')
                continue
        except ValueError:
            print('Please enter a valid number.')
            continue

        capital_gains_tax_rate = 0.07
        change_rate = input('Capital gains tax rate is 7% in Washington. Do you want to change the rate? (yes/no): ')
        if change_rate.lower() in ['yes', 'y']:
            rate_input = input('Enter the new tax rate (for example 7 or 0.07): ')
            try:
                capital_gains_tax_rate = parse_tax_rate(rate_input)
                print(f'Tax rate updated to {capital_gains_tax_rate:.2%}')
            except ValueError:
                print('Invalid input for tax rate. Using the default rate of 7%.')

        tax = calculate_capital_gains_tax(amount, capital_gains_tax_rate)
        remaining = amount - tax

        print('\nCapital gains tax results:')
        print(f'  Amount of capital gains: ${amount:,.2f}')
        print(f'  Tax rate applied: {capital_gains_tax_rate:.2%}')
        print(f'  Capital gains tax: ${tax:,.2f}')
        print(f'  Remaining amount after tax: ${remaining:,.2f}\n')

        again = input('Do you want to calculate another amount? (yes/no): ')
        if again.lower() not in ['yes', 'y']:
            continue_calculating = False


if __name__ == '__main__':
    main()
