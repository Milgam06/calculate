import math

try:
    x1 = int(input("x1 값 > "))
    x2 = int(input("x2 값 > "))
    y1 = int(input("y1 값 > "))
    y2 = int(input("y2 값 > "))

except:
    print("<정수만 넣을 수 있습니다>")
    pass
    
lineLength = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

print(f"√(({x2} - {x1})² + ({y2} - {y1})²) = √{round(math.pow(lineLength, 2))}")
print(f"√{round(math.pow(lineLength, 2))} = {lineLength}")