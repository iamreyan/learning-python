n = int(input("Enter a number: "))
print(f"Multiplication table of {n} is:")

for i in range(1, 11):
  print(f"{n} x {i} = {n * i}")
