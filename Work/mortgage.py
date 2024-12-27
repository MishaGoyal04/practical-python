# mortgage.py
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)


# Exercise 1.8
# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    months += 1

if principal > 0:
    principal = principal * (1+rate/12) - (payment + 1000)
    total_paid = total_paid + (payment+1000)
else:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print(f'Total paid: {total_paid:.2f}')
print(f'Months: {months}')



# Exercise 1.9
# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0  

# Extra payment parameters
extra_payment_start_month = 61  # Start extra payments after 5 years
extra_payment_end_month = 108   # End extra payments after 9 years
extra_payment = 1000            # Extra payment amount

while principal > 0:
    # Increment the month count
    months += 1

    # Determine the payment amount
    if extra_payment_start_month <= months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

# Print the results
print(f'Total paid: {total_paid:.2f}')
print(f'Months: {months}')



# Exercise 1.10
# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0  # Count the number of months

# Extra payment parameters
extra_payment_start_month = 61  # Start extra payments after 5 years
extra_payment_end_month = 108   # End extra payments after 9 years
extra_payment = 1000            # Extra payment amount

# Print table header
print(f"{'Month':<10}{'Total Paid':<15}{'Remaining Principal':<20}")

# Main loop
while principal > 0:
    # Increment the month count
    months += 1

    # Determine the payment amount
    if extra_payment_start_month <= months <= extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment

    # Update principal and total paid
    principal = principal * (1 + rate / 12) - current_payment
    total_paid += current_payment

    # Print the month, total paid, and remaining principal
    print(f"{months:<10}{total_paid:<15.2f}{principal:<20.2f}")

# Print final summary
print(f"\nTotal paid: {total_paid:.2f}")
print(f"Months: {months}")


