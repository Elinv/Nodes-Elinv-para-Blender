import bpy, time
import mathutils
import json 
import numpy as np
import bmesh
def mIPFOzIWc(snClassName, jsonDicLoad):
    indArr = []
    for x in jsonDicLoad.keys():
        for y in jsonDicLoad.get(x).keys():
            for k in jsonDicLoad.get(x)[y].keys():
                if x == 'prop':         #Recuperar en Propiedades
                    if k == '__class__.__name__':       #Por el class name
                        if jsonDicLoad.get(x)[y][k] == snClassName:
                            indArr.append(y)
    return indArr    #Regresa la clave
def xhNzZQzEI(jsonDicLoad, ind, key):
    res = jsonDicLoad.get('prop')[ind][key]
    res = res.replace("(", "").replace(")", "")
    resArr = res.split(",")
    return list(map(float, resArr))
def PIvnwjQEI(n):
    for i in n.inputs:
        try:
            print(i.bl_idname, "  ", i.name, "  ", str(i.default_value))
        except:
            print (i.bl_idname, "  ",i.name, "  ")
def PxJkenhfk(filename, dict):
    outfile = open(filename, "w") 
    outfile.write(json.dumps(dict))
    outfile.close()
def KJwyRCDcC(filename):
    jsonDicLoad = {}
    with open(filename) as f:
        jsonDicLoad = json.load(f)
    aaGgRPxow(jsonDicLoad)
def aaGgRPxow(jsonDicLoad):
    area = bpy.context.area
    area.type = 'NODE_EDITOR'
    area.ui_type = 'ShaderNodeTree'
    material = None
    for x in jsonDicLoad.keys():
        for y in jsonDicLoad.get(x).keys():
            for z in jsonDicLoad.get(x)[y].keys():
                if x == 'nodos':
                    if z == 'Material':
                        matName = jsonDicLoad.get(x)[y]['Material']
                        material = bpy.data.materials.new(name=matName)
                        material.use_nodes = True
                        mater = material.node_tree
                        for node in mater.nodes:
                            mater.nodes.remove(node)
                    if z == '__class__.__name__':
                        nodeType = jsonDicLoad.get(x)[y]['__class__.__name__']
                        nodesOut = material.node_tree.nodes.new(nodeType)
                        nodesOut.name = jsonDicLoad.get(x)[y]['name']
                        nodesOut.location[0] = jsonDicLoad.get(x)[y]['location[0]']
                        nodesOut.location[1] = jsonDicLoad.get(x)[y]['location[1]']
    bpy.context.object.active_material = material
    uFCnUXmLQ(jsonDicLoad, material)
def uFCnUXmLQ(jsonDicLoad, material):
    fName = ''
    fSocket = ''
    tName = ''
    tSocket = ''
    for x in jsonDicLoad.keys():
        for y in jsonDicLoad.get(x).keys():
            for z in jsonDicLoad.get(x)[y].keys():
                if x == 'links':
                    if z == 'from_node.name':
                        fName = jsonDicLoad.get(x)[y][z]
                    if z == 'from_socket.identifier':
                        fSocket = jsonDicLoad.get(x)[y][z]
                    if z == 'to_node.bl_idname':
                        tName = jsonDicLoad.get(x)[y][z]
                    if z == 'to_socket.identifier':
                        tSocket = jsonDicLoad.get(x)[y][z]
                        mat1 = material.node_tree.nodes.get(fName)
                        mat2 = material.node_tree.nodes.get(tName)
                        material.node_tree.links.new(mat1.outputs[fSocket], mat2.inputs[tSocket])
    YfqITBGoo(jsonDicLoad)
