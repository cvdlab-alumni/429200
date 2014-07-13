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

DRAW = COMP([VIEW,STRUCT,MKPOLS])

pavimento_verts = [[0,0],[19,0],[19,17],[24,17],[24,31],[0,31]]
pavimento_cells = [[1,2,3,4,5,6]]
pavimento_pols = None
cuboDiff = CUBOID([5,17,1])
cuboT = T(1)(19)(cuboDiff)

def creaTerreno():
	controlpoints=[ [[ 0,0,0],[0 ,3  ,4],[0,6,3],[0,10,0]],
   					[[ 3,0,2],[2 ,2.5,5],[3,6,5],[4,8,2]],
   					[[ 6,0,2],[8 ,3 , 5],[7,6,4.5],[6,10,2.5]],
   					[[10,0,0],[11,3  ,4],[11,6,3],[10,9,0]]
   				   ]
	domain = larDomain([20])
	dom2D = larExtrude1(domain, 20*[1./20])
	mapping = larBicubicSurface(controlpoints)
	modello = larMap(mapping)(dom2D)
	V,CV = modello
	modello = (V,[range(len(V))])
	terreno = STRUCT(MKPOLS(modello))
	return COMP([COLOR([0.09,0.44,0.27]),T([1,2])([-30,-20]),S([1,2])([2,2])])(terreno)

bozzolo = creaTerreno()

PIATTAFORM = CUBOID([48.1,31,3])
PIATTACOLOR = COLOR([0.5019,0.5019,0.5019])(PIATTAFORM)
PIATTAT = T([1,2,3])([-22,-6.3,7.3])(PIATTACOLOR)

GRID = COMP([INSR(PROD),AA(QUOTE)])
finestraCAMRS = MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[2],[1],[4]]))
finestraCAMCUC = MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[3],[1],[3]]))
finestraCAMMP = MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[1],[2],[2]]))
finestraCAMCSS2 = MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[1],[1.46],[2]]))
finestraCAMSAL = MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[3],[1],[4]]))
finestraCAMRST = T([1,3])([14,1])(finestraCAMRS)
finestraCAMSALT = T([1,2,3])([15,30,1])(finestraCAMSAL)
finestraCAMCUCT = T([1,2,3])([5,30,3])(finestraCAMCUC)
finestraCAMMPT = T([1,2,3])([0,2,3])(finestraCAMMP)
finestraCAMCSS2T = T([1,2,3])([0,18.27,3])(finestraCAMCSS2)
finestraCAMCSS1 = T(2)(11)(finestraCAMMPT)


finestre = STRUCT([finestraCAMRST,finestraCAMSALT,finestraCAMCUCT,finestraCAMMPT,finestraCAMCSS1,finestraCAMCSS2T])




PortaBase = CUBOID([3.1,1,5])
portaDiff = CUBOID([1,0.35,2])
portaDiffT = T([1,3])([0.3,0.4])(portaDiff)
portaDiffTT = T(2)(0.65)(portaDiffT)
portaDiff2 = portaDiffT
portaDiff2T = T(1)(1.4)(portaDiff2)
portaDiff2TT = T(2)(0.65)(portaDiff2T)
portaDiff3 = portaDiffT
portaDiff3T = T(3)(2.4)(portaDiff3)
portaDiff3TT = T(2)(0.65)(portaDiff3T)
portaDiff4 = portaDiff3T
portaDiff4T = T(1)(1.4)(portaDiff4)
portaDiff4TT = T(2)(0.65)(portaDiff4T)
Porta1Blocco = DIFFERENCE([PortaBase,portaDiffT,portaDiffTT,portaDiff2T,portaDiff2TT,portaDiff3T,portaDiff3TT,portaDiff4T,portaDiff4TT])
PortaColorata = COLOR([0.3960,0.2627,0.1294])(Porta1Blocco)
PortaColorataFuori = COLOR([0.5019,0.5019,0.5019])(Porta1Blocco)

