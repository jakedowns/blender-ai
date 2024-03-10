import bpy

# Ensure you have the 'requests' library installed for your Blender's Python
# import requests

class SimpleRESTOperator(bpy.types.Operator):
    """Trigger this operator to make a REST API call"""
    bl_idname = "object.simple_rest_operator"
    bl_label = "Call REST API"
    
    # Example properties (you can replace these with any data relevant to your API call)
    api_url: bpy.props.StringProperty(name="API URL")
    api_key: bpy.props.StringProperty(name="API Key")

    def execute(self, context):
        # Here you would make the REST API call using the 'requests' library
        # For example: response = requests.get(self.api_url, headers={"Authorization": self.api_key})
        # This is just a placeholder print statement
        print(f"Calling API at {self.api_url} with key {self.api_key}")
        
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
        # Draw text input for API Key
        layout.prop(context.scene, "api_key")

        # Draw the operator button
        layout.operator(SimpleRESTOperator.bl_idname)

def register():
    bpy.utils.register_class(SimpleRESTOperator)
    bpy.utils.register_class(SimpleRESTPanel)
    bpy.types.Scene.api_url = bpy.props.StringProperty(name="API URL")
    bpy.types.Scene.api_key = bpy.props.StringProperty(name="API Key")

def unregister():
    bpy.utils.unregister_class(SimpleRESTOperator)
    bpy.utils.unregister_class(SimpleRESTPanel)
    del bpy.types.Scene.api_url
    del bpy.types.Scene.api_key

if __name__ == "__main__":
    register()
