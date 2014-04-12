#Stefano Cursi #429200

from pyplasm import *
from larcc import *



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


#SEMI-CIRCONFERENZA
def disk2D(p):
 u,v = p
 return [v*COS(u), v*SIN(u)]
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(1)(3)])
#FINE SEMI-CIRCONFERENZA

#Funzioni base larcc

def translatePoints (points, tvect): 
    return [VECTSUM([p,tvect]) for p in points]

def translatePoints (points, tvect): # d-dimensional
    return [VECTSUM([p,tvect]) for p in points]

def scalePoints (points, svect): # d-dimensional
	return [AA(PROD)(TRANS([p,svect])) for p in points]

#Funzione per creare le Sfere 
def larMap(coordFuncs):
    def larMap0(domain):
		V,CV = domain
		V = TRANS(CONS(coordFuncs)(V))
		return V,CV 
    return larMap0

def larDomain(shape):
	V,CV = larSimplexGrid(shape)
	V = scalePoints(V, [1./d for d in shape])
	return V,CV

def larIntervals(shape):
    def larIntervals0(size):
        V,CV = larDomain(shape)
        V = scalePoints(V, [scaleFactor for scaleFactor in size])
        return V,CV
    return larIntervals0


def larSphere(radius=1):
    def larSphere0(shape=[10,10]):
        V,CV = larIntervals(shape)([PI,2*PI])
        V = translatePoints(V,[-PI/2,-PI])
        domain = V,CV
        x = lambda V : [radius*COS(p[0])*SIN(p[1]) for p in V]
        y = lambda V : [radius*COS(p[0])*COS(p[1]) for p in V]
        z = lambda V : [radius*SIN(p[0]) for p in V]
        return larMap([x,y,z])(domain)
    return larSphere0


verticiMattoncino = [[1,-2],[3,-2],[3,-1],[1,-1]]
Mattoncino2D = JOIN(AA(MK)(verticiMattoncino))
Mattoncino3D = PROD([Mattoncino2D, Q(1)])
mattoncino3DAlzato = T(3)(4)(Mattoncino3D)
mattoncino3DAlzatoDiFronte = T([1,2,3])([0,33,0])(mattoncino3DAlzato)

CrestaNord = STRUCT(NN(8)([T(1)(3.2),mattoncino3DAlzato]))
CrestaTraslataNord = COLOR([0.80,0.4,0.11])(T(1)(-1)(CrestaNord))
CrestaSud = STRUCT(NN(8)([T(1)(3.2),mattoncino3DAlzatoDiFronte]))
CrestaTraslataSud = COLOR([0.80,0.4,0.11])(T(1)(-1)(CrestaSud))

mattoncinoRuotato = (ROTATE([1,2])(PI/2))(mattoncino3DAlzato)
mattoncinoRuotatoTraslato = T(1)(28)(mattoncinoRuotato)
CrestaFacciataSinistra = STRUCT(NN(4)([T(2)(3.2),mattoncinoRuotatoTraslato]))
CrestaFacciataSinistraTraslata = T(2)(-4.5)(CrestaFacciataSinistra)
CrestaFacciataSinistraColorata = COLOR([0.80,0.4,0.11])(CrestaFacciataSinistraTraslata)

CrestaFacciataDestra = T(2)(19)(CrestaFacciataSinistraColorata)
CrestaFacciataDestraColorata = COLOR([0.80,0.4,0.11])(CrestaFacciataDestra)

F = [[0,0],[0.5,0],[1,0.5],[1,1],[0.5,1.5],[0,1.5],[-0.5,1],[-0.5,0.5]]
cellsColonnine = [[1,2,3,4,5,6,7,8]]
polsColonnine = None
Colonnina = MKPOL([F, cellsColonnine, polsColonnine])
Colonnina3D = PROD([Colonnina, Q(2.2)])
Colonnina3DColorata = COLOR([0.35,0,1])(Colonnina3D)
Colonnina3DTraslata = T([1,2,3])([30,12,5])(Colonnina3DColorata)
Colonnina3DTraslata1 = T(2)(4.5)(Colonnina3DTraslata)
Colonnina3DTraslata2 = T(1)(-4)(Colonnina3DTraslata)
Colonnina3DTraslata3 = T(1)(-4)(Colonnina3DTraslata1)
Colonnina3DTraslata4 = T([1,2,3])([-19,4,0])(Colonnina3DTraslata3)
Colonnina3DTraslata5 = T(2)(-12.5)(Colonnina3DTraslata4)



