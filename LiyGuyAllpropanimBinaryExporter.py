import bpy
import bmesh
import os
import math
import struct

def writeObjPosrot(objeccy):
    worldmtx = objeccy.matrix_world
    pos = worldmtx.translation
    rot = worldmtx.to_euler()
    file.write( struct.pack('>ffffff', pos.x, pos.y, pos.z, rot.x, rot.y, rot.z) )

C = bpy.context

filename = "guyAllpropAnimfullseq"
liyaname = filename + ".liyab"
file = open(os.environ['HOME'] + "/" + liyaname, "wb")

framecount = 4207

print("export")

bpy.ops.screen.frame_jump(end=False)

primcount = (6 * 3) + 2
file.write(primcount.to_bytes(2, byteorder='big'))
file.write(framecount.to_bytes(2, byteorder='big'))

print(str(primcount) + "prims")

for f in range(framecount):      
    writeObjPosrot( bpy.data.objects.get("gillpencil") )
    writeObjPosrot( bpy.data.objects.get("gillnotebook_bind") )
    writeObjPosrot( bpy.data.objects.get("cafedoor_left") )
    file.write( struct.pack('>ff', bpy.data.objects.get("oplocker.004").matrix_world.to_euler().z, bpy.data.objects.get("oplocker.001").matrix_world.to_euler().z) )
    bpy.ops.screen.frame_offset(delta=1) 

file.close()