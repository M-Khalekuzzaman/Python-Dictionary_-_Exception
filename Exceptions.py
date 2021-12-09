#Runtime error/Incorrect input / Incorrect code
try :
    list = [20,0,10]
    result =int( list[0] / list[3])
    print(result)
    print('Done')

except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError :
    print("Index error")
finally:
    print("Succesfull")

