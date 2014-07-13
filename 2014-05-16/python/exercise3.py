from larcc import *
from lar2psm import *
from largrid import *
from morph import*
from mapper import *
from smplxn import *
from simplexn import *
from myfont import *
from splines import *   
from architectural import *
from boolean import *
from boolean1 import *
from boolean2 import *
from sysml import *

def MergeAndRemoveBlocks(diagram,master,toRemove,toMerge) : 	
	maxx = len(master[1])-1 
	master = diagram2cell(diagram,master,toMerge)
	toRemove[0] = toRemove[0]+maxx
	master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]  
	return master

def merging_numbering_elimination(diagrams,master,toRemove,toMerge) :
	for i in range(len(diagrams)) :
		V,CV = master
		maxx = len(CV)-1 #salvo il numero di cella massimo
		master = diagram2cell(diagrams[i],master,toMerge[i])
		V,CV = master 
		for j in range(len(toRemove[i])) :
			toRemove[i][j] += maxx #aggiorno i toRemove
		master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove[i])]
	return master 



master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
toRemove = [13,33,17,37]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]  #tolgo la cella num 13,33,17,37 da CV

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

toRemove = [[2],[4,10]]
toMerge = [29,34]
diagram1 = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
diagram2 = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
diagrams = [diagram1,diagram2]

master = merging_numbering_elimination(diagrams,master,toRemove,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)