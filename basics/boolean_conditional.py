def main():
    print("Enter a value:")
    data = input()
    print("Enter a number:")
    num = input()

    # Logical Operators
    # if(a and b)
    # if(a or b)
    # if(not a)
    if( int(num) == 0):
        print("ZERO")
    elif(int(num) < 0 ):
        print("NEGATIVE")
    else:
        print("POSITIVE")

    # 0 is default false.
    if(0):
        print("yay")
    # None, empty objects and some other things are inherently falsy.

    # is vs. "=="
    a = 1
    a == 1 # True
    a is 1 # True

    l = [1,2,3]
    k = [1,2,3]

    l == k # True - is checking the value of the objects
    l is k # False - is is checking if they are stored in the same place of memory
    l = k
    l is k # True

    return 0


main()