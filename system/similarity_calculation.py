from shapely.geometry import Polygon
import shapely.wkt
from rdflib import Graph,Literal
import rdflib
import pyproj
import os
import re
from rdflib.namespace import XSD
# dg = datagraph.DataGraph()
# dem="H:/geomorphology/material_from_NNU/Model and Data/preData/noprj_dem.tif"
# v = "H:/geomorphology/following_NNU/geomorphic_following/PROJECT/water_net.shp"
# folder = ""
#
# instance_name='DEM1'
# datatype_class='DEM'
#
#
# data_graph_R = dg.raster_graph(datagraph.DATA, instance_name, dem, datatype_class )
# data_graph_V = dg.vector_graph(datagraph.DATA, 'DEM1', v, 'DEM' )
#
# raster_file_name = 'H:/SHACL/shacl-params/shacl-params/data/raster_graph_1.ttl'
raster_file_name = 'H:/SHACL/shacl-params/shacl-params/data/raster_graph_1_3000.ttl'
# dg.graph_2_file( data_graph_R, raster_file_name)
# dg.graph_2_file( data_graph_V, 'G:/SHACL/shacl-params/shacl-params/data/vector_graph_1.ttl')
#
# # Create a Graph object
#

# Parse the RDF file
def parse_graph(file_path,instance_name):
    h = Graph()
    # file_path = 'G:/SHACL/shacl-params/shacl-params/data/raster_graph_1.ttl'
    h.parse(file_path, format="turtle")

    data_name = h.value(  subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name) ),  # DEM1 is same as the instance name
                                  predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#dataName'),
                                  any=False  )

    data_suffix = h.value(  subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name) ),  # DEM1 is same as the instance name
                                  predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#suffix'),
                                  any=False  )
    data_linearUnit = h.value(  subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name) ),  # DEM1 is same as the instance name
                                  predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#linearUnit'),
                                  any=False  )
    data_projected = h.value(  subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name) ),  # DEM1 is same as the instance name
                                  predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#projected'),
                                  any=False  )
    # print(data_projected)


    data_spatialFeature = h.value(  subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name) ),  # DEM1 is same as the instance name
                                  predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#extent'),
                                  any=False  )

    data_geographicCoordinateSystem = h.value(  subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name) ),  # DEM1 is same as the instance name
                                  predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#geographicCoordinateSystem'),
                                  any=False  )

    data_format = h.value(subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name)),# DEM1 is same as the instance name
                predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#dataFormat'),
                any=False)

    data_datum = h.value(subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name)),# DEM1 is same as the instance name
                predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#hasCRSProj4'),
                any=False)

    data_spatialResolution = h.value(  subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name) ),  # DEM1 is same as the instance name
                                  predicate=rdflib.term.URIRef('http://www.w3.org/ns/dcat#spatialResolutionInMeters')
                                    )

    # # a=h.objects(subject=rdflib.term.URIRef('http://www.w3.org/ns/dcat#DEM1'),predicate=rdflib.term.URIRef('http://www.w3.org/ns/dcat#spatialResolutionInMeters')
    # #                                )
    # # print(a)
    # if isinstance(data_spatialResolution, Literal) and data_spatialResolution.datatype == XSD.decimal:
    #     decimal_value = data_spatialResolution.toPython()
    #     print(f"Decimal Value: {decimal_value}")
    # else:
    #    print(f"Object: {data_spatialResolution}")
    # for triple in h:
    #     print(triple)
    if data_projected is True:
        data_prosys = h.value(
            subject=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#' + str(instance_name)),
            # DEM1 is same as the instance name
            predicate=rdflib.term.URIRef('http://www.semanticweb.org/Geo_computation/data#projectedCoordinateSystem'),
            any=False)
        return data_spatialFeature,data_spatialResolution,data_format,data_datum,data_geographicCoordinateSystem,data_prosys,data_linearUnit,data_projected,data_name
    else:
        return  data_spatialFeature,data_spatialResolution,data_format,data_datum,data_geographicCoordinateSystem,1,data_linearUnit,data_projected,data_name

# raster_file_path = raster_file_name
# parse_result=parse_graph(raster_file_path,instance_name)
# suffix = parse_result[0]
# linearUnit = parse_result[1]
# projected = parse_result[2]
# geographicCoordinateSystem = parse_result[3]
# spatialFeature = parse_result[4]
# spatialResolution = parse_result[5]
# polygon = shapely.wkt.loads(spatialFeature)

