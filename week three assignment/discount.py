def calculate_discount(price, discount_percent):
    if disount_percent >= 20:
        d_price = price * (1-discount_percent/100)
        return d_price
    else:
        return price
    
    initial_price = float(input("Enter the initial price of the item: "))
    discount = float(input("Enter the discount percentage: "))
    bp = calculate_discount(initial_price, discount)
    print("Final price after applying the discount: ",bp)