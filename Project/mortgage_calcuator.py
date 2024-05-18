# Find out how long a payoff a mortgage

principal= 500000
payment= 2684.11
rate= 0.05
total_paid= 0

#extra payment info

extra_payment= 1000
extra_payment_start_month= 1
extra_payment_end_month= 60
month= 0

print('Month','Intrest','Remaining','Principal')
while principal> 0:
    month+=1
    if month>=extra_payment_start_month and month<=extra_payment_end_month:
        total_payment= payment+extra_payment
    else:
        total_payment=payment

    intrest=principal*rate/12
    principal=principal+intrest-total_payment
    total_paid += total_payment
    print(({month,intrest,total_payment-intrest,principal)

print("Total_paid",total_paid)