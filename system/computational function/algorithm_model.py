
import owlready2
from pyshacl import validate
import re
import pandas
from owlready2 import *
import math
import csv
from collections import Counter
import arcpy
from arcpy import env
from arcpy.sa import *
from osgeo import  gdal, osr ,ogr
from os import path



def DEM_instance_creator(ontology,instance_name,dempath,data_class):
    a = get_ontology(ontology).load()
    on_class=a.classes()
    on_object_property=a.object_properties()
    on_data_property=a.data_properties()
    # on_individual=a.individuals()
    on_anxioms=a.general_axioms()
    # on=a.get_triples()
    on=a.variables()
    on_rule=a.rules()
    l_object_property=list(on_object_property)
    l_class=list(on_class)
    l_rules=list(on_rule)
    instance=on_class
    my_dict = {str(item).split('.')[1]: item for item in l_class}
    dem_instance=my_dict[str(data_class)](instance_name)
    dem_instance.path = [str(dempath)]
    a.save(ontology)



def knowledge_graph_data(ontology,data_name):
    a = get_ontology(ontology).load()
    on_class=a.classes()
    on_object_property=a.object_properties()
    on_data_property=a.data_properties()
    on_individual=a.individuals()
    on_anxioms=a.general_axioms()
    # on=a.get_triples()
    on=a.variables()
    on_rule=a.rules()
    l_object_property=list(on_object_property)
    l_class=list(on_class)
    l_rules=list(on_rule)
    l_individuals=list(on_individual)
    my_dict = {str(item).split('.')[1]: item for item in l_individuals}
    my_object_project = {str(item).split('.')[1]: item for item in l_object_property}
    data=(my_dict[str(data_name)].path)[0]
    return data


def clear_folder(folder_path):
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)

def kg_class(ontology):
    a = get_ontology(ontology).load()
    on_class=a.classes()
    on_object_property=a.object_properties()
    on_data_property=a.data_properties()
    # on_individual=a.individuals()
    on_anxioms=a.general_axioms()
    # on=a.get_triples()
    on=a.variables()
    on_rule=a.rules()
    l_object_property=list(on_object_property)
    l_class=list(on_class)
    l_rules=list(on_rule)
    instance=on_class
    my_dict = {str(item).split('.')[1]: item for item in l_class}
    return my_dict


def kg_input(ontology,model_name):
    mydict=kg_class(ontology)
    input_of_model=mydict[model_name].hasInput
    function_name=(mydict[model_name].function)[0]
    # print(function_name)
    if len(input_of_model)==1:
        pathdic1={}
        input_example=input_of_model[0].instances()
        # =my_dict[name1].instances()
        input_path=input_example[0].path
        key=input_of_model[0]
        print(key)
        key_split= str(key).split('.')
        key_part = key_split[-1]
        pathdic1[key_part] = input_path[0]
        # print(input_of_model,input_example,input_path)
        return pathdic1,function_name
    else:
        inputdic = {str(item).split('.')[1]: item for item in input_of_model}  # Assuming input_of_model is a dictionary
        # print(inputdic)
        function_name = (mydict[model_name].function)[0]
        pathdic = {}
        for key in inputdic:
            input_ins = (inputdic[key]).instances()
            input_path = input_ins
            int=input_path[0].path
            pathdic[key] = int[0]
        print(pathdic)
        return pathdic,function_name


def RASTER_CLIP(data,output,x_min,y_min,x_max,y_max):
  rectangle = str(x_min)+' '+str(y_min)+' '+str(x_max)+' '+str(y_max)
  arcpy.Clip_management(data,rectangle,output,"", "", "NONE", "NO_MAINTAIN_EXTENT")


#DEM_projection： dem is the input name of dem data
def Project_DEM(input,dem_name,work_space,ontology):

    #get the projection value
    ds = gdal.Open(input)
    if ds is None:
        raise ValueError('Invalid raster data')
    metadata = dict()
    srs = osr.SpatialReference(ds.GetProjectionRef())
    metadata['isProjected'] = srs.IsProjected()
    if metadata['isProjected'] > 0 :
        projected = True
    else:
        projected = False
    #do the projection action
    if projected is False:
        # data_category="continuous data"
        # if data_category is "continuous data":
        resampling_type = "BILINEAR"
        # else: resampling_type = "NEAREST"
        # print(out_coor_system)
        # print(resampling_type)
        input_file = input
        output_file = work_space + str(dem_name)+"_"+"pro" + ".tif"
        out_coor_system_sr=arcpy.SpatialReference(54017)
        arcpy.management.ProjectRaster(input_file, output_file, (out_coor_system_sr), resampling_type, "", "", "", "", "")
        print("model_PROJECT_RASTER runs successfully")
        data_class='Projected_DEM'
        R_ed = str(dem_name) + "_" + "pro"
        DEM_instance_creator(ontology,R_ed,output_file,data_class)
        return R_ed
    else:
        print("do not need projection")
        return input

def Identify_water_net(input,work_space,dem_name,ontology):
    input_data=input['Projected_DEM']
    print("inputdata",input_data)
    outFlowDirection = FlowDirection(str(input_data), 'NORMAL', '', 'D8')
    outFlowDirection_name='H:/DEM/app/test/outflowdir'
    outFlowDirection.save(outFlowDirection_name)

    outFlowAccumulation=FlowAccumulation(outFlowDirection_name, '', 'FLOAT', 'D8')
    outFlowAccumulation_name='H:/DEM/app/test/outflowacc.tif'
    outFlowAccumulation.save(outFlowAccumulation_name)
    stats = arcpy.GetRasterProperties_management(outFlowAccumulation_name, "MAXIMUM", "")
    if int(stats[0])<4444:
        deep= 3000
    else:
        deep=4444
    output_file_raster = SetNull((Raster(outFlowAccumulation_name) < deep), 1)
    output='H:/DEM/app/test/'+dem_name+'_'+'waternet.shp'
    arcpy.conversion.RasterToPolyline(output_file_raster, output,'ZERO', 0,
                                      'SIMPLIFY',"")
    print("model_Identify_water_net runs successfully")
    data_class='Water_net'
    R_ed = str(dem_name) + "_" + "waternet"
    DEM_instance_creator(ontology,R_ed,output,data_class)
    return R_ed

def Validate_DEM(input,work_space,dem_name,ontology):
    input_data=input['Projected_DEM']
    print("inputdata",input_data)
    output_file_name=work_space + dem_name +'_'+ "vadem.tif"
    output_file= Con(Raster(input_data)>-1000,1,0)
    output_file.save(output_file_name)
    print("model_Validate_DEM runs successfully")
    data_class='Valid_DEM'
    R_ed = str(dem_name) + "_" + "vadem"
    DEM_instance_creator(ontology,R_ed,output_file_name,data_class)
    return R_ed

