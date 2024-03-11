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
def xIGfkzulD(filename, dict):
    outfile = open(filename, "w") 
    outfile.write(json.dumps(dict))
    outfile.close()
def oGZfnSlXV(filename):
    jsonDicLoad = {}
    with open(filename) as f:
        jsonDicLoad = json.load(f)
    gwrgNbPts(jsonDicLoad)
def gwrgNbPts(jsonDicLoad):
    area = bpy.context.area
    area.type = 'NODE_EDITOR'
    area.ui_type = 'CompositorNodeTree'
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    for node in tree.nodes:
        tree.nodes.remove(node)
    for x in jsonDicLoad.keys():
        for y in jsonDicLoad.get(x).keys():
            for z in jsonDicLoad.get(x)[y].keys():
                if x == 'nodos':
                    if z == '__class__.__name__':
                        nodeType = jsonDicLoad.get(x)[y]['__class__.__name__']
                        nodesOut = tree.nodes.new(nodeType)
                        nodesOut.name = jsonDicLoad.get(x)[y]['name']
                        nodesOut.location[0] = jsonDicLoad.get(x)[y]['location[0]']
                        nodesOut.location[1] = jsonDicLoad.get(x)[y]['location[1]']
    mYvybjdsV(jsonDicLoad, tree, nodesOut)
def mYvybjdsV(jsonDicLoad, tree, nodesOut):
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
                        nodo1 = tree.nodes.get(fName)
                        nodo2 = tree.nodes.get(tName)
                        tree.links.new(nodo1.outputs[fSocket], nodo2.inputs[tSocket])
    hFwVcYkxJ(jsonDicLoad, tree, nodesOut)
