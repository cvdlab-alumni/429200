from larcc import * 

DRAW = COMP([VIEW,STRUCT,MKPOLS])

pavimento_verts = [[0,0],[19,0],[19,17],[24,17],[24,31],[0,31]]
pavimento_cells = [[1,2,3,4,5,6]]
pavimento_pols = None
cuboDiff = CUBOID([5,17,1])
cuboT = T(1)(19)(cuboDiff)

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
VIEW(Casa)

v = contatoreV
CV = contatoreCelle

CasaConMuri = STRUCT([muriMP,muriMSTras,muriCSS1Tras,muriCSS2Tras,muriCUCTras,muriSALTras,muriMuroEntrataTras])
VIEW(CasaConMuri)

CasaConPorteFinestre = STRUCT([stanzaMPconPortaFinestra,stanzaRSconPortaFinestraT,stanzaCSS1conPortaFinestraT,stanzaCSS2conPortaFinestraT,stanzaCUCconPortaFinestraT,stanzaSALconPortaFinestraT,
	stanzaMuroEntrataconPortaT,pavimento])
VIEW(CasaConPorteFinestre)