def Identify_DEM_boundary(input,work_space,dem_name,ontology):
    input_file = input['Projected_DEM']
    print("inputdata", input_file)
    output_file_name = work_space + dem_name + '_' + "dembound.shp"
    arcpy.ddd.RasterDomain(input_file, output_file_name, "POLYGON")
    # output_file.save(output_file_name)
    print("model_Identify_DEM_boundary runs successfully")
    data_class = 'DEM_boundary'
    R_ed = str(dem_name) + "_" + "dembound"
    DEM_instance_creator(ontology, R_ed, output_file_name, data_class)
    return R_ed


def Calculate_slope_value(input,work_space,dem_name,ontology):
    input_file = input['Projected_DEM']
    print("inputdata", input_file)
    output_file_name = work_space + dem_name + '_' + "slope.tif"
    outSlope = Slope(str(input_file), 'DEGREE', 1, 'PLANAR')
    outSlope.save(output_file_name)
    print("model_Calculate_slope_value runs successfully")
    data_class = 'Slope_value'
    R_ed = str(dem_name) + "_" + "slope"
    DEM_instance_creator(ontology, R_ed, output_file_name, data_class)
    return R_ed

def Detect_mountain_unit(work_space,dem_name,ontology):
    input_file = "H:/DEM/app/app_clip/watershed_clip_input.tif"
    # print("inputdata", input_file)
    output_file_name = work_space + dem_name + '_' + "pro_watershed.tif"
    resampling_type = "BILINEAR"
    out_coor_system_sr = arcpy.SpatialReference(54017)
    arcpy.management.ProjectRaster(input_file, output_file_name, (out_coor_system_sr), resampling_type, "", "", "", "", "")
    final_output_file_name=work_space + dem_name + '_' + "mountain_unit.shp"
    arcpy.conversion.RasterToPolygon(output_file_name, final_output_file_name, 'SIMPLIFY', "VALUE","", "")
    print("model_Detect_mountain_unit runs successfully")
    data_class = 'Mountain_unit'
    R_ed = str(dem_name) + "_" + "mountain_unit"
    DEM_instance_creator(ontology, R_ed, final_output_file_name, data_class)
    return R_ed

def Rough_Classification_of_mountain_and_plain(input,work_space,dem_name,ontology):
    input_file = input['Slope_value']
    print("inputdata", input_file)
    output_file_name = work_space + dem_name + '_' + "slope_threshold.tif"
    output_file = (Raster(input_file) > 3)
    output_file.save(output_file_name)
    middle_output_file_name=work_space + dem_name + '_' + "focal_mountain_plain.tif"
    middle_output_file = FocalStatistics(output_file_name, NbrRectangle(5, 5, "CELL"), 'MAJORITY', 'DATA', "")
    middle_output_file.save(middle_output_file_name)
    final_output_file_name=work_space + dem_name + '_' + "rough_mountain_plain.tif"
    final_output_file = Reclassify(middle_output_file_name, "Value",
                             RemapRange([[0, 0, 1], [1, 1, 0], ["NODATA", "NODATA", "NODATA"],
                                                                              ]), 'DATA')
    final_output_file.save(final_output_file_name)
    print("model_Rough_Classification_of_mountain_and_plain runs successfully")
    data_class = 'Rough_mountain_plain'
    R_ed = str(dem_name) + "_" + "rough_mountain_plain"
    DEM_instance_creator(ontology, R_ed, final_output_file_name, data_class)
    return R_ed


def Identify_plain_within_mountains(input,work_space,dem_name,ontology):
    input_file = input['Slope_value']
    print("inputdata", input_file)
    input_file2 = input['Water_net']
    output_file_name = work_space + dem_name + '_' + "distance_accum.tif"
    output_file = DistanceAccumulation(input_file2, "", "",input_file, "", VfBinary(1, -30, 30),"", HfBinary(1, 45), "",
    "", "","", "","", "", 'PLANAR')
    output_file.save(output_file_name)
    middle_output_file_name = work_space + dem_name + '_' + "ras_distance_accum.tif"
    middle_output_file=Con(Raster(output_file_name) < 89, 1, 0)
    middle_output_file.save(middle_output_file_name)

    middle_output_file_name2 = work_space + dem_name + '_' + "ras_distance_accum2.tif"
    middle_output_file2 = Con( IsNull(middle_output_file_name) ,1,0)
    middle_output_file2.save(middle_output_file_name2)

    # middle_output_file_name3 = work_space + dem_name + '_' + "ras_distance_mosaic.tif"
    arcpy.management.Mosaic(middle_output_file_name, middle_output_file_name2, 'SUM', 'FIRST',
                                                                                  "", "", "",
                                                                                  0, 'NONE')
    # middle_output_file3.save(middle_output_file_name3)

    final_output_file_name = work_space + dem_name + '_' + "plain_within_mountains.tif"
    final_output_file = ExtractByMask(middle_output_file_name2, input_file)
    final_output_file.save(final_output_file_name)
    print("model_Identify_plain_within_mountains runs successfully")
    data_class = 'Plain_within_mountain'
    R_ed = str(dem_name) + "_" + "plain_within_mountains"
    DEM_instance_creator(ontology, R_ed, final_output_file_name, data_class)
    return R_ed



def Merge_area_of_mountain_and_plain(input,work_space,dem_name,ontology):
    input_file = input['Rough_mountain_plain']
    print("inputdata", input_file)
    input_file2 = input['Plain_within_mountain']
    output_file_name = work_space + dem_name + '_' + "merge.tif"
    output_file= Con( (Raster(input_file)+ Raster(input_file2))>0, 1,0)
    output_file.save(output_file_name)
    middle_output_file_name=work_space + dem_name + '_' + "merge_filter.tif"
    middle_output_file=MajorityFilter(output_file_name, 'EIGHT', 'MAJORITY')
    middle_output_file.save(middle_output_file_name)
    middle_output_file_name2 = work_space + dem_name + '_' + "merge_filter2.tif"
    middle_output_file2 = MajorityFilter(middle_output_file_name, 'EIGHT', 'MAJORITY')
    middle_output_file2.save(middle_output_file_name2)
    final_output_file_name=work_space + dem_name + '_' + "Merge_mountain_plain.tif"
    final_output_file=Reclassify(middle_output_file_name2, "Value", RemapRange([[0,0,1],['NODATA','NODATA','NODATA']]), 'NODATA' )
    final_output_file.save(final_output_file_name)
    print("model_Merge_area_of_mountain_and_plain runs successfully")
    data_class = 'Merge_mountain_plain'
    R_ed = str(dem_name) + "_" + "merge_mountain_plain"
    DEM_instance_creator(ontology, R_ed, final_output_file_name, data_class)
    return R_ed

