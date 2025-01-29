def total_calc(bill_amount,tips_perc):
    total=bill_amount*(1+0.01*tips_perc)
    total=round(total,2)
    print(f"please pay ${total}")
total_calc(100,5)