vertsMuroNord = [[0,0],[30,0],[30,4],[0,4]]
MuroNord2D = JOIN(AA(MK)(vertsMuroNord))
MuroNord3D = PROD([MuroNord2D, Q(2)])


vertsMuroOvest = [[0,0],[8,0],[8,2],[0,2]]
MuroOvest2D = JOIN(AA(MK)(vertsMuroOvest))
MuroOvest3D = PROD([MuroOvest2D, Q(2)])
MuroOvest3DRuotato = (ROTATE([1,2])(PI/2))(MuroOvest3D)
MuroOvest3DRuotatoBis = (ROTATE([1,3])(-PI/2))(MuroOvest3DRuotato)
MuroOvest3DAlzato = T(3)(2)(MuroOvest3DRuotatoBis)

MuroDietroSinistra = STRUCT([MuroOvest3DAlzato,MuroOvest3DRuotatoBis])
MuroDietroDestra = T(2)(22)(MuroDietroSinistra)

vertsMuroEst = [[0,0],[12.7,0],[12.7,4],[0,4]]
MuroEst2D = JOIN(AA(MK)(vertsMuroEst))
MuroEst3D = PROD([MuroEst2D, Q(2)])

vertsMuroPortaPrincipale = [[0,5],[6,5],[6,10],[0,10]]
MuroPortaPrincipale2D = JOIN(AA(MK)(vertsMuroPortaPrincipale))
MuroPortaPrincipale3D = PROD([MuroPortaPrincipale2D, Q(6)])

vertsMuroRossoAlCentro = [[19,12.5],[20,12.5],[20,17.5],[19,17.5]]
MuroPortaRossaAlCentro2D = JOIN(AA(MK)(vertsMuroRossoAlCentro))
Balconcino = PROD([MuroPortaRossaAlCentro2D, Q(2)])
BalconcinoTraslato = T(3)(4.5)(Balconcino)


porta_verts = [[0.5,1],[2.5,1],[2.5,1.5],[0.5,1.5]]
porta = JOIN(AA(MK)(porta_verts))
parte_superiore_arcata = MAP(disk2D)(domain2D)
arcata = STRUCT([(T([1,2])([2,0.5])(porta)),(T([1,2])([3.5, 2]))(parte_superiore_arcata)])
tantiArchi = T(1)(-2.5)(STRUCT(NN(4)([T(1)(4),arcata])))
tantiArchiSpessi = PROD([tantiArchi, Q(4)])

#VIEW(PortonePrincipaleConDoppioArco)

arcata2 = STRUCT([(T([1,2])([1,0.5])(porta)),(T([1,2])([2.5, 2]))(parte_superiore_arcata)])
tantiArchiN = T(1)(-2.5)(STRUCT(NN(10)([T(1)(2.5),arcata])))
tantiArchiN2 = T(1)(-4.3)(STRUCT(NN(5)([T(1)(3.0),arcata2])))
tantiArchiN3 = T(1)(-3.6)(STRUCT(NN(5)([T(1)(3.0),arcata2])))
tantiArchiSpessiN2 = PROD([tantiArchiN2, Q(4)])
tantiArchiSpessiN3 = PROD([tantiArchiN3, Q(4)])
tantiArchiSpessiN = PROD([tantiArchiN, Q(4)])
MuroNordConArchiGirato = DIFFERENCE([COLOR([0.80,0.4,0.11])(MuroNord3D), tantiArchiSpessiN])
MuroNordConArchi = (ROTATE([2,3])(PI/2))(MuroNordConArchiGirato)

MuroSudConArchi = (T([2])([32])(MuroNordConArchi))

MuroEstConArchiGirato = DIFFERENCE([COLOR([0.80,0.4,0.11])(MuroEst3D), tantiArchiSpessiN2])
MuroEstConArchi = (ROTATE([2,3])(PI/2))(MuroEstConArchiGirato)
MuroEstConArchiRuotato = (ROTATE([1,2])(PI/2))(MuroEstConArchiGirato)
MuroEstConArchiRuotatoBis = (ROTATE([1,3])(-PI/2))(MuroEstConArchiRuotato)

MuroEstConArchiGirato1 = DIFFERENCE([COLOR([0.80,0.4,0.11])(MuroEst3D), tantiArchiSpessiN3])
MuroEstConArchi1 = (ROTATE([2,3])(PI/2))(MuroEstConArchiGirato1)
MuroEstConArchiRuotato1 = (ROTATE([1,2])(PI/2))(MuroEstConArchiGirato1)
MuroEstConArchiRuotatoBis1 = (ROTATE([1,3])(-PI/2))(MuroEstConArchiRuotato1)

