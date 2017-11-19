import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()
x+=2

## Makes the land flat with grass
mc.setBlocks(-128, y-10,-128, 128, y-1, 128, block.DIRT.id)
mc.setBlocks(-128, y-1, -128, 128 , y, 128, block.GRASS.id)
mc.setBlocks(-128, y, -128, 128 , y+64, 128, block.AIR.id)

## Build the castle walls and fill with air
mc.setBlocks(x, y, z, x+29, y+4, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+2, y, z+2, x+27, y+4, z+27,  block.AIR.id)

## Build the castle and fill with air
mc.setBlocks(x+10, y, z+10, x+20, y+10, z+20, block.COBBLESTONE.id)
mc.setBlocks(x+11, y, z+11, x+19, y+9, z+19,  block.AIR.id)

## dig and fill moat with water
mc.setBlocks(x-3, y-3, z-3, x+32, y-1, z-1, block.WATER.id)
mc.setBlocks(x+30, y-3, z-3, x+32, y-1, z+32, block.WATER.id)
mc.setBlocks(x-1, y-3, z-3, x-3, y-1, z+32, block.WATER.id)
mc.setBlocks(x-3, y-3, z+30, x+32, y-1, z+32, block.WATER.id)

##Add a gap for the main entrance
mc.setBlocks(x+13, y, z, x+14, y+3, z+1, block.WOOD.id)
mc.setBlocks(x+21,y,z+15,x+21,y+1,z+15, block.DOOR_WOOD.id)

#x+=5

##Build the tower and fill with air
#mc.setBlocks(x, y+5, z, x+3, y+10, z+3, block.WOOD_PLANKS.id)
#mc.setBlocks(x+1, y, z+1, x+2, y+9, z+2,  block.AIR.id)

##Add the top of the tower
#mc.setBlocks(x, y+11, z, x, y+13, z, block.WOOD_PLANKS.id,)
#mc.setBlocks(x, y+11, z+3, x, y+13, z+3, block.WOOD_PLANKS.id)
#mc.setBlocks(x+3, y+11, z,x+3, y+13, z, block.WOOD_PLANKS.id)
#mc.setBlocks(x+3, y+11, z+3, x+3, y+13, z+3, block.WOOD_PLANKS.id)
#mc.setBlocks(x, y+14, z, x+3, y+14, z+3, block.WOOD_PLANKS.id)
