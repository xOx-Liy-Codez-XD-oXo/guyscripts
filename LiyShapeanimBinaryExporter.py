import bpy
import bmesh
import os
import math
import struct

C = bpy.context

filename = C.object.name + "shapeanim"
liyaname = filename + ".liyab"
file = open(os.environ['HOME'] + "/" + liyaname, "wb")

framecount = 4207

print("export")

bpy.ops.screen.frame_jump(end=False)

primcount = len(C.object.data.shape_keys.key_blocks)-1  # includes basis so -1
file.write(primcount.to_bytes(2, byteorder='big'))
file.write(framecount.to_bytes(2, byteorder='big'))

print(str(primcount) + "prims")

for f in range(framecount):      
    for k in range(len(C.object.data.shape_keys.key_blocks)-1):
         file.write( struct.pack('>f', C.object.data.shape_keys.key_blocks[k+1].value) )
    bpy.ops.screen.frame_offset(delta=1) 

file.close()