def Vectorize_Merge_area_of_mountain_and_plain(input,work_space,dem_name,ontology):
    input_file = input['Merge_mountain_plain']
    print("inputdata", input_file)
    output_file_name = work_space + dem_name + '_' + "POLYGON_merge.shp"
    arcpy.conversion.RasterToPolygon(input_file, output_file_name, 'SIMPLIFY', "VALUE","", "")
    arcpy.management.AddField(output_file_name, 'parea', 'FLOAT',
                                  "", "", "",
                                  "", "", "", "")
    arcpy.management.CalculateField(output_file_name, 'parea', '!shape.area!/1000000',
                            "PYTHON3", "", "TEXT", "")
    middle_output_file_name = work_space + dem_name + '_' + "polygon_merge_filter"
    arcpy.MakeFeatureLayer_management(output_file_name, middle_output_file_name)
    final_output_file_name = work_space + dem_name + '_' + "VECTOR_Merge_mountain_plain.shp"
    arcpy.management.SelectLayerByAttribute(middle_output_file_name, 'NEW_SELECTION', '"parea" < 0.5', "NON_INVERT")
    arcpy.management.DeleteRows(middle_output_file_name)
    arcpy.management.EliminatePolygonPart(middle_output_file_name, final_output_file_name,
                                          'AREA', 0.16, 0, 'CONTAINED_ONLY')
    print("model_Vectorize_Merge_area_of_mountain_and_plain runs successfully")
    data_class = 'Vector_merge_mountain_plain'
    R_ed = str(dem_name) + "_" + "vector_merge_mountain_plain"
    DEM_instance_creator(ontology, R_ed, final_output_file_name, data_class)
    return R_ed


def Vectorize_Complete_mountain_and_plain(input,work_space,dem_name,ontology):
    # extent = arcpy.Extent(10914556.3679671, 3874892.40388475, 10982247.6636282, 3904560.62918709)
    # arcpy.env.extent = extent
    input_file1 = input['Vector_merge_mountain_plain']
    input_file2 = input['Projected_DEM']
    input_file3 = input['Valid_DEM']
    # print("inputdata", input_file)
    output_file_name = work_space + dem_name + '_' + "zonal_merge.tif"

    output_file= ZonalStatistics(input_file1, 'Id', input_file2, 'RANGE',
                                 'DATA', "CURRENT_SLICE",
                                 90, "AUTO_DETECT")
    output_file.save(output_file_name)
    output_file_name3 = dem_name + '_' + "MOSAIC_zonal_merge.tif"
    arcpy.management.MosaicToNewRaster([output_file_name, input_file3], work_space, output_file_name3,
                                       "", '8_BIT_UNSIGNED', "", 1,
                                       'LAST', 'FIRST')
    output_file_name2 = work_space + dem_name + '_' + "zonal_merge_RE_CLA.tif"
    output_file2=Reclassify((work_space+output_file_name3), 'VALUE', RemapRange([[30,10000,1],['NODATA','NODATA',0]]), 'NODATA')
    output_file2.save(output_file_name2)
    final_output_file_name=work_space + dem_name + '_' + "complete_mountain_and_plain.shp"
    arcpy.conversion.RasterToPolygon((output_file_name2), final_output_file_name, 'SIMPLIFY', 'VALUE',"", "")
    print("model_Vectorize_Complete_mountain_and_plain runs successfully")
    data_class = 'Vector_complete_mountain_plain'
    R_ed = str(dem_name) + "_" + "complete_mountain_and_plain"
    DEM_instance_creator(ontology, R_ed, final_output_file_name, data_class)
    return R_ed




