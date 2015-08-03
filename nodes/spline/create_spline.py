import bpy
from bpy.props import *
from ... events import propertyChanged
from ... base_types.node import AnimationNode
from ... data_structures.splines.poly_spline import PolySpline
from ... data_structures.splines.bezier_spline import BezierSpline

splineTypeItems = [
    ("BEZIER", "Bezier", "Each control point has two handles"),
    ("POLY", "Poly", "Linear interpolation between the spline points")]

class CreateSpline(bpy.types.Node, AnimationNode):
    bl_idname = "mn_CreateSpline"
    bl_label = "Create Spline"

    inputNames = { "Points" : "points",
                   "Cyclic" : "cyclic" }

    outputNames = { "Spline" : "spline" }

    splineType = EnumProperty(name = "Spline Type", items = splineTypeItems, update = propertyChanged)

    def create(self):
        self.inputs.new("mn_VectorListSocket", "Points")
        self.inputs.new("mn_BooleanSocket", "Cyclic").value = False
        self.outputs.new("mn_SplineSocket", "Spline")

    def draw_buttons(self, context, layout):
        layout.prop(self, "splineType", text = "")

    def execute(self, points, cyclic):
        if self.splineType == "BEZIER": spline = BezierSpline()
        if self.splineType == "POLY": spline = PolySpline()
        spline.appendPoints(points)
        spline.isCyclic = cyclic
        return spline