MuroEstAlPostoSuo1 = (T([1,2,3])([28,0,0])(MuroEstConArchiRuotatoBis))

MuroEstAlPostoSuo2 = (T([1,2,3])([28,17.8,0])(MuroEstConArchiRuotatoBis1))



porta_verts1 = [[0.5,1],[2.5,1],[2.5,4],[0.5,4]]
porta1 = JOIN(AA(MK)(porta_verts1))
parte_superiore_arcata1 = MAP(disk2D)(domain2D)
arcata1 = STRUCT([(T([1,2])([2,0.5])(porta1)),(T([1,2])([3.5, 4.5]))(parte_superiore_arcata1)])
tantiArchi1 = (T([1,2])([-4.3,3.5])((STRUCT(NN(2)([T(1)(2.5),arcata1])))))
tantiArchiSpessi1 = PROD([tantiArchi1, Q(6)])
PortonePrincipaleConDoppioArco = DIFFERENCE([MuroPortaPrincipale3D, tantiArchiSpessi1])
PortonePrincipaleConDoppioArcoRuotato = (ROTATE([1,2])(PI/2))(PortonePrincipaleConDoppioArco)
PortonePrincipaleConDoppioArcoRuotatoBis = (ROTATE([1,3])(PI/2))(PortonePrincipaleConDoppioArcoRuotato)
PortonePrincipaleConDoppioArcoRuotatoTris = (ROTATE([1,3])(PI))(PortonePrincipaleConDoppioArcoRuotatoBis)

PortoneAlPostoSuo = (T([1,2,3])([25,12,-5])(PortonePrincipaleConDoppioArcoRuotatoTris))

porta_verts2 = [[0.5,1],[2.5,1],[2.5,4],[0.5,4]]
porta2 = JOIN(AA(MK)(porta_verts2))
parte_superiore_arcata2 = MAP(disk2D)(domain2D)
arcata2 = STRUCT([(T([1,2])([2,0.5])(porta2)),(T([1,2])([3.5, 4]))(parte_superiore_arcata2)])
tantiArchi2 = (T([1,2])([-4.3,3.5])((STRUCT(NN(2)([T(1)(2.5),arcata2])))))
tantiArchiSpessi2 = (T([1,2,3])([12,-5,0])((PROD([tantiArchi2, Q(6)]))))


tantiArchiSpessi2Ruotati = (ROTATE([1,2])(PI/2))(tantiArchiSpessi2)
tantiArchiSpessi2RuotatiBis = (ROTATE([1,3])(PI/2))(tantiArchiSpessi2Ruotati)
tantiArchiSpessi2RuotatiTris = (ROTATE([1,3])(PI))(tantiArchiSpessi2RuotatiBis)

archiFinishTraslati = T(1)(5)(tantiArchiSpessi2RuotatiTris)

arconeRosso = DIFFERENCE([ReggiCipolle, archiFinishTraslati])

V,CV = larSphere(2)()
V = translatePoints(V,[0.5,-2.5,17.5])
sfera1 = (STRUCT(MKPOLS([V,CV])))
sfera1Colorata = COLOR([0.80,0.4,0.11])(sfera1)

V,CV = larSphere(2)()
V = translatePoints(V,[29.5,-2.5,17.5])
sfera2 = (STRUCT(MKPOLS([V,CV])))
sfera2Colorata = COLOR([0.80,0.4,0.11])(sfera2)

V,CV = larSphere(2)()
V = translatePoints(V,[29.5,32.5,17.5])
sfera3 = (STRUCT(MKPOLS([V,CV])))
sfera3Colorata = COLOR([0.80,0.4,0.11])(sfera3)

V,CV = larSphere(2)()
V = translatePoints(V,[0.5,32.5,17.5])
sfera4 = (STRUCT(MKPOLS([V,CV])))
sfera4Colorata = COLOR([0.80,0.4,0.11])(sfera4)

V,CV = larSphere(2)()
V = translatePoints(V,[3,9.5,6])
sfera5 = (STRUCT(MKPOLS([V,CV])))
sfera5Colorata = COLOR([0.80,0.4,0.11])(sfera5)

V,CV = larSphere(2)()
V = translatePoints(V,[3,20.5,6])
sfera6 = (STRUCT(MKPOLS([V,CV])))
sfera6Colorata = COLOR([0.80,0.4,0.11])(sfera6)