def YfqITBGoo(jsonDicLoad):
    namemat=bpy.context.active_object.active_material.name
    mat=bpy.data.materials[namemat]
    nodes=mat.node_tree.nodes 
    for n in nodes:
        if n.type == "MAPPING":
            indJson = mIPFOzIWc("ShaderNodeMapping", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.vector_type = jsonDicLoad.get('prop')[ind]["vector_type"]
                    valor = xhNzZQzEI(jsonDicLoad, ind, "inputs['Location'].default_value")
                    n.inputs['Location'].default_value = valor
                    valor = xhNzZQzEI(jsonDicLoad, ind, "inputs['Rotation'].default_value")
                    n.inputs['Rotation'].default_value = valor
                    valor = xhNzZQzEI(jsonDicLoad, ind, "inputs['Scale'].default_value")
                    n.inputs['Scale'].default_value = valor
        if n.type == "TEX_COORD":
            indJson = mIPFOzIWc("ShaderNodeTexCoord", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.name = jsonDicLoad.get('prop')[ind]["name"]
                    n.from_instancer = jsonDicLoad.get('prop')[ind]["from_instancer"]
                    objeto = jsonDicLoad.get('prop')[ind]["object"]
                    try:
                        n.object = bpy.data.objects[objeto]
                    except:
                        n.object = None
        if n.type == "OUTPUT_MATERIAL":
            indJson = mIPFOzIWc("ShaderNodeOutputMaterial", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.name = jsonDicLoad.get('prop')[ind]["name"]
                    n.is_active_output = jsonDicLoad.get('prop')[ind]["is_active_output"]
                    n.target = jsonDicLoad.get('prop')[ind]["target"]
        if n.type == "BSDF_PRINCIPLED":
            indJson = mIPFOzIWc("ShaderNodeBsdfPrincipled", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    print("")
                    n.name = jsonDicLoad.get('prop')[ind]["name"]
                    n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                    n.inputs[1].default_value = jsonDicLoad.get('prop')[ind]["inputs[1].default_value"]
                    n.inputs[2].default_value = jsonDicLoad.get('prop')[ind]["inputs[2].default_value"]
                    n.inputs[3].default_value = jsonDicLoad.get('prop')[ind]["inputs[3].default_value"]
                    n.inputs[4].default_value = jsonDicLoad.get('prop')[ind]["inputs[4].default_value"]
                    n.inputs[6].default_value = jsonDicLoad.get('prop')[ind]["inputs[6].default_value"]
                    n.subsurface_method = jsonDicLoad.get('prop')[ind]["subsurface_method"]
                    n.inputs[7].default_value = jsonDicLoad.get('prop')[ind]["inputs[7].default_value"]
                    n.inputs[8].default_value[0] = jsonDicLoad.get('prop')[ind]["inputs[8].default_value[0]"]
                    n.inputs[8].default_value[1] = jsonDicLoad.get('prop')[ind]["inputs[8].default_value[1]"]
                    n.inputs[8].default_value[2] = jsonDicLoad.get('prop')[ind]["inputs[8].default_value[2]"]
                    n.inputs[9].default_value = jsonDicLoad.get('prop')[ind]["inputs[9].default_value"]
                    n.inputs[10].default_value = jsonDicLoad.get('prop')[ind]["inputs[10].default_value"]
                    n.inputs[11].default_value = jsonDicLoad.get('prop')[ind]["inputs[11].default_value"]
                    n.distribution = jsonDicLoad.get('prop')[ind]["distribution"]
                    n.inputs[12].default_value = jsonDicLoad.get('prop')[ind]["inputs[12].default_value"]
                    n.inputs[13].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[13].default_value")
                    n.inputs[14].default_value = jsonDicLoad.get('prop')[ind]["inputs[14].default_value"]
                    n.inputs[15].default_value = jsonDicLoad.get('prop')[ind]["inputs[15].default_value"]
                    n.inputs[17].default_value = jsonDicLoad.get('prop')[ind]["inputs[17].default_value"]
                    n.inputs[18].default_value = jsonDicLoad.get('prop')[ind]["inputs[18].default_value"]
                    n.inputs[19].default_value = jsonDicLoad.get('prop')[ind]["inputs[19].default_value"]
                    n.inputs[20].default_value = jsonDicLoad.get('prop')[ind]["inputs[20].default_value"]
                    n.inputs[21].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[21].default_value")
                    n.inputs[23].default_value = jsonDicLoad.get('prop')[ind]["inputs[23].default_value"]
                    n.inputs[24].default_value = jsonDicLoad.get('prop')[ind]["inputs[24].default_value"]
                    n.inputs[25].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[25].default_value")
                    n.inputs[26].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[26].default_value")
                    n.inputs[27].default_value = jsonDicLoad.get('prop')[ind]["inputs[27].default_value"]
        if n.type == "TEX_IMAGE":
            indJson = mIPFOzIWc("ShaderNodeTexImage", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.interpolation = jsonDicLoad.get('prop')[ind]["interpolation"]
                    n.projection = jsonDicLoad.get('prop')[ind]["projection"]
                    n.projection_blend = jsonDicLoad.get('prop')[ind]["projection_blend"]
                    try:
                        n.image = bpy.data.images.load(jsonDicLoad.get('prop')[ind]["image.filepath"])
                        n.image.source = jsonDicLoad.get('prop')[ind]["image.source"]
                        n.image.colorspace_settings.name = jsonDicLoad.get('prop')[ind]["image.colorspace_settings.name"]
                        n.image.alpha_mode = jsonDicLoad.get('prop')[ind]["image.alpha_mode"]
                        n.image_user.frame_current = jsonDicLoad.get('prop')[ind]["image_user.frame_current"]
                        n.image_user.frame_duration = jsonDicLoad.get('prop')[ind]["image_user.frame_duration"]
                        n.image_user.frame_offset = jsonDicLoad.get('prop')[ind]["image_user.frame_offset"]
                        n.image_user.frame_start = jsonDicLoad.get('prop')[ind]["image_user.frame_start"]
                        n.image_user.tile = jsonDicLoad.get('prop')[ind]["image_user.tile"]
                        n.image_user.use_auto_refresh = jsonDicLoad.get('prop')[ind]["image_user.use_auto_refresh"]
                    except:
                        print("Text Image no contiene imagenes para cargar!")
        if n.type == "TEX_GRADIENT":
            indJson = mIPFOzIWc("ShaderNodeTexGradient", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.gradient_type = jsonDicLoad.get("prop")[ind]["gradient_type"]
                    n.label = str(jsonDicLoad.get('prop')[ind]["label"])
                    n.name = str(jsonDicLoad.get('prop')[ind]["name"])
        if n.type == "VALTORGB":
            indJson = mIPFOzIWc("ShaderNodeValToRGB", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):                
                    n.color_ramp.interpolation = jsonDicLoad.get("prop")[ind]["color_ramp.interpolation"]
                    n.color_ramp.color_mode = jsonDicLoad.get("prop")[ind]["color_ramp.color_mode"]
                    n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
                    countEle = jsonDicLoad.get("prop")[ind]["countElement"]
                    n.color_ramp.elements[0].position = jsonDicLoad.get("prop")[ind]["color_ramp.elements[0].position"]
                    n.color_ramp.elements[0].color = xhNzZQzEI(jsonDicLoad, ind, "color_ramp.elements[0].color")
                    n.color_ramp.elements[1].position = jsonDicLoad.get("prop")[ind]["color_ramp.elements[1].position"]
                    n.color_ramp.elements[1].color = xhNzZQzEI(jsonDicLoad, ind, "color_ramp.elements[1].color")
                    for x in range(countEle):
                        if x > 1:
                            pos = jsonDicLoad.get("prop")[ind]["color_ramp.elements[" + str(x) + "].position"]
                            el = n.color_ramp.elements.new(pos)
                            el.color = xhNzZQzEI(jsonDicLoad, ind, "color_ramp.elements[" + str(x) + "].color")
        if n.type == "BSDF_GLOSSY":
            indJson = mIPFOzIWc("ShaderNodeBsdfAnisotropic", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):                
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.distribution = jsonDicLoad.get("prop")[ind]["distribution"]
                    n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                    n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                    n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                    n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"] 
        if n.type == "LAYER_WEIGHT":
            indJson = mIPFOzIWc("ShaderNodeLayerWeight", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):                
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "FRESNEL":
            indJson = mIPFOzIWc("ShaderNodeFresnel", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):                
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "EMISSION":
            indJson = mIPFOzIWc("ShaderNodeEmission", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")  #Color
                    n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_DIFFUSE":
            indJson = mIPFOzIWc("ShaderNodeBsdfDiffuse", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):                
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")       #Color
                    n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MIX_SHADER":
            indJson = mIPFOzIWc("ShaderNodeMixShader", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):                
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BUMP":
            indJson = mIPFOzIWc("ShaderNodeBump", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.invert = jsonDicLoad.get("prop")[ind]["invert"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "GAMMA":
            indJson = mIPFOzIWc("ShaderNodeGamma", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_CHECKER":
            indJson = mIPFOzIWc("ShaderNodeTexChecker", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[2].default_value")
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MIX":
            indJson = mIPFOzIWc("ShaderNodeMix", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.data_type = jsonDicLoad.get("prop")[ind]["data_type"]
                n.blend_type = jsonDicLoad.get("prop")[ind]["blend_type"]
                n.clamp_result = jsonDicLoad.get("prop")[ind]["clamp_result"]
                n.clamp_factor = jsonDicLoad.get("prop")[ind]["clamp_factor"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[0]"]
                n.inputs[4].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[1]"]
                n.inputs[4].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[2]"]
                n.inputs[5].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[5].default_value[0]"]
                n.inputs[5].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[5].default_value[1]"]
                n.inputs[5].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[5].default_value[2]"]
                n.inputs[6].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[6].default_value")
                n.inputs[7].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[7].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "RGBTOBW":
            indJson = mIPFOzIWc("ShaderNodeRGBToBW", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_MUSGRAVE":
            indJson = mIPFOzIWc("ShaderNodeTexMusgrave", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.musgrave_dimensions = jsonDicLoad.get("prop")[ind]["musgrave_dimensions"]
                n.musgrave_type = jsonDicLoad.get("prop")[ind]["musgrave_type"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[5].default_value = jsonDicLoad.get("prop")[ind]["inputs[5].default_value"]
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.inputs[7].default_value = jsonDicLoad.get("prop")[ind]["inputs[7].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_NOISE":
            indJson = mIPFOzIWc("ShaderNodeTexNoise", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.noise_dimensions = jsonDicLoad.get("prop")[ind]["noise_dimensions"]
                n.normalize =  jsonDicLoad.get("prop")[ind]["normalize"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[5].default_value = jsonDicLoad.get("prop")[ind]["inputs[5].default_value"]
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "RGBTOBW":
            indJson = mIPFOzIWc("ShaderNodeRGBToBW", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MATH":
            indJson = mIPFOzIWc("ShaderNodeMath", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.operation = jsonDicLoad.get("prop")[ind]["operation"]
                n.use_clamp = jsonDicLoad.get("prop")[ind]["use_clamp"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_VORONOI":
            indJson = mIPFOzIWc("ShaderNodeTexVoronoi", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.voronoi_dimensions = jsonDicLoad.get("prop")[ind]["voronoi_dimensions"]
                n.feature = jsonDicLoad.get("prop")[ind]["feature"]
                n.distance = jsonDicLoad.get("prop")[ind]["distance"]
                n.normalize = jsonDicLoad.get("prop")[ind]["normalize"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[5].default_value = jsonDicLoad.get("prop")[ind]["inputs[5].default_value"]
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.inputs[7].default_value = jsonDicLoad.get("prop")[ind]["inputs[7].default_value"]
                n.inputs[8].default_value = jsonDicLoad.get("prop")[ind]["inputs[8].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DISPLACEMENT":
            indJson = mIPFOzIWc("ShaderNodeDisplacement", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.space = jsonDicLoad.get("prop")[ind]["space"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BLACKBODY":
            indJson = mIPFOzIWc("ShaderNodeBlackbody", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BRIGHTCONTRAST":
            indJson = mIPFOzIWc("ShaderNodeBrightContrast", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BACKGROUND":
            indJson = mIPFOzIWc("ShaderNodeBackground", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "AMBIENT_OCCLUSION":
            indJson = mIPFOzIWc("ShaderNodeAmbientOcclusion", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.samples = jsonDicLoad.get("prop")[ind]["samples"]
                n.inside = jsonDicLoad.get("prop")[ind]["inside"]
                n.only_local = jsonDicLoad.get("prop")[ind]["only_local"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_GLASS":
            indJson = mIPFOzIWc("ShaderNodeBsdfGlass", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.distribution = jsonDicLoad.get("prop")[ind]["distribution"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_HAIR":
            indJson = mIPFOzIWc("ShaderNodeBsdfHair", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.component = jsonDicLoad.get("prop")[ind]["component"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_HAIR_PRINCIPLED":
            indJson = mIPFOzIWc("ShaderNodeBsdfHairPrincipled", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.model = jsonDicLoad.get("prop")[ind]["model"]
                n.parametrization = jsonDicLoad.get("prop")[ind]["parametrization"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[3].default_value")
                n.inputs[4].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[0]"]
                n.inputs[4].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[1]"]
                n.inputs[4].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[2]"]
                n.inputs[5].default_value = jsonDicLoad.get("prop")[ind]["inputs[5].default_value"]
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.inputs[7].default_value = jsonDicLoad.get("prop")[ind]["inputs[7].default_value"]
                n.inputs[8].default_value = jsonDicLoad.get("prop")[ind]["inputs[8].default_value"]
                n.inputs[9].default_value = jsonDicLoad.get("prop")[ind]["inputs[9].default_value"]
                n.inputs[10].default_value = jsonDicLoad.get("prop")[ind]["inputs[10].default_value"]
                n.inputs[11].default_value = jsonDicLoad.get("prop")[ind]["inputs[11].default_value"]
                n.inputs[12].default_value = jsonDicLoad.get("prop")[ind]["inputs[12].default_value"]
                n.inputs[13].default_value = jsonDicLoad.get("prop")[ind]["inputs[13].default_value"]
                n.inputs[14].default_value = jsonDicLoad.get("prop")[ind]["inputs[14].default_value"]
                n.inputs[15].default_value = jsonDicLoad.get("prop")[ind]["inputs[15].default_value"]
                n.inputs[16].default_value = jsonDicLoad.get("prop")[ind]["inputs[16].default_value"]
                n.inputs[17].default_value = jsonDicLoad.get("prop")[ind]["inputs[17].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BEVEL":
            indJson = mIPFOzIWc("ShaderNodeBevel", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.samples = jsonDicLoad.get("prop")[ind]["samples"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "ATTRIBUTE":
            indJson = mIPFOzIWc("ShaderNodeAttribute", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.attribute_type = jsonDicLoad.get("prop")[ind]["attribute_type"]
                n.attribute_name = jsonDicLoad.get("prop")[ind]["attribute_name"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_REFRACTION":
            indJson = mIPFOzIWc("ShaderNodeBsdfRefraction", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.distribution = jsonDicLoad.get("prop")[ind]["distribution"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_SHEEN":
            indJson = mIPFOzIWc("ShaderNodeBsdfSheen", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.distribution = jsonDicLoad.get("prop")[ind]["distribution"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_TOON":
            indJson = mIPFOzIWc("ShaderNodeBsdfToon", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.component = jsonDicLoad.get("prop")[ind]["component"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_TRANSLUCENT":
            indJson = mIPFOzIWc("ShaderNodeBsdfTranslucent", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BSDF_TRANSPARENT":
            indJson = mIPFOzIWc("ShaderNodeBsdfTransparent", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "EEVEE_SPECULAR":
            indJson = mIPFOzIWc("ShaderNodeEeveeSpecular", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[3].default_value")
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.inputs[7].default_value = jsonDicLoad.get("prop")[ind]["inputs[7].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBRGB":
            indJson = mIPFOzIWc("ShaderNodeCombineRGB", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBHSV":
            indJson = mIPFOzIWc("ShaderNodeCombineHSV", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBXYZ":
            indJson = mIPFOzIWc("ShaderNodeCombineXYZ", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CLAMP":
            indJson = mIPFOzIWc("ShaderNodeClamp", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.clamp_type = jsonDicLoad.get("prop")[ind]["clamp_type"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBINE_COLOR":
            indJson = mIPFOzIWc("ShaderNodeCombineColor", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CURVE_FLOAT":
            indJson = mIPFOzIWc("ShaderNodeFloatCurve", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "HUE_SAT":
            indJson = mIPFOzIWc("ShaderNodeHueSaturation", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[4].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "INVERT":
            indJson = mIPFOzIWc("ShaderNodeInvert", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "LIGHT_FALLOFF":
            indJson = mIPFOzIWc("ShaderNodeLightFalloff", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MAP_RANGE":
            indJson = mIPFOzIWc("ShaderNodeMapRange", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.data_type = jsonDicLoad.get("prop")[ind]["data_type"]
                n.interpolation_type = jsonDicLoad.get("prop")[ind]["interpolation_type"]
                n.clamp = jsonDicLoad.get("prop")[ind]["clamp"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[5].default_value = jsonDicLoad.get("prop")[ind]["inputs[5].default_value"]
                n.inputs[7].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[7].default_value[0]"]
                n.inputs[7].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[7].default_value[1]"]
                n.inputs[7].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[7].default_value[2]"]
                n.inputs[8].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[8].default_value[0]"]
                n.inputs[8].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[8].default_value[1]"]
                n.inputs[8].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[8].default_value[2]"]
                n.inputs[9].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[9].default_value[0]"]
                n.inputs[9].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[9].default_value[1]"]
                n.inputs[9].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[9].default_value[2]"]
                n.inputs[10].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[10].default_value[0]"]
                n.inputs[10].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[10].default_value[1]"]
                n.inputs[10].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[10].default_value[2]"]
                n.inputs[11].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[11].default_value[0]"]
                n.inputs[11].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[11].default_value[1]"]
                n.inputs[11].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[11].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MIX_RGB":
            indJson = mIPFOzIWc("ShaderNodeMixRGB", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.blend_type = jsonDicLoad.get("prop")[ind]["blend_type"]
                n.use_clamp = jsonDicLoad.get("prop")[ind]["use_clamp"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[2].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "NORMAL":
            indJson = mIPFOzIWc("ShaderNodeNormal", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.outputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind,"outputs[0].default_value")
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "NORMAL_MAP":
            indJson = mIPFOzIWc("ShaderNodeNormalMap", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.space = jsonDicLoad.get("prop")[ind]["space"]
                n.uv_map = jsonDicLoad.get("prop")[ind]["uv_map"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "OUTPUT_WORLD":
            indJson = mIPFOzIWc("ShaderNodeOutputWorld", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.target = jsonDicLoad.get("prop")[ind]["target"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SCRIPT":
            indJson = mIPFOzIWc("ShaderNodeScript", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.script = jsonDicLoad.get("prop")[ind]["script"]
                n.filepath = jsonDicLoad.get("prop")[ind]["filepath"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "OUTPUT_LINESTYLE":
            indJson = mIPFOzIWc("ShaderNodeOutputLineStyle", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.blend_type = jsonDicLoad.get("prop")[ind]["blend_type"]
                n.use_clamp = jsonDicLoad.get("prop")[ind]["use_clamp"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "OUTPUT_LIGHT":
            indJson = mIPFOzIWc("ShaderNodeOutputLight", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.target = jsonDicLoad.get("prop")[ind]["target"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "OUTPUT_AOV":
            indJson = mIPFOzIWc("ShaderNodeOutputAOV", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "RGB":
            indJson = mIPFOzIWc("ShaderNodeRGB", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.outputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "outputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CURVE_RGB":
            indJson = mIPFOzIWc("ShaderNodeRGBCurve", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPARATE_COLOR":
            indJson = mIPFOzIWc("ShaderNodeSeparateColor", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPHSV":
            indJson = mIPFOzIWc("ShaderNodeSeparateHSV", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPRGB":
            indJson = mIPFOzIWc("ShaderNodeSeparateRGB", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPXYZ":
            indJson = mIPFOzIWc("ShaderNodeSeparateXYZ", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[0]"]
                n.inputs[0].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[1]"]
                n.inputs[0].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SQUEEZE":
            indJson = mIPFOzIWc("ShaderNodeSqueeze", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SUBSURFACE_SCATTERING":
            indJson = mIPFOzIWc("ShaderNodeSubsurfaceScattering", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.falloff = jsonDicLoad.get("prop")[ind]["falloff"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[0]"]
                n.inputs[2].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[1]"]
                n.inputs[2].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[2]"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TANGENT":
            indJson = mIPFOzIWc("ShaderNodeTangent", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.direction_type = jsonDicLoad.get("prop")[ind]["direction_type"]
                n.axis = jsonDicLoad.get("prop")[ind]["axis"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_WHITE_NOISE":
            indJson = mIPFOzIWc("ShaderNodeTexWhiteNoise", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.noise_dimensions = jsonDicLoad.get("prop")[ind]["noise_dimensions"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VALUE":
            indJson = mIPFOzIWc("ShaderNodeValue", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.outputs[0].default_value = jsonDicLoad.get("prop")[ind]["outputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "UVALONGSTROKE":
            indJson = mIPFOzIWc("ShaderNodeUVAlongStroke", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.use_tips = jsonDicLoad.get("prop")[ind]["use_tips"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "UVMAP":
            indJson = mIPFOzIWc("ShaderNodeUVMap", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.from_instancer = jsonDicLoad.get("prop")[ind]["from_instancer"]
                n.uv_map = jsonDicLoad.get("prop")[ind]["uv_map"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VERTEX_COLOR":
            indJson = mIPFOzIWc("ShaderNodeVertexColor", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.layer_name = jsonDicLoad.get("prop")[ind]["layer_name"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "WIREFRAME":
            indJson = mIPFOzIWc("ShaderNodeWireframe", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.use_pixel_size = jsonDicLoad.get("prop")[ind]["use_pixel_size"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "WAVELENGTH":
            indJson = mIPFOzIWc("ShaderNodeWavelength", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VOLUME_SCATTER":
            indJson = mIPFOzIWc("ShaderNodeVolumeScatter", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_MAGIC":
            indJson = mIPFOzIWc("ShaderNodeTexMagic", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.turbulence_depth = jsonDicLoad.get("prop")[ind]["turbulence_depth"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_IES":
            indJson = mIPFOzIWc("ShaderNodeTexIES", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.ies = jsonDicLoad.get("prop")[ind]["ies"]
                n.filepath = jsonDicLoad.get("prop")[ind]["filepath"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_BRICK":
            indJson = mIPFOzIWc("ShaderNodeTexBrick", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.offset = jsonDicLoad.get("prop")[ind]["offset"]
                n.offset_frequency = jsonDicLoad.get("prop")[ind]["offset_frequency"]
                n.squash = jsonDicLoad.get("prop")[ind]["squash"]
                n.squash_frequency = jsonDicLoad.get("prop")[ind]["squash_frequency"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[2].default_value")
                n.inputs[3].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[3].default_value")
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[5].default_value = jsonDicLoad.get("prop")[ind]["inputs[5].default_value"]
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.inputs[7].default_value = jsonDicLoad.get("prop")[ind]["inputs[7].default_value"]
                n.inputs[8].default_value = jsonDicLoad.get("prop")[ind]["inputs[8].default_value"]
                n.inputs[9].default_value = jsonDicLoad.get("prop")[ind]["inputs[9].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_POINTDENSITY":
            indJson = mIPFOzIWc("ShaderNodeTexPointDensity", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.point_source = jsonDicLoad.get("prop")[ind]["point_source"]
                n.space = jsonDicLoad.get("prop")[ind]["space"]
                n.radius = jsonDicLoad.get("prop")[ind]["radius"]
                n.interpolation = jsonDicLoad.get("prop")[ind]["interpolation"]
                n.resolution = jsonDicLoad.get("prop")[ind]["resolution"]
                n.particle_color_source = jsonDicLoad.get("prop")[ind]["particle_color_source"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
                objeto = jsonDicLoad.get('prop')[ind]["object"]
                try:
                    n.object = bpy.data.objects[objeto]
                except:
                    n.object = None
        if n.type == "TEX_SKY":
            indJson = mIPFOzIWc("ShaderNodeTexSky", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.sky_type = jsonDicLoad.get("prop")[ind]["sky_type"]
                n.sun_disc = jsonDicLoad.get("prop")[ind]["sun_disc"]
                n.sun_size = jsonDicLoad.get("prop")[ind]["sun_size"]
                n.sun_intensity = jsonDicLoad.get("prop")[ind]["sun_intensity"]
                n.sun_elevation = jsonDicLoad.get("prop")[ind]["sun_elevation"]
                n.sun_rotation = jsonDicLoad.get("prop")[ind]["sun_rotation"]
                n.altitude = jsonDicLoad.get("prop")[ind]["altitude"]
                n.air_density = jsonDicLoad.get("prop")[ind]["air_density"]
                n.dust_density = jsonDicLoad.get("prop")[ind]["dust_density"]
                n.ozone_density = jsonDicLoad.get("prop")[ind]["ozone_density"]                
                n.sun_direction = xhNzZQzEI(jsonDicLoad, ind,"sun_direction")
                n.turbidity = jsonDicLoad.get("prop")[ind]["turbidity"]
                n.ground_albedo = jsonDicLoad.get("prop")[ind]["ground_albedo"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_WAVE":
            indJson = mIPFOzIWc("ShaderNodeTexWave", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.wave_type = jsonDicLoad.get("prop")[ind]["wave_type"]
                n.bands_direction = jsonDicLoad.get("prop")[ind]["bands_direction"]
                n.wave_profile = jsonDicLoad.get("prop")[ind]["wave_profile"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[5].default_value = jsonDicLoad.get("prop")[ind]["inputs[5].default_value"]
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEX_ENVIRONMENT":
            indJson = mIPFOzIWc("ShaderNodeTexEnvironment", jsonDicLoad)
            try:
                for ind in indJson:
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.interpolation = jsonDicLoad.get("prop")[ind]["interpolation"]
                    n.projection = jsonDicLoad.get("prop")[ind]["projection"]
                    n.source = jsonDicLoad.get("prop")[ind]["source"]
                    n.colorspace_settings.name = jsonDicLoad.get("prop")[ind]["colorspace_settings.name"]
                    n.alpha_mode = jsonDicLoad.get("prop")[ind]["alpha_mode"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
            except:
                for ind in indJson:
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
                    n.interpolation = jsonDicLoad.get("prop")[ind]["interpolation"]
                    n.projection = jsonDicLoad.get("prop")[ind]["projection"]                    
        if n.type == "CURVE_VEC":
            indJson = mIPFOzIWc("ShaderNodeVectorCurve", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "PRINCIPLED_VOLUME":
            indJson = mIPFOzIWc("ShaderNodeVolumePrincipled", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.inputs[5].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[5].default_value")
                n.inputs[6].default_value = jsonDicLoad.get("prop")[ind]["inputs[6].default_value"]
                n.inputs[7].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[7].default_value")
                n.inputs[8].default_value = jsonDicLoad.get("prop")[ind]["inputs[8].default_value"]
                n.inputs[9].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[9].default_value")
                n.inputs[10].default_value = jsonDicLoad.get("prop")[ind]["inputs[10].default_value"]
                n.inputs[11].default_value = jsonDicLoad.get("prop")[ind]["inputs[11].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VECTOR_DISPLACEMENT":
            indJson = mIPFOzIWc("ShaderNodeVectorDisplacement", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.space = jsonDicLoad.get("prop")[ind]["space"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VECT_MATH":
            indJson = mIPFOzIWc("ShaderNodeVectorMath", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.operation = jsonDicLoad.get("prop")[ind]["operation"]
                n.inputs[0].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[0]"]
                n.inputs[0].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[1]"]
                n.inputs[0].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[2]"]
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.inputs[2].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[0]"]
                n.inputs[2].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[1]"]
                n.inputs[2].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[2]"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VECTOR_ROTATE":
            indJson = mIPFOzIWc("ShaderNodeVectorRotate", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.rotation_type = jsonDicLoad.get("prop")[ind]["rotation_type"]
                n.invert = jsonDicLoad.get("prop")[ind]["invert"]
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.inputs[2].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[0]"]
                n.inputs[2].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[1]"]
                n.inputs[2].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[2]"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[0]"]
                n.inputs[4].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[1]"]
                n.inputs[4].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VECT_TRANSFORM":
            indJson = mIPFOzIWc("ShaderNodeVectorTransform", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.vector_type = jsonDicLoad.get("prop")[ind]["vector_type"]
                n.convert_from = jsonDicLoad.get("prop")[ind]["convert_from"]
                n.convert_to = jsonDicLoad.get("prop")[ind]["convert_to"]
                n.inputs[0].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[0]"]
                n.inputs[0].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[1]"]
                n.inputs[0].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
    time.sleep(1)
    bpy.ops.node.view_all()
