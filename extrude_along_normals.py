# extrude object along face normals by a set distance
# mark lagana 2022

import bpy

def main():
    b_obj = bpy.data.objects['Suzanne'] # change Suzanne to your part name
    distance = 5 # distance to extrude, make negative to go opposite direction
    extrude_along_face_normals(b_obj, distance)

def extrude_along_face_normals(blender_obj, distance):
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = blender_obj
    bpy.context.active_object.select_set(True)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region={  "use_normal_flip":False,
                                                                        "use_dissolve_ortho_edges":False,
                                                                        "mirror":False},
                                            TRANSFORM_OT_shrink_fatten={"value":distance,
                                                                        "use_even_offset":False,
                                                                        "mirror":False,
                                                                        "use_proportional_edit":False,
                                                                        "proportional_edit_falloff":'SMOOTH',
                                                                        "proportional_size":1,
                                                                        "use_proportional_connected":False,
                                                                        "use_proportional_projected":False,
                                                                        "snap":False,
                                                                        "snap_target":'CLOSEST',
                                                                        "snap_point":(0, 0, 0),
                                                                        "snap_align":False,
                                                                        "snap_normal":(0, 0, 0),
                                                                        "release_confirm":False,
                                                                        "use_accurate":False})
    bpy.ops.object.editmode_toggle()
    bpy.context.active_object.select_set(False)


if __name__ == '__main__':
    main()
