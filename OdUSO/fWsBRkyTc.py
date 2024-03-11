import bpy, time
from . YsWDOZZWR import *
class oBtrRuRoS(bpy.types.Operator):
    bl_idname = "nodesall.crea_todoslosnodosshader"
    bl_label = "Shader"
    def execute(self, context):
        WOPiYrfBj(self, context, ODrVngONe, self, context)        
        return {"FINISHED"}           
class sETANlUUa(bpy.types.Operator):
    bl_idname = "nodesall.crea_todoslosnodoscompositing"
    bl_label = "Compositing"
    def execute(self, context):
        WOPiYrfBj(self, context, NnMNuEgSm, self, context)           
        return {"FINISHED"}           
def mAawrIfZz(self, context, enumPropVar):
    try:
        enum_items = context.scene.bl_rna.properties[enumPropVar].enum_items
        identifiers = [enum_item.identifier for enum_item in enum_items]
        index = identifiers.index(context.scene.myEnumTypeNodeCreator)
        pro = bpy.context.scene.bl_rna.properties[enumPropVar]
        listName = [e.name for e in pro.enum_items]
        listidentifier = [e.identifier for e in pro.enum_items]
        listdescription = [e.description for e in pro.enum_items]
    except:
        print("Excepción en mAawrIfZz function")
        self.report({'INFO'}, "Seleccione type nodo a crear!")
        return -1
    return [listName, listidentifier, listdescription, index, listName[index], listidentifier[index], listdescription[index]]
class OKqkSiMhf(bpy.types.Operator):
    bl_idname = "nodesall.creanodetypeselectlist"
    bl_label = "Crea nodo con nombre de clase"
    def execute(self, context):
        arrValues = mAawrIfZz(self, context, "myEnumTypeNodeCreator")
        if arrValues != -1:
            sel = arrValues[4]
            if sel == 'Compositing':
                WOPiYrfBj(self, context, jXNhfRGQw, self, context)
            elif sel == 'Geometry':
                print(sel)
            elif sel == 'Shader':
                WOPiYrfBj(self, context, KghRxGeWN, self, context)            
        return {"FINISHED"}  
