# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
# from PyQt5.QtCore import Qt
#
# class DisplayPage(QWidget):
#     def __init__(self, result):
#         super().__init__()
#         self.result = result
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Display')
#
#         display_layout = QVBoxLayout()
#         self.display_label = QLineEdit()
#         self.display_label.setReadOnly(True)
#         self.display_label.setAlignment(Qt.AlignCenter)
#         self.display_label.setText(self.result)
#         display_layout.addWidget(self.display_label)
#
#         self.setLayout(display_layout)
#
#     def display_result(self, result):
#         self.result = result
#         self.display_label.setText(self.result)
#
#
# def main():
#     app = QApplication(sys.argv)
#     display_page = DisplayPage("No result passed")
#     display_page.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
import arcpy
# Set the workspace environment
arcpy.env.workspace = 'H:/DEM/app/'

# Define input shapefile and output raster paths
input_shapefile = "H:/DEM/app/test1.shp"
output_raster = "H:/DEM/app/test11.tif"  # Raster format

# Define output PNG or JPG file path
output_image = "H:/DEM/app/test11.png"  # Change the extension to .jpg for JPG format

# Convert shapefile to raster
arcpy.conversion.PolygonToRaster(input_shapefile, 'gridcode', output_raster, '', '', '', '')

# Convert raster to PNG or JPG
arcpy.management.CopyRaster(output_raster, output_image, format="PNG")  # Change "PNG" to "JPEG" for JPG format
