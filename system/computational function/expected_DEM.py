import re

# Function to replace placeholders with real values
def replace_placeholder(ttl_content, placeholder, value):
    return ttl_content.replace(placeholder, value)

# Function to replace extent coordinates
def replace_extent_coordinates(extent, coordinates):
    pattern = re.compile(r'\b(a|b|c|d)\b')
    extent_replaced = re.sub(pattern, lambda match: str(coordinates[match.group(0)]), extent)
    return extent_replaced
def coordinates1(top1,top2):
    # a_lat = top1  # Example coordinates for vertex 'a'
    # b_lat = top2  # Example coordinates for vertex 'b'
    top_left_coordinates1 = top1.split(",")[1].split()
    latitude1 = top_left_coordinates1[0]
    longitude1 = top_left_coordinates1[1]
    top_left_coordinates2 = top2.split(",")[1].split()
    latitude2 = top_left_coordinates2[0]
    longitude2 = top_left_coordinates2[1]

    return latitude1, longitude1,latitude2, longitude2
    # return a_lat,b_lat
def coordinates2(bottom1,bottom2):
    c_lat = bottom1  # Example coordinates for vertex 'c'
    d_lat = bottom2  # Example coordinates for vertex 'd'
    return c_lat,d_lat
# Define the numeric value
spatial_resolution_value = '10'

# Read the TTL file
with open('//replace with your ttl file', 'r') as file:
    ttl_content = file.read()

# Replace the extent coordinates placeholders


# Replace the extent coordinates placeholders
extent_match = re.search(r'data:extent "(.*?)"\^\^geo:wktLiteral', ttl_content)
if extent_match:
    extent = extent_match.group(1)
    # a_lat, b_lat = coordinates1(coordinates1[0],coordinates1[1])
    # c_lat, d_lat = coordinates2(coordinates2[0], coordinates2[1])
    extent_coordinates = {
        'a': 10,
        'b': 20,
        'c': 30,
        'd': 40
    }
 # Replace placeholders with real coordinates
    new_extent = replace_extent_coordinates(extent, extent_coordinates)

    # Replace the old extent with the new one in the TTL content
    new_ttl_content = ttl_content.replace(extent, new_extent)
# Update the spatial resolution placeholder 'e' with the true numeric value
    ttl_content = replace_placeholder(ttl_content, 'dcat:spatialResolutionInMeters e', f'dcat:spatialResolutionInMeters {spatial_resolution_value}')

# Write the modified TTL content back to the file
with open('//replace with your ttl file', 'w') as file:
    file.write(new_ttl_content)
