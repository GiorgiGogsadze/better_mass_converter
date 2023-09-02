amount = float(input("Amount: "))
unit = input("T or KG? ")
if unit == "T":
  print(f"{amount * 1000} Kg.")
elif unit == "KG":
  print(f"{amount / 1000} T.")
else:
  print("Error")