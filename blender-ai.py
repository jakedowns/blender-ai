import bpy

class APIKeyDialogOperator(bpy.types.Operator):
    bl_idname = "object.api_key_dialog_operator"
    bl_label = "Enter API Key"
    
    api_key: bpy.props.StringProperty(name="API Key", subtype='PASSWORD')
    
    def execute(self, context):
        context.scene.api_key = self.api_key
        print("API Key stored securely")  # For debugging; remove in production
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class SimpleRESTOperator(bpy.types.Operator):
    """Trigger this operator to make a REST API call"""
    bl_idname = "object.simple_rest_operator"
    bl_label = "Call REST API"
    
    # Example property
    api_url: bpy.props.StringProperty(name="API URL")

    def execute(self, context):
        api_key = context.scene.api_key
        # Make the REST API call here using the 'requests' library and the stored api_key
        print(f"Calling API at {self.api_url} with the stored API key")
        return {'FINISHED'}

class SimpleRESTPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Simple REST API Panel"
    bl_idname = "OBJECT_PT_simple_rest"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Simple REST'

    def draw(self, context):
        layout = self.layout

        # Draw text input for API URL
        layout.prop(context.scene, "api_url")
        
        # Button to open API Key dialog
        layout.operator(APIKeyDialogOperator.bl_idname)

        # Draw the operator button for REST API call
        layout.operator(SimpleRESTOperator.bl_idname)

def register():
    bpy.utils.register_class(SimpleRESTOperator)
    bpy.utils.register_class(SimpleRESTPanel)
    bpy.utils.register_class(APIKeyDialogOperator)
    bpy.types.Scene.api_url = bpy.props.StringProperty(name="API URL")
    bpy.types.Scene.api_key = bpy.props.StringProperty(name="API Key")

def unregister():
    bpy.utils.unregister_class(SimpleRESTOperator)
    bpy.utils.unregister_class(SimpleRESTPanel)
    bpy.utils.unregister_class(APIKeyDialogOperator)
    del bpy.types.Scene.api_url
    del bpy.types.Scene.api_key

if __name__ == "__main__":
    register()