# #input of models
# def INPUT(i):
#     pattern = re.compile(r'[^.]+$')
#     type_in1 = re.search(pattern, str(l_ndividual[i].has_Input[0]))
#     type_input1 = str(type_in1.group())
#     return type_input1
#
# #output of models
# def OUTPUT(o):
#     pattern = re.compile(r'[^.]+$')
#     type_out1 = re.search(pattern, str(l_ndividual[o].has_Output[0]))
#     type_output1 = str(type_out1.group())
#     return type_output1
#
#
#
#
#
#
#
#
# #model_SLOPE
# def SLOPE_VALUE(input_data,n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     method = str(l_ndividual[n].method[0])
#     output_measurement = str(l_ndividual[n].output_measurement[0])
#     z_factor = l_ndividual[n].z_factor[0]
#     input_file = raw_data_space + type_input + ".tif"
#     outSlope = Slope(str(input_file), output_measurement, z_factor, method)
#     outSlope.save(work_space + type_output + ".tif")
#     return print("model_SLOPE runs successfully")
#
#
# #step1_model1
# # SLOPE(2)
#
#
#
#
#
# def PROJECT_RASTER_3(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     out_coor_system = str(l_ndividual[n].output_coordinate_system[0])
#     resampling_type = str(l_ndividual[n].resampling_technique[0])
#     print(out_coor_system)
#     print(resampling_type)
#     input_file = raw_data_space + type_input + ".tif"
#     output_file=work_space + type_output + ".tif"
#     out_coor_system_sr=arcpy.SpatialReference(54017)
#     arcpy.management.ProjectRaster(input_file, output_file, (out_coor_system_sr), resampling_type, "", "", "", "", "")
#     return print("model_PROJECT_RASTER_3 runs successfully")
#
#
#
#
# # arcpy.management.ProjectRaster(in_raster, out_raster, out_coor_system, {resampling_type}, {cell_size}, {geographic_transform}, {Registration_Point}, {in_coor_system}, {vertical})
#
# def ADD_FIELD(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     input_file = work_space + type_input + ".shp"
#     field_name = str(l_ndividual[n].field_name[0])
#     field_type = str(l_ndividual[n].field_type[0])
#     arcpy.management.AddField(input_file, field_name, field_type,
#                               "", "", "",
#                               "", "", "", "")
#     return print("model_ADD_FIELD runs successfully")
#
#
#
#
#
#
# def RASTER_CALCULATOR_1(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     expression = str(l_ndividual[n].map_algebra_expressions[0])
#     threshold_slope = (l_ndividual[n].threshold_slope[0])
#     print(expression)
#     print(threshold_slope)
#     input_file = work_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=Raster(input_file)>threshold_slope
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_1 runs successfully")
#
# def RASTER_CALCULATOR_2(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     threshold_ZhenAcc = (l_ndividual[n].threshold_ZhenAcc[0])
#     input_file = raw_data_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=SetNull( (Raster(input_file) <  threshold_ZhenAcc) ,1)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_2 runs successfully")
#
# def RASTER_CALCULATOR_3(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     threshold_deep = (l_ndividual[n].threshold_deep[0])
#     input_file = work_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= Con(Raster(input_file)< threshold_deep ,1,0)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_3 runs successfully")
#
# def RASTER_CALCULATOR_4(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=  Con( IsNull(input_file) ,1,0)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_4 runs successfully")
#
# def RASTER_CALCULATOR_5(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = raw_data_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= Raster(input_file) > 14000
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_5 runs successfully")
#
# def RASTER_CALCULATOR_6(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_in_2 = re.search(pattern, str(l_ndividual[n].has_Input[1]))
#     type_input_2 = str(type_in_2.group())
#     print(type_input_2)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = work_space + type_input_1 + ".tif"
#     input_file_2 = work_space + type_input_2 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= Con( (Raster(input_file_1)+ Raster(input_file_2))>0, 1,0)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_6 runs successfully")
#
#
# def RASTER_CALCULATOR_7(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = raw_data_space + type_input_1 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=  Con(Raster(input_file_1)>-1000,1,0)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_7 runs successfully")
#
#
#
# def RASTER_CALCULATOR_8(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = raw_data_space + type_input_1 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=  (Raster(input_file_1)> -1000)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_8 runs successfully")
#
#
# def RASTER_CALCULATOR_9(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_in_2 = re.search(pattern, str(l_ndividual[n].has_Input_cost_raster[0]))
#     type_input_2 = str(type_in_2.group())
#     print(type_input_2)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = work_space + type_input_1 + ".tif"
#     input_file_2 = work_space + type_input_2 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=Con( IsNull(Raster(input_file_1)) & Raster(input_file_2)==1, 1, 0)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_9 runs successfully")
#
#
# def RASTER_CALCULATOR_10(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_in_2 = re.search(pattern, str(l_ndividual[n].has_Input_cost_raster[0]))
#     type_input_2 = str(type_in_2.group())
#     print(type_input_2)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = work_space + type_input_1 + ".tif"
#     input_file_2 = work_space + type_input_2 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=Raster(input_file_1) * (Raster(input_file_2) + 1)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_10 runs successfully")
#
#
# def RASTER_CALCULATOR_11(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = work_space + type_input_1 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= SetNull(Raster(input_file_1)==1,0)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_11 runs successfully")
#
# def RASTER_CALCULATOR_12(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_in_2 = re.search(pattern, str(l_ndividual[n].has_Input_cost_raster[0]))
#     type_input_2 = str(type_in_2.group())
#     print(type_input_2)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = raw_data_space + type_input_1 + ".tif"
#     input_file_2 = work_space + type_input_2 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= Raster(input_file_1) - Raster(input_file_2)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_12 runs successfully")
#
# def RASTER_CALCULATOR_13(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_in_2 = re.search(pattern, str(l_ndividual[n].has_Input[1]))
#     type_input_2 = str(type_in_2.group())
#     print(type_input_2)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = work_space + type_input_1 + ".tif"
#     input_file_2 = work_space + type_input_2 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= Raster(input_file_1) + Raster(input_file_2)
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_13 runs successfully")
#
#
# def RASTER_CALCULATOR_14(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in_1 = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input_1 = str(type_in_1.group())
#     print(type_input_1)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file_1 = work_space + type_input_1 + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=  Raster(input_file_1) + 100
#     output_file.save(output_file_name)
#     return print("model_RASTER_CALCULATOR_14 runs successfully")
#
#
#
#
# def MOSAIC(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     type_in_Target_raster = re.search(pattern, str(l_ndividual[n].has_Target_raster[0]))
#     type_in_Target_raster_input = str(type_in_Target_raster.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     matching_method = (l_ndividual[n].matching_method[0])
#     colormap = (l_ndividual[n].colormap[0])
#     mosaic_type = (l_ndividual[n].mosaic_type[0])
#     input_file = work_space + type_input + ".tif"
#     input_file_Target = work_space + type_in_Target_raster_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=arcpy.management.Mosaic(input_file, input_file_Target, mosaic_type, colormap,
#                                         "", "", "",
#                                         0, matching_method)
#     # output_file.save(output_file_name)
#     return print("model_MOSAIC runs successfully")
#
# def EXTRACT_BY_MASK(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     type_in_mask_raster = re.search(pattern, str(l_ndividual[n].has_Input_mask_data[0]))
#     type_in_mask_raster_input = str(type_in_mask_raster.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     input_file_mask = work_space + type_in_mask_raster_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=ExtractByMask(input_file, input_file_mask,"","")
#     output_file.save(output_file_name)
#     return print("model_EXTRACT_BY_MASK runs successfully")
#
#
# def ERASE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_in_Erase_raster = re.search(pattern, str(l_ndividual[n].has_Erase_feature[0]))
#     type_in_Erase_raster_input = str(type_in_Erase_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     input_file_Erase = work_space + type_in_Erase_raster_input + ".shp"
#     output_file_name=work_space + type_output + ".shp"
#     arcpy.analysis.Erase(input_file, input_file_Erase, output_file_name, "")
#     return print("model_ERASE runs successfully")
#
#
# def MAJORITY_FILTER(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     majority_definition = str(l_ndividual[n].majority_definition[0])
#     number_neighbors = str(l_ndividual[n].number_neighbors[0])
#     output_file=MajorityFilter(input_file, number_neighbors, majority_definition)
#     output_file.save(output_file_name)
#     return print("model_MAJORITY_FILTER runs successfully")
#
#
# def STREAM_LINK(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_in_flow_direction_raster = re.search(pattern, str(l_ndividual[n].has_Input_flow_direction_raster[0]))
#     type_in_flow_direction_raster_input = str(type_in_flow_direction_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     input_file_flow_direction = raw_data_space + type_in_flow_direction_raster_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= StreamLink(input_file, input_file_flow_direction)
#     output_file.save(output_file_name)
#     return print("model_STREAM_LINK runs successfully")
#
# def SELECT_LAYER_BY_ATTRIBUTE_ELIMINATE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     type_final_out = re.search(pattern, str(l_ndividual[n].has_Final_Output[0]))
#     type_final_output= str(type_final_out.group())
#     print(type_final_output)
#     input_file = work_space + type_input + ".shp"
#     output_file_name = work_space + type_output
#     selection_type=str(l_ndividual[n].selection_type[0])
#     selection = str(l_ndividual[n].selection[0])
#     outFeatureClass = work_space + type_final_output + ".shp"
#     arcpy.MakeFeatureLayer_management(input_file, output_file_name)
#     arcpy.management.SelectLayerByAttribute(output_file_name, selection_type, '"mu_area" < 0.16', "NON_INVERT")
#     arcpy.Eliminate_management(output_file_name, outFeatureClass, selection,"")
#     return print("model_SELECT_LAYER_BY_ATTRIBUTE runs successfully")
#
#
# def SELECT_LAYER_BY_ATTRIBUTE_DELETE_ROW_ELIMINATE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     type_final_out = re.search(pattern, str(l_ndividual[n].has_Final_Output[0]))
#     type_final_output= str(type_final_out.group())
#     print(type_final_output)
#     input_file = work_space + type_input + ".shp"
#     output_file_name = work_space + type_output
#     selection_type=str(l_ndividual[n].selection_type[0])
#     condition = str(l_ndividual[n].condition[0])
#     part_option = str(l_ndividual[n].part_option[0])
#     outFeatureClass = work_space + type_final_output + ".shp"
#     arcpy.MakeFeatureLayer_management(input_file, output_file_name)
#     arcpy.management.SelectLayerByAttribute(output_file_name, selection_type, '"parea" < 0.5', "NON_INVERT")
#     arcpy.management.DeleteRows(output_file_name)
#     arcpy.management.EliminatePolygonPart(output_file_name, outFeatureClass,
#                                           condition, 0.16, 0, part_option)
#     return print("model_SELECT_LAYER_BY_ATTRIBUTE_DELETE_ROW_ELIMINATE runs successfully")
#
#
#
#
#
# def SELECT_LAYER_BY_ATTRIBUTE_LOCATION_ELIMINATE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     type_Select = re.search(pattern, str(l_ndividual[n].has_Select_feature[0]))
#     type_Select_output = str(type_Select.group())
#     type_Update = re.search(pattern, str(l_ndividual[n].has_Update_feature[0]))
#     type_Update_output = str(type_Update.group())
#     type_final_out = re.search(pattern, str(l_ndividual[n].has_Final_Output[0]))
#     type_final_output= str(type_final_out.group())
#     print(type_final_output)
#     input_file = work_space + type_input + ".shp"
#     output_file_name = work_space + type_output
#     output_update = work_space + type_Update_output
#     selection_type=str(l_ndividual[n].selection_type[0])
#     selection=str(l_ndividual[n].selection[0])
#     invert_spatial_relationship = str(l_ndividual[n].invert_spatial_relationship[0])
#     overlap_type = str(l_ndividual[n].overlap_type[0])
#     outSelect = work_space + type_Select_output + ".shp"
#     outFeatureClass = work_space + type_final_output + ".shp"
#     arcpy.MakeFeatureLayer_management(input_file, output_file_name)
#     arcpy.management.SelectLayerByAttribute(output_file_name, selection_type, '"gridcode" = 1', "NON_INVERT")
#     arcpy.MakeFeatureLayer_management(outSelect, output_update)
#     arcpy.management.SelectLayerByLocation(output_update, overlap_type, output_file_name, "",
#                                            selection_type, invert_spatial_relationship)
#     arcpy.management.Eliminate(output_update, outFeatureClass, selection, "", "")
#     return print("model_SELECT_LAYER_BY_ATTRIBUTE_LOCATION_ELIMINATE runs successfully")
#
#
#
#
#
# def CALCULATE_FIELD(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     field=str(l_ndividual[n].field[0])
#     expression_type = str(l_ndividual[n].expression_type[0])
#     expression=str(l_ndividual[n].expression[0])
#     arcpy.management.CalculateField(input_file, field, expression,
#                                     expression_type, "", "TEXT", "")
#     return print("model_CALCULATE_FIELD runs successfully")
#
#
# def WATERSHED(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_pour_point = re.search(pattern, str(l_ndividual[n].has_Input_pour_point_data[0]))
#     type_input_pour_point = str(type_pour_point.group())
#     print(type_input_pour_point)
#     type_in_flow_direction_raster = re.search(pattern, str(l_ndividual[n].has_Input_flow_direction_raster[0]))
#     type_in_flow_direction_raster_input = str(type_in_flow_direction_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     pour_point_field = str(l_ndividual[n].pour_point_field[0])
#     input_file = work_space + type_input_pour_point + ".tif"
#     input_file_flow_direction = raw_data_space + type_in_flow_direction_raster_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file= Watershed(input_file_flow_direction, input_file, pour_point_field)
#     output_file.save(output_file_name)
#     return print("model_WATERSHED runs successfully")
#
#
# def UPDATE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_in_Update_raster = re.search(pattern, str(l_ndividual[n].has_Update_feature[0]))
#     type_in_Update_raster_input = str(type_in_Update_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     input_file_Update = work_space + type_in_Update_raster_input + ".shp"
#     output_file_name=work_space + type_output + ".shp"
#     keep_borders=str(l_ndividual[n].keep_borders[0])
#     arcpy.analysis.Update(input_file, input_file_Update, output_file_name, keep_borders, "")
#     return print("model_UPDATE runs successfully")
#
#
#
#
# def RASTER_DOMAIN(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     out_geometry_type = (l_ndividual[n].out_geometry_type[0])
#     input_file = work_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".shp"
#     arcpy.ddd.RasterDomain(input_file, output_file_name, out_geometry_type)
#     return print("model_RASTER_DOMAIN runs successfully")
#
# def RASTER_DOMAIN_2(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     out_geometry_type = (l_ndividual[n].out_geometry_type[0])
#     input_file = raw_data_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".shp"
#     arcpy.ddd.RasterDomain(input_file, output_file_name, out_geometry_type)
#     return print("model_RASTER_DOMAIN_2 runs successfully")
#
#
#
# def RASTER_TO_POLYLINE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     background_value = (l_ndividual[n].background_value[0])
#     minimum_dangle_length = (l_ndividual[n].minimum_dangle_length[0])
#     simplify_polylines = (l_ndividual[n].simplify_polylines[0])
#     input_file = work_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".shp"
#     arcpy.conversion.RasterToPolyline(input_file, output_file_name,background_value, minimum_dangle_length,
#                                       simplify_polylines,"")
#     return print("model_RASTER_TO_POLYLINE runs successfully")
#
# def test(a,b):
#     c=a+b
#     print(c)
#
# def RASTER_TO_POLYGON(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     raster_field = (l_ndividual[n].field[0])
#     simplify = (l_ndividual[n].simplify[0])
#     input_file = work_space + type_input + ".tif"
#     output_file_name=work_space + type_output + ".shp"
#     arcpy.conversion.RasterToPolygon(input_file, output_file_name, simplify, raster_field,
#                                      "", "")
#     return print("model_RASTER_TO_POLYGON runs successfully")
#
# def FOCAL_STATISTICS_1(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     output_file_name = work_space + type_output + ".tif"
#     height = (l_ndividual[n].height[0])
#     width = (l_ndividual[n].width[0])
#     units = (l_ndividual[n].units[0])
#     neighbor = (l_ndividual[n].neighborhood[0])
#     ignore = (l_ndividual[n].ignore_nodata[0])
#     statistics = (l_ndividual[n].statistics_type[0])
#     output_file=FocalStatistics(input_file, NbrRectangle(width, height, units), statistics, ignore, "")
#     output_file.save(output_file_name)
#     return print("model_FOCAL_STATISTICS_1 runs successfully")
#
# def DISTANCE_ACCUMULATION(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     type_in_cost_raster = re.search(pattern, str(l_ndividual[n].has_Input_cost_raster[0]))
#     type_in_cost_raster_input = str(type_in_cost_raster.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     distance_method = (l_ndividual[n].distance_method[0])
#     input_file = work_space + type_input + ".shp"
#     input_file_cost = work_space + type_in_cost_raster_input + ".tif"
#     output_file_name=work_space + type_output + ".tif"
#     output_file=DistanceAccumulation(input_file, "", "",
#                                      input_file_cost, "", VfBinary(1, -30, 30),
#                                      "", HfBinary(1, 45), "",
#                                      "", "",
#                                      "", "",
#                                      "", "", distance_method)
#     output_file.save(output_file_name)
#     return print("model_DISTANCE_ACCUMULATION runs successfully")
#
# def CALCULATE_GEOMETRY_ATTRIBUTES(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     area_unit=str(l_ndividual[n].area_unit[0])
#     arcpy.management.CalculateGeometryAttributes(input_file, [["mu_area", "AREA"]], "", area_unit, "", "SAME_AS_INPUT")
#     return print("model_CALCULATE_GEOMETRY_ATTRIBUTES runs successfully")
#
# def ELIMINATE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".lyrx"
#     output_file_name=work_space + type_output + ".shp"
#     selection = str(l_ndividual[n].selection[0])
#     arcpy.management.Eliminate(input_file, output_file_name, selection, "", "")
#     return print("model_ELIMINATE runs successfully")
#
#
# def RECLASSIFY_1(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     output_file_name = work_space + type_output + ".tif"
#     start1 = (l_ndividual[n].start1[0])
#     start2 = (l_ndividual[n].start2[0])
#     start3 = (l_ndividual[n].start3[0])
#     end1 = (l_ndividual[n].end1[0])
#     end2 = (l_ndividual[n].end2[0])
#     end3 = (l_ndividual[n].end3[0])
#     new1 = (l_ndividual[n].new1[0])
#     new2 = (l_ndividual[n].new2[0])
#     new3 = (l_ndividual[n].new3[0])
#     missing_values = (l_ndividual[n].missing_values[0])
#     reclass_field = (l_ndividual[n].reclass_field[0])
#     output_file=Reclassify(input_file, reclass_field, RemapRange([[start1,end1,new1],[start2,end2,new2],[start3,end3,new3],
#                                      ]), missing_values)
#     output_file.save(output_file_name)
#     return print("model_FOCAL_RECLASSIFY_1 runs successfully")
#
# def RECLASSIFY_2(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     output_file_name = work_space + type_output + ".tif"
#     start1 = (l_ndividual[n].start1[0])
#     start2 = (l_ndividual[n].start2[0])
#     end1 = (l_ndividual[n].end1[0])
#     end2 = (l_ndividual[n].end2[0])
#     new1 = (l_ndividual[n].new1[0])
#     new2 = (l_ndividual[n].new2[0])
#     missing_values = (l_ndividual[n].missing_values[0])
#     reclass_field = (l_ndividual[n].reclass_field[0])
#     output_file=Reclassify(input_file, reclass_field, RemapRange([[start1,end1,new1],[start2,end2,new2]]), missing_values)
#     output_file.save(output_file_name)
#     return print("model_FOCAL_RECLASSIFY_2 runs successfully")
#
#
# def RECLASSIFY_4(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = raw_data_space + type_input + ".tif"
#     output_file_name = work_space + type_output + ".tif"
#     start1 = (l_ndividual[n].start1[0])
#     start2 = (l_ndividual[n].start2[0])
#     start3 = (l_ndividual[n].start3[0])
#     start4 = (l_ndividual[n].start4[0])
#     start5 = (l_ndividual[n].start5[0])
#     end1 = (l_ndividual[n].end1[0])
#     end2 = (l_ndividual[n].end2[0])
#     end3 = (l_ndividual[n].end3[0])
#     end4 = (l_ndividual[n].end4[0])
#     end5 = (l_ndividual[n].end5[0])
#     new1 = (l_ndividual[n].new1[0])
#     new2 = (l_ndividual[n].new2[0])
#     new3 = (l_ndividual[n].new3[0])
#     new4 = (l_ndividual[n].new4[0])
#     new5 = (l_ndividual[n].new5[0])
#     missing_values = (l_ndividual[n].missing_values[0])
#     reclass_field = (l_ndividual[n].reclass_field[0])
#     output_file=Reclassify(input_file, reclass_field, RemapRange([[start1,end1,new1],[start2,end2,new2],[start3,end3,new3],[start4,end4,new4],[start5,end5,new5]]), missing_values)
#     output_file.save(output_file_name)
#     return print("model_FOCAL_RECLASSIFY_4 runs successfully")
#
# def RECLASSIFY_6(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     output_file_name = work_space + type_output + ".tif"
#     start1 = (l_ndividual[n].start1[0])
#     start2 = (l_ndividual[n].start2[0])
#     start3 = (l_ndividual[n].start3[0])
#     start4 = (l_ndividual[n].start4[0])
#     start5 = (l_ndividual[n].start5[0])
#     start6 = (l_ndividual[n].start6[0])
#     end1 = (l_ndividual[n].end1[0])
#     end2 = (l_ndividual[n].end2[0])
#     end3 = (l_ndividual[n].end3[0])
#     end4 = (l_ndividual[n].end4[0])
#     end5 = (l_ndividual[n].end5[0])
#     end6 = (l_ndividual[n].end6[0])
#     new1 = (l_ndividual[n].new1[0])
#     new2 = (l_ndividual[n].new2[0])
#     new3 = (l_ndividual[n].new3[0])
#     new4 = (l_ndividual[n].new4[0])
#     new5 = (l_ndividual[n].new5[0])
#     new6 = (l_ndividual[n].new6[0])
#     missing_values = (l_ndividual[n].missing_values[0])
#     reclass_field = (l_ndividual[n].reclass_field[0])
#     output_file=Reclassify(input_file, reclass_field, RemapRange([[start1,end1,new1],[start2,end2,new2],[start3,end3,new3],[start4,end4,new4],[start5,end5,new5],[start6,end6,new6]]), missing_values)
#     output_file.save(output_file_name)
#     return print("model_FOCAL_RECLASSIFY_6 runs successfully")
#
# def ZONAL_STATISTICS_1(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_has_Input = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_has_Input.group())
#     print(type_input)
#     type_Input_value_raster = re.search(pattern, str(l_ndividual[n].has_Input_value_raster[0]))
#     type_Input_value_raster_input = str(type_Input_value_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     type_Extent = re.search(pattern, str(l_ndividual[n].has_Extent[0]))
#     type_Extent_output = str(type_Extent.group())
#     print(type_output)
#     ignore_nodata = str(l_ndividual[n].ignore_nodata[0])
#     statistics_type = str(l_ndividual[n].statistics_type[0])
#     zone_field = str(l_ndividual[n].zone_field[0])
#     input_file = work_space + type_input + ".shp"
#     input_file_value_raster = raw_data_space + type_Input_value_raster_input + ".tif"
#     output_file_name = work_space + type_output + ".tif"
#     extent=work_space + type_Extent_output + ".tif"
#     arcpy.env.extent=extent
#     output_file= ZonalStatistics(input_file, zone_field, input_file_value_raster, statistics_type,
#                                  ignore_nodata, "CURRENT_SLICE",
#                                  90, "AUTO_DETECT",
#                                  "ARITHMETIC", 360)
#     output_file.save(output_file_name)
#     return print("model_ZONAL_STATISTICS_1 runs successfully")
#
#
#
# def ZONAL_STATISTICS_2(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_has_Input = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_has_Input.group())
#     print(type_input)
#     type_Input_value_raster = re.search(pattern, str(l_ndividual[n].has_Input_value_raster[0]))
#     type_Input_value_raster_input = str(type_Input_value_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     ignore_nodata = str(l_ndividual[n].ignore_nodata[0])
#     statistics_type = str(l_ndividual[n].statistics_type[0])
#     zone_field = str(l_ndividual[n].zone_field[0])
#     input_file = work_space + type_input + ".tif"
#     input_file_value_raster = raw_data_space + type_Input_value_raster_input + ".tif"
#     output_file_name = work_space + type_output + ".tif"
#     output_file= ZonalStatistics(input_file, zone_field, input_file_value_raster, statistics_type,
#                                  ignore_nodata, "CURRENT_SLICE",
#                                  90, "AUTO_DETECT",
#                                  "ARITHMETIC", 360)
#     output_file.save(output_file_name)
#     return print("model_ZONAL_STATISTICS_2 runs successfully")
#
#
#
# def MOSAIC_TO_NEW_RASTER(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_has_Input = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_has_Input.group())
#     print(type_input)
#     type_Input_value_raster = re.search(pattern, str(l_ndividual[n].has_Input[1]))
#     type_Input_value_raster_input = str(type_Input_value_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     mosaic_colormap_mode = str(l_ndividual[n].mosaic_colormap_mode[0])
#     mosaic_method = str(l_ndividual[n].mosaic_method[0])
#     number_of_bands = l_ndividual[n].number_of_bands[0]
#     pixel_type = str(l_ndividual[n].pixel_type[0])
#     input_file = work_space + type_input + ".tif"
#     input_file_value_raster = work_space + type_Input_value_raster_input + ".tif"
#     output_file_name = type_output + ".tif"
#     arcpy.management.MosaicToNewRaster([input_file,input_file_value_raster], work_space, output_file_name,
#                                        "", pixel_type, "", number_of_bands,
#                                        mosaic_method, mosaic_colormap_mode)
#     return print("model_MOSAIC_TO_NEW_RASTER runs successfully")
#
# def CALCULATE_VALUE(n):
#     id = l_ndividual[n].id[0]
#     fid = int(id) + 107
#     return fid
#
# def SELECT(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = raw_data_space + type_input + ".shp"
#     output_file_name = work_space + type_output + ".shp"
#     # value=CALCULATE_VALUE(m)
#     arcpy.analysis.Select(input_file, output_file_name, '"FID" =459' )
#     return print("model_SELECT runs successfully")
#
# def FEATURE_TO_RASTER(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     type_cell = re.search(pattern, str(l_ndividual[n].cell_size[0]))
#     type_cell_output = str(type_cell.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     output_file_name = work_space + type_output + ".tif"
#     cell_size=raw_data_space + type_cell_output + ".tif"
#     field = str(l_ndividual[n].field[0])
#     arcpy.conversion.FeatureToRaster(input_file, field, output_file_name, cell_size)
#     return print("model_FEATURE_TO_RASTER runs successfully")
#
#
#
# def PAIRWISE_CLIP(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_in_Clip_raster = re.search(pattern, str(l_ndividual[n].has_Clip_Feature[0]))
#     type_in_Clip_raster_input = str(type_in_Clip_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     input_file_Clip = work_space + type_in_Clip_raster_input + ".shp"
#     output_file_name=work_space + type_output + ".shp"
#     arcpy.analysis.PairwiseClip(input_file, input_file_Clip, output_file_name, "")
#     return print("model_PAIRWISE_CLIP runs successfully")
#
#
# def MULTIPART_TO_SINGLEPART(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     output_file_name = work_space + type_output + ".shp"
#     arcpy.management.MultipartToSinglepart(input_file, output_file_name)
#     return print("model_MULTIPART_TO_SINGLEPART runs successfully")
#
# def PAIRWISE_ERASE(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     type_in_Erase_raster = re.search(pattern, str(l_ndividual[n].has_Erase_feature[0]))
#     type_in_Erase_raster_input = str(type_in_Erase_raster.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".shp"
#     input_file_Erase = work_space + type_in_Erase_raster_input + ".shp"
#     output_file_name=work_space + type_output + ".shp"
#     arcpy.analysis.PairwiseErase(input_file, input_file_Erase, output_file_name, "")
#     return print("model_PAIRWISE_ERASE runs successfully")
#
#
# def CLIP_RASTER(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_in_Clip_raster = re.search(pattern, str(l_ndividual[n].rectangle[0]))
#     type_in_Clip_raster_input = str(type_in_Clip_raster.group())
#     type_out = re.search(pattern, str(l_ndividual[n].has_Output[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = work_space + type_input + ".tif"
#     input_file_Clip = work_space + type_in_Clip_raster_input + ".shp"
#     output_file_name=work_space + type_output + ".tif"
#     clipping_geometry=str(l_ndividual[n].clipping_geometry[0])
#     maintain_clipping_extent = str(l_ndividual[n].maintain_clipping_extent[0])
#     nodata_value = str(l_ndividual[n].nodata_value[0])
#     arcpy.management.Clip(input_file, "",output_file_name, input_file_Clip,
#                           nodata_value, clipping_geometry, maintain_clipping_extent)
#     return print("model_CLIP_RASTER runs successfully")
#
#
# def APPLY_SYSBOLOGY_FROM_LAYER(n):
#     print(l_ndividual[n])
#     pattern = re.compile(r'[^.]+$')
#     type_in = re.search(pattern, str(l_ndividual[n].has_Input[0]))
#     type_input = str(type_in.group())
#     print(type_input)
#     type_out = re.search(pattern, str(l_ndividual[n].has_input_symbology_layer[0]))
#     type_output = str(type_out.group())
#     print(type_output)
#     input_file = "H:/geomorphology/following_NNU/geomorphic_following/TEST/" + type_input + ".shp"
#     output_file_name=raw_data_space + type_output + ".lyrx"
#     arcpy.management.ApplySymbologyFromLayer(input_file, output_file_name,
#                                              "", "")
#     return print("model_APPLY_SYSBOLOGY_FROM_LAYER runs successfully")


