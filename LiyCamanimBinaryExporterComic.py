import bpy
import bmesh
import os
import math
import struct

C = bpy.context

filename = "comicCameraSeq"
liyaname = filename + ".liyab"
file = open(os.environ['HOME'] + "/" + liyaname, "wb")

framecount = 166

print("export")

bpy.ops.screen.frame_jump(end=False)

primcount = 7   # Pos, rot, fov#, dof
file.write(primcount.to_bytes(2, byteorder='big'))
file.write(framecount.to_bytes(2, byteorder='big'))

print(str(primcount) + "prims")

camOb = bpy.data.objects.get("Camera")
camCam = bpy.data.cameras["Camera"]
#focOb = bpy.data.objects.get("wiiFocus")
for f in range(framecount):      
    worldmtx = camOb.matrix_world
    pos = worldmtx.translation
    rot = worldmtx.to_euler()
    fov = camCam.angle * (180/3.141592653589793)/2
    #dof = focOb.matrix_world.translation.x
        
   # file.write( struct.pack('>ffffffff', pos.x, pos.y, pos.z, rot.x, rot.y, rot.z, fov, dof) )
    file.write( struct.pack('>fffffff', pos.x, pos.y, pos.z, rot.x, rot.y, rot.z, fov) )
    bpy.ops.screen.frame_offset(delta=1) 

file.close()