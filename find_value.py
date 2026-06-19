list1 = ["number", "string", "flat", "celcius", "bisyaka", "donut"]
opt = input(" find: ")
if opt.lower() in list1:
    print( "found ", opt, " in the list")
else:
    print( opt, " not found in the list")
#done