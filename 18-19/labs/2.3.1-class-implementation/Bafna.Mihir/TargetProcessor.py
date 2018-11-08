import math
class TargetProcessor:
    degrees = u'\N{DEGREE SIGN}'
    centimeters = " cm"

    def __init__(self):
        pass

    def findDistanceAzimuth(self,f,w,iw,x,h):
        d = (f*w)/iw
        az = math.atan(x/f)*180/math.pi
        al = math.atan(h/f)*180/math.pi
        return round(d,2),round(az,4),round(al,4)

    def displayValues(self,distance,azimuth,altitude):
        print("\n"+"Distance = " + str(distance)+self.centimeters)
        print("Azimuth = " + str(azimuth)+self.degrees)
        print("Angle of Altitude = "+ str(altitude)+self.degrees+"\n")
