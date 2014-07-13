function creaPorteFinestre(){

var PorteFinestre = new THREE.Object3D();

function createMeshPorte(x,y,z,texture1,orient) {
var geome = new THREE.BoxGeometry(x,y,z);
		var texture1 = THREE.ImageUtils.loadTexture("assets/textures/general/" + texture1)
		texture1.wrapS = THREE.RepeatWrapping;
		texture1.wrapT = THREE.RepeatWrapping;
		geome.computeVertexNormals();
		
		var mat1 = new THREE.MeshLambertMaterial({side: THREE.DoubleSide});
			mat1.map = texture1;
			//mat.map.repeat.set(4, 4);
		var mesh1 = new THREE.Mesh(geome, mat1);
		
		mesh1.position.x = -x/2*orient;
		
		
		mesh1.interact = function(){
			if(mesh1.parent.rotation.z == Math.PI / 2*orient)
			mesh1.parent.rotation.z = 0;
			else
			mesh1.parent.rotation.z = Math.PI/ 2*orient;
		};
		
	  return mesh1;
		}
		
	var portoneBox1 = createMeshPorte(3,0.7,8, "portonePrincipale.jpg",1);
	var portoneBox2 = createMeshPorte(3,0.7,8, "portonePrincipale.jpg",-1);
	var portoneMesh1 = new THREE.Object3D();
	portoneMesh1.add(portoneBox1);
	portoneMesh1.position.set(35,7.2,5);
	var portoneMesh2 = new THREE.Object3D();
	portoneMesh2.add(portoneBox2);
	portoneMesh2.position.set(29,7.2,5);
	
	/*
	var portoneBox = new THREE.BoxGeometry(3,1,8);
	var portoneShape1 = createMeshPorte(portoneBox, "portonePrincipale.jpg");
	var portoneShape2 = createMeshPorte(portoneBox, "portonePrincipale.jpg");
	portoneShape1.position.set(33.5,7.4,5);
	portoneShape2.position.set(30.5,7.4,5);
	*/
	
	
	var portaComuneBox = createMeshPorte(4,1,8, "portaComune.jpg",1);
	var portaComuneBox1 = createMeshPorte(4,1,8, "portaComune.jpg",1);
	var portaComuneBox2 = createMeshPorte(4,1,8, "portaComune.jpg",-1);
	var portaComuneBox3 = createMeshPorte(4,1,8, "portaComune.jpg",1);
	var portaComuneShape1 = new THREE.Object3D();
	portaComuneShape1.add(portaComuneBox);
	portaComuneShape1.rotation.z = Math.PI / 2;
	portaComuneShape1.position.set(27.5,13,5);
	var portaComuneShape2 = new THREE.Object3D();
	portaComuneShape2.add(portaComuneBox1);
	portaComuneShape2.rotation.z = Math.PI / 2;
	portaComuneShape2.position.set(27.5,20,5);
	var portaComuneShape3 = new THREE.Object3D();
	portaComuneShape3.add(portaComuneBox2);
	portaComuneShape3.rotation.z = - Math.PI / 2;
	portaComuneShape3.position.set(41.5,20,5);
	var portaComuneShape4 = new THREE.Object3D();
	portaComuneShape4.add(portaComuneBox3);
	portaComuneShape4.position.set(33,21.5,5);
	
	
	
	var portaPiccolaBox = createMeshPorte(2,0.5,8, "portaComune.jpg",-1);
	var portaPiccolaBox1 = createMeshPorte(2,0.5,8, "portaComune.jpg",1);
	var portaPiccolaShape1 = new THREE.Object3D();
	portaPiccolaShape1.add(portaPiccolaBox);
	portaPiccolaShape1.position.set(38,21.5,5);
	var portaPiccolaShape2 = new THREE.Object3D();
	portaPiccolaShape2.add(portaPiccolaBox1);
	portaPiccolaShape2.position.set(40,14.5,5);

	

	var finestraStefanoGeometry = new THREE.BoxGeometry(4,1,8);
	var finestraMaterial = new THREE.MeshLambertMaterial({ color: 0xABCDEF, transparent: true, opacity: 0.5});
	var vetroGrande = new THREE.Mesh(finestraStefanoGeometry, finestraMaterial);
	var vetroGrande1 = vetroGrande.clone();
	
	
	var finestraMediaGeometry = new THREE.BoxGeometry(4,1,4);
	var vetroMedio = new THREE.Mesh(finestraMediaGeometry, finestraMaterial);
	var vetroMedio1 = vetroMedio.clone();
	var vetroMedio2 = vetroMedio.clone();
	
	var finestraPiccolaGeometry = new THREE.BoxGeometry(2,1,4);
	var vetroPiccolo = new THREE.Mesh(finestraPiccolaGeometry, finestraMaterial);
	
	
	var steccaLungaBox = new THREE.BoxGeometry(0.2,1.2,8);
	var steccaLungaMaterial = new THREE.MeshLambertMaterial({ color: 0xFFFFFF});
	var steccaLungaMesh = new THREE.Mesh(steccaLungaBox,steccaLungaMaterial);
	var steccaLungaMesh1 = steccaLungaMesh.clone();
	
	var steccaCortaBox = new THREE.BoxGeometry(0.2,1.3,4);
	var steccaCortaMaterial = new THREE.MeshLambertMaterial({ color: 0xFFFFFF});
	var steccaCortaMesh = new THREE.Mesh(steccaCortaBox,steccaCortaMaterial);
	var steccaCortaMesh1 = steccaCortaMesh.clone();
	var steccaCortaMesh2 = steccaCortaMesh.clone();
	var steccaCortaMesh3 = steccaCortaMesh.clone();
	
	var steccaPiccolaBox = new THREE.BoxGeometry(0.2,1.4,2.2);
	var steccaPiccolaMaterial = new THREE.MeshLambertMaterial({ color: 0xFFFFFF});
	var steccaPiccolaMesh = new THREE.Mesh(steccaPiccolaBox,steccaPiccolaMaterial);
	var steccaPiccolaMesh1 = steccaPiccolaMesh.clone();

	var steccaCortaMeshPerMedia = new THREE.Mesh(steccaCortaBox,steccaCortaMaterial);
	var steccaCortaMeshPerPiccola = new THREE.Mesh(steccaCortaBox,steccaCortaMaterial);
	
	
	
	function FinestraGrandeConStecche(Vetro, stecca1,stecca2,stecca3,stecca4,stecca5,stecca6,orient){
		var finestraConVetroGrande = new THREE.Object3D();
		Vetro.add(stecca1);
		Vetro.add(stecca2);
		Vetro.add(stecca3);
		Vetro.add(stecca4);
		Vetro.add(stecca5);
		Vetro.add(stecca6);
		stecca1.position.set(-2,0,0);
		stecca2.position.set(2,0,0);
		stecca6.position.set(0,0,0);
		stecca3.rotation.y = Math.PI /2;
		stecca3.position.set(0,0,4);
		stecca4.rotation.y = Math.PI /2;
		stecca4.position.set(0,0,-4);
		stecca5.rotation.y = Math.PI /2;
		stecca5.position.set(0,0,0);
		
		Vetro.interact = function(){
			if(Vetro.parent.rotation.z == Math.PI / 2*orient)
			Vetro.parent.rotation.z = 0;
			else
			Vetro.parent.rotation.z = Math.PI/ 2*orient;
		};
		
		Vetro.position.set(-2,0,0);
		
		finestraConVetroGrande.add(Vetro);
		
		
		return finestraConVetroGrande;
	}
	
	function FinestraMediaConStecche(Vetro, stecca1,stecca2,stecca3,stecca4,stecca5,stecca6,orient){
		var finestraConVetroMedio = new THREE.Object3D();
		Vetro.add(stecca1);
		Vetro.add(stecca2);
		Vetro.add(stecca3);
		Vetro.add(stecca4);
		Vetro.add(stecca5);
		Vetro.add(stecca6);
		stecca1.position.set(-2,0,0);
		stecca2.position.set(2,0,0);
		stecca6.position.set(0,0,0);
		stecca3.rotation.y = Math.PI /2;
		stecca3.position.set(0,0,2);
		stecca4.rotation.y = Math.PI /2;
		stecca4.position.set(0,0,-2);
		stecca5.rotation.y = Math.PI /2;
		stecca5.position.set(0,0,0);
		
		Vetro.interact = function(){
			if(Vetro.parent.rotation.z == Math.PI / 2*orient)
			Vetro.parent.rotation.z = 0;
			else
			Vetro.parent.rotation.z = Math.PI/ 2*orient;
		};
		
		Vetro.position.set(-2,0,0);
		
		finestraConVetroMedio.add(Vetro);
		
		
		return finestraConVetroMedio;
	}
	
	function FinestraPiccolaConStecche(Vetro, stecca1,stecca2,stecca3,stecca4,stecca5,stecca6,orient){
		var finestraConVetroPiccolo = new THREE.Object3D();
		Vetro.add(stecca1);
		Vetro.add(stecca2);
		Vetro.add(stecca3);
		Vetro.add(stecca4);
		Vetro.add(stecca5);
		Vetro.add(stecca6);
		stecca1.position.set(-1,0,0);
		stecca2.position.set(1,0,0);
		stecca6.position.set(0,0,0);
		stecca3.rotation.y = Math.PI /2;
		stecca3.position.set(0,0,2);
		stecca4.rotation.y = Math.PI /2;
		stecca4.position.set(0,0,-2);
		stecca5.rotation.y = Math.PI /2;
		stecca5.position.set(0,0,0);
		
		Vetro.interact = function(){
			if(Vetro.parent.rotation.z == Math.PI / 2*orient)
			Vetro.parent.rotation.z = 0;
			else
			Vetro.parent.rotation.z = Math.PI/ 2*orient;
		};
		
		Vetro.position.set(-1,0,0);
		
		finestraConVetroPiccolo.add(Vetro);
		
		return finestraConVetroPiccolo;
	}
	
	
	
	var finestraCameraStefano = FinestraGrandeConStecche(vetroGrande,steccaLungaMesh,steccaLungaMesh.clone(),steccaCortaMesh,steccaCortaMesh.clone(),steccaCortaMesh.clone(),
														steccaLungaMesh.clone(),1);
	finestraCameraStefano.rotation.z = Math.PI /2;
	finestraCameraStefano.position.set(0.5,13,5);
	
	var finestraSalone = FinestraGrandeConStecche(vetroGrande1,steccaLungaMesh1,steccaLungaMesh1.clone(),steccaCortaMesh1,steccaCortaMesh1.clone(),steccaCortaMesh1.clone(),
														steccaLungaMesh1.clone(),1);
	finestraSalone.rotation.z = Math.PI /2;
	finestraSalone.position.set(62.5,13,5);
	
	var finestraCameraMamma = FinestraMediaConStecche(vetroMedio,steccaCortaMeshPerMedia,steccaCortaMeshPerMedia.clone(),steccaCortaMeshPerMedia.clone(),
											steccaCortaMeshPerMedia.clone(),steccaCortaMeshPerMedia.clone(),steccaCortaMeshPerMedia.clone(),-1);
	finestraCameraMamma.position.set(20,31.5,7);
	
	var finestraBagnoGrande = FinestraMediaConStecche(vetroMedio1,steccaCortaMesh2,steccaCortaMesh2.clone(),steccaCortaMesh2.clone(),
											steccaCortaMesh2.clone(),steccaCortaMesh2.clone(),steccaCortaMesh2.clone(),-1);
	finestraBagnoGrande.position.set(33,31.5,7);
	
	var finestraCucina = FinestraMediaConStecche(vetroMedio2,steccaCortaMesh3,steccaCortaMesh3.clone(),steccaCortaMesh3.clone(),
											steccaCortaMesh3.clone(),steccaCortaMesh3.clone(),steccaCortaMesh3.clone(),1);
	finestraCucina.rotation.z = Math.PI /2;
	finestraCucina.position.set(62.5,24,7);
	
	var finestraBagnoPiccolo = FinestraPiccolaConStecche(vetroPiccolo,steccaCortaMeshPerPiccola,steccaCortaMeshPerPiccola.clone(),steccaPiccolaMesh,
															steccaPiccolaMesh.clone(),steccaPiccolaMesh.clone(),steccaCortaMeshPerPiccola.clone(),-1);
	finestraBagnoPiccolo.position.set(40,31.5,7);
	
	
	
	PorteFinestre.add(portaComuneShape1);	
	PorteFinestre.add(portaComuneShape2);
	PorteFinestre.add(portaComuneShape3);
	PorteFinestre.add(portaComuneShape4);
	PorteFinestre.add(portaPiccolaShape1);
	PorteFinestre.add(portaPiccolaShape2);
	PorteFinestre.add(portoneMesh1);
	PorteFinestre.add(portoneMesh2);
	PorteFinestre.add(finestraCameraStefano);
	PorteFinestre.add(finestraSalone);
	PorteFinestre.add(finestraCameraMamma);
	PorteFinestre.add(finestraBagnoGrande);
	PorteFinestre.add(finestraCucina);
	PorteFinestre.add(finestraBagnoPiccolo);
	
	
	return PorteFinestre;
};