#order of the operations
# #1
# # SLOPE(148)
# # PROJECT_RASTER(89)
# # RASTER_CALCULATOR_1(98)
# # FOCAL_STATISTICS_1(58)
# # RECLASSIFY_1(133)

#
# #2
# # SLOPE(149)
# # RASTER_CALCULATOR_2(111)
# # RASTER_TO_POLYLINE(132)
# # DISTANCE_ACCUMULATION(24)
# # RASTER_CALCULATOR_3(114)
# # RASTER_CALCULATOR_4(115)
# # MOSAIC(66)
# # EXTRACT_BY_MASK(47)

#
# #3
# # RASTER_CALCULATOR_5(115)
# # STREAM_LINK(149)
# # WATERSHED(154)
# # PROJECT_RASTER(91)
# # RASTER_TO_POLYGON(125)
# # PROJECT_RASTER_3(94)
# # RASTER_DOMAIN(123)
# # ERASE(40)
# # UPDATE(152)
# # CALCULATE_GEOMETRY_ATTRIBUTES(14)
# # SELECT_LAYER_BY_ATTRIBUTE_ELIMINATE(140)
# # SELECT_LAYER_BY_ATTRIBUTE_ELIMINATE(141)

#
# #4
# # RASTER_CALCULATOR_6(117)
# # MAJORITY_FILTER(60)
# # MAJORITY_FILTER(63)
# # RECLASSIFY_2(132)
# # RASTER_TO_POLYGON(125)
# # ADD_FIELD(1)
# # CALCULATE_FIELD(6)
# # SELECT_LAYER_BY_ATTRIBUTE_DELETE_ROW_ELIMINATE(141)
# # ZONAL_STATISTICS_1(153)
# # RECLASSIFY_2(132)
# # RASTER_CALCULATOR_7(117)
# # MOSAIC_TO_NEW_RASTER(66)
# # RASTER_TO_POLYGON(126)

