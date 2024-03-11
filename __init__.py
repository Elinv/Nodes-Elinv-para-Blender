bl_info = {
    "name": "Node Shading Elinv",
    "author": "Elinv",
    "version": (0, 0, 1),
    "blender": (4, 0, 2),
    "location": "Node Shading Editor > Sidebar > Node Elv",
    "description": "Node Shading Elinv",
    "category": "Development",
}
import bpy, sys
from bpy.types import Panel, Scene
from . OdUSO.sLvaQgJAR import *
from . OdUSO.yMgMQBJUz import *
from . OdUSO.LTjtPsvlE import *
from . OdUSO.fWsBRkyTc import *
from . OdUSO.YsWDOZZWR import *
from bpy.props import (
    BoolProperty,
)
class PanelNuevo(bpy.types.Panel):
    bl_label = "Nodes Elinv"
    bl_idname = "NODE_PT_Shading_Elinv"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_context = ""
    bl_category = "Node Elv"
    @classmethod
    def poll(self, context):
        return context.object is not None
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        icon = 'TRIA_DOWN' if context.scene.spShader else 'TRIA_RIGHT'
        row.prop(context.scene, 'spShader', icon=icon, icon_only=True)
        row.label(text='Shader Space')
        row.separator()
        if context.scene.spShader:
            row = layout.row()
            row.operator("nodeshader.crea_material_img_textura")
            row1 = layout.row()
            row1.separator()
            box = self.layout.box()
            row1 = layout.row()
            row1.separator()
            boxAllNod = self.layout.box()
            boxAllNod.label(text="Create all Nodes", icon="X")
            boxAllNod.operator("nodesall.crea_todoslosnodosshader")
            boxAllNod.operator("nodesall.crea_todoslosnodoscompositing")            
            row1 = layout.row()
            row1.separator()
            box = self.layout.box()
            row1 = layout.row()
            row1.separator()
            boxNodeAdd = self.layout.box()
            boxNodeAdd.label(text="Create node by class name")
            boxNodeAdd.prop(context.scene, 'input')
            boxNodeAdd.column().prop(context.scene, "myEnumTypeNodeCreator")
            boxNodeAdd.operator("nodesall.creanodetypeselectlist")
            row1 = layout.row()
            row1.separator()
            box = self.layout.box()
            row1 = layout.row()
            row1.separator()
            row = layout.row()
            row.operator("nodeshader.nodosproplinks")
            row = layout.row()
            row.operator("nodeshader.getjsonnode")
            row2 = layout.row()
            row2.separator()
        row = layout.row()
        icon = 'TRIA_DOWN' if context.scene.spCompositing else 'TRIA_RIGHT'
        row.prop(context.scene, 'spCompositing', icon=icon, icon_only=True)
        row.label(text='Compositing Space')
        row.separator()
        if context.scene.spCompositing:
            row = layout.row()
            row.operator("nodecomp.render_imagen_compositing")
            row = layout.row()
            row.operator("nodecomp.nodosproplinks")
            row = layout.row()
            row.operator("nodecomp.getjsonnode")
            row.separator()      
        row = layout.row()
        icon = 'TRIA_DOWN' if context.scene.spActivation else 'TRIA_RIGHT'
        row.prop(context.scene, 'spActivation', icon=icon, icon_only=True)
        row.label(text='Activation Space')
        row.separator()
        if context.scene.spActivation:
            box = self.layout.box()            
            scene = context.scene
            inpUN = scene.inpUserName
            inpPW = scene.inpPassword
            inpKA = scene.keyActivation
            layout.prop(context.scene, 'inpUserName')
            layout.prop(context.scene, 'inpPassword')
            layout.prop(context.scene, 'keyActivation')            
            rowCur = layout.row()
            rowCur.operator("trial.full", icon='LAYER_ACTIVE')
            if inpUN == "Solicita Pass y User Name" and inpPW == "A elinv.elinv@gmail.com" and inpKA == "Serial activación.":
                rowCur.enabled = False
            else:
                rowCur.enabled = True
            box = self.layout.box()
def draw_menu(self, context):
    layout = self.layout
    boxNodeAdd = self.layout.box()
    layout.separator()
    layout.operator("node.copy", text="Copy Node")
    layout.operator("node.paste", text="Paste Nodes")
    layout.separator()
    layout.operator("node.clearcomparr", text="Clear Nodes Compositing")
    layout.operator("node.clearshadarr", text="Clear Nodes Shader")
classes = (PanelNuevo,
            YyKPTIWYl,
            rWeVDmfia,
            pKRjuakBD,
            NztDXFeao,    
            PeIsItoye,
            OaFuIyuGC,
            oBtrRuRoS,
            OKqkSiMhf,
            sETANlUUa,
            OGMDZFHhT,
            DOSmAUexO,
            lcewKvzaC,
            nlVAjsgps,
            CnzXPaTMV,
          )
def register():
    Scene.spShader = BoolProperty(
        default=False
    )
    Scene.spCompositing = BoolProperty(
        default=False
    )
    Scene.spActivation = BoolProperty(
        default=False
    )    
    try:
        from bpy.utils import register_class
        for cls in classes:
            register_class(cls)
    except:     
        for cls in classes:
            register_class(cls)
    bpy.types.NODE_MT_context_menu.append(draw_menu)
    bpy.types.Scene.input = bpy.props.StringProperty(name='Input',default='ShaderNodeBsdfAnisotropic')
    bpy.types.Scene.inpUserName = bpy.props.StringProperty(name='Usuario: ',default='Solicita Pass y User Name')
    bpy.types.Scene.inpPassword = bpy.props.StringProperty(name='Password: ',default='A elinv.elinv@gmail.com')
    bpy.types.Scene.keyActivation = bpy.props.StringProperty(name='Key Activation:',default='Serial activación.')
    bpy.types.Scene.myEnumTypeNodeCreator = bpy.props.EnumProperty(name="Type_Node", items={
        ("Shader","Shader","Shader",2),
        ("Compositing","Compositing","Compositing",1),
        ("Geometry","Geometry","Geometry",3),
    })
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.input        
    bpy.types.NODE_MT_context_menu.remove(draw_menu)
    del bpy.types.Scene.myEnumTypeNodeCreator
    del bpy.types.Scene.inpUserName
    del bpy.types.Scene.inpPassword    
    del bpy.types.Scene.keyActivation
if __name__ == "__main__":
    register()
