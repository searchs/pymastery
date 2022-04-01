# Error Handling
while True:

    try:
        age = int(input("Please enter your age: "))
        print(f"Your {age} years old.")
        break
    except ValueError as ve:
        print("Erro Message: ", ve.getMessage)
        print("Please enter a number as age: ")
    finally:
        print("No more age related question!")
