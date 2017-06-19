while True:
    try:                    #start of try block
        number = int(input("Enter a number : \n"))
        print(str(18/number))
        break
    except ValueError:      #start of catch block
        print("Please enter number only")
    except ZeroDivisionError:
        print("Can't be divide be zero")
    except:                 #for no matched exceptions
        print("No siutable error description found")
        break
    finally:                #execute finally block
        print("Loop completed")
    