import bpy
import bmesh
import os
import math
import struct

C = bpy.context

filename = C.object.name + "finalseq"
liyaname = filename + ".liyab"
file = open(os.environ['HOME'] + "/" + liyaname, "wb")

framecount = 4207
startframe = 1

print("export")

bones = C.object.data.bones
posebones = C.object.pose.bones

bpy.context.scene.frame_current = startframe

primcount = len(bones) * 7
file.write(primcount.to_bytes(2, byteorder='big'))
file.write(framecount.to_bytes(2, byteorder='big'))

print(str(primcount) + "prims")

boneIndecies = []
boneIndeciesIdx = []
for b in range(len(bones)):
    bonename = []
    for n in range(len(bones[b].name)): 
        if (bones[b].name[n] == ","):
            break
        bonename.append(bones[b].name[n])
    bonename = int(''.join(bonename))
    boneIndecies.append(bonename)
    boneIndeciesIdx.append(b)

while(True): # sort bone indeciesidx
    sortedYet = 1
    for i in range(len(boneIndecies)-1):
        if boneIndecies[i] > boneIndecies[i+1]:
            sortedYet = 0
            b = boneIndecies[i]
            boneIndecies[i] = boneIndecies[i+1]
            boneIndecies[i+1] = b
            b = boneIndeciesIdx[i]
            boneIndeciesIdx[i] = boneIndeciesIdx[i+1]
            boneIndeciesIdx[i+1] = b
    if(sortedYet == 1):
        break
    
bonePoseIndecies = []
bonePoseIndeciesIdx = []
for b in range(len(posebones)):
    bonename = []
    for n in range(len(posebones[b].name)): 
        if (posebones[b].name[n] == ","):
            break
        bonename.append(posebones[b].name[n])
    bonename = int(''.join(bonename))
    bonePoseIndecies.append(bonename)
    bonePoseIndeciesIdx.append(b)
    
while(True): # sort bonepose indeciesidx
    sortedYet = 1
    for i in range(len(bonePoseIndecies)-1):
        if bonePoseIndecies[i] > bonePoseIndecies[i+1]:
            sortedYet = 0
            b = bonePoseIndecies[i]
            bonePoseIndecies[i] = bonePoseIndecies[i+1]
            bonePoseIndecies[i+1] = b
            b = bonePoseIndeciesIdx[i]
            bonePoseIndeciesIdx[i] = bonePoseIndeciesIdx[i+1]
            bonePoseIndeciesIdx[i+1] = b
    if(sortedYet == 1):
        break
    
boneDefaultPos = []
boneDefaultRot = []
    
for b in range(len(bones)):
    p = bones[b].matrix_local.to_translation()
    v = bones[b].matrix_local.to_quaternion()
    
    boneDefaultPos.append(p)
    boneDefaultRot.append(v)
    
#print(boneDefaultRot)
    
for f in range(framecount):
    for b in range(len(bones)):
        mtxpos = posebones[bonePoseIndeciesIdx[b]].matrix.to_translation()
        mtxpos -= boneDefaultPos[boneIndeciesIdx[b]]
        s = posebones[bonePoseIndeciesIdx[b]].matrix.to_scale()
        drot = posebones[bonePoseIndeciesIdx[b]].matrix.to_quaternion() @ boneDefaultRot[boneIndeciesIdx[b]].inverted()
        mtxpos = mtxpos - posebones[bonePoseIndeciesIdx[b]].matrix.to_translation()
        mtxpos = drot @ mtxpos
        mtxpos *= s
        mtxpos = mtxpos + posebones[bonePoseIndeciesIdx[b]].matrix.to_translation()
        p1 = mtxpos[0]
        p2 = mtxpos[1]
        p3 = mtxpos[2]
        
        drot = drot.to_euler()
        
        file.write( struct.pack('>fffffff', p1, p2, p3, drot.x, drot.y, drot.z, s.x) )
    bpy.ops.screen.frame_offset(delta=1) 

file.close()