def ODrVngONe(self, context):
    area = bpy.context.area
    area.type = 'NODE_EDITOR'
    area.ui_type = 'ShaderNodeTree'
    obj = context.active_object
    me = obj.data
    material = bpy.data.materials.new(name="Elinv_All_Node")
    material.use_nodes = True
    mater = material.node_tree
    mat = bpy.context.object.active_material
    bpy.context.object.active_material = material
    for node in mater.nodes:
        mater.nodes.remove(node)
    arrNodes = [
        "ShaderNodeAddShader",
        "ShaderNodeAmbientOcclusion",
        "ShaderNodeAttribute",
        "ShaderNodeBackground",
        "ShaderNodeBevel",
        "ShaderNodeBlackbody",
        "ShaderNodeBrightContrast",
        "ShaderNodeBsdfAnisotropic",
        "ShaderNodeBsdfDiffuse",
        "ShaderNodeBsdfGlass",
        "ShaderNodeBsdfHair",
        "ShaderNodeBsdfHairPrincipled",
        "ShaderNodeBsdfPrincipled",
        "ShaderNodeBsdfRefraction",
        "ShaderNodeBsdfSheen",
        "ShaderNodeBsdfToon",
        "ShaderNodeBsdfTranslucent",
        "ShaderNodeBsdfTransparent",
        "ShaderNodeBump",
        "ShaderNodeCameraData",
        "ShaderNodeClamp",
        "ShaderNodeCombineColor",
        "ShaderNodeCombineHSV",
        "ShaderNodeCombineRGB",
        "ShaderNodeCombineXYZ",
        "ShaderNodeDisplacement",
        "ShaderNodeEeveeSpecular",
        "ShaderNodeEmission",
        "ShaderNodeFloatCurve",
        "ShaderNodeFresnel",
        "ShaderNodeGamma",
        "ShaderNodeGroup",
        "ShaderNodeHairInfo",
        "ShaderNodeHoldout",
        "ShaderNodeHueSaturation",
        "ShaderNodeInvert",
        "ShaderNodeLayerWeight",
        "ShaderNodeLightFalloff",
        "ShaderNodeLightPath",
        "ShaderNodeMapRange",
        "ShaderNodeMapping",
        "ShaderNodeMath",
        "ShaderNodeMix",
        "ShaderNodeMixRGB",
        "ShaderNodeMixShader",
        "ShaderNodeNewGeometry",
        "ShaderNodeNormal",
        "ShaderNodeNormalMap",
        "ShaderNodeObjectInfo",
        "ShaderNodeOutputAOV",
        "ShaderNodeOutputLight",
        "ShaderNodeOutputLineStyle",
        "ShaderNodeOutputMaterial",
        "ShaderNodeOutputWorld",
        "ShaderNodeParticleInfo",
        "ShaderNodePointInfo",
        "ShaderNodeRGB",
        "ShaderNodeRGBCurve",
        "ShaderNodeRGBToBW",
        "ShaderNodeScript",
        "ShaderNodeSeparateColor",
        "ShaderNodeSeparateHSV",
        "ShaderNodeSeparateRGB",
        "ShaderNodeSeparateXYZ",
        "ShaderNodeShaderToRGB",
        "ShaderNodeSqueeze",
        "ShaderNodeSubsurfaceScattering",
        "ShaderNodeTangent",
        "ShaderNodeTexBrick",
        "ShaderNodeTexChecker",
        "ShaderNodeTexCoord",
        "ShaderNodeTexEnvironment",
        "ShaderNodeTexGradient",
        "ShaderNodeTexIES",
        "ShaderNodeTexImage",
        "ShaderNodeTexMagic",
        "ShaderNodeTexMusgrave",
        "ShaderNodeTexNoise",
        "ShaderNodeTexPointDensity",
        "ShaderNodeTexSky",
        "ShaderNodeTexVoronoi",
        "ShaderNodeTexWave",
        "ShaderNodeTexWhiteNoise",
        "ShaderNodeUVAlongStroke",
        "ShaderNodeUVMap",
        "ShaderNodeValToRGB",
        "ShaderNodeValue",
        "ShaderNodeVectorCurve",
        "ShaderNodeVectorDisplacement",
        "ShaderNodeVectorMath",
        "ShaderNodeVectorRotate",
        "ShaderNodeVectorTransform",
        "ShaderNodeVertexColor",
        "ShaderNodeVolumeAbsorption",
        "ShaderNodeVolumeInfo",
        "ShaderNodeVolumePrincipled",
        "ShaderNodeVolumeScatter",
        "ShaderNodeWavelength",
        "ShaderNodeWireframe",
    ]
    locX = 0
    locY = 0
    cont = 0
    count = len(arrNodes)
    y = 0
    for x in arrNodes:
        matOut = mater.nodes.new(type = x) #material.node_tree.nodes.get('Material Output')
        matOut.location = (locX, locY)
        cont += 1
        locX += 250
        if cont % 5 == 0:
            locX = 0
            locY += 420
        if y == count:
            bpy.ops.node.view_all()
        else:
            y += 1
