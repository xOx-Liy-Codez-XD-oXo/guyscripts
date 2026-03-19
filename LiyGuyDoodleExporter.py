import bpy
import bmesh
import os
import math
import struct

def writeObjPosrot(objeccy):
    worldmtx = objeccy.matrix_world
    pos = worldmtx.translation
    rot = worldmtx.to_euler()
    scl = worldmtx.to_scale()
    file.write( struct.pack('>fffffff', pos.x, pos.y, pos.z, rot.z, scl.x, scl.y, scl.z) )
    
def writeObjPosrotNormal(objeccy):
    worldmtx = objeccy.matrix_world
    pos = worldmtx.translation
    rot = worldmtx.to_euler()
    scl = worldmtx.to_scale()
    file.write( struct.pack('>fffffffff', pos.x, pos.y, pos.z, rot.x, rot.y, rot.z, scl.x, scl.y, scl.z) )

C = bpy.context

filename = "guyDoodleAnimfullseq"
liyaname = filename + ".liyab"
file = open(os.environ['HOME'] + "/" + liyaname, "wb")

framecount = 730

print("export")

bpy.context.scene.frame_current = 1853

primcount = (37 * 7) + 1 + 9
file.write(primcount.to_bytes(2, byteorder='big'))
file.write(framecount.to_bytes(2, byteorder='big'))

print(str(primcount) + "prims")

for f in range(framecount):      
    writeObjPosrot( bpy.data.objects.get("gilldoodleAsurprise") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAwave") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAwaveArmA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAwaveArmB") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAblowerA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAblowerB") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAfallhead") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAfalleyesA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAfalleyesB") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAfalltorsoA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAfalltorsoB") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAheart") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleAsadder") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBdripA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBdripB") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup1") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup2") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup3") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup4") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup5") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup6") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup7") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup8") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup9") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup10") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup11") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup12") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBgetup13") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBswoosh") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBtripA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBtripB") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBscrambletorso") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBscramblearmA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBscramblearmB") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBscramblelegsA") )
    writeObjPosrot( bpy.data.objects.get("gilldoodleBscramblelegsB") )
    writeObjPosrot( bpy.data.objects.get("doodle1") )
    file.write( struct.pack('>f', bpy.data.materials["doodle1"].node_tree.nodes["Value"].outputs[0].default_value + 0.01 ) )
    writeObjPosrotNormal( bpy.data.objects.get("pagebackdrop") )
    file.write( struct.pack('>f', bpy.data.materials["doodle2"].node_tree.nodes["Value"].outputs[0].default_value + 0.01 ) )
    writeObjPosrot( bpy.data.objects.get("doodle2") )
    file.write( struct.pack('>f', bpy.data.materials["doodle3"].node_tree.nodes["Value"].outputs[0].default_value + 0.01 ) )
    writeObjPosrot( bpy.data.objects.get("doodle3") )
    

    bpy.ops.screen.frame_offset(delta=1) 

file.close()