def hFwVcYkxJ(jsonDicLoad, tree, nodesOut):
    for n in tree.nodes:
        if n.type == "VIEWER":
            indJson = mIPFOzIWc("CompositorNodeViewer", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.name = jsonDicLoad.get('prop')[ind]["name"]
                    n.use_alpha = jsonDicLoad.get('prop')[ind]["use_alpha"]
                    n.inputs[1].default_value = jsonDicLoad.get('prop')[ind]["inputs[1].default_value"]
        if n.type == "COMPOSITE":
            indJson = mIPFOzIWc("CompositorNodeComposite", jsonDicLoad)
            for ind in indJson:
                if (jsonDicLoad.get("prop")[ind]["name"] == n.name):
                    n.name = jsonDicLoad.get('prop')[ind]["name"]
                    n.use_alpha = jsonDicLoad.get('prop')[ind]["use_alpha"]
                    n.inputs[1].default_value = jsonDicLoad.get('prop')[ind]["inputs[1].default_value"]
        if n.type == "R_LAYERS":
            indJson = mIPFOzIWc("CompositorNodeRLayers", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
                n.layer = jsonDicLoad.get("prop")[ind]["layer"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "IMAGE":
            indJson = mIPFOzIWc("CompositorNodeImage", jsonDicLoad)
            try:
                for ind in indJson:
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.source = jsonDicLoad.get("prop")[ind]["source"]
                    n.colorspace_settings.name = jsonDicLoad.get("prop")[ind]["colorspace_settings.name"]
                    n.alpha_mode = jsonDicLoad.get("prop")[ind]["alpha_mode"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]
            except:
                for ind in indJson:
                    n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                    n.name = jsonDicLoad.get("prop")[ind]["name"]                
        if n.type == "ALPHAOVER":
            indJson = mIPFOzIWc("CompositorNodeAlphaOver", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.use_premultiply = jsonDicLoad.get("prop")[ind]["use_premultiply"]
                n.premul = jsonDicLoad.get("prop")[ind]["premul"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]                
        if n.type == "SCALE":
            indJson = mIPFOzIWc("CompositorNodeScale", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.space = jsonDicLoad.get("prop")[ind]["space"]
                n.frame_method = jsonDicLoad.get("prop")[ind]["frame_method"]
                n.offset_y = jsonDicLoad.get("prop")[ind]["offset_y"]
                n.offset_x = jsonDicLoad.get("prop")[ind]["offset_x"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBRGBA":
            indJson = mIPFOzIWc("CompositorNodeCombRGBA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBYCCA":
            indJson = mIPFOzIWc("CompositorNodeCombYCCA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBYUVA":
            indJson = mIPFOzIWc("CompositorNodeCombYUVA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBINE_COLOR":
            indJson = mIPFOzIWc("CompositorNodeCombineColor", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.ycc_mode = jsonDicLoad.get("prop")[ind]["ycc_mode"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBHSVA":
            indJson = mIPFOzIWc("CompositorNodeCombHSVA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COMBINE_XYZ":
            indJson = mIPFOzIWc("CompositorNodeCombineXYZ", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VIEWSWITCH":
            indJson = mIPFOzIWc("CompositorNodeSwitchView", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MATH":
            indJson = mIPFOzIWc("CompositorNodeMath", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.operation = jsonDicLoad.get("prop")[ind]["operation"]
                n.use_clamp = jsonDicLoad.get("prop")[ind]["use_clamp"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "ID_MASK":
            indJson = mIPFOzIWc("CompositorNodeIDMask", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.index = jsonDicLoad.get("prop")[ind]["index"]
                n.use_antialiasing = jsonDicLoad.get("prop")[ind]["use_antialiasing"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "LEVELS":
            indJson = mIPFOzIWc("CompositorNodeLevels", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.channel = jsonDicLoad.get("prop")[ind]["channel"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "NORMALIZE":
            indJson = mIPFOzIWc("CompositorNodeNormalize", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VALUE":
            indJson = mIPFOzIWc("CompositorNodeValue", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.outputs[0].default_value = jsonDicLoad.get("prop")[ind]["outputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPARATE_XYZ":
            indJson = mIPFOzIWc("CompositorNodeSeparateXYZ", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[0]"]
                n.inputs[0].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[1]"]
                n.inputs[0].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "OUTPUT_FILE":
            indJson = mIPFOzIWc("CompositorNodeOutputFile", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.base_path = jsonDicLoad.get("prop")[ind]["base_path"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MASK":
            indJson = mIPFOzIWc("CompositorNodeMask", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.size_source = jsonDicLoad.get("prop")[ind]["size_source"]
                n.use_motion_blur = jsonDicLoad.get("prop")[ind]["use_motion_blur"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DILATEERODE":
            indJson = mIPFOzIWc("CompositorNodeDilateErode", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.distance = jsonDicLoad.get("prop")[ind]["distance"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MAP_RANGE":
            indJson = mIPFOzIWc("CompositorNodeMapRange", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.use_clamp = jsonDicLoad.get("prop")[ind]["use_clamp"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MAP_VALUE":
            indJson = mIPFOzIWc("CompositorNodeMapValue", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.offset[0] = jsonDicLoad.get("prop")[ind]["offset[0]"]
                n.size[0] = jsonDicLoad.get("prop")[ind]["size[0]"]
                n.use_min = jsonDicLoad.get("prop")[ind]["use_min"]
                n.min[0] = jsonDicLoad.get("prop")[ind]["min[0]"]
                n.use_max = jsonDicLoad.get("prop")[ind]["use_max"]
                n.max[0] = jsonDicLoad.get("prop")[ind]["max[0]"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DOUBLEEDGEMASK":
            indJson = mIPFOzIWc("CompositorNodeDoubleEdgeMask", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inner_mode = jsonDicLoad.get("prop")[ind]["inner_mode"]
                n.edge_mode = jsonDicLoad.get("prop")[ind]["edge_mode"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "ELLIPSEMASK":
            indJson = mIPFOzIWc("CompositorNodeEllipseMask", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.x = jsonDicLoad.get("prop")[ind]["x"]
                n.y = jsonDicLoad.get("prop")[ind]["y"]
                n.width = jsonDicLoad.get("prop")[ind]["width"]
                n.height = jsonDicLoad.get("prop")[ind]["height"]
                n.rotation = jsonDicLoad.get("prop")[ind]["rotation"]
                n.mask_type = jsonDicLoad.get("prop")[ind]["mask_type"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CURVE_VEC":
            indJson = mIPFOzIWc("CompositorNodeCurveVec", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[0]"]
                n.inputs[0].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[1]"]
                n.inputs[0].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TIME":
            indJson = mIPFOzIWc("CompositorNodeTime", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.frame_start = jsonDicLoad.get("prop")[ind]["frame_start"]
                n.frame_end = jsonDicLoad.get("prop")[ind]["frame_end"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CRYPTOMATTE":
            indJson = mIPFOzIWc("CompositorNodeCryptomatte", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.matte_id = jsonDicLoad.get("prop")[ind]["matte_id"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[2].default_value")
                n.inputs[3].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[3].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BOXMASK":
            indJson = mIPFOzIWc("CompositorNodeBoxMask", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.x = jsonDicLoad.get("prop")[ind]["x"]
                n.y = jsonDicLoad.get("prop")[ind]["y"]
                n.width = jsonDicLoad.get("prop")[ind]["width"]
                n.height = jsonDicLoad.get("prop")[ind]["height"]
                n.rotation = jsonDicLoad.get("prop")[ind]["rotation"]
                n.mask_type = jsonDicLoad.get("prop")[ind]["mask_type"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TRACKPOS":
            indJson = mIPFOzIWc("CompositorNodeTrackPos", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.tracking_object = jsonDicLoad.get("prop")[ind]["tracking_object"]
                n.track_name = jsonDicLoad.get("prop")[ind]["track_name"]
                n.position = jsonDicLoad.get("prop")[ind]["position"]
                videoPath = jsonDicLoad.get("prop")[ind]["video"]                
                n.name = jsonDicLoad.get("prop")[ind]["name"]
                n.label = videoPath
                bpy.data.movieclips.load(videoPath)
        if n.type == "MOVIECLIP":
            indJson = mIPFOzIWc("CompositorNodeMovieClip", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
                videoPath = jsonDicLoad.get("prop")[ind]["video"]
                n.label = videoPath      
                bpy.data.movieclips.load(videoPath)
        if n.type == "CRYPTOMATTE_V2":
            indJson = mIPFOzIWc("CompositorNodeCryptomatteV2", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.source = jsonDicLoad.get("prop")[ind]["source"]
                n.layer_name = jsonDicLoad.get("prop")[ind]["layer_name"]
                n.matte_id = jsonDicLoad.get("prop")[ind]["matte_id"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "ANTIALIASING":
            indJson = mIPFOzIWc("CompositorNodeAntiAliasing", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.threshold = jsonDicLoad.get("prop")[ind]["threshold"]
                n.contrast_limit = jsonDicLoad.get("prop")[ind]["contrast_limit"]
                n.corner_rounding = jsonDicLoad.get("prop")[ind]["corner_rounding"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BILATERALBLUR":
            indJson = mIPFOzIWc("CompositorNodeBilateralblur", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.iterations = jsonDicLoad.get("prop")[ind]["iterations"]
                n.sigma_color = jsonDicLoad.get("prop")[ind]["sigma_color"]
                n.sigma_space = jsonDicLoad.get("prop")[ind]["sigma_space"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CHROMA_MATTE":
            indJson = mIPFOzIWc("CompositorNodeChromaMatte", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.tolerance = jsonDicLoad.get("prop")[ind]["tolerance"]
                n.threshold = jsonDicLoad.get("prop")[ind]["threshold"]
                n.gain = jsonDicLoad.get("prop")[ind]["gain"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COLOR_MATTE":
            indJson = mIPFOzIWc("CompositorNodeColorMatte", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.color_hue = jsonDicLoad.get("prop")[ind]["color_hue"]
                n.color_saturation = jsonDicLoad.get("prop")[ind]["color_saturation"]
                n.color_value = jsonDicLoad.get("prop")[ind]["color_value"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "RGBTOBW":
            indJson = mIPFOzIWc("CompositorNodeRGBToBW", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPYUVA":
            indJson = mIPFOzIWc("CompositorNodeSepYUVA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPHSVA":
            indJson = mIPFOzIWc("CompositorNodeSepHSVA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPRGBA":
            indJson = mIPFOzIWc("CompositorNodeSepRGBA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BRIGHTCONTRAST":
            indJson = mIPFOzIWc("CompositorNodeBrightContrast", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.use_premultiply = jsonDicLoad.get("prop")[ind]["use_premultiply"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BOKEHBLUR":
            indJson = mIPFOzIWc("CompositorNodeBokehBlur", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.use_variable_size = jsonDicLoad.get("prop")[ind]["use_variable_size"]
                n.blur_max = jsonDicLoad.get("prop")[ind]["blur_max"]
                n.use_extended_bounds = jsonDicLoad.get("prop")[ind]["use_extended_bounds"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BLUR":
            indJson = mIPFOzIWc("CompositorNodeBlur", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.filter_type = jsonDicLoad.get("prop")[ind]["filter_type"]
                n.use_variable_size = jsonDicLoad.get("prop")[ind]["use_variable_size"]
                n.use_bokeh = jsonDicLoad.get("prop")[ind]["use_bokeh"]
                n.use_gamma_correction = jsonDicLoad.get("prop")[ind]["use_gamma_correction"]
                n.use_relative = jsonDicLoad.get("prop")[ind]["use_relative"]
                n.size_x = jsonDicLoad.get("prop")[ind]["size_x"]
                n.size_y = jsonDicLoad.get("prop")[ind]["size_y"]
                n.use_extended_bounds = jsonDicLoad.get("prop")[ind]["use_extended_bounds"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CHANNEL_MATTE":
            indJson = mIPFOzIWc("CompositorNodeChannelMatte", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.color_space = jsonDicLoad.get("prop")[ind]["color_space"]
                n.matte_channel = jsonDicLoad.get("prop")[ind]["matte_channel"]
                n.limit_method = jsonDicLoad.get("prop")[ind]["limit_method"]
                n.limit_max = jsonDicLoad.get("prop")[ind]["limit_max"]
                n.limit_min = jsonDicLoad.get("prop")[ind]["limit_min"]
                n.limit_channel = jsonDicLoad.get("prop")[ind]["limit_channel"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COLOR_SPILL":
            indJson = mIPFOzIWc("CompositorNodeColorSpill", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.channel = jsonDicLoad.get("prop")[ind]["channel"]
                n.limit_method = jsonDicLoad.get("prop")[ind]["limit_method"]
                n.limit_channel = jsonDicLoad.get("prop")[ind]["limit_channel"]
                n.ratio = jsonDicLoad.get("prop")[ind]["ratio"]
                n.use_unspill = jsonDicLoad.get("prop")[ind]["use_unspill"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "BOKEHIMAGE":
            indJson = mIPFOzIWc("CompositorNodeBokehImage", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.flaps = jsonDicLoad.get("prop")[ind]["flaps"]
                n.angle = jsonDicLoad.get("prop")[ind]["angle"]
                n.rounding = jsonDicLoad.get("prop")[ind]["rounding"]
                n.catadioptric = jsonDicLoad.get("prop")[ind]["catadioptric"]
                n.shift = jsonDicLoad.get("prop")[ind]["shift"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COLORBALANCE":
            indJson = mIPFOzIWc("CompositorNodeColorBalance", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.correction_method = jsonDicLoad.get("prop")[ind]["correction_method"]
                n.lift = xhNzZQzEI(jsonDicLoad, ind, "lift")
                n.gamma = xhNzZQzEI(jsonDicLoad, ind, "gamma")
                n.gain = xhNzZQzEI(jsonDicLoad, ind, "gain")
                n.offset = xhNzZQzEI(jsonDicLoad, ind, "offset")
                n.power = xhNzZQzEI(jsonDicLoad, ind, "power")
                n.slope = xhNzZQzEI(jsonDicLoad, ind, "slope")
                n.offset_basis = jsonDicLoad.get("prop")[ind]["offset_basis"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "COLORCORRECTION":
            indJson = mIPFOzIWc("CompositorNodeColorCorrection", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.red = jsonDicLoad.get("prop")[ind]["red"]
                n.green = jsonDicLoad.get("prop")[ind]["green"]
                n.blue = jsonDicLoad.get("prop")[ind]["blue"]
                n.master_saturation = jsonDicLoad.get("prop")[ind]["master_saturation"]
                n.highlights_saturation = jsonDicLoad.get("prop")[ind]["highlights_saturation"]
                n.midtones_saturation = jsonDicLoad.get("prop")[ind]["midtones_saturation"]
                n.shadows_saturation = jsonDicLoad.get("prop")[ind]["shadows_saturation"]
                n.master_contrast = jsonDicLoad.get("prop")[ind]["master_contrast"]
                n.highlights_contrast = jsonDicLoad.get("prop")[ind]["highlights_contrast"]
                n.midtones_contrast = jsonDicLoad.get("prop")[ind]["midtones_contrast"]
                n.shadows_contrast = jsonDicLoad.get("prop")[ind]["shadows_contrast"]
                n.master_gamma = jsonDicLoad.get("prop")[ind]["master_gamma"]
                n.highlights_gamma = jsonDicLoad.get("prop")[ind]["highlights_gamma"]
                n.midtones_gamma = jsonDicLoad.get("prop")[ind]["midtones_gamma"]
                n.shadows_gamma = jsonDicLoad.get("prop")[ind]["shadows_gamma"]
                n.master_gain = jsonDicLoad.get("prop")[ind]["master_gain"]
                n.highlights_gain = jsonDicLoad.get("prop")[ind]["highlights_gain"]
                n.midtones_gain = jsonDicLoad.get("prop")[ind]["midtones_gain"]
                n.shadows_gain = jsonDicLoad.get("prop")[ind]["shadows_gain"]
                n.master_lift = jsonDicLoad.get("prop")[ind]["master_lift"]
                n.highlights_lift = jsonDicLoad.get("prop")[ind]["highlights_lift"]
                n.midtones_lift = jsonDicLoad.get("prop")[ind]["midtones_lift"]
                n.shadows_lift = jsonDicLoad.get("prop")[ind]["shadows_lift"]
                n.midtones_start = jsonDicLoad.get("prop")[ind]["midtones_start"]
                n.midtones_end = jsonDicLoad.get("prop")[ind]["midtones_end"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CONVERT_COLORSPACE":
            indJson = mIPFOzIWc("CompositorNodeConvertColorSpace", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.from_color_space = jsonDicLoad.get("prop")[ind]["from_color_space"]
                n.to_color_space = jsonDicLoad.get("prop")[ind]["to_color_space"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CROP":
            indJson = mIPFOzIWc("CompositorNodeCrop", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.use_crop_size = jsonDicLoad.get("prop")[ind]["use_crop_size"]
                n.relative = jsonDicLoad.get("prop")[ind]["relative"]
                n.min_x = jsonDicLoad.get("prop")[ind]["min_x"]
                n.max_x = jsonDicLoad.get("prop")[ind]["max_x"]
                n.min_y = jsonDicLoad.get("prop")[ind]["min_y"]
                n.max_y = jsonDicLoad.get("prop")[ind]["max_y"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DISPLACE":
            indJson = mIPFOzIWc("CompositorNodeDisplace", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DIFF_MATTE":
            indJson = mIPFOzIWc("CompositorNodeDiffMatte", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.tolerance = jsonDicLoad.get("prop")[ind]["tolerance"]
                n.falloff = jsonDicLoad.get("prop")[ind]["falloff"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CORNERPIN":
            indJson = mIPFOzIWc("CompositorNodeCornerPin", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.inputs[2].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[0]"]
                n.inputs[2].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[1]"]
                n.inputs[2].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[2]"]
                n.inputs[3].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[3].default_value[0]"]
                n.inputs[3].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[3].default_value[1]"]
                n.inputs[3].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[3].default_value[2]"]
                n.inputs[4].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[0]"]
                n.inputs[4].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[1]"]
                n.inputs[4].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[4].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DBLUR":
            indJson = mIPFOzIWc("CompositorNodeDBlur", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.iterations = jsonDicLoad.get("prop")[ind]["iterations"]
                n.center_x = jsonDicLoad.get("prop")[ind]["center_x"]
                n.center_y = jsonDicLoad.get("prop")[ind]["center_y"]
                n.distance = jsonDicLoad.get("prop")[ind]["distance"]
                n.angle = jsonDicLoad.get("prop")[ind]["angle"]
                n.spin = jsonDicLoad.get("prop")[ind]["spin"]
                n.zoom = jsonDicLoad.get("prop")[ind]["zoom"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DEFOCUS":
            indJson = mIPFOzIWc("CompositorNodeDefocus", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.bokeh = jsonDicLoad.get("prop")[ind]["bokeh"]
                n.angle = jsonDicLoad.get("prop")[ind]["angle"]
                n.use_gamma_correction = jsonDicLoad.get("prop")[ind]["use_gamma_correction"]
                n.f_stop = jsonDicLoad.get("prop")[ind]["f_stop"]
                n.blur_max = jsonDicLoad.get("prop")[ind]["blur_max"]
                n.threshold = jsonDicLoad.get("prop")[ind]["threshold"]
                n.use_preview = jsonDicLoad.get("prop")[ind]["use_preview"]
                n.use_zbuffer = jsonDicLoad.get("prop")[ind]["use_zbuffer"]
                n.z_scale = jsonDicLoad.get("prop")[ind]["z_scale"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DENOISE":
            indJson = mIPFOzIWc("CompositorNodeDenoise", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.prefilter = jsonDicLoad.get("prop")[ind]["prefilter"]
                n.use_hdr = jsonDicLoad.get("prop")[ind]["use_hdr"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "EXPOSURE":
            indJson = mIPFOzIWc("CompositorNodeExposure", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "FILTER":
            indJson = mIPFOzIWc("CompositorNodeFilter", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.filter_type = jsonDicLoad.get("prop")[ind]["filter_type"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DESPECKLE":
            indJson = mIPFOzIWc("CompositorNodeDespeckle", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.threshold = jsonDicLoad.get("prop")[ind]["threshold"]
                n.threshold_neighbor = jsonDicLoad.get("prop")[ind]["threshold_neighbor"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "CURVE_RGB":
            indJson = mIPFOzIWc("CompositorNodeCurveRGB", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[2].default_value")
                n.inputs[3].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[3].default_value")
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "DISTANCE_MATTE":
            indJson = mIPFOzIWc("CompositorNodeDistanceMatte", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.tolerance = jsonDicLoad.get("prop")[ind]["tolerance"]
                n.falloff = jsonDicLoad.get("prop")[ind]["falloff"]
                n.channel = jsonDicLoad.get("prop")[ind]["channel"]
                n.channel = jsonDicLoad.get("prop")[ind]["channel"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "FLIP":
            indJson = mIPFOzIWc("CompositorNodeFlip", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.axis = jsonDicLoad.get("prop")[ind]["axis"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "GAMMA":
            indJson = mIPFOzIWc("CompositorNodeGamma", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "GLARE":
            indJson = mIPFOzIWc("CompositorNodeGlare", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.glare_type = jsonDicLoad.get("prop")[ind]["glare_type"]
                n.quality = jsonDicLoad.get("prop")[ind]["quality"]
                n.iterations = jsonDicLoad.get("prop")[ind]["iterations"]
                n.color_modulation = jsonDicLoad.get("prop")[ind]["color_modulation"]
                n.mix = jsonDicLoad.get("prop")[ind]["mix"]
                n.threshold = jsonDicLoad.get("prop")[ind]["threshold"]
                n.streaks = jsonDicLoad.get("prop")[ind]["streaks"]
                n.angle_offset = jsonDicLoad.get("prop")[ind]["angle_offset"]
                n.fade = jsonDicLoad.get("prop")[ind]["fade"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "HUECORRECT":
            indJson = mIPFOzIWc("CompositorNodeHueCorrect", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "HUE_SAT":
            indJson = mIPFOzIWc("CompositorNodeHueSat", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "LUMA_MATTE":
            indJson = mIPFOzIWc("CompositorNodeLumaMatte", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.limit_max = jsonDicLoad.get("prop")[ind]["limit_max"]
                n.limit_min = jsonDicLoad.get("prop")[ind]["limit_min"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "KEYING":
            indJson = mIPFOzIWc("CompositorNodeKeying", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.blur_pre = jsonDicLoad.get("prop")[ind]["blur_pre"]
                n.screen_balance = jsonDicLoad.get("prop")[ind]["screen_balance"]
                n.despill_factor = jsonDicLoad.get("prop")[ind]["despill_factor"]
                n.despill_balance = jsonDicLoad.get("prop")[ind]["despill_balance"]
                n.edge_kernel_radius = jsonDicLoad.get("prop")[ind]["edge_kernel_radius"]
                n.edge_kernel_tolerance = jsonDicLoad.get("prop")[ind]["edge_kernel_tolerance"]
                n.clip_black = jsonDicLoad.get("prop")[ind]["clip_black"]
                n.clip_white = jsonDicLoad.get("prop")[ind]["clip_white"]
                n.dilate_distance = jsonDicLoad.get("prop")[ind]["dilate_distance"]
                n.feather_falloff = jsonDicLoad.get("prop")[ind]["feather_falloff"]
                n.feather_distance = jsonDicLoad.get("prop")[ind]["feather_distance"]
                n.blur_post = jsonDicLoad.get("prop")[ind]["blur_post"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "INPAINT":
            indJson = mIPFOzIWc("CompositorNodeInpaint", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.distance = jsonDicLoad.get("prop")[ind]["distance"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MAP_UV":
            indJson = mIPFOzIWc("CompositorNodeMapUV", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.alpha = jsonDicLoad.get("prop")[ind]["alpha"]
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "LENSDIST":
            indJson = mIPFOzIWc("CompositorNodeLensdist", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.use_projector = jsonDicLoad.get("prop")[ind]["use_projector"]
                n.use_jitter = jsonDicLoad.get("prop")[ind]["use_jitter"]
                n.use_fit = jsonDicLoad.get("prop")[ind]["use_fit"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MIX_RGB":
            indJson = mIPFOzIWc("CompositorNodeMixRGB", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.inputs[2].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[2].default_value")
                n.blend_type = jsonDicLoad.get("prop")[ind]["blend_type"]
                n.use_clamp = jsonDicLoad.get("prop")[ind]["use_clamp"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.use_alpha = jsonDicLoad.get("prop")[ind]["use_alpha"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "INVERT":
            indJson = mIPFOzIWc("CompositorNodeInvert", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.invert_rgb = jsonDicLoad.get("prop")[ind]["invert_rgb"]
                n.invert_alpha = jsonDicLoad.get("prop")[ind]["invert_alpha"]
                n.inputs[0].default_value = jsonDicLoad.get("prop")[ind]["inputs[0].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "MOVIEDISTORTION":
            indJson = mIPFOzIWc("CompositorNodeMovieDistortion", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.distortion_type = jsonDicLoad.get("prop")[ind]["distortion_type"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "KUWAHARA":
            indJson = mIPFOzIWc("CompositorNodeKuwahara", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.variation = jsonDicLoad.get("prop")[ind]["variation"]
                n.size = jsonDicLoad.get("prop")[ind]["size"]
                n.uniformity = jsonDicLoad.get("prop")[ind]["uniformity"]
                n.sharpness = jsonDicLoad.get("prop")[ind]["sharpness"]
                n.eccentricity = jsonDicLoad.get("prop")[ind]["eccentricity"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "PLANETRACKDEFORM":
            indJson = mIPFOzIWc("CompositorNodePlaneTrackDeform", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.use_motion_blur = jsonDicLoad.get("prop")[ind]["use_motion_blur"]
                n.tracking_object = jsonDicLoad.get("prop")[ind]["tracking_object"]
                n.plane_track_name = jsonDicLoad.get("prop")[ind]["plane_track_name"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "NORMAL":
            indJson = mIPFOzIWc("CompositorNodeNormal", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.outputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "outputs[0].default_value")
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "PREMULKEY":
            indJson = mIPFOzIWc("CompositorNodePremulKey", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.mapping = jsonDicLoad.get("prop")[ind]["mapping"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "PIXELATE":
            indJson = mIPFOzIWc("CompositorNodePixelate", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TRANSLATE":
            indJson = mIPFOzIWc("CompositorNodeTranslate", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.use_relative = jsonDicLoad.get("prop")[ind]["use_relative"]
                n.wrap_axis = jsonDicLoad.get("prop")[ind]["wrap_axis"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SPLITVIEWER":
            indJson = mIPFOzIWc("CompositorNodeSplitViewer", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.axis = jsonDicLoad.get("prop")[ind]["axis"]
                n.factor = jsonDicLoad.get("prop")[ind]["factor"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VECBLUR":
            indJson = mIPFOzIWc("CompositorNodeVecBlur", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[0]"]
                n.inputs[2].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[1]"]
                n.inputs[2].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[2].default_value[2]"]
                n.use_curved = jsonDicLoad.get("prop")[ind]["use_curved"]
                n.samples = jsonDicLoad.get("prop")[ind]["samples"]
                n.factor = jsonDicLoad.get("prop")[ind]["factor"]
                n.speed_min = jsonDicLoad.get("prop")[ind]["speed_min"]
                n.speed_max = jsonDicLoad.get("prop")[ind]["speed_max"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "VALTORGB":
            indJson = mIPFOzIWc("CompositorNodeValToRGB", jsonDicLoad)
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
        if n.type == "RGB":
            indJson = mIPFOzIWc("CompositorNodeRGB", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.outputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "outputs[0].default_value")
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPARATE_COLOR":
            indJson = mIPFOzIWc("CompositorNodeSeparateColor", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.ycc_mode = jsonDicLoad.get("prop")[ind]["ycc_mode"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TONEMAP":
            indJson = mIPFOzIWc("CompositorNodeTonemap", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.tonemap_type = jsonDicLoad.get("prop")[ind]["tonemap_type"]
                n.intensity = jsonDicLoad.get("prop")[ind]["intensity"]
                n.contrast = jsonDicLoad.get("prop")[ind]["contrast"]
                n.adaptation = jsonDicLoad.get("prop")[ind]["adaptation"]
                n.correction = jsonDicLoad.get("prop")[ind]["correction"]
                n.key = jsonDicLoad.get("prop")[ind]["key"]
                n.offset = jsonDicLoad.get("prop")[ind]["offset"]
                n.gamma = jsonDicLoad.get("prop")[ind]["gamma"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SUNBEAMS":
            indJson = mIPFOzIWc("CompositorNodeSunBeams", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.source[0] = jsonDicLoad.get("prop")[ind]["source[0]"]
                n.source[1] = jsonDicLoad.get("prop")[ind]["source[1]"]
                n.ray_length = jsonDicLoad.get("prop")[ind]["ray_length"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SETALPHA":
            indJson = mIPFOzIWc("CompositorNodeSetAlpha", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SEPYCCA":
            indJson = mIPFOzIWc("CompositorNodeSepYCCA", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.mode = jsonDicLoad.get("prop")[ind]["mode"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "STABILIZE2D":
            indJson = mIPFOzIWc("CompositorNodeStabilize", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.invert = jsonDicLoad.get("prop")[ind]["invert"]
                n.filter_type = jsonDicLoad.get("prop")[ind]["filter_type"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TEXTURE":
            indJson = mIPFOzIWc("CompositorNodeTexture", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.texture = jsonDicLoad.get("prop")[ind]["texture"]
                n.inputs[0].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[0]"]
                n.inputs[0].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[1]"]
                n.inputs[0].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[0].default_value[2]"]
                n.inputs[1].default_value[0] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[0]"]
                n.inputs[1].default_value[1] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[1]"]
                n.inputs[1].default_value[2] = jsonDicLoad.get("prop")[ind]["inputs[1].default_value[2]"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "ROTATE":
            indJson = mIPFOzIWc("CompositorNodeRotate", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.filter_type = jsonDicLoad.get("prop")[ind]["filter_type"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "TRANSFORM":
            indJson = mIPFOzIWc("CompositorNodeTransform", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.filter_type = jsonDicLoad.get("prop")[ind]["filter_type"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[2].default_value = jsonDicLoad.get("prop")[ind]["inputs[2].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.inputs[4].default_value = jsonDicLoad.get("prop")[ind]["inputs[4].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "SWITCH":
            indJson = mIPFOzIWc("CompositorNodeSwitch", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[1].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[1].default_value")
                n.check = jsonDicLoad.get("prop")[ind]["check"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
        if n.type == "ZCOMBINE":
            indJson = mIPFOzIWc("CompositorNodeZcombine", jsonDicLoad)
            for ind in indJson:
                n.__class__.__name__ = jsonDicLoad.get("prop")[ind]["__class__.__name__"]
                n.inputs[0].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[0].default_value")
                n.inputs[2].default_value = xhNzZQzEI(jsonDicLoad, ind, "inputs[2].default_value")
                n.use_alpha = jsonDicLoad.get("prop")[ind]["use_alpha"]
                n.use_antialias_z = jsonDicLoad.get("prop")[ind]["use_antialias_z"]
                n.inputs[1].default_value = jsonDicLoad.get("prop")[ind]["inputs[1].default_value"]
                n.inputs[3].default_value = jsonDicLoad.get("prop")[ind]["inputs[3].default_value"]
                n.name = jsonDicLoad.get("prop")[ind]["name"]
    time.sleep(1)
    bpy.context.area.ui_type = 'CompositorNodeTree'
    bpy.ops.node.view_all()