#
# #5
# # SELECT(137)
# # RASTER_DOMAIN_2(122)
# # PAIRWISE_CLIP(80)
# # ERASE(42)
# # UPDATE(151)
# # MULTIPART_TO_SINGLEPART(77)
# # RECLASSIFY_4(134)
# # RASTER_CALCULATOR_8(118)
# # SELECT_LAYER_BY_ATTRIBUTE_LOCATION_ELIMINATE(142)
# # FEATURE_TO_RASTER(55)
# # FEATURE_TO_RASTER(52)
# # RASTER_CALCULATOR_9(120)
# # RASTER_CALCULATOR_10(96)
# # RECLASSIFY_1(135)
# # MOSAIC_TO_NEW_RASTER(70)
# # RASTER_CALCULATOR_11(100)
# # EXTRACT_BY_MASK(48)
# # ZONAL_STATISTICS_2(154)
# # RASTER_CALCULATOR_12(101)
# # RECLASSIFY_6(136)
# # RASTER_CALCULATOR_13(105)
# # RASTER_TO_POLYGON(127)
# # PAIRWISE_ERASE(83)
# # CLIP_RASTER(17)
# # RASTER_CALCULATOR_14(107)
# # MOSAIC_TO_NEW_RASTER(73)
# # RASTER_TO_POLYGON(128)
# # CALCULATE_FIELD(8)
# # CALCULATE_FIELD(11)
# APPLY_SYSBOLOGY_FROM_LAYER(3)




