def validate(n):
    lst = [int(i) for i in str(n)]
    print(lst)
    if len(lst) % 2 == 0:
        for i in range(0, len(lst)-1, 2):
            print(lst[i] * 2)
        for i in range(len(lst)):
            if lst[i] > 9:
                lst[i]-9
                print(lst)
        lst = sum(lst)
        if lst % 10 == 0:
            print(lst)
            print("Valid")
        else:
            print("Not valid")
            print(lst)

validate(123456)