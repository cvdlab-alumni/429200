function creaShapeMuri(){
	var muri = new THREE.Object3D();

 function createMesh(geom, texture) {
		
		
		
		var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + texture)
		texture.wrapS = THREE.RepeatWrapping;
		texture.wrapT = THREE.RepeatWrapping;
		geom.computeVertexNormals();
		
		var mat = new THREE.MeshLambertMaterial({side: THREE.DoubleSide});
			mat.map = texture;
			mat.map.repeat.set(4, 4);
		var mesh = new THREE.Mesh(geom, mat);
		
	  return mesh;
		}
		
	var giardinoPlane = new THREE.PlaneGeometry(80,60,50,50);
	var giardinoPlaneShape = createMesh(giardinoPlane, "grass_texture.jpg");
	giardinoPlaneShape.position.set(32,18,0);
			
	var pavimentoCameraStefanoPlane = new THREE.PlaneGeometry(27,8,50,50);
	var pavimentoCameraStefanoShape = createMesh(pavimentoCameraStefanoPlane, "pavimentoStefano.jpg");
	pavimentoCameraStefanoShape.position.set(14.5,11,1.05);
	
	var pavimentoCameraMammaPlane = new THREE.PlaneGeometry(28,17,50,50);
	var pavimentoCameraMammaShape = createMesh(pavimentoCameraMammaPlane, "pavimentoMamma.jpg");
	pavimentoCameraMammaShape.position.set(14,23,1.05);
	
	var pavimentoCameraBagnoGrandePlane = new THREE.PlaneGeometry(9,10,50,50);
	var pavimentoCameraBagnoGrandeShape = createMesh(pavimentoCameraBagnoGrandePlane, "piastrelleCessoGrande.jpg");
	pavimentoCameraBagnoGrandeShape.position.set(32,26,1.05);
	
	var pavimentoCameraBagnoPiccoloPlane = new THREE.PlaneGeometry(6,10,50,50);
	var pavimentoCameraBagnoPiccoloShape = createMesh(pavimentoCameraBagnoPiccoloPlane, "piastrelleCessoPiccolo.jpg");
	pavimentoCameraBagnoPiccoloShape.position.set(39,26,1.05);
	
	var pavimentoCameraCucinaPlane = new THREE.PlaneGeometry(21,17,50,50);
	var pavimentoCameraCucinaShape = createMesh(pavimentoCameraCucinaPlane, "piastrelleCucina.jpg");
	pavimentoCameraCucinaShape.position.set(52,23,1.05);
	
	var pavimentoCameraSalonePlane = new THREE.PlaneGeometry(26,14,50,50);
	var pavimentoCameraSaloneShape = createMesh(pavimentoCameraSalonePlane, "pavimentoSalone.jpg");
	pavimentoCameraSaloneShape.position.set(49,8,1.05);
	
	var pavimentoEntrata1Plane = new THREE.PlaneGeometry(8,7,50,50);
	var pavimentoEntrata1Shape = createMesh(pavimentoEntrata1Plane, "pavimentoEntrata.jpg");
	pavimentoEntrata1Shape.position.set(32,11.5,1.05);
	
	var pavimentoEntrata2Plane = new THREE.PlaneGeometry(14,6,50,50);
	var pavimentoEntrata2Shape = createMesh(pavimentoEntrata2Plane, "pavimentoEntrata.jpg");
	pavimentoEntrata2Shape.position.set(35,18,1.05);
	
	
	
	function createMuroCameraStefano(cartaParati) {
		function drawShape() {
			var shapeStefano = new THREE.Shape();
				shapeStefano.moveTo(0,11);
				shapeStefano.lineTo(28,11);
				shapeStefano.lineTo(28,0);
				shapeStefano.lineTo(0,0);
				shapeStefano.lineTo(0,11);
			
		return shapeStefano;
		}
		var shape14 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shape14;		
	}
	
	var muroStefano1Shape = new createMuroCameraStefano("Bianco.jpg");
	muroStefano1Shape.rotation.x = Math.PI / 2;
	muroStefano1Shape.position.set(0,6.95,0);
	
	var muroStefano2Shape = new createMuroCameraStefano("Bianco.jpg");
	muroStefano2Shape.rotation.x = Math.PI / 2;
	muroStefano2Shape.position.set(0,8.05,0);
	
	var muroStefano3Shape = new createMuroCameraStefano("Bianco.jpg");
	muroStefano3Shape.rotation.x = Math.PI / 2;
	muroStefano3Shape.position.set(0,13.95,0);
	
	var muroStefano4Shape = new createMuroCameraStefano("Bianco.jpg");
	muroStefano4Shape.rotation.x = Math.PI / 2;
	muroStefano4Shape.position.set(0,15.05,0);
	
	
	
	
	function createMuroCameraMamma(cartaParati) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,11);
				shape.lineTo(63,11);
				shape.lineTo(63,0);
				shape.lineTo(0,0);
				shape.lineTo(0,11);
			var hole1 = new THREE.Path();
				hole1.moveTo(20,0);
				hole1.lineTo(20,9);
				hole1.lineTo(16,9);
				hole1.lineTo(16,5);
				hole1.lineTo(20,5);
				shape.holes.push(hole1);
			var hole21 = new THREE.Path();
				hole21.moveTo(33,0);
				hole21.lineTo(33,9);
				hole21.lineTo(29,9);
				hole21.lineTo(29,5);
				hole21.lineTo(33,5);
				shape.holes.push(hole21);
			var hole31 = new THREE.Path();
				hole31.moveTo(40,0);
				hole31.lineTo(40,9);
				hole31.lineTo(38,9);
				hole31.lineTo(38,5);
				hole31.lineTo(40,5);
				shape.holes.push(hole31);
			
		
		return shape;
		}
		var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
	
	return shape1;		
	}
	
	var wallCreateMuroCameraMamma1 = createMuroCameraMamma("Bianco.jpg");
		wallCreateMuroCameraMamma1.rotation.x = Math.PI / 2
		wallCreateMuroCameraMamma1.position.set(0,30.95,0);
	var wallCreateMuroCameraMamma2 = createMuroCameraMamma("Bianco.jpg");
		wallCreateMuroCameraMamma2.rotation.x = Math.PI / 2
		wallCreateMuroCameraMamma2.position.set(0,32.05,0);
		
	
	
	
	
	
		
	function createMuroCamerePorte(cartaParati) {
		function drawShape2() {
			var shapeCameraPorte = new THREE.Shape();
				shapeCameraPorte.moveTo(0,11);
				shapeCameraPorte.lineTo(25,11);
				shapeCameraPorte.lineTo(25,0);
				shapeCameraPorte.lineTo(0,0);
				shapeCameraPorte.lineTo(0,11);
			var hole2 = new THREE.Path();
				hole2.moveTo(6,0);
				hole2.lineTo(6,9);
				hole2.lineTo(2,9);
				hole2.lineTo(2,0);
				hole2.lineTo(6,0);
				shapeCameraPorte.holes.push(hole2);
			var hole3 = new THREE.Path();
				hole3.moveTo(13,0);
				hole3.lineTo(13,9);
				hole3.lineTo(9,9);
				hole3.lineTo(9,0);
				hole3.lineTo(13,0);
				shapeCameraPorte.holes.push(hole3);
			
		return shapeCameraPorte;
		}
		var shape2 = createMesh(new THREE.ShapeGeometry(drawShape2()),cartaParati);
		
	return shape2;		
	}	
	
	var wallCreateMuroCameraPorte1 = createMuroCamerePorte("Bianco.jpg");
		wallCreateMuroCameraPorte1.rotation.x = Math.PI / 2;
		wallCreateMuroCameraPorte1.rotation.y = Math.PI / 2;
		wallCreateMuroCameraPorte1.position.set(26.95,7,0);	
	var wallCreateMuroCameraPorte2 = createMuroCamerePorte("Bianco.jpg");
		wallCreateMuroCameraPorte2.rotation.x = Math.PI / 2;
		wallCreateMuroCameraPorte2.rotation.y = Math.PI / 2;
		wallCreateMuroCameraPorte2.position.set(28.05,7,0);	
		
	
	
	
	
	
	
	function createMuroCameraFinestraStefano(cartaParati) {
		function drawShape() {
			var shapeCameraFinestre = new THREE.Shape();
				shapeCameraFinestre.moveTo(0,11);
				shapeCameraFinestre.lineTo(25,11);
				shapeCameraFinestre.lineTo(25,0);
				shapeCameraFinestre.lineTo(0,0);
				shapeCameraFinestre.lineTo(0,11);
			var hole4 = new THREE.Path();
				hole4.moveTo(6,0);
				hole4.lineTo(6,9);
				hole4.lineTo(2,9);
				hole4.lineTo(2,1);
				hole4.lineTo(6,1);
				shapeCameraFinestre.holes.push(hole4);
			
		return shapeCameraFinestre;
		}
		var shape3 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shape3;		
	}
	
	var wallCreateMuroCameraFinestraStefano1 = createMuroCameraFinestraStefano("Bianco.jpg");
		wallCreateMuroCameraFinestraStefano1.rotation.x = Math.PI / 2;
		wallCreateMuroCameraFinestraStefano1.rotation.y = Math.PI / 2;
		wallCreateMuroCameraFinestraStefano1.position.set(-0.05,7,0);
	var wallCreateMuroCameraFinestraStefano2 = createMuroCameraFinestraStefano("Bianco.jpg");
		wallCreateMuroCameraFinestraStefano2.rotation.x = Math.PI / 2;
		wallCreateMuroCameraFinestraStefano2.rotation.y = Math.PI / 2;
		wallCreateMuroCameraFinestraStefano2.position.set(1.05,7,0);
	
	
	
	
	
	
	function createMuroCucinaSaloneFinestre(cartaParati) {
		function drawShape() {
			var shapeCameraCucinaSaloneFinestre = new THREE.Shape();
				shapeCameraCucinaSaloneFinestre.moveTo(0,11);
				shapeCameraCucinaSaloneFinestre.lineTo(32,11);
				shapeCameraCucinaSaloneFinestre.lineTo(32,0);
				shapeCameraCucinaSaloneFinestre.lineTo(0,0);
				shapeCameraCucinaSaloneFinestre.lineTo(0,11);
			var hole44 = new THREE.Path();
				hole44.moveTo(13,0);
				hole44.lineTo(13,9);
				hole44.lineTo(9,9);
				hole44.lineTo(9,1);
				hole44.lineTo(13,1);
				shapeCameraCucinaSaloneFinestre.holes.push(hole44);
			var hole54 = new THREE.Path();
				hole54.moveTo(24,0);
				hole54.lineTo(24,9);
				hole54.lineTo(20,9);
				hole54.lineTo(20,5);
				hole54.lineTo(24,5);
				shapeCameraCucinaSaloneFinestre.holes.push(hole54);
			
		return shapeCameraCucinaSaloneFinestre;
		}
		var shape33 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shape33;		
	}
	
	var wallCucinaSaloneFinestre1 = createMuroCucinaSaloneFinestre("Bianco.jpg");
		wallCucinaSaloneFinestre1.rotation.x = Math.PI / 2;
		wallCucinaSaloneFinestre1.rotation.y = Math.PI / 2;
		wallCucinaSaloneFinestre1.position.set(63.05,0,0);
	var wallCucinaSaloneFinestre2 = createMuroCucinaSaloneFinestre("Bianco.jpg");
		wallCucinaSaloneFinestre2.rotation.x = Math.PI / 2;
		wallCucinaSaloneFinestre2.rotation.y = Math.PI / 2;
		wallCucinaSaloneFinestre2.position.set(61.95,0,0);
	
	
	
	
	
	
	
	
	function createMuroSaloneMarco(cartaParati) {
		function drawShape() {
			var shapeSaloneMarco = new THREE.Shape();
				shapeSaloneMarco.moveTo(0,11);
				shapeSaloneMarco.lineTo(27,11);
				shapeSaloneMarco.lineTo(27,0);
				shapeSaloneMarco.lineTo(0,0);
				shapeSaloneMarco.lineTo(0,11);
			
		return shapeSaloneMarco;
		}
		var shapefattaSaloneMarco = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shapefattaSaloneMarco;		
	}
	
	var wallSaloneMarco1 = createMuroSaloneMarco("Bianco.jpg");
		wallSaloneMarco1.rotation.x = Math.PI / 2;
		wallSaloneMarco1.position.set(36,-0.05,0);
	var wallSaloneMarco2 = createMuroSaloneMarco("Bianco.jpg");
		wallSaloneMarco2.rotation.x = Math.PI / 2;
		wallSaloneMarco2.position.set(36,1.05,0);
		
	
	
	function createMuroSaloneMarcoPorta(cartaParati) {
		function drawShape() {
			var shapeSaloneMarcoPorta = new THREE.Shape();
				shapeSaloneMarcoPorta.moveTo(0,11);
				shapeSaloneMarcoPorta.lineTo(27,11);
				shapeSaloneMarcoPorta.lineTo(27,0);
				shapeSaloneMarcoPorta.lineTo(0,0);
				shapeSaloneMarcoPorta.lineTo(0,11);
			var holeportaSalone = new THREE.Path();
				holeportaSalone.moveTo(4,0);
				holeportaSalone.lineTo(4,9);
				holeportaSalone.lineTo(2,9);
				holeportaSalone.lineTo(2,0);
				holeportaSalone.lineTo(4,0);
				shapeSaloneMarcoPorta.holes.push(holeportaSalone);
			
		return shapeSaloneMarcoPorta;
		}
		var shapeSaloneMarcoPortaVar = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shapeSaloneMarcoPortaVar;		
	}
	
	var wallSaloneMarcoPorta1 = createMuroSaloneMarcoPorta("Bianco.jpg");
		wallSaloneMarcoPorta1.rotation.x = Math.PI / 2;
		wallSaloneMarcoPorta1.position.set(36,13.95,0);
	var wallSaloneMarcoPorta2 = createMuroSaloneMarcoPorta("Bianco.jpg");
		wallSaloneMarcoPorta2.rotation.x = Math.PI / 2;
		wallSaloneMarcoPorta2.position.set(36,15.05,0);
		
		
	
	
	
	
	function createMuroSeparaCase(cartaParati) {
		function drawShape() {
			var shapeMuroSepara = new THREE.Shape();
				shapeMuroSepara.moveTo(0,11);
				shapeMuroSepara.lineTo(15,11);
				shapeMuroSepara.lineTo(15,0);
				shapeMuroSepara.lineTo(0,0);
				shapeMuroSepara.lineTo(0,11);
	return shapeMuroSepara;
		}
		var shapeMuroSeparaCase = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shapeMuroSeparaCase;		
	}
	
	var muroSeparaCaseConBuco1 = createMuroSeparaCase("Bianco.jpg");
		muroSeparaCaseConBuco1.rotation.x = Math.PI / 2;
		muroSeparaCaseConBuco1.rotation.y = Math.PI / 2;
		muroSeparaCaseConBuco1.position.set(35.95,0,0);
	var muroSeparaCaseConBuco2 = createMuroSeparaCase("Bianco.jpg");
		muroSeparaCaseConBuco2.rotation.x = Math.PI / 2;
		muroSeparaCaseConBuco2.rotation.y = Math.PI / 2;
		muroSeparaCaseConBuco2.position.set(37.05,0,0);
	

	
	function createMuroSeparaCessi(cartaParati) {
		function drawShape() {
			var shapeMuroSeparaCessi = new THREE.Shape();
				shapeMuroSeparaCessi.moveTo(0,11);
				shapeMuroSeparaCessi.lineTo(11,11);
				shapeMuroSeparaCessi.lineTo(11,0);
				shapeMuroSeparaCessi.lineTo(0,0);
				shapeMuroSeparaCessi.lineTo(0,11);
	return shapeMuroSeparaCessi;
		}
		var shapeMuroSeparaCes = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shapeMuroSeparaCes;		
	}
	
	var muroSeparaCessiConBuco1 = createMuroSeparaCessi("Bianco.jpg");
		muroSeparaCessiConBuco1.rotation.x = Math.PI / 2;
		muroSeparaCessiConBuco1.rotation.y = Math.PI / 2;
		muroSeparaCessiConBuco1.position.set(35.95,21,0);
	var muroSeparaCessiConBuco2 = createMuroSeparaCessi("Bianco.jpg");
		muroSeparaCessiConBuco2.rotation.x = Math.PI / 2;
		muroSeparaCessiConBuco2.rotation.y = Math.PI / 2;
		muroSeparaCessiConBuco2.position.set(37.05,21,0);
		
	
	
	function createMuroPorta(cartaParati) {
		function drawShape() {
			var shapePorta = new THREE.Shape();
				shapePorta.moveTo(0,11);
				shapePorta.lineTo(8,11);
				shapePorta.lineTo(8,0);
				shapePorta.lineTo(0,0);
				shapePorta.lineTo(0,11);
			var holeporta = new THREE.Path();
				holeporta.moveTo(7,0);
				holeporta.lineTo(7,9);
				holeporta.lineTo(1,9);
				holeporta.lineTo(1,1);
				holeporta.lineTo(7,1);
				shapePorta.holes.push(holeporta);
			
		return shapePorta;
		}
		var shapePortaVar = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shapePortaVar;		
	}
	
	var muroPortone1 = createMuroPorta("Bianco.jpg");
		muroPortone1.rotation.x = Math.PI / 2;
		muroPortone1.position.set(28,6.95,0);
	var muroPortone2 = createMuroPorta("Bianco.jpg");
		muroPortone2.rotation.x = Math.PI / 2;
		muroPortone2.position.set(28,8.05,0);
	
	
	
	function createMuroCucinaPorta(cartaParati) {
		function drawShape() {
			var shapeCucinaPorta = new THREE.Shape();
				shapeCucinaPorta.moveTo(0,11);
				shapeCucinaPorta.lineTo(18,11);
				shapeCucinaPorta.lineTo(18,0);
				shapeCucinaPorta.lineTo(0,0);
				shapeCucinaPorta.lineTo(0,11);
			var holeCucinaporta = new THREE.Path();
				holeCucinaporta.moveTo(6,0);
				holeCucinaporta.lineTo(6,9);
				holeCucinaporta.lineTo(2,9);
				holeCucinaporta.lineTo(2,1);
				holeCucinaporta.lineTo(6,1);
				shapeCucinaPorta.holes.push(holeCucinaporta);
			
		return shapeCucinaPorta;
		}
		var shapeCucinaPortaVar = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shapeCucinaPortaVar;		
	}
	
	var muroCucinaPorta1 = createMuroCucinaPorta("Bianco.jpg");
		muroCucinaPorta1.rotation.x = Math.PI / 2;
		muroCucinaPorta1.rotation.y = Math.PI / 2;
		muroCucinaPorta1.position.set(40.95,14,0);
	var muroCucinaPorta2 = createMuroCucinaPorta("Bianco.jpg");
		muroCucinaPorta2.rotation.x = Math.PI / 2;
		muroCucinaPorta2.rotation.y = Math.PI / 2;
		muroCucinaPorta2.position.set(42.05,14,0);
	
	
	
	
	function createMuroBagni(cartaParati) {
		function drawShape() {
			var shapeBagni = new THREE.Shape();
				shapeBagni.moveTo(0,11);
				shapeBagni.lineTo(14,11);
				shapeBagni.lineTo(14,0);
				shapeBagni.lineTo(0,0);
				shapeBagni.lineTo(0,11);
			var holeBagni1 = new THREE.Path();
				holeBagni1.moveTo(5,0);
				holeBagni1.lineTo(5,9);
				holeBagni1.lineTo(1,9);
				holeBagni1.lineTo(1,0);
				holeBagni1.lineTo(5,0);
				shapeBagni.holes.push(holeBagni1);
			var holeBagni2 = new THREE.Path();
				holeBagni2.moveTo(12,0);
				holeBagni2.lineTo(12,9);
				holeBagni2.lineTo(10,9);
				holeBagni2.lineTo(10,0);
				holeBagni2.lineTo(12,0);
				shapeBagni.holes.push(holeBagni2);
			
		return shapeBagni;
		}
		var shapeCucinaPortaVar = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shapeCucinaPortaVar;		
	}
	
	var muroBagni1 = createMuroBagni("Bianco.jpg");
		muroBagni1.rotation.x = Math.PI / 2;
		muroBagni1.position.set(28,20.95,0);
	var muroBagni2 = createMuroBagni("Bianco.jpg");
		muroBagni2.rotation.x = Math.PI / 2;
		muroBagni2.position.set(28,22.05,0);
	
	
	
	muri.add(muroBagni1);
	muri.add(muroBagni2);
	muri.add(muroPortone1);
	muri.add(muroPortone2);
	muri.add(muroCucinaPorta1);
	muri.add(muroCucinaPorta2);
		
		
	muri.add(pavimentoCameraMammaShape);
	muri.add(pavimentoCameraStefanoShape);
	muri.add(pavimentoCameraBagnoGrandeShape);
	muri.add(pavimentoCameraBagnoPiccoloShape);
	muri.add(pavimentoCameraCucinaShape);
	muri.add(pavimentoCameraSaloneShape);
	muri.add(pavimentoEntrata1Shape);
	muri.add(pavimentoEntrata2Shape);
	muri.add(giardinoPlaneShape);
	
	muri.add(muroStefano3Shape);
	muri.add(muroStefano4Shape);
	muri.add(muroStefano1Shape);
	muri.add(muroStefano2Shape);
	
		
	muri.add(wallCreateMuroCameraMamma1);
	muri.add(wallCreateMuroCameraMamma2);
	
	muri.add(wallCreateMuroCameraPorte1);
	muri.add(wallCreateMuroCameraPorte2);
	
	muri.add(wallCreateMuroCameraFinestraStefano1);
	muri.add(wallCreateMuroCameraFinestraStefano2);
	
		
	muri.add(wallCucinaSaloneFinestre1);
	muri.add(wallCucinaSaloneFinestre2);
	
	muri.add(wallSaloneMarco1);
	muri.add(wallSaloneMarco2);
	
	muri.add(wallSaloneMarcoPorta1);
	muri.add(wallSaloneMarcoPorta2);	
	muri.add(muroSeparaCaseConBuco1);
	muri.add(muroSeparaCaseConBuco2);
   
	muri.add(muroSeparaCessiConBuco1);
	muri.add(muroSeparaCessiConBuco2);
	
	
	
	return muri;
};