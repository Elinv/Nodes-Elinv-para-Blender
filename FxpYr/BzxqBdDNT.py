import bpy
def SDuMrIojV(self, context):
    obj = context.active_object
    me = obj.data
    material = bpy.data.materials.new(name="Imagen_Elinv")
    material.use_nodes = True
    material.node_tree.nodes.remove(
        material.node_tree.nodes.get('Principled BSDF'))
    material_output = material.node_tree.nodes.get('Material Output')
    material_output.location = (0, 0)
    BsdfPrincipled = material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
    BsdfPrincipled.location = (-300, 0)
    link = material.node_tree.links.new
    link(material_output.inputs[0], BsdfPrincipled.outputs[0])
    textImg = material.node_tree.nodes.new('ShaderNodeTexImage')
    textImg.location = (-600, 0)
    link(BsdfPrincipled.inputs[0], textImg.outputs[0])
    link(BsdfPrincipled.inputs[4], textImg.outputs[1])
    mappingElv = material.node_tree.nodes.new('ShaderNodeMapping')
    mappingElv.location = (-900, 0)
    link(textImg.inputs[0], mappingElv.outputs[0])
    textCoord = material.node_tree.nodes.new('ShaderNodeTexCoord')
    textCoord.location = (-1200, 0)
    link(mappingElv.inputs[0], textCoord.outputs[2])
    bpy.context.object.active_material = material
