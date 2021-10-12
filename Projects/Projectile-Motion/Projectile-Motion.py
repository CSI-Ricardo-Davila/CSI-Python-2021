import math
from ExperimentalData import ExperimentalData
# gun= "mp5"
# CartridgeCalibre = "9x19mm Parabellum"
# ammunition = "9x19mm PBP gzh"
# ProjectileVelocity_mps= 560 
# building = "Oriental Plaza"
# buildingHeight_m = 64


def experiment(experimentalData:ExperimentalData):
   #Calculate the time the bullet will fly for#
    time_s = math.sqrt((2*experimentalData.buildingHeight_m)/experimentalData.gravity)
    #Using the time and velocity,calculate how far it will travel#
    distance_m = experimentalData.ProjectileVelocity_mps * time_s

    print(f"We will shoot the {experimentalData.gun} from {experimentalData.building}, which is {experimentalData.buildingHeight_m}m high. The {experimentalData.gun}'s catridge calibre is {experimentalData.CartridgeCalibre} and it is using the {experimentalData.ammunition} bullets. The {experimentalData.gun} shoots at {experimentalData.ProjectileVelocity_mps} m/s, and it took { round(time_s, 2) } seconds to hit the ground and it traveled {round(distance_m, 2) } meters.")

MyData = ExperimentalData("mp5", "9x19mm Parabellum","9x19mm PBP gzh",560,"Oriental Plaza", 64, 9.8)

# experimentalData={
# "gun" : "mp5",
# "CartridgeCalibre" : "9x19mm Parabellum",
# "ammunition" : "9x19mm PBP gzh",
# "ProjectileVelocity_mps" : 560,
# "building" : "Oriental Plaza",
# "buildingHeight_m" : 64,
# "gravity": 9.8
# }

experiment(MyData)

