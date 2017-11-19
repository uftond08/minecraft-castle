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

## Dig and fill moat with water
mc.setBlocks(x-3, y-3, z-3, x+32, y-1, z-1, block.WATER.id)
mc.setBlocks(x+30, y-3, z-3, x+32, y-1, z+32, block.WATER.id)
mc.setBlocks(x-1, y-3, z-3, x-3, y-1, z+32, block.WATER.id)
mc.setBlocks(x-3, y-3, z+30, x+32, y-1, z+32, block.WATER.id)

## Added a door and drawbridge 
mc.setBlocks(x+13, y, z, x+14, y+3, z+1, block.WOOD.id)
mc.setBlocks(x+21, y, z+15, x+21, y+1, z+15, block.DOOR_WOOD.id)

## Added battlements to the castle and wall
## Wall
mc.setBlocks(x+29, y+5, z, x+29, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+27, y+5, z, x+27, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+25, y+5, z, x+25, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+23, y+5, z, x+23, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+21, y+5, z, x+21, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+19, y+5, z, x+19, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+17, y+5, z, x+17, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+15, y+5, z, x+15, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+13, y+5, z, x+13, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+11, y+5, z, x+11, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+9, y+5, z, x+9, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+7, y+5, z, x+7, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+5, y+5, z, x+5, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+3, y+5, z, x+3, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x+1, y+5, z, x+1, y+5, z, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z, x, y+5, z, block.COBBLESTONE.id)

mc.setBlocks(x+29, y+5, z+29, x+29, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+27, x+29, y+5, z+27, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+25, x+29, y+5, z+25, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+23, x+29, y+5, z+23, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+21, x+29, y+5, z+21, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+19, x+29, y+5, z+19, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+17, x+29, y+5, z+17, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+15, x+29, y+5, z+15, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+13, x+29, y+5, z+13, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+11, x+29, y+5, z+11, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+9, x+29, y+5, z+9, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+7, x+29, y+5, z+7, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+5, x+29, y+5, z+5, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+3, x+29, y+5, z+3, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z+1, x+29, y+5, z+1, block.COBBLESTONE.id)
mc.setBlocks(x+29, y+5, z, x+29, y+5, z, block.COBBLESTONE.id)

mc.setBlocks(x+29, y+5, z+29, x+29, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+27, y+5, z+29, x+27, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+25, y+5, z+29, x+25, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+23, y+5, z+29, x+23, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+21, y+5, z+29, x+21, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+19, y+5, z+29, x+19, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+17, y+5, z+29, x+17, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+15, y+5, z+29, x+15, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+13, y+5, z+29, x+13, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+11, y+5, z+29, x+11, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+9, y+5, z+29, x+9, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+7, y+5, z+29, x+7, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+5, y+5, z+29, x+5, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+3, y+5, z+29, x+3, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x+1, y+5, z+29, x+1, y+5, z+29, block.COBBLESTONE.id)

mc.setBlocks(x, y+5, z+29, x, y+5, z+29, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+27, x, y+5, z+27, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+25, x, y+5, z+25, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+23, x, y+5, z+23, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+21, x, y+5, z+21, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+19, x, y+5, z+19, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+17, x, y+5, z+17, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+15, x, y+5, z+15, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+13, x, y+5, z+13, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+11, x, y+5, z+11, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+9, x, y+5, z+9, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+7, x, y+5, z+7, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+5, x, y+5, z+5, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+3, x, y+5, z+3, block.COBBLESTONE.id)
mc.setBlocks(x, y+5, z+1, x, y+5, z+1, block.COBBLESTONE.id)

## Castle
mc.setBlocks(x+10, y+11, z+20, x+10, y+11, z+20, block.COBBLESTONE.id)
mc.setBlocks(x+12, y+11, z+20, x+12, y+11, z+20, block.COBBLESTONE.id)
mc.setBlocks(x+14, y+11, z+20, x+14, y+11, z+20, block.COBBLESTONE.id)
mc.setBlocks(x+16, y+11, z+20, x+16, y+11, z+20, block.COBBLESTONE.id)
mc.setBlocks(x+18, y+11, z+20, x+18, y+11, z+20, block.COBBLESTONE.id)
 
mc.setBlocks(x+20, y+11, z+12, x+20, y+11, z+12, block.COBBLESTONE.id) 
mc.setBlocks(x+20, y+11, z+14, x+20, y+11, z+14, block.COBBLESTONE.id) 
mc.setBlocks(x+20, y+11, z+16, x+20, y+11, z+16, block.COBBLESTONE.id) 
mc.setBlocks(x+20, y+11, z+18, x+20, y+11, z+18, block.COBBLESTONE.id) 
mc.setBlocks(x+20, y+11, z+20, x+20, y+11, z+20, block.COBBLESTONE.id)

mc.setBlocks(x+20, y+11, z+10, x+20, y+11, z+10, block.COBBLESTONE.id)
mc.setBlocks(x+18, y+11, z+10, x+18, y+11, z+10, block.COBBLESTONE.id)
mc.setBlocks(x+16, y+11, z+10, x+16, y+11, z+10, block.COBBLESTONE.id)
mc.setBlocks(x+14, y+11, z+10, x+14, y+11, z+10, block.COBBLESTONE.id)
mc.setBlocks(x+12, y+11, z+10, x+12, y+11, z+10, block.COBBLESTONE.id)

mc.setBlocks(x+10, y+11, z+10, x+10, y+11, z+10, block.COBBLESTONE.id)
mc.setBlocks(x+10, y+11, z+12, x+10, y+11, z+12, block.COBBLESTONE.id)
mc.setBlocks(x+10, y+11, z+14, x+10, y+11, z+14, block.COBBLESTONE.id)
mc.setBlocks(x+10, y+11, z+16, x+10, y+11, z+16, block.COBBLESTONE.id)
mc.setBlocks(x+10, y+11, z+18, x+10, y+11, z+18, block.COBBLESTONE.id)
