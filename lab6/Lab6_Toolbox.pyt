# Lab 6: Map generation toolbox     Lauren Medlin   02/21/2023
import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]


class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "graduatedcolor"
        self.description = "Create a gradauted colored map based on attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        #Orginial project name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name",
            name="aprxInputName",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        #Layer Classification for Color Map
        param1= arcpy.Parameter(
            displayName="Layer to Classify",
            name="LayertoClassify",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )
        #Output Folder Location
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder",
            direction="Input"
        )
        #Output Project Name
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #Define Progressor Variables
        readTime = 3 #the time for users to read the progress
        start = 0 #beginning position of the progressor
        max = 100 #end position
        step = 33 #the progress interval to move the progressor

        #Setup Progressor 
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) #pause the excution for 3 seconds
        #Add Message to Results Pane
        arcpy.AddMessage("Validating Project File...")

        #Project File
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)

        #Grabbing the first instance of a map from the .aprx
        campus = project.listMaps('Map')[0]

        #Increment Progressor
        arcpy.SetProgressorPosition(start + step) #now is 33% completed
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        #Looping Through Map Layers
        for layer in campus.listLayers():
            #Check if the layer is a Feature Layer
            if layer.isFeatureLayer:
                #Copy the Layer's Symbology
                symbology = layer.symbology
                #Making sure symbology has render attribute
                if hasattr(symbology, 'renderer'):
                    #Check Layer Name
                    if layer.name == parameters[1].valueAsText: #check if the layer name match the input layer

                        #Increment Progressor
                        arcpy.SetProgressorPosition(start + step*2) #Now is 66% completed
                        arcpy.SetProgressorLabel("Calculating and Classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and Classifying...")

                        #Update the Copy's Renderer to "Graduated Colors Renderer"
                        symbology.updateRenderer("GraduatedColorsRenderer")

                        #Tell arcpy which field we want to base our choropleth off of
                        symbology.renderer.classificationField = "Shape_Area"

                        #Number of Classes for Map
                        symbology.renderer.breakCount = 5

                        #Color Ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]

                        #Setting Layer symbology equal to the copy's
                        layer.symbology = symbology

                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print("No Layers Found")
        #Increment Progressor
        arcpy.SetProgressorPosition(start + step*3) #Now is 99% completed
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")

        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + "aprx")
        #Param 2 is the folder location and param 3 is the name of the new project
        return
