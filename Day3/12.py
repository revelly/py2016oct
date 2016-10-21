#handling exceptions
for x in range(3):
    try:
        amount = int(input("Enter Amount"))
        break
    except ValueError:
        print("Enter valid number")
else:
    print("Exiting after max retrie")
