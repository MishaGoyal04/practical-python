# bounce.py
initial_height = 100
bounce_factor = 3 / 5

print("Bounce    Height (m)")

current_height = initial_height 

for bounce in range (1, 11):
  current_height *= bounce_factor
  print (f"{bounce:<8} {current_height:.2f}")
# Exercise 1.5
