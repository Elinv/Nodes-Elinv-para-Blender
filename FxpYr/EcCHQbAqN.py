import bpy
def CaYVUUudH(self, context): 
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    for node in tree.nodes:
        print(node.__class__.__name__)
        print(node.location)
        tree.nodes.remove(node)
    c_nod_View = tree.nodes.new('CompositorNodeViewer')   
    c_nod_View.location = -82.8610, -118.5290
    c_nod_Comp = tree.nodes.new('CompositorNodeComposite')   
    c_nod_Comp.location = -79.6813, 115.4979
    c_nod_RLay = tree.nodes.new('CompositorNodeRLayers')   
    c_nod_RLay.location = -610.9098, -106.9146
    c_nodAlphaOver = tree.nodes.new('CompositorNodeAlphaOver')   
    c_nodAlphaOver.location = -293.9697, 52.3220
    c_nodImage = tree.nodes.new('CompositorNodeImage')   
    c_nodImage.location = -565.6271, 86.6977  
    links = tree.links
    links.new(c_nodAlphaOver.outputs[0], c_nod_Comp.inputs[0])
    links.new(c_nodAlphaOver.outputs[0], c_nod_View.inputs[0])
    links.new(c_nodImage.outputs[0], c_nodAlphaOver.inputs[1])
    links.new(c_nod_RLay.outputs[0], c_nodAlphaOver.inputs[2])