sfera = COLOR([1,0.843,0])(SPHERE(0.09)([8,8]))
pomello1 = T([1,2,3])([2.8,0,2.62])(sfera)
pomello2 = T(2)(1)(pomello1)
PortaConPomello = STRUCT([PortaColorata,pomello1,pomello2])
PortoneDiFuori = STRUCT([PortaColorataFuori,pomello1,pomello2])
Portoneee = (ROTATE)([1,2])(PI/2)(PortaConPomello)

portaBaseRs = CUBOID([2,1,5])
portaNormaleDiff = CUBOID([1,0.25,4])
portaNormaleDiffT1 = T([1,3])([0.5,0.7])(portaNormaleDiff)
portaNormaleDiff2 = T([1,3])([0.5,0.7])(portaNormaleDiff)
portaNormaleDiff2T = T(2)(0.75)(portaNormaleDiff2)
portaNormale = DIFFERENCE([portaBaseRs,portaNormaleDiffT1,portaNormaleDiff2T])
PortaNormaleColorata = COLOR([0.3960,0.2627,0.1294])(portaNormale)
pomelloNormale1 = T([1,2,3])([0.3,0,2.62])(sfera)
pomelloNormale2 = T(2)(1)(pomelloNormale1)
portaPom12 = STRUCT([PortaNormaleColorata,pomelloNormale1,pomelloNormale2])
portaNormaleCAMRS = T([1,2])([14,11])(portaPom12)
portaNormaleConPomelloCAMRS = STRUCT([portaNormaleCAMRS])

portaNormaleConPomelloCAMPM = T(1)(-5)(portaNormaleConPomelloCAMRS)
portaNormaleCAMPM = S([1,2,3])([1.2,1,1])(portaNormaleConPomelloCAMPM)
portaNormaleCAMPMT = T(1)(-2)(portaNormaleCAMPM)

portaCSS1R = (ROTATE)([1,2])(PI/2)(portaNormaleConPomelloCAMRS)
portaCSS1S = S([1,2,3])([0.9,1,1])
portaCSS1T = T([1,2])([19,-1])(portaCSS1R)

portaSAL = S([1,2,3])([1,0.9,1])(portaCSS1T)
portaSALT = T([1,2])([5,6.6])(portaSAL)

portaCSS2 = S([1,2,3])([1,0.9,1])(portaSALT)
portaCSS2T = T([1,2])([-5,1.8])(portaCSS2)

portaCUC = S([1,2,3])([1.1,1,1])(portaNormaleCAMPMT)
portaCUCT = T([1,2])([-1.2,9])(portaCUC)

PortoneT = T([1,2,3])([19,12.4,0])(Portoneee)

porteTutte = STRUCT([PortoneT,portaNormaleConPomelloCAMRS,portaNormaleCAMPMT,portaCSS1T,portaSALT,portaCSS2T,portaCUCT])

Base = CUBOID([5,17,0.1])
Scalino = CUBOID([5,12,0.4])
Scalino1 = CUBOID([5,12,0.8])
Scalino2 = CUBOID([5,11,1.2])
Scalino3 = CUBOID([5,10,1.6])
Scalino4 = CUBOID([5,9,2.0])
Scalino5 = CUBOID([5,8,2.4])
Scalino6 = CUBOID([5,7,2.8])
Scalino7 = CUBOID([5,6,3.2])
Scalino8 = CUBOID([5,5,3.5])

Diff = CUBOID([6.7,5.7,1])
Diff1 = CUBOID([6.7,4.7,1])
Differenza = STRUCT([Diff,T(3)(1)(Diff1)])
#VIEW(Differenza)


SCALA1 = STRUCT([Base,Scalino,Scalino1,Scalino2,Scalino3,Scalino4,Scalino5,Scalino6,
   Scalino7,Scalino8])

SCALA = DIFFERENCE([SCALA1,Differenza])
#VIEW(SCALA)



