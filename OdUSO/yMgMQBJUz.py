import bpy, math, sys, os
import numpy as np
import shutil
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty
from . biuPbxnCZ import *
from .. FxpYr.EcCHQbAqN import *
from .. FxpYr.AtisvxdBx import *
from . YsWDOZZWR import *
class OaFuIyuGC(bpy.types.Operator):
    bl_idname = "nodecomp.render_imagen_compositing"
    bl_label = "Render Imagen Compositing"
    def execute(self, context):
        WOPiYrfBj(self, context, CaYVUUudH, self, context, False)
        return {"FINISHED"}
class NztDXFeao(bpy.types.Operator, ImportHelper):
    bl_idname = "nodecomp.nodosproplinks"
    bl_label = "Grabar nodos y links"
    filename_ext = ".json"
    filter_glob: StringProperty(default="*.json", options={"HIDDEN"})  # type: ignore
    def execute(self, context):
        if WOPiYrfBj(self, context, "", self, context, True) == 0:
            obj = context.active_object
            expPropDic.clear()
            expLinksDic.clear()
            nodosDic.clear()
            bpy.context.scene.use_nodes = True
            tree = bpy.context.scene.node_tree
            if len(tree.nodes) > 0:
                links = tree.links
                for n in links:
                    expLinksDic[len(expLinksDic)] = {
                        "from_node.name": n.from_node.name,  # n.from_node.name,
                        "from_socket.identifier": n.from_socket.identifier,
                        "to_node.bl_idname": n.to_node.name,
                        "to_socket.identifier": n.to_socket.identifier,
                    }
                for n in tree.nodes:
                    nodosDic[len(nodosDic)] = {
                        "name": n.name,
                        "type": n.type,
                        "__class__.__name__": n.__class__.__name__,
                        "location[0]": n.location[0],
                        "location[1]": n.location[1],
                    }
                AtisvxdBx(n, tree.nodes)
                nodeElv = {"links": expLinksDic, "prop": expPropDic, "nodos": nodosDic}
                filename = ""
                direct = os.path.abspath(self.filepath)
                if os.path.isdir(direct):
                    fileName = os.path.join(direct) + "/" + obj.name + self.filename_ext
                else:
                    fileName = os.path.join(direct) + self.filename_ext
                fileNamesp = fileName.replace(" ", "_")
                fileNamesp = fileName.replace(".json.json", ".json")
                bpy.context.window_manager.clipboard = str(nodeElv)
                fileNamesp = fileNamesp.replace(" ", "_")
                xIGfkzulD(fileNamesp, nodeElv)
                bpy.ops.screen.screenshot_area(filepath=fileNamesp + ".png")
        return {"FINISHED"}
class PeIsItoye(bpy.types.Operator, ImportHelper):
    bl_idname = "nodecomp.getjsonnode"
    bl_label = "Cargar y crear Nodos"
    filename_ext = ".json"
    filter_glob: bpy.props.StringProperty(
        default="*.json;*.png;", options={"HIDDEN"}
    )  # type: ignore
    def execute(self, context):
        if WOPiYrfBj(self, context, "", self, context, True) == 0:
            obj = context.active_object
            filename = os.path.abspath(self.filepath)
            filename = filename.replace(".json.png", ".json")
            if os.path.isfile(filename):
                self.report({"INFO"}, "El archivo se ha cargado")
            else:
                self.report({"INFO"}, "No ha seleccionado archivo")
            oGZfnSlXV(filename)
        return {"FINISHED"}
