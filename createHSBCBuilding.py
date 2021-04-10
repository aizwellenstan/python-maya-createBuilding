import maya.cmds as mc
if mc.window("dumWin", exists = True):
    mc.deleteUI("dumWin")
    
myWindow = mc.window("dumWin", t="Building Generator ver 0.1r", w = 300, h = 300)
mc.columnLayout(adj = True)
mc.separator(height = 10, style = "double")
mc.button(h=100, l = "Create HSBC Building", c = "hsbc()")

mc.showWindow(myWindow)

def hsbc():
    hsbcBuilding = mc.polyCube(h = 9, n = "HSBC")
    mc.move(0, 9/2.0, 0, hsbcBuilding)
    mc.polyExtrudeFacet(hsbcBuilding[0] + ".f[1]", ltz = .5, ls = (.1, .1, 0))
    mc.select(clear = True)
