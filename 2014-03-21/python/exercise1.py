#Stefano Cursi #429200

from pyplasm import *

vertsFloor1 = [[0,0],[30,0],[30,30],[0,30]]
cellsFloor1 = [[1,2,3,4]]
polsFloor1 = None
vertsDIFF = [[2,2],[28,2],[28,28],[2,28]]
cellsDIFF = [[1,2,3,4]]
polsDIFF = None
bucoCentrale = MKPOL([vertsDIFF,cellsDIFF,polsDIFF])
vertsColonna = [[0,0],[1,0],[2,1],[2,2],[1,3],[0,3],[-1,2],[-1,1]]
cellsColonna = [[1,2,3,4,5,6,7,8]]
polsColonna = None
Colonna = MKPOL([vertsColonna,cellsColonna,polsColonna])
Colonna3D = PROD([Colonna, Q(16)])
vertsFloor3 = [[27,12.5],[31,12.5],[31,17.5],[27,17.5]]
cellsFloor3 = [[1,2,3,4]]
polsFloor3 = None
vertsFloor4 = [[0,8],[8,8],[8,22],[0,22]]
cellsFloor4 = [[1,2,3,4]]
polsFloor4 = None
vertsFloor5 = [[19,12.5],[20,12.5],[20,17.5],[19,17.5]]
cellsFloor5 = [[1,2,3,4]]
polsFloor5 = None



floor1 = MKPOL([vertsFloor1, cellsFloor1, polsFloor1])
floor2 = DIFFERENCE([floor1,bucoCentrale])
floor3 = MKPOL([vertsFloor3,cellsFloor3,polsFloor3]) 
floor4 = MKPOL([vertsFloor4,cellsFloor4,polsFloor4])
floor5 = MKPOL([vertsFloor5,cellsFloor5,polsFloor5])



piani1 = COLOR([0.80,0.66,0.49])(floor1)
piani2 = COLOR([0.80,0.4,0.11])(T([1,2,3])([0,0,4])(floor2))
piani3 = COLOR([0.29,0.46,0.43])(T([1,2,3])([0,0,6])(floor3))
piani4 = COLOR([0.55,0.137,0.137])(T([1,2,3])([0,0,5])(floor4))
piani5 = COLOR([0.29,0.46,0.43])(T([1,2,3])([-12,0,6])(floor5))


Colonne = STRUCT([COLOR(WHITE)(T([1,2,3])([0,-1,0])(Colonna)),COLOR(WHITE)(T([1,2,3])([0,-1,4])(Colonna)),
	COLOR(WHITE)(T([1,2,3])([29,-1,0])(Colonna)),COLOR(WHITE)(T([1,2,3])([29,-1,4])(Colonna)),COLOR(WHITE)(T([1,2,3])([29,28,0])(Colonna)),
	COLOR(WHITE)(T([1,2,3])([29,28,4])(Colonna)),COLOR(WHITE)(T([1,2,3])([0,28,0])(Colonna)),COLOR(WHITE)(T([1,2,3])([0,28,4])(Colonna)),
	COLOR(WHITE)(T([1,2,3])([0,-1,16])(Colonna)),COLOR(WHITE)(T([1,2,3])([29,-1,16])(Colonna)),COLOR(WHITE)(T([1,2,3])([29,28,16])(Colonna)),
	COLOR(WHITE)(T([1,2,3])([0,28,16])(Colonna))])

two_and_half_model = STRUCT([piani1,piani2,piani3,piani4,piani5,Colonne])

VIEW(two_and_half_model)