# Extract the coordinates from the polygon
# coordinates = list(polygon.exterior.coords)

# Find the minimum and maximum pairs of coordinates
# min_coords = min(coordinates)
# max_coords = max(coordinates)
# area = (max_coords[0] - min_coords[0]) * (max_coords[1] - min_coords[1])
# print("Minimum Coordinates:", min_coords)
# print("Maximum Coordinates:", max_coords)
# print(area)


def similarity(input_data,expected_data,instance_name):
    a=parse_graph(input_data, instance_name)
    b=parse_graph(expected_data, instance_name)
    # region
    polygon_a = shapely.wkt.loads(a[0])
    coordinates_a = list(polygon_a.exterior.coords)
    min_coords_a = min(coordinates_a)
    max_coords_a = max(coordinates_a)
    area_a = (max_coords_a[0] - min_coords_a[0]) * (max_coords_a[1] - min_coords_a[1])
    # print(area_a)
    polygon_b = shapely.wkt.loads(b[0])
    coordinates_b = list(polygon_b.exterior.coords)
    min_coords_b = min(coordinates_b)
    max_coords_b = max(coordinates_b)
    area_b = (max_coords_b[0] - min_coords_b[0]) * (max_coords_b[1] - min_coords_b[1])
    # print(area_b)
    area = (area_b/area_a)*0.7306

    #resolution
    if a[1]==b[1]:
        resolution=1*0.1884
    elif a[1]<b[1]:
        resolution=0.5*0.1884
    elif a[1]>b[1]:
        resolution=0.25*0.1884

    #data_type

    type=1*0.5

    #data_format
    if a[2]==b[2]:
        format=1*0.5
    elif a[2] in []:
        format=0.85*0.5
    elif a[2]in[]:
        format=0.65*0.5
    else:
        format=0.35*0.5

    #coordinate_system
    crs_a = pyproj.CRS(a[3])
    datum_a = crs_a.datum
    crs_b = pyproj.CRS(b[3])
    datum_b = crs_b.datum

    #projection_system
    if a[4] is False:
        prosys_a=1
    # else

    if a[4]==b[4]:
        coor=1*0.081
    if datum_a==datum_b and a[5] != b[5]:
        coor=0.5*0.081
    if datum_a != datum_b:
        coor = 0.25 * 0.081
    #temporal
    time=1*0.1759
    #content
    content=1*0.4762

    total=(area+coor+resolution)*0.2888+time+content+(type+format)*0.0591
    return total,area,coor,resolution,time,content,type,format


def process_folder(folder_path,update):
    similarity_scores = {}

    # Read all files in the folder
    files = os.listdir(folder_path)
    # print(files)
    # Iterate over each file
    for file in files:
        if file.endswith(".ttl"):  # Process only TIFF files
            # print(file)

            # Extract filename without extension
            filename = os.path.splitext(file)[0]
            file_path = os.path.join(folder_path, file)
            # print(filename)
            # print(file_path)
            # Use regex to extract string part (xxxx) from filename
            name = filename

                # Calculate similarity score for the file
            score = similarity(file_path,update,"DEM1")
            # print(score)
            # Store filename and corresponding score in the dictionary
            similarity_scores[filename] = score[0]

    # Sort similarity_scores by values in descending order
    sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    # Get the top three highest scores
    top_three = sorted_scores[:3]

    # Create a dictionary with the top three highest scores labeled as 1, 2, and 3
    top_three_dict = {i: {'name': name, 'score': score} for i, (name, score) in enumerate(top_three, start=1)}
    print(top_three_dict)
    return top_three_dict

# process_folder("H:/DEM/data_graph/")

# instance_name="DEM1"
# input1='H:/DEM/data_graph/SRTM_90.ttl'
# input2='H:/DEM/data_graph/GMTED_250.ttl'
# input3='H:/DEM/data_graph/TanDEM_90.ttl'
# input4='H:/DEM/data_graph/FABDEM_30.ttl'
# expected='H:/DEM/expected_DEM/expected_DEM1.ttl'
#
# a= similarity(input1,expected,instance_name)
# print(a[0])
# b= similarity(input2,expected,instance_name)
# print(b[0])
# c= similarity(input3,expected,instance_name)
# print(c[0])
# d= similarity(input4,expected,instance_name)
# print(d[0])




