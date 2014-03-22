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


parete = PROD([floor2, Q(4)])
Entrata = PROD([floor3, Q(6)])
ReggiCipolle = PROD([floor4, Q(5)])
Balconcino = PROD([floor5, Q(6)])

#SEMI-CIRCONFERENZA
def disk2D(p):
 u,v = p
 return [v*COS(u), v*SIN(u)]
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(1)(3)])
#FINE SEMI-CIRCONFERENZA

vertsMuroNord = [[0,0],[30,0],[30,4],[0,4]]
MuroNord2D = JOIN(AA(MK)(vertsMuroNord))
MuroNord3D = PROD([MuroNord2D, Q(2)])

vertsMuroEst = [[0,0],[12,0],[12,4],[0,4]]
MuroEst2D = JOIN(AA(MK)(vertsMuroEst))
MuroEst3D = PROD([MuroEst2D, Q(2)])

vertsMuroPortaPrincipale = [[0,5],[6,5],[6,10],[0,10]]
MuroPortaPrincipale2D = JOIN(AA(MK)(vertsMuroPortaPrincipale))
MuroPortaPrincipale3D = PROD([MuroPortaPrincipale2D, Q(6)])


porta_verts = [[0.5,1],[2.5,1],[2.5,1.5],[0.5,1.5]]
porta = JOIN(AA(MK)(porta_verts))
parte_superiore_arcata = MAP(disk2D)(domain2D)
arcata = STRUCT([(T([1,2])([2,0.5])(porta)),(T([1,2])([3.5, 2]))(parte_superiore_arcata)])
tantiArchi = T(1)(-2.5)(STRUCT(NN(4)([T(1)(4),arcata])))
tantiArchiSpessi = PROD([tantiArchi, Q(4)])

#VIEW(PortonePrincipaleConDoppioArco)

arcata2 = STRUCT([(T([1,2])([1,0.5])(porta)),(T([1,2])([2.5, 2]))(parte_superiore_arcata)])
tantiArchiN = T(1)(-2.5)(STRUCT(NN(10)([T(1)(2.5),arcata])))
tantiArchiN2 = T(1)(-2.5)(STRUCT(NN(5)([T(1)(2.5),arcata2])))
tantiArchiSpessiN2 = PROD([tantiArchiN2, Q(4)])
tantiArchiSpessiN = PROD([tantiArchiN, Q(4)])
MuroNordConArchiGirato = DIFFERENCE([COLOR([0.80,0.4,0.11])(MuroNord3D), tantiArchiSpessiN])
MuroNordConArchi = (ROTATE([2,3])(PI/2))(MuroNordConArchiGirato)

MuroSudConArchi = (T([2])([32])(MuroNordConArchi))

MuroEstConArchiGirato = DIFFERENCE([COLOR([0.80,0.4,0.11])(MuroEst3D), tantiArchiSpessiN2])
MuroEstConArchi = (ROTATE([2,3])(PI/2))(MuroEstConArchiGirato)
MuroEstConArchiRuotato = (ROTATE([1,2])(PI/2))(MuroEstConArchiGirato)
MuroEstConArchiRuotatoBis = (ROTATE([1,3])(-PI/2))(MuroEstConArchiRuotato)

MuroEstAlPostoSuo1 = (T([1,2,3])([28,0,0])(MuroEstConArchiRuotatoBis))

MuroEstAlPostoSuo2 = (T([1,2,3])([28,17.8,0])(MuroEstConArchiRuotatoBis))



porta_verts1 = [[0.5,1],[2.5,1],[2.5,1.5],[0.5,1.5]]
porta1 = JOIN(AA(MK)(porta_verts1))
parte_superiore_arcata1 = MAP(disk2D)(domain2D)
arcata1 = STRUCT([(T([1,2])([2,0.5])(porta1)),(T([1,2])([3.5, 2]))(parte_superiore_arcata1)])
tantiArchi1 = (T([1,2])([-4.3,3.5])((STRUCT(NN(2)([T(1)(2.5),arcata1])))))
tantiArchiSpessi1 = PROD([tantiArchi1, Q(6)])
PortonePrincipaleConDoppioArco = DIFFERENCE([MuroPortaPrincipale3D, tantiArchiSpessi1])
PortonePrincipaleConDoppioArcoRuotato = (ROTATE([1,2])(PI/2))(PortonePrincipaleConDoppioArco)
PortonePrincipaleConDoppioArcoRuotatoBis = (ROTATE([1,3])(PI/2))(PortonePrincipaleConDoppioArcoRuotato)
PortonePrincipaleConDoppioArcoRuotatoTris = (ROTATE([1,3])(PI))(PortonePrincipaleConDoppioArcoRuotatoBis)

