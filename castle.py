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
mc.setBlocks(x, y, z, x+49, y+5, z+49, block.COBBLESTONE.id)
mc.setBlocks(x+3, y, z+3, x+46, y+5, z+46,  block.AIR.id)

## Build the castle and fill with air
mc.setBlocks(x+17, y, z+18, x+32, y+15, z+33, block.COBBLESTONE.id)
mc.setBlocks(x+18, y, z+19, x+31, y+14, z+32,  block.AIR.id)

## dig and fill moat with water
mc.setBlocks(x-5, y-5, z-5, x+54, y-1, z-1, block.WATER.id)
mc.setBlocks(x+50, y-5, z, x+54, y-1, z+54, block.WATER.id)
mc.setBlocks(x-1, y-5, z, x-5, y-1, z+54, block.WATER.id)
mc.setBlocks(x-5, y-5, z+50, x+54, y-1, z+54, block.WATER.id)



##Add the floor to the Mill
#mc.setBlocks(x, y-1, z, x+8, y-1, z+11, block.WOOL.id,1)

##Add a gap for the main entrance
#mc.setBlocks(x+3, y, z, x+4, y+1, z, block.AIR.id)

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