# 67 MODELS IN TOTAL














































# sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
# d = l_class[0].__class__
# result = str(d)
# print(d)
# print(result)

# from rdflib import Graph
#
# g = Graph()
# g.parse("E:/UNNC/note/semester3/mathML.owl")

# rule1=l_rules[0]
# print(rule1)
# bosy=rule1.body[0].arguments
# head=rule1.head[0].class_predicate
# print(bosy)
# print(head)

# mountain_A = l_class[30]("mountain_A")
# mountain_A.topographic_relief = [int(15)]
# mountain_A.altitude=[int(500)]
# # print(type(mountain_2.topographic_relief[0]))
# a.save("G:/geomorphology/ontology/Reasoning_geomorphic_classification_system.owl")
# a=get_ontology("G:/geomorphology/ontology/Reasoning_geomorphic_classification_system.owl").load()
# sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
# d = mountain_A.__class__
# result = str(d)
# print(d)
# print(result)



# for i in range(1,4):
#     mountain_A = l_class[30]("mountain_"+str(i))
#     mountain_A.topographic_relief = [int(i)]
# # print(type(mountain_2.topographic_relief[0]))
#     a.save("G:/geomorphology/ontology/Reasoning_geomorphic_classification_system.owl")
#     a=get_ontology("G:/geomorphology/ontology/Reasoning_geomorphic_classification_system.owl").load()
#
#     sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
#     d = mountain_A.__class__
#     result = str(d)
#     print(d)
#     print(result)
# print(l_ndividual)

