list1 = [23, 12, 567, 34, 89, 9, 5,]
max(list1)
min(list1)
while True:
    opt = input(" find value: ")
    if opt.lower() == "min":
        print(min(list1))
    elif opt.lower() == "max":
        print(max(list1))
    else:
        print("Invalid input.")

#done