def NnMNuEgSm(self, context):
    area = bpy.context.area
    area.type = 'NODE_EDITOR'
    area.ui_type = 'CompositorNodeTree'
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    for node in tree.nodes:
        print(node.__class__.__name__)
        print(node.location)
        tree.nodes.remove(node)
    arrNodes = [
        "CompositorNodeAlphaOver",
        "CompositorNodeAntiAliasing",
        "CompositorNodeBilateralblur",
        "CompositorNodeBlur",
        "CompositorNodeBokehBlur",
        "CompositorNodeBokehImage",
        "CompositorNodeBoxMask",
        "CompositorNodeBrightContrast",
        "CompositorNodeChannelMatte",
        "CompositorNodeChromaMatte",
        "CompositorNodeColorBalance",
        "CompositorNodeColorCorrection",
        "CompositorNodeColorMatte",
        "CompositorNodeColorSpill",
        "CompositorNodeCombHSVA",
        "CompositorNodeCombRGBA",
        "CompositorNodeCombYCCA",
        "CompositorNodeCombYUVA",
        "CompositorNodeCombineColor",
        "CompositorNodeCombineXYZ",
        "CompositorNodeComposite",
        "CompositorNodeConvertColorSpace",
        "CompositorNodeCornerPin",
        "CompositorNodeCrop",
        "CompositorNodeCryptomatte",
        "CompositorNodeCryptomatteV2",
        "CompositorNodeCurveRGB",
        "CompositorNodeCurveVec",
        "CompositorNodeDBlur",
        "CompositorNodeDefocus",
        "CompositorNodeDenoise",
        "CompositorNodeDespeckle",
        "CompositorNodeDiffMatte",
        "CompositorNodeDilateErode",
        "CompositorNodeDisplace",
        "CompositorNodeDistanceMatte",
        "CompositorNodeDoubleEdgeMask",
        "CompositorNodeEllipseMask",
        "CompositorNodeExposure",
        "CompositorNodeFilter",
        "CompositorNodeFlip",
        "CompositorNodeGamma",
        "CompositorNodeGlare",
        "CompositorNodeGroup",
        "CompositorNodeHueCorrect",
        "CompositorNodeHueSat",
        "CompositorNodeIDMask",
        "CompositorNodeImage",
        "CompositorNodeInpaint",
        "CompositorNodeInvert",
        "CompositorNodeKeying",
        "CompositorNodeKeyingScreen",
        "CompositorNodeKuwahara",
        "CompositorNodeLensdist",
        "CompositorNodeLevels",
        "CompositorNodeLumaMatte",
        "CompositorNodeMapRange",
        "CompositorNodeMapUV",
        "CompositorNodeMapValue",
        "CompositorNodeMask",
        "CompositorNodeMath",
        "CompositorNodeMixRGB",
        "CompositorNodeMovieClip",
        "CompositorNodeMovieDistortion",
        "CompositorNodeNormal",
        "CompositorNodeNormalize",
        "CompositorNodeOutputFile",
        "CompositorNodePixelate",
        "CompositorNodePlaneTrackDeform",
        "CompositorNodePosterize",
        "CompositorNodePremulKey",
        "CompositorNodeRGB",
        "CompositorNodeRGBToBW",
        "CompositorNodeRLayers",
        "CompositorNodeRotate",
        "CompositorNodeScale",
        "CompositorNodeSceneTime",
        "CompositorNodeSepHSVA",
        "CompositorNodeSepRGBA",
        "CompositorNodeSepYCCA",
        "CompositorNodeSepYUVA",
        "CompositorNodeSeparateColor",
        "CompositorNodeSeparateXYZ",
        "CompositorNodeSetAlpha",
        "CompositorNodeSplitViewer",
        "CompositorNodeStabilize",
        "CompositorNodeSunBeams",
        "CompositorNodeSwitch",
        "CompositorNodeSwitchView",
        "CompositorNodeTexture",
        "CompositorNodeTime",
        "CompositorNodeTonemap",
        "CompositorNodeTrackPos",
        "CompositorNodeTransform",
        "CompositorNodeTranslate",
        "CompositorNodeValToRGB",
        "CompositorNodeValue",
        "CompositorNodeVecBlur",
        "CompositorNodeViewer",
        "CompositorNodeZcombine",
    ]
    locX = 0
    locY = 0
    cont = 0
    for x in arrNodes:
        c_nod_View = tree.nodes.new(type = x)   
        c_nod_View.location = (locX, locY)
        cont += 1
        locX += 250
        if cont % 5 == 0:
            locX = 0
            locY -= 420
def jXNhfRGQw(self, context):
    area = bpy.context.area
    area.type = 'NODE_EDITOR'
    area.ui_type = 'CompositorNodeTree'
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    for node in tree.nodes:
        print(node.__class__.__name__)
        print(node.location)
        tree.nodes.remove(node)
    scene = context.scene
    x = scene.input 
    try: 
        c_nod_View = tree.nodes.new(type = x)   
        c_nod_View.location = (0, 0)
    except:
        self.report({'INFO'}, "No es un nodo tipo compositing!")
def KghRxGeWN(self, context):
    area = bpy.context.area
    area.type = 'NODE_EDITOR'
    area.ui_type = 'ShaderNodeTree'
    obj = context.active_object
    me = obj.data
    selection = bpy.context.object
    currentMaterial = selection.active_material
    currentMaterial.use_nodes = True
    mater = currentMaterial.node_tree
    for node in mater.nodes:
        mater.nodes.remove(node)
    scene = context.scene
    texto = scene.input        
    matOut = mater.nodes.new(type = texto) #material.node_tree.nodes.get('Material Output')
    matOut.location = (0, 0)