# pattern = re.compile(r'[^.]+$')
# type = re.search(pattern, result)
# type_out = str(type.group())
# print(type_out)


# writer = csv.writer(targetFile)
# writer.writerow(type_out)
# print("successful")





# data= pandas.read_excel('G:/geomorphology/ontology/test_data_relief.xlsx',engine='openpyxl',sheet_name="Sheet1")
# df = data.where(data.notnull(), None)
# # concent_dic = con.Context.database("H:/competition/victory.xlsx")
# final=[]
# for m in range(3,10):
#     relief=df.iat[m,5]
#     pixel = df.iat[m,0]
#     altitude_p=df.iat[m,2]
#     # d=es.Version.empty_list_or_not(reference,reference_re)
#     # pattern = re.compile(r'(\d{4})', re.S)
#     # reference_year = re.findall(pattern, str(d))
#     mountain_A = l_class[30]("mountain_"+str(m))
#     mountain_A.topographic_relief = [int(relief)]#have to define the data type as the int
#     mountain_A.altitude = [int(altitude_p)]
#     a.save("G:/geomorphology/ontology/Reasoning_geomorphic_classification_system.owl")
#     a = get_ontology("G:/geomorphology/ontology/Reasoning_geomorphic_classification_system.owl").load()
#     sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
#     d = mountain_A.__class__
#     result = str(d)
#     #print(d)
#     #print(result)
#     pattern = re.compile(r'[^.]+$')
#     type = re.search(pattern, result)
#     type_out=str(type.group())
#     final_out=re.findall('.*?(?=>)',type_out)
#     final.append(final_out[0])
#     print("successful")
# print(final)
# def out_result(self):
#     number= Counter(self)
#     out=number.most_common()
#     if out[0][1]==out[1][1]:
#         return out[0][0],out[1][0]
#     if out[0][1]> out[1][1]:
#         return out[0][0]
# print(out_result(final))
#