name = input("What is your name? ")
print("hello", name)
age = input("How old are you? ")
print("you were probably born in", 2024-int(age))
try:
    age = int(age)
    print("you were probably born in", 2024 - age)
    #new_age = age / 0
except ValueError:
    print("you are trying to trick me")
    print("better luck next time")
except ZeroDivisionError:
    print("you can't divide by zero")
except:
    print("something unexpected happened")
else:
    print("you were probably born in", 2024-age)
finally:
    print("thanks for playing")