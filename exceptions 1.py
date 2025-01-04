try:
    text = input("Enter a value")
except EOFError:
    print("EOF Error")
except KeyboardInterrupt:
    print("You cancelled the operation")
else:
    print(f"you entered {text}")