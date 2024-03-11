import bpy
nodeCompCopyClassName = []
nodeShadCopyClassName = []
class OGMDZFHhT(bpy.types.Operator):
    bl_idname = "node.copy"
    bl_label = "Copy Nodes"
    def execute(self, context):
        if bpy.context.area.type == 'NODE_EDITOR' and bpy.context.area.ui_type == 'CompositorNodeTree':
            print("Compositor node editor")
            sel = [x for x in bpy.context.scene.node_tree.nodes if x.select]
            global nodeCompCopyClassName
            for x in sel:
                nodeCompCopyClassName.append(x.__class__.__name__)
            self.report({'INFO'}, str(nodeCompCopyClassName) + " <= Agregados")
        elif bpy.context.area.type == 'NODE_EDITOR' and bpy.context.area.ui_type == 'ShaderNodeTree':
            print("Shader node editor")
            sel = [x for x in bpy.context.object.active_material.node_tree.nodes if x.select]
            global nodeShadCopyClassName
            for x in sel:
                nodeShadCopyClassName.append(x.__class__.__name__)
            self.report({'INFO'}, str(nodeShadCopyClassName) + " <= Agregados")
        return {"FINISHED"}  
class DOSmAUexO(bpy.types.Operator):
    bl_idname = "node.paste"
    bl_label = "Paste Nodes"
    def execute(self, context):
        if bpy.context.area.type == 'NODE_EDITOR' and bpy.context.area.ui_type == 'CompositorNodeTree':
            print("Compositor node editor")
            bpy.context.scene.use_nodes = True
            tree = bpy.context.scene.node_tree
            locX = 0
            locY = 0
            cont = 0
            global nodeCompCopyClassName
            for x in nodeCompCopyClassName:
                c_nod_View = tree.nodes.new(type = x)   
                c_nod_View.location = (locX, locY)
                cont += 1
                locX += 250
                if cont % 5 == 0:
                    locX = 0
                    locY -= 420
            self.report({'INFO'}, str(nodeCompCopyClassName) + " <= Creados")
        elif bpy.context.area.type == 'NODE_EDITOR' and bpy.context.area.ui_type == 'ShaderNodeTree':
            print("Shader node editor")
            material = bpy.context.object.active_material.node_tree
            locX = 0
            locY = 0
            cont = 0
            for x in nodeShadCopyClassName:
                matOut = material.nodes.new(type = x) 
                matOut.location = (locX, locY)
                print(x, " == ", matOut.name)
                cont += 1
                locX += 250
                if cont % 5 == 0:
                    locX = 0
                    locY -= 420
            self.report({'INFO'}, str(nodeShadCopyClassName) + " <= Creados")
        return {"FINISHED"}              
class lcewKvzaC(bpy.types.Operator):
    bl_idname = "node.clearcomparr"
    bl_label = "Clear Nodes Compositing."
    def execute(self, context):
        global nodeCompCopyClassName
        nodeCompCopyClassName.clear()
        return {'FINISHED'}
class nlVAjsgps(bpy.types.Operator):
    bl_idname = "node.clearshadarr"
    bl_label = "Clear Nodes Shader."
    def execute(self, context):
        global nodeShadCopyClassName
        nodeShadCopyClassName.clear()
        return {'FINISHED'}    
