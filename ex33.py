def looper (untill):
  i = 0
  numbers = []

  while i < untill:
    print(f"At the top is {i}")
    numbers.append(i)

    i += 1

    print("Numbwrs now: ", numbers)
    print(f"At the bottom, is {i}")

  print("The numbers: ")

  for num in numbers:
    print(num)

looper(4)