function caricaOggetti(){

var oggetti = new THREE.Object3D();

var divano = new THREE.Object3D();
var sediaARotelle = new THREE.Object3D();
var tavoloSalone = new THREE.Object3D();
var tavoloCucina = new THREE.Object3D();
var lettoGrande = new THREE.Object3D();
var lavandinoCucina = new THREE.Object3D();
var armadio = new THREE.Object3D();
var fornello = new THREE.Object3D();
var lettoStefano = new THREE.Object3D();
var armadio1 = new THREE.Object3D();
var pc = new THREE.Object3D();

var loader = new THREE.OBJLoader();
      loader.load('assets/models/largeCouch.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xeeeeee});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
      
		divano.add(mesh);
		divano.rotation.y = Math.PI;
		divano.position.set(52,-16,25);
      });
	  
var loader = new THREE.OBJLoader();
      loader.load('assets/models/officeChair3.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0x050402});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(0.04,0.04,0.04);
      
		sediaARotelle.add(mesh);
		sediaARotelle.rotation.y = Math.PI;
		sediaARotelle.position.set(33,-12,28.95);
      });
	  
var loader = new THREE.OBJLoader();
      loader.load('assets/models/table2.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0x986960});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(0.8,0.8,0.8);
      
		tavoloSalone.add(mesh);
		tavoloSalone.rotation.y = Math.PI;
		//tavoloSalone.rotation.z = Math.PI / 2;
		tavoloSalone.position.set(42,7,24);
      });
	  
var loader = new THREE.OBJLoader();
      loader.load('assets/models/tableNoire.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0x986960});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(2.5,2.5,2.5);
      
		tavoloCucina.add(mesh);
		tavoloCucina.rotation.y = Math.PI;
		//tavoloCucina.rotation.z = Math.PI / 2;
		tavoloCucina.position.set(52,23,25);
      });
	  
var loader = new THREE.OBJLoader();
      loader.load('assets/models/letto.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0x007BA7});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(0.04,0.04,0.04);
      
		lettoGrande.add(mesh);
		lettoGrande.rotation.y = Math.PI;
		lettoGrande.rotation.z = Math.PI / 2;
		lettoGrande.position.set(-3,21,24);
      });
	  
var loader = new THREE.OBJLoader();
      loader.load('assets/models/lettoSoppalcoArancio.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xFF8C69});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(0.04,0.04,0.04);
      
		lettoStefano.add(mesh);
		lettoStefano.rotation.y = Math.PI;
		lettoStefano.rotation.z = Math.PI / 2;
		lettoStefano.position.set(-3,19,24);
      });
	  
var loader = new THREE.OBJLoader();
      loader.load('assets/models/lavello_doppio_Scene.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xFFE4C4});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		//mesh.scale.set(0.04,0.04,0.04);
      
		lavandinoCucina.add(mesh);
		lavandinoCucina.rotation.y = Math.PI;
		lavandinoCucina.rotation.z = Math.PI;
		lavandinoCucina.position.set(51,29.6,27);
      });

var loader = new THREE.OBJLoader();
      loader.load('assets/models/pantry.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xFFE4C4});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(5,5,5);
      
		armadio.add(mesh);
		armadio.rotation.y = Math.PI;
		armadio.rotation.z = - Math.PI / 2;
		armadio.position.set(26,28,27);
      });

var loader = new THREE.OBJLoader();
      loader.load('assets/models/pantry.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xFFE4C4});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(4,3,6);
      
		armadio1.add(mesh);
		armadio1.rotation.y = Math.PI;
		armadio1.rotation.z =  Math.PI;
		armadio1.position.set(14,13,26);
      });
	  
var loader = new THREE.OBJLoader();
      loader.load('assets/models/cucina.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xFFE4C4});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(0.04,0.04,0.04);
      
		fornello.add(mesh);
		fornello.rotation.y = Math.PI;
		fornello.rotation.z = Math.PI;
		fornello.position.set(57,28.5,24);
      });

	  var loader = new THREE.OBJLoader();
      loader.load('assets/models/portable.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0x410012});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
		
		mesh.rotation.x = -Math.PI/2;
		mesh.position.z = 23;
		
		mesh.castShadow = true;
		mesh.receiveShadow = true;
		mesh.scale.set(0.4,0.4,0.4);
      
		pc.add(mesh);
		pc.rotation.y = Math.PI;
		pc.rotation.z =  Math.PI * 5/3;
		pc.position.set(12,13,30);
      });
	  
	  

	  
	 

oggetti.add(divano);
oggetti.add(sediaARotelle);	
oggetti.add(tavoloSalone);
oggetti.add(tavoloCucina);
oggetti.add(lettoGrande);
oggetti.add(lavandinoCucina);
oggetti.add(armadio);
oggetti.add(fornello);
oggetti.add(lettoStefano);
oggetti.add(armadio1);
oggetti.add(pc);
	
	return oggetti;
	};