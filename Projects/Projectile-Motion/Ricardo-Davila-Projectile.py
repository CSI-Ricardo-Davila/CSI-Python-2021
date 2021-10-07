import math

gun= "mp5"
CartridgeCalibre = "9x19mm Parabellum"
ammunittion = "9x19mm PBP gzh"
ProjectileVelocity_mps= 560 
building = "Oriental Plaza"
buildingHeight_m = 64

#Calculate the time the bullet will fly for#
time_s = math.sqrt((2*buildingHeight_m)/9.8)
#Using the time and velocity,calculate how far it will travel#
distance_m = ProjectileVelocity_mps * time_s

print(f"We will shoot the {gun} from {building}, which is {buildingHeight_m}m high. The {gun}'s catridge calibre is {CartridgeCalibre} and it is using the {ammunittion} bullets. The {gun} shoots at {ProjectileVelocity_mps} m/s, and we will se how much does it take to hit the ground and how far it goes.")


