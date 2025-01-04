
try:
    print(a)
except Exception as e:
    print(f"Something is wrong. The error is str{e}")
finally:
    print("Try and Except is finished right here")


try:
    print("Opening text file")
    b=open("txt.txt")
    print("Content of file")
    print(b)
finally:
    print("Closing the file")
    b.close()