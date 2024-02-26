def usdcny(usd):
    conversion_rate = 6.75
    cny_amount = usd * conversion_rate
    formatted_cny = "{:.2f}".format(cny_amount)
    return f"{formatted_cny} Chinese Yuan"