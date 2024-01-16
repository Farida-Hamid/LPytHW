def looper (untill, step=1):
  i = 0
  numbers = []

  while i < untill:
    print(f"At the top is {i}")
    numbers.append(i)

    i += step

    print("Numbwrs now: ", numbers)
    print(f"At the bottom, is {i}")

  print("The numbers: ")

  for num in numbers:
    print(num)

looper(4)
looper(9, 3)