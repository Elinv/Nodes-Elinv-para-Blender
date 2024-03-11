import bpy, math, sys, os
import numpy as np
import shutil
from bpy_extras.io_utils import ImportHelper 
from bpy.props import StringProperty
from . wEOhjFXji import *
from . YsWDOZZWR import * 
from .. FxpYr.BzxqBdDNT import *
from .. FxpYr.ZpPZWMihh import *
class YyKPTIWYl(bpy.types.Operator):
    bl_idname = "nodeshader.crea_material_img_textura"
    bl_label = "Crear texture image"
    def execute(self, context):
        WOPiYrfBj(self, context, SDuMrIojV, self, context)
        return {"FINISHED"}
class rWeVDmfia(bpy.types.Operator, ImportHelper):
    bl_idname = "nodeshader.nodosproplinks"
    bl_label = "Grabar nodos y links"
    filename_ext = ".json"
    filter_glob: StringProperty(
        default='*.json',
        options={'HIDDEN'}
    ) # type: ignore
    def execute(self, context):
        if WOPiYrfBj(self, context, "", self, context, True) == 0:
            obj = context.active_object
            namemat=bpy.context.active_object.active_material.name
            mat=bpy.data.materials[namemat]
            expPropDic.clear()
            expLinksDic.clear()
            nodosDic.clear()
            nodosDic[len(nodosDic)] = {"Material":namemat}
            nodes=mat.node_tree.nodes
            if len(nodes) > 0:
                links=mat.node_tree.links
                for n in links:
                    expLinksDic[len(expLinksDic)] = {
                        "from_node.name": n.from_node.name, #n.from_node.name,
                        "from_socket.identifier": n.from_socket.identifier,
                        "to_node.bl_idname": n.to_node.name,
                        "to_socket.identifier": n.to_socket.identifier 
                    }
                for n in nodes:            
                    nodosDic[len(nodosDic)] = {
                        "name":n.name, 
                        "type":n.type, 
                        "__class__.__name__":n.__class__.__name__,
                        "location[0]":n.location[0],
                        "location[1]":n.location[1]
                    }            
                vAfqSCzgy(n, nodes)            
                nodeElv = {
                "links" : expLinksDic,
                "prop" : expPropDic,
                "nodos" : nodosDic
                }         
                filename = ""
                direct = os.path.abspath(self.filepath)
                if os.path.isdir(direct):
                    fileName = os.path.join(direct) + "/" + obj.name + self.filename_ext
                else:
                    fileName = os.path.join(direct) + self.filename_ext
                fileNamesp = fileName.replace(" ", "_")
                fileNamesp = fileName.replace(".json.json", ".json")
                indImg = mIPFOzIWc("ShaderNodeTexImage", nodeElv)
                if indImg:
                    for imgs in indImg:
                        try:
                            imgOrigen = nodeElv.get('prop')[imgs]["image.filepath"]
                            arcExtImg = imgOrigen.split("/")[-1]
                            shutil.copy(imgOrigen, fileNamesp+"_"+arcExtImg)
                            nodeElv['prop'][imgs]["image.filepath"] = fileNamesp+"_"+arcExtImg
                        except:
                            self.report({'INFO'}, "Error en Image Texture con File Path: ")
                bpy.context.window_manager.clipboard = str(nodeElv)
                fileNamesp = fileNamesp.replace(" ", "_")
                PxJkenhfk(fileNamesp, nodeElv)
                bpy.ops.screen.screenshot_area(filepath=fileNamesp + '.png')
        return {"FINISHED"}
class pKRjuakBD(bpy.types.Operator, ImportHelper):
    bl_idname = "nodeshader.getjsonnode"
    bl_label = "Cargar y crear materiales"
    filename_ext = ".json" 
    filter_glob: bpy.props.StringProperty(
        default='*.json;*.png;',
        options={'HIDDEN'}
    )    # type: ignore
    def execute(self, context):
        if WOPiYrfBj(self, context, "", self, context, True) == 0:
            obj = context.active_object
            filename = os.path.abspath(self.filepath)
            filename = filename.replace(".json.png", ".json")
            if os.path.isfile(filename):
                self.report({'INFO'}, "El archivo se ha cargado")
            else:            
                self.report({'INFO'}, "No ha seleccionado archivo")
            KJwyRCDcC(filename)
        return {"FINISHED"}
