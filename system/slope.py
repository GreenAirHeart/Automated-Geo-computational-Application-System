
# from arcpy.sa import *
# #
# # #model_SLOPE
# # import sys
# import arcpy
# from arcpy import env
# from arcpy.sa import *

def SLOPE(data_linearUnit, classification_system_unit):
    if str(data_linearUnit) == str(1.0):
        method = "PLANAR"
        z = float(1)  # z_factor
        output_measurement = None
    else:
        method = "GEODESIC"
        z = str(data_linearUnit).upper()  # z_unit
        output_measurement = None

    if str(classification_system_unit).lower() == "degree":
        output_measurement = "DEGREE"
    elif str(classification_system_unit).lower() == "percent":
        output_measurement = "PERCENT_RISE"

    return method, output_measurement, z


    # outSlope = arcpy.sa.Slope(str(input_file), output_measurement, z, method)
    # outSlope.save(folder + "slope_output" + instance_name + ".tif")
def my_function(b):
    a=b+1
    print(a)

function_name = "my_function"
globals()[function_name](6)

#test-------------------------------------------------------------------------------------------------
# a = "place_a"
# b = "place_b"
# c = "place_c"
# d = "place_d"
# e = "D:/geomorphic_ontology/geomorphology/following_NNU/geomorphic_following/AUTO_Project_result/"
# result=SLOPE(c,d)
# print(str(a))
# print(str(e),str(b))
# print((result[2]), str(result[1]), str(result[0]))
# print(type((result[2])))
# # print('"' + (a) + '"')
# # if str(a) == str("D:/geomorphic_ontology/geomorphology/material_from_NNU/Model and Data/preData/prj_dem.tif"):
# #     print("yes")
# # else: print("no")
# #,'"{}"'.format(result[1]),float(result[2]), '"{}"'.format(result[0]))
# # Perform arcpy operation that may raise a RuntimeError
# # Replace with the specific arcpy function causing the error
# try:
#
#     import arcpy
#     # outSlope = arcpy.sa.Slope(str("D:/geomorphic_ontology/geomorphology/material_from_NNU/Model and Data/preData/prj_dem.tif"), "DEGREE", 1, "PLANAR")
#     outSlope = arcpy.sa.Slope(str(a),str(result[1]), result[2], str(result[0]))
#     # outSlope.save("D:/geomorphic_ontology/geomorphology/following_NNU/geomorphic_following/AUTO_Project_result/slope_4.tif")
#     outSlope.save(str(e) + "slope_output" + str(b) + ".tif")  #cannot use the same file name  -----  can be used as the input data for the next data
#
# except RuntimeError as w:
#     # Handle the exception
#     print("An error occurred:", str(w))
# test------------------------------------------------------------------------------------------------------------------------




# import arcpy
# outSlope = arcpy.sa.Slope(str("D:/geomorphic_ontology/geomorphology/material_from_NNU/Model and Data/preData/prj_dem.tif"), "DEGREE", 1, "PLANAR")
# outSlope.save("D:/geomorphic_ontology/geomorphology/following_NNU/geomorphic_following/AUTO_Project_result/slope.tif")
# print(sys.path)
# def add(a,b):
#     c = str(a) + str(b)
#     return c
# a = "1"
# b = "2"
# c = "3"
# print(c)
