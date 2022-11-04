import math

#값 클래스 생성
def CTP(mass1, radius1, speed1):
    speed1 = float(speed1)
    radius1 = float(radius1)
    print("질량 > {}kg\n속력 > {}m/s\n반지름 > {}m".format(mass1, speed1, radius1))
    print("구심력 공식 > mv^/r")
    result1 = math.pow((mass1 * speed1), 2) / radius1
    print(str(result1) + " N")
        

def CTF(mass2, speed2, radius2):
    mass2 = float(mass2)
    speed2 = float(speed2)
    radius2 = float(radius2)
    print("질량 > {}kg\n속력 > {}m/s\n반지름 > {}m".format(mass2, speed2, radius2))
    print("원심력 공식 > -mv^/r")
    result2 = (math.pow(-1 * (mass2 * speed2), 2)) / radius2
    print(str(result2) + " N")

Choice = str(input("구심력 or 원심력\n> "))
if Choice == "구심력":
    mass = float(input("질량> "))
    radius = float(input("반지름> "))
    speed = float(input("속도> "))
    print(CTP(mass, radius, speed))

elif Choice == "원심력":
    mass = float(input("질량> "))
    radius = float(input("반지름> "))
    speed = float(input("속도> "))
    print(CTF(mass, radius, speed))