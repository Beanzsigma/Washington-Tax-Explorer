valid_counties = ["king", "pierce", "snohomish", "spokane", "other"]

continue_calculating = True
while continue_calculating:
    usercounty = input("Enter the county you are in (King, Pierce, Snohomish, Spokane, other): ").lower()

    if usercounty not in valid_counties:
        print("Please enter a valid county.")
        continue

    print(f"You entered: {usercounty.capitalize()} County")
    if usercounty == "king":
        tax_rate = 0.0085
    elif usercounty == "pierce":
        tax_rate = 0.0092
    elif usercounty == "snohomish":
        tax_rate = 0.0080
    elif usercounty == "spokane":
        tax_rate = 0.0091
    else:
        print("Tax rate not available for 'other' counties.")
        continue

    useramount = input("What is your property value: ")

    try:
        cleaned = useramount.replace("$", "").replace(",", "").strip()
        amount = float(cleaned)
        if amount <= 0:
            print("Please enter a positive amount.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    tax_amount = amount * tax_rate
    print(f"Your property tax for {usercounty.capitalize()} County is: ${tax_amount:,.2f}")

    continue_input = input("Do you want to calculate another property tax? (yes/no): ").lower()
    if continue_input != "yes":
        continue_calculating = False