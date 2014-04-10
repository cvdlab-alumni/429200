from larcc import *

#creo la funzione per eliminare i doppioni
def face2edge(FV):
	edges = AA(sorted)(CAT([TRANS([face[:-1], face[1:]]) for face in FV]))
	edges = AA(eval)(set(AA(str)(edges)))
	return edges

#mi creo i vertici
V = [[3,3],[6,3],[13,3],[9,5],[12,5],[13,5],[15,5],[3,7],[6,7],[3,10],[5,10],[9,10],[3,12],[5,12],[9,11],[12,11],[15,11]]

#li unisco in stanze
CV=[[9,10,13,12,9],[0,1,8,7,0],[1,2,5,4,3,11,10,9,7,8],[3,4,15,14,11],[4,5,6,16,15]]

#poliline parte da un vertice e torna nello stesso 
[9,10,13,12,9]

EV=face2edge(CV)

#strumenti per i modelli
V0 = AA(LIST)([0.,3.,6.,9.,12.])
C0V = AA(LIST)(range(5))
C1V = [[0,1],[1,2],[2,3],[3,4]]



#creo i modelli
modelFloor = V0,C0V

modelEdges = (V,EV)

modelFaces = (V,CV)

modelWall = V0,C1V


# i modelli li eseguo in lar
mod2D = larModelProduct([modelFaces,modelFloor])
mod1D = larModelProduct([modelEdges,modelFloor])
mod11D = larModelProduct([modelEdges,modelWall])

#VIEW(EXPLODE(1.2,1.2,1)(MKPOLS(modelEdges)))

#VIEW(EXPLODE(1.2,1.2,1)(MKPOLS(mod1D)))

#VIEW(STRUCT(MKPOLS((mod2D))+AA(COLOR(RED))(MKPOLS((mod1D)))))

#VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS(mod11D)))

#VIEW(STRUCT(MKPOLS((mod2D))+AA(COLOR(RED))(MKPOLS((mod1D)))+(MKPOLS((mod11D)))))

VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((mod2D))+AA(COLOR(RED))(MKPOLS((mod1D)))+(MKPOLS((mod11D)))))


