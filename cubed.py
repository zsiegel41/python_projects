def cube():
    x = input("Enter a number: ")
    try:
        x = int(x)
    except ValueError:
        print("Please enter an integer")
    print(x * x * x)

