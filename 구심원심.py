import math


class CTP: #값 클래스 생성
    def __init__(self, mass1, radius1, speed1):
        self.mass1 = float(mass1)
        self.speed1 = float(speed1)
        self.radius1 = float(radius1)
        print("질량 > {}kg\n속력 > {}m/s\n반지름 > {}m".format(mass1, speed1, radius1))
        print("구심력 공식 > mv^/r")
        V2_1 = math.pow(speed1, 2)
        result1 = (mass1 * V2_1) / radius1
        print(str(result1) + " N")
        
class CTF:
    def __init__(self, mass2, speed2, radius2):
        self.mass2 = float(mass2)
        self.speed2 = float(speed2)
        self.radius2 = float(radius2)
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