PortoneAlPostoSuo = (T([1,2,3])([25,12.5,-5])(PortonePrincipaleConDoppioArcoRuotatoTris))

porta_verts2 = [[0.5,1],[2.5,1],[2.5,4],[0.5,4]]
porta2 = JOIN(AA(MK)(porta_verts2))
parte_superiore_arcata2 = MAP(disk2D)(domain2D)
arcata2 = STRUCT([(T([1,2])([2,0.5])(porta2)),(T([1,2])([3.5, 4]))(parte_superiore_arcata2)])
tantiArchi2 = (T([1,2])([-4.3,3.5])((STRUCT(NN(2)([T(1)(2.5),arcata2])))))
tantiArchiSpessi2 = (T([1,2,3])([12,-5,0])((PROD([tantiArchi2, Q(6)]))))


tantiArchiSpessi2Ruotati = (ROTATE([1,2])(PI/2))(tantiArchiSpessi2)
tantiArchiSpessi2RuotatiBis = (ROTATE([1,3])(PI/2))(tantiArchiSpessi2Ruotati)
tantiArchiSpessi2RuotatiTris = (ROTATE([1,3])(PI))(tantiArchiSpessi2RuotatiBis)


arconeRosso = DIFFERENCE([Balconcino, (T([1,2,3])([17,0,0])(tantiArchiSpessi2RuotatiTris))])



sfera = COLOR([0.80,0.4,0.11])(SPHERE(2)([32,32]))
sferaGrande = COLOR([1,0.38,0.27])(SPHERE(4)([32,32]))
cipollina1 = (T([1,2,3])([1,-2,18])(sfera))
cipollina2 = (T([1,2,3])([29,-2,18])(sfera))
cipollina3 = (T([1,2,3])([29,33,18])(sfera))
cipollina4 = (T([1,2,3])([1,33,18])(sfera))
cipollina5 = (T([1,2,3])([3,9,6])(sfera))
cipollina6 = (T([1,2,3])([3,21,6])(sfera))

cipolla1 = (T([1,2,3])([3,15,8])(sferaGrande))


cono = CONE([1,1.5])(8)
cono1 = (T([1,2,3])([1,-2,20])(cono))
cono2 = (T([1,2,3])([29,-2,20])(cono))
cono3 = (T([1,2,3])([29,33,20])(cono))
cono4 = (T([1,2,3])([1,33,20])(cono))
cono5 = (T([1,2,3])([3,9,8])(cono))
cono6 = (T([1,2,3])([3,21,8])(cono))
cono7 = (T([1,2,3])([3,15,12])(cono))

colonnina = CUBOID([1,5,1])



piani1 = COLOR([0.80,0.66,0.49])(floor1)
piani2 = COLOR([0.80,0.4,0.11])(T([1,2,3])([0,0,4])(floor2))
piani3 = COLOR([0.29,0.46,0.43])(T([1,2,3])([0,0,6])(floor3))
piani4 = COLOR([0.55,0.137,0.137])(T([1,2,3])([0,0,5])(floor4))
piani5 = COLOR([0.54,0,0])(T([1,2,3])([-12,0,6])(floor5))




Colonne = STRUCT([COLOR(WHITE)(T([1,2,3])([0,-4,0])(Colonna3D)),
	COLOR(WHITE)(T([1,2,3])([29,-4,0])(Colonna3D)),COLOR(WHITE)(T([1,2,3])([29,31,0])(Colonna3D)),
	COLOR(WHITE)(T([1,2,3])([0,31,0])(Colonna3D))])


Livelli = STRUCT([piani1,piani4,piani5,Colonne])

Pareti = STRUCT([COLOR([0.80,0.4,0.11])(MuroNordConArchi),COLOR([0.80,0.4,0.11])(MuroSudConArchi),
	COLOR([0.80,0.4,0.11])(MuroEstAlPostoSuo1),COLOR([0.80,0.4,0.11])(MuroEstAlPostoSuo2),COLOR([0.29,0.46,0.43])(PortoneAlPostoSuo),COLOR([0.55,0.137,0.137])(ReggiCipolle),
	COLOR([0.54,0.137,0.137])(T([1,2,3])([-12,0,0])(arconeRosso))])

Coni = STRUCT([cono1,cono2,cono3,cono4,cono5,cono6,cono7])

solid_model_3D = STRUCT([Pareti,Livelli,cipollina1,cipollina2,cipollina3,cipollina4,cipollina5,cipollina6,cipolla1,Coni])

VIEW(solid_model_3D)