V,CV = larSphere(0.9)()
V = translatePoints(V,[30.3,12.8,8])
sfera7 = (STRUCT(MKPOLS([V,CV])))
sfera7Colorata = COLOR([0.6,0.4,0.8])(sfera7)

sferaGrande = COLOR([1,0.38,0.27])(SPHERE(4)([32,32]))
cipollina1 = sfera1Colorata
cipollina2 = sfera2Colorata
cipollina3 = sfera3Colorata
cipollina4 = sfera4Colorata
cipollina5 = sfera5Colorata
cipollina6 = sfera6Colorata
cipollinaMini1 = sfera7Colorata
cipollinaMini2 = T(2)(4.5)(cipollinaMini1)
cipollinaMini3 = T([1,2,3])([-23,4,0])(cipollinaMini2)
cipollinaMini4 = T(2)(-12.5)(cipollinaMini3)
cipollinaMini5 = T(1)(-4)(cipollinaMini1)
cipollinaMini6 = T(1)(-4)(cipollinaMini2)

cipolla1 = (T([1,2,3])([3,15,8])(sferaGrande))


cono = COLOR([0.6,0.2,0])(CONE([1,1])(8))
conogrosso = COLOR([0.6,0.2,0])(CONE([2,1.5])(8))
cono1 = (T([1,2,3])([0.5,-2.5,19.3])(cono))
cono2 = (T([1,2,3])([29.5,-2.5,19.3])(cono))
cono3 = (T([1,2,3])([29.5,32.5,19.3])(cono))
cono4 = (T([1,2,3])([0.5,32.5,19.3])(cono))
cono5 = (T([1,2,3])([3,9.5,7.8])(cono))
cono6 = (T([1,2,3])([3,20.5,7.8])(cono))
cono7 = (T([1,2,3])([3,15,11.5])(conogrosso))

colonnina = CUBOID([1,5,1])



piani1 = COLOR([0.80,0.66,0.49])(floor1)
piani2 = COLOR([0.80,0.4,0.11])(T([1,2,3])([0,0,4])(floor2))
piani3 = COLOR([0.29,0.46,0.43])(T([1,2,3])([0,0,6])(floor3))
piani4 = COLOR([0.55,0.137,0.137])(T([1,2,3])([0,0,5])(floor4))
piani5 = COLOR([0.54,0,0])(T([1,2,3])([-12,0,6])(floor5))




Colonne = STRUCT([COLOR(WHITE)(T([1,2,3])([0,-4,0])(Colonna3D)),
	COLOR(WHITE)(T([1,2,3])([29,-4,0])(Colonna3D)),COLOR(WHITE)(T([1,2,3])([29,31,0])(Colonna3D)),
	COLOR(WHITE)(T([1,2,3])([0,31,0])(Colonna3D))])

Colonnine = STRUCT([Colonnina3DTraslata,Colonnina3DTraslata1,Colonnina3DTraslata2,Colonnina3DTraslata3,Colonnina3DTraslata4,Colonnina3DTraslata5])

Livelli = STRUCT([piani1,piani4,piani5,Colonne])

Pareti = STRUCT([COLOR([0.80,0.4,0.11])(MuroNordConArchi),COLOR([0.80,0.4,0.11])(MuroSudConArchi),
	COLOR([0.80,0.4,0.11])(MuroEstAlPostoSuo1),COLOR([0.80,0.4,0.11])(MuroEstAlPostoSuo2),COLOR([0.29,0.46,0.43])(PortoneAlPostoSuo),COLOR([0.55,0.137,0.137])(arconeRosso),
	COLOR([0.54,0.137,0.137])(T([1,2,3])([-12,0,0])(BalconcinoTraslato)),COLOR([0.80,0.4,0.11])(MuroDietroSinistra),COLOR([0.80,0.4,0.11])(MuroDietroDestra)])

Coni = STRUCT([cono1,cono2,cono3,cono4,cono5,cono6,cono7])

Cipolle = STRUCT([cipollina1,cipollina2,cipollina3,cipollina4,cipollina5,cipollina6,cipolla1])

CipolleMini = STRUCT([cipollinaMini1,cipollinaMini2,cipollinaMini3,cipollinaMini4,cipollinaMini5,cipollinaMini6])

Creste = STRUCT([CrestaTraslataNord,CrestaTraslataSud,CrestaFacciataSinistraColorata,CrestaFacciataDestraColorata])

ParetiSuLivelli = STRUCT([Pareti,Livelli,Coni,Cipolle,CipolleMini,Creste,Colonnine])

VIEW(ParetiSuLivelli)







