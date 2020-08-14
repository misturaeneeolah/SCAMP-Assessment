a = int(input("Insert number of digits"))
one = 0
two = 1
if a <= 0:
    print("Try a greater number",f)
else:
    print(one,two,end=" ")
    for x in range (2,a) :
        next = one + two
        print(next, end=" ")
        one = two
        two = next
