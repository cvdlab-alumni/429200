from larcc import *

master = assemblyDiagramInit([9,9,2])([[1,26,1,8,1,4,1,20,1],
                                        [1,6,1,6,1,6,1,9,1],
                                        [1,10]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

finestraCucina1 = assemblyDiagramInit([1,2,3])([[1],[2,7],[4,4,2]])
master = diagram2cell(finestraCucina1,master,159)

finestraCucina2 = assemblyDiagramInit([1,1,3])([[1],[1],[4,4,2]])
master = diagram2cell(finestraCucina2,master,157)

finestraCucina3 = assemblyDiagramInit([1,2,3])([[1],[5,1],[4,4,2]])
master = diagram2cell(finestraCucina3,master,155)

finestraSalone = assemblyDiagramInit([1,3,2])([[1],[1,4,1],[8,2]])
master = diagram2cell(finestraSalone,master,151)

portaCucina = assemblyDiagramInit([1,3,2])([[1],[1,4,1],[8,2]])
master = diagram2cell(portaCucina,master,119)

finestraCesso2 = assemblyDiagramInit([3,1,3])([[1,2,1],[1],[4,4,2]])
master = diagram2cell(finestraCesso2,master,107)

portaCesso2 = assemblyDiagramInit([3,1,2])([[1,2,1],[1],[8,2]])
master = diagram2cell(portaCesso2,master,103)

portaSalone = assemblyDiagramInit([3,1,2])([[1,2,1],[1],[8,2]])
master = diagram2cell(portaSalone,master,99)

finestraCesso1 = assemblyDiagramInit([3,1,3])([[1,4,3],[1],[4,4,2]])
master = diagram2cell(finestraCesso1,master,71)

portaCesso1 = assemblyDiagramInit([3,1,2])([[1,4,3],[1],[8,2]])
master = diagram2cell(portaCesso1,master,67)

portaEntrata = assemblyDiagramInit([3,1,2])([[1,6,1],[1],[8,2]])
master = diagram2cell(portaEntrata,master,59)

portaCameraGenitori = assemblyDiagramInit([1,3,2])([[1],[1,4,1],[8,2]])
master = diagram2cell(portaCameraGenitori,master,47)

portaCameraStefano = assemblyDiagramInit([1,3,2])([[1],[1,4,1],[8,2]])
master = diagram2cell(portaCameraStefano,master,43)

finestraCameraGenitori = assemblyDiagramInit([3,1,3])([[15,4,7],[1],[4,4,2]])
master = diagram2cell(finestraCameraGenitori,master,35)

finestraCameraStefano = assemblyDiagramInit([1,3,2])([[1],[1,4,1],[8,2]])
master = diagram2cell(finestraCameraStefano,master,7)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

emptyChain = [239,232,224,218,212,206,199,191,185,178,170,164,160,154,148,130,128,126,122,120,118,105,103,101,96,93,90,88,86,76,63,60,58,56,53,52,51,50,37,36,35,34,32,30,28,24,20,19,18,17,3,2,1,0]
solidCV = [cell for k,cell in enumerate(master[1]) if not (k in emptyChain)]

exteriorCV =  [cell for k,cell in enumerate(master[1]) if k in emptyChain]
exteriorCV += exteriorCells(master)
CV = solidCV + exteriorCV
V = master[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]

BF = boundaryCells(solidCV,FV)
boundaryFaces = [FV[face] for face in BF]
B_Rep = V,boundaryFaces

verts, triangles = quads2tria(B_Rep)
B_Rep = V,boundaryFaces
VIEW(STRUCT(MKPOLS((verts, triangles))))

def objExporter((V,FV), filePath):
    out_file = open(filePath,"w")
    out_file.write("# List of Vertices:\n")
    for v in V:
        out_file.write("v")
        for c in v:
            out_file.write(" " + str(c))
        out_file.write("\n")
    out_file.write("# Face Definitions:\n")
    for f in FV:
        out_file.write("f")
        for v in f:
            out_file.write(" " + str(v+1))
        out_file.write("\n")
    out_file.close()

objExporter((verts,triangles),"C:\Users\Marco\Desktop\ProgettoFinale.obj")