pavimentoStrambo = MKPOL([pavimento_verts,pavimento_cells,pavimento_pols])
pavimentoStramboP = PROD([pavimentoStrambo, Q(0.3)])
pavimento = DIFFERENCE([pavimentoStramboP,cuboT])


contatoreCelle = 0
contatoreV = 0

masterMP = assemblyDiagramInit([3,3,1])([[1,11,1],[1,10,1],[7]])
V,CV = masterMP
StanzaMP = SKEL_1(STRUCT(MKPOLS(masterMP)))
StanzaMP = cellNumberingMod (masterMP,StanzaMP)(range(len(CV)),CYAN,2)
contatoreCelle = len(CV)
contatoreV = len(V)
#VIEW(StanzaMP)
toRemove = [4]
masterToRemoveMP = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
muriMP = STRUCT(MKPOLS(masterToRemoveMP))

diagram = assemblyDiagramInit([3,1,2])([[8.5,2.5,1],[1],[5,2]])
master = diagram2cell(diagram,masterToRemoveMP,4)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [9]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaMPconPorta = STRUCT(MKPOLS(master))

toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
diagram = assemblyDiagramInit([1,3,3])([[1],[1,2,7],[3,2,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaMPconPortaFinestra = STRUCT(MKPOLS(master))
#VIEW(stanzaMPconPortaFinestra)


masterRS = assemblyDiagramInit([3,3,1])([[1,5,1],[1,10,1],[7]])
V,CV = masterRS
StanzaRS = SKEL_1(STRUCT(MKPOLS(masterRS)))
StanzaRS = cellNumberingMod (masterRS,StanzaRS)(range(len(CV)),CYAN,2,contatoreCelle)
StanzaRS_traslata = T(1)(12)(StanzaRS)
contatoreCelle = len(CV) + contatoreCelle
contatoreV = len(V) + contatoreV
toRemove = [4]
masterToRemoveMS = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
muriMS = STRUCT(MKPOLS(masterToRemoveMS))
muriMSTras = T(1)(12)(muriMS)

diagram = assemblyDiagramInit([3,1,2])([[1,2,2],[1],[5,2]])
master = diagram2cell(diagram,masterToRemoveMS,4)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [9]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaMSconPorta = STRUCT(MKPOLS(master))

toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
diagram = assemblyDiagramInit([3,1,3])([[1,2,2],[1],[1,4,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaRSconPortaFinestra = STRUCT(MKPOLS(master))

stanzaRSconPortaFinestraT = T(1)(12)(stanzaRSconPortaFinestra)
#VIEW(stanzaRSconPortaFinestraT)



masterCSS1 = assemblyDiagramInit([3,3,1])([[1,6,1],[1,5,1],[7]])
V,CV = masterCSS1
StanzaCSS1 = SKEL_1(STRUCT(MKPOLS(masterCSS1)))
StanzaCSS1 = cellNumberingMod (masterCSS1,StanzaCSS1)(range(len(CV)),CYAN,2,contatoreCelle)
StanzaCSS1_traslata = T(2)(11)(StanzaCSS1)
contatoreCelle = len(CV) + contatoreCelle
contatoreV = len(V)
toRemove = [4]
masterToRemoveCSS1 = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
muriCSS1 = STRUCT(MKPOLS(masterToRemoveCSS1))
muriCSS1Tras = T(2)(11)(muriCSS1)

diagram = assemblyDiagramInit([1,3,2])([[1],[1,2,2],[5,2]])
master = diagram2cell(diagram,masterToRemoveCSS1,6)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [9]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaCSS1conPorta = STRUCT(MKPOLS(master))

toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
diagram = assemblyDiagramInit([1,3,3])([[1],[1,2,2],[3,2,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaCSS1conPortaFinestra = STRUCT(MKPOLS(master))

stanzaCSS1conPortaFinestraT = T(2)(11)(stanzaCSS1conPortaFinestra)
#VIEW(stanzaCSS1conPortaFinestraT)


masterCSS2 = assemblyDiagramInit([3,3,1])([[1,6,1],[1,2,1],[7]])
V,CV = masterCSS2
StanzaCSS2 = SKEL_1(STRUCT(MKPOLS(masterCSS2)))
StanzaCSS2 = cellNumberingMod (masterCSS2,StanzaCSS2)(range(len(CV)),CYAN,2,contatoreCelle)
StanzaCSS2_traslata = T(2)(17)(StanzaCSS2)
contatoreCelle = len(CV) + contatoreCelle
contatoreV = len(V)
toRemove = [4]
masterToRemoveCSS2 = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
muriCSS2 = STRUCT(MKPOLS(masterToRemoveCSS2))
muriCSS2Tras = T(2)(17)(muriCSS2)

diagram = assemblyDiagramInit([1,3,2])([[1],[0.3,1.6,0.3],[5,2]])
master = diagram2cell(diagram,masterToRemoveCSS2,6)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [9]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaCSS2conPorta = STRUCT(MKPOLS(master))

toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
diagram = assemblyDiagramInit([1,3,3])([[1],[0.3,1.6,0.3],[3,2,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaCSS2conPortaFinestra = STRUCT(MKPOLS(master))

stanzaCSS2conPortaFinestraT = T(2)(17)(stanzaCSS2conPortaFinestra)
#VIEW(stanzaCSS2conPortaFinestraT)


masterCUC = assemblyDiagramInit([3,3,1])([[1,11,1],[1,9,1],[7]])
V,CV = masterCUC
StanzaCUC = SKEL_1(STRUCT(MKPOLS(masterCUC)))
StanzaCUC = cellNumberingMod (masterCUC,StanzaCUC)(range(len(CV)),CYAN,2,contatoreCelle)
StanzaCUC_traslata = T(2)(20)(StanzaCUC)
contatoreCelle = len(CV) + contatoreCelle
contatoreV = len(V)
toRemove = [4]
masterToRemoveCUC = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
muriCUC = STRUCT(MKPOLS(masterToRemoveCUC))
muriCUCTras = T(2)(20)(muriCUC)

diagram = assemblyDiagramInit([3,1,2])([[8,2.8,1],[1],[5,2]])
master = diagram2cell(diagram,masterToRemoveCUC,3)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [9]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaCUCconPorta = STRUCT(MKPOLS(master))

toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
diagram = assemblyDiagramInit([3,1,3])([[4,3,4],[1],[3,3,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaCUCconPortaFinestra = STRUCT(MKPOLS(master))

stanzaCUCconPortaFinestraT = T(2)(20)(stanzaCUCconPortaFinestra)
#VIEW(stanzaCUCconPortaFinestraT)


masterSAL = assemblyDiagramInit([3,3,1])([[1,10,1],[1,12,1],[7]])
V,CV = masterSAL
StanzaSAL = SKEL_1(STRUCT(MKPOLS(masterSAL)))
StanzaSAL = cellNumberingMod (masterSAL,StanzaSAL)(range(len(CV)),CYAN,2,contatoreCelle)
StanzaSAL_traslata = T([1,2])([12,17])(StanzaSAL)
contatoreCelle = len(CV) + contatoreCelle
contatoreV = len(V)
toRemove = [4]
masterToRemoveSAL = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
muriSAL = STRUCT(MKPOLS(masterToRemoveSAL))
muriSALTras = T([1,2])([12,17])(muriSAL)

diagram = assemblyDiagramInit([1,3,2])([[1],[0.3,1.6,9.9],[5,2]])
master = diagram2cell(diagram,masterToRemoveSAL,1)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [9]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaSALconPorta = STRUCT(MKPOLS(master))

toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
diagram = assemblyDiagramInit([3,1,3])([[2,3,5],[1],[1,4,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaSALconPortaFinestra = STRUCT(MKPOLS(master))

stanzaSALconPortaFinestraT = T([1,2])([12,17])(stanzaSALconPortaFinestra)
#VIEW(stanzaSALconPortaFinestraT)


masterMuroEntrata = assemblyDiagramInit([1,1,1])([[1],[7],[7]])
V,CV = masterMuroEntrata
MuroEntrata = SKEL_1(STRUCT(MKPOLS(masterMuroEntrata)))
MuroEntrata = cellNumberingMod (masterMuroEntrata,MuroEntrata)(range(len(CV)),CYAN,2,contatoreCelle)
MuroEntrata_traslata = T([1,2])([18,11])(MuroEntrata)
contatoreCelle = len(CV) + contatoreCelle
contatoreV = len(V)
toRemove = [4]
masterToRemoveMuroEntrata = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
muriMuroEntrata = STRUCT(MKPOLS(masterToRemoveMuroEntrata))
muriMuroEntrataTras = T([1,2])([18,11])(muriMuroEntrata)

diagram = assemblyDiagramInit([1,3,2])([[1],[1,2.2,1.8],[5,2]])
master = diagram2cell(diagram,masterToRemoveMuroEntrata,0)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [2]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
stanzaMuroEntrataconPorta = STRUCT(MKPOLS(master))
stanzaMuroEntrataconPortaT = T([1,2])([18,11])(stanzaMuroEntrataconPorta)
#VIEW(stanzaMuroEntrataconPorta)


Casa = STRUCT([StanzaMP,StanzaRS_traslata,StanzaCSS1_traslata,StanzaCSS2_traslata,StanzaCUC_traslata,
	StanzaSAL_traslata,MuroEntrata_traslata])
#VIEW(Casa)

v = contatoreV
CV = contatoreCelle

CasaConMuri = STRUCT([muriMP,muriMSTras,muriCSS1Tras,muriCSS2Tras,muriCUCTras,muriSALTras,muriMuroEntrataTras])
#VIEW(CasaConMuri)

CasaConPorteFinestre = STRUCT([stanzaMPconPortaFinestra,stanzaRSconPortaFinestraT,stanzaCSS1conPortaFinestraT,stanzaCSS2conPortaFinestraT,stanzaCUCconPortaFinestraT,stanzaSALconPortaFinestraT,
	stanzaMuroEntrataconPortaT,pavimento,porteTutte,finestre])
#VIEW(CasaConPorteFinestre)

CasaRibalta = S(1)(-1)(CasaConPorteFinestre)
CasaRibaltaT = T(1)(48)(CasaRibalta)
#VIEW(CasaRibaltaT)

ScalaT = T([1,2,3])([19,0,0])(SCALA)
ScalaS = S(2)(-1)(ScalaT)
ScalaST = T([1,2,3])([5,17,3.5])(ScalaS)

Piano = STRUCT([CasaConPorteFinestre,CasaRibaltaT,ScalaT,ScalaST])
VIEW(Piano)
Piano1 = T(3)(7)(Piano)
Piano2 = T(3)(7)(Piano1)
Piano3ConScala = T(3)(7)(Piano2)
Piano3 = DIFFERENCE([Piano3ConScala,ScalaT])

sottoScala_verts = [[19,0],[19,17],[29,17],[29,0]]
sottoScala = JOIN(AA(MK)(sottoScala_verts)) 

TerrazzaSingola = T(3)(28)(pavimento)
TerrazzaSingolaRibaltata = S(1)(-1)(TerrazzaSingola)
TerrazzaSRT = T(1)(48)(TerrazzaSingolaRibaltata)
Terrazza = STRUCT([TerrazzaSRT,TerrazzaSingola])

Portone_verts = [[20,0,0],[20,0,4],[23,0,4],[23,0,0],[20,2,0],[20,2,4],[23,2,4],[23,2,0]]
Portone_J = JOIN(AA(MK)(Portone_verts))
Portone = T([1,2])([3.5,-1])(Portone_J)


parete_verts = [[19,0,0],[19,0,24.7],[29,0,24.7],[29,0,0],[19,-0.3,0],[19,-0.3,24.7],[29,-0.3,24.7],[29,-0.3,0]]
parete = JOIN(AA(MK)(parete_verts))
parete1 = DIFFERENCE([parete,Portone])


dominio = INTERVALS(1)(20)
lato_sx = BEZIER(S1)([[6.49, 3.89], [5.65, 5.52], [2.02, 5.6], [0.93, 3.98]]) 
lato_sx_map = MAP(lato_sx)(dominio)
latoProd = PROD([lato_sx_map, Q(5)])
parabola = (ROTATE)([3,2])(PI/2)(latoProd)

tenda = T([1,2,3])([4,5,36.5])(parabola)

bastone_verts = [[3,0],[2.8,0.2],[2.8,0.4],[3.2,0.4]]
bastoneBase = JOIN(AA(MK)(bastone_verts))
bastone = PROD([bastoneBase, Q(4.2)])
bastoneTetto = T([1,2,3])([2.2,5,28])(bastone)
bastoneTetto1 = T(2)(5)(bastoneTetto)
bastoneTetto2 = T(1)(5)(bastoneTetto)
bastoneTetto3 = T([1,2])([5,5])(bastoneTetto)

gazebo = STRUCT([tenda,bastoneTetto,bastoneTetto1,bastoneTetto2,bastoneTetto3])
gazebo1 = T(2)(14)(gazebo)
gazebo2 = T(1)(33)(gazebo)
gazebo3 = T(1)(33)(gazebo1)
gazebo4 = T(1)(16)(gazebo1)

insiemeGazebi = (STRUCT([gazebo,gazebo1,gazebo2,gazebo3,gazebo4]))

dominio = INTERVALS(1)(20)
ringhiera = BEZIER(S1)([[4.64, 3.76], [4.93, 5.46], [2.76, 5.51], [3.13, 3.76]])
ringhieraMap = MAP(ringhiera)(dominio)
ringhieraProd = PROD([ringhieraMap, Q(0.5)])
ringhieraMapRuotato = (ROTATE)([3,2])(PI/2)(ringhieraProd)
ringhieraMapRuotatoBis = R([3,1])(PI)(ringhieraMapRuotato)
#VIEW(ringhieraMapRuotatoBis)

ringhieraT = T([1,2,3])([4.7,0,24.5])(ringhieraMapRuotatoBis)
ringhieraSparsa = S(1)(0.9)(T(1)(-1.5)(STRUCT(NN(14)([T(1)(1.5),ringhieraT]))))
ringhieraSparsa1 = T(1)(29)(ringhieraSparsa)
ringhieraSparsa2 = S(1)(0.85)(T([1,2,3])([28.1,0,0])(STRUCT(NN(24)([T(1)(1.5),ringhieraT]))))
ringhiera_y = R([1,2])(PI/2)(ringhieraSparsa2) 
ringhieraLunga = T([1,2])([0.6,-25])(ringhiera_y)
ringhieraLungaB = T(1)(47.5)(ringhieraLunga)
ringhieraSparsaDietro = S(1)(0.85)(T(1)(-1.5)(STRUCT(NN(37)([T(1)(1.5),ringhieraT]))))
ringhieraDietro_1 = T([1,2])([0.3,30.5])(ringhieraSparsaDietro)

ringhiere = COLOR(RED)(STRUCT([ringhieraSparsa,ringhieraSparsa1,ringhieraLunga,ringhieraLungaB,ringhieraDietro_1]))

Palazzo = STRUCT([Piano,Piano1,Piano2,Piano3,sottoScala,Terrazza,parete1,tenda,insiemeGazebi,ringhiere])
VIEW(Palazzo)

PalazzoTraslato = T([1,2,3])([-22,-6.3,10.4])(Palazzo)
PortaColorataFuoriT = T([1,2,3])([1.5,-6.8,13])(PortoneDiFuori)
Cancello = S([1,2,3])([1,1,0.8])(PortaColorataFuoriT)
PalazzoSuCollina = STRUCT([bozzolo,PalazzoTraslato,PIATTAT,Cancello])
VIEW(PalazzoSuCollina)








