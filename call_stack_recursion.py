def funcThree():
    print("three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

funcOne()