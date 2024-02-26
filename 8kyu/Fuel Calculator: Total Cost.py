def fuel_price(litres, price_per_litre):
    # Calculate the total cost based on the number of liters and price per liter
    total_cost = litres * price_per_litre

    # Apply the discount based on the number of liters purchased
    if litres >= 10:
        total_cost -= 0.25 * litres
    elif litres >= 8:
        total_cost -= 0.20 * litres
    elif litres >= 6:
        total_cost -= 0.15 * litres
    elif litres >= 4:
        total_cost -= 0.10 * litres
    elif litres >= 2:
        total_cost -= 0.05 * litres

    return round(total_cost, 2)

print(fuel_price(10, 21.5))
print(fuel_price(40, 10))
print(fuel_price(15, 5.83))