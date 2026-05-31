num1 = 10
num2 = 10
try:
    print(num1 / num2)
except Exception:
    print("Error occurred!")
else:
    print("This is else block!")
finally:    print("This is finally block!")
