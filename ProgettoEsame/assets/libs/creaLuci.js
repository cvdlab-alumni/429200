function creaLuci(){
var luci = new THREE.Object3D();

var lampadario = new THREE.Object3D();
	var target = new THREE.BoxGeometry(1,1,1);
	var targetMaterial = new THREE.MeshLambertMaterial({transparent: true, opacity: 0});
	var targetMesh = new THREE.Mesh(target,targetMaterial);
	targetMesh.position.set(0,-10,0);
	
	
	var bottone1 = creaBottone();
		bottone1.position.set(12,-4,7.9);
		
	var bottone2 = creaBottone();
		bottone2.position.set(11,-4,2.9);
	
	var bottone3 = creaBottone();
		bottone3.position.set(-4.5,-4,7.9);
		
	var bottone4 = creaBottone();
		bottone4.position.set(-3.4,-4,4.2);
		
	var bottone5 = creaBottone();
		bottone5.position.set(1.4,-4,4.2);
		
	var bottone6 = creaBottone();
		bottone6.rotation.y = Math.PI / 2;
		bottone6.position.set(-9.9,-4,2);
		
	var bottone7 = creaBottone();
		bottone7.position.set(-9,-4,-6.8);
	
	
	function creaBottone(){
	
		var bottone = new THREE.BoxGeometry(0.5,0.8,0.2);
		var bottoneMaterial = new THREE.MeshLambertMaterial({color: 0x000000});
		var bottoneMesh = new THREE.Mesh(bottone,bottoneMaterial);
	
	
		bottoneMesh.interact = function(){
		if(bottoneMesh.parent.children[1].intensity == 0)
			{
			bottoneMesh.parent.children[1].intensity = 2;
			bottoneMesh.parent.children[3].material = new THREE.MeshLambertMaterial({color: 0xFFFFFF, transparent: true, opacity:1, side: THREE.BackSide});
			}
			
		else{
			bottoneMesh.parent.children[1].intensity = 0;
			bottoneMesh.parent.children[3].material = new THREE.MeshLambertMaterial({color: 0xffffff, transparent: true, opacity: 0.3, side: THREE.FrontSide});
			}
	}
	
	return bottoneMesh;
	}
	
	var SpotLightGiardino = new THREE.SpotLight(0xffffff);
		SpotLightGiardino.intensity = 2;
		SpotLightGiardino.angle = 180 * Math.PI / 180;
		SpotLightGiardino.exponent = 0;
		SpotLightGiardino.distance = 30;
		SpotLightGiardino.position.set(22,-9,10);
		SpotLightGiardino.target = targetMesh;
		
	
	
	
	
	var SpotLight = new THREE.SpotLight(0xffffff);
		SpotLight.intensity = 2;
		SpotLight.angle = 180 * Math.PI / 180;
		SpotLight.exponent = 0;
		SpotLight.distance = 22;
		SpotLight.position.set(0,0,0);
		SpotLight.target = targetMesh;
		
		var SpotLightBagni = new THREE.SpotLight(0xffffff);
		SpotLightBagni.intensity = 1;
		SpotLightBagni.angle = 180 * Math.PI / 180;
		SpotLightBagni.exponent = 0;
		SpotLightBagni.distance = 22;
		SpotLightBagni.position.set(0,0,0);
		SpotLightBagni.target = targetMesh;
		
	var PointLight = new THREE.PointLight(0xffffff);
	PointLight.distance = 5;
		
		lampadario.add(bottone1);
		lampadario.add(SpotLight);
		//lampadario.add(PointLight);
		lampadario.add(targetMesh);
	
	
	var lampadario2 = new THREE.Object3D();
	lampadario2.position.set(14,11,9);
	lampadario2.add(bottone2);
	lampadario2.add(SpotLight.clone());
	//lampadario2.add(PointLight.clone());
	lampadario2.add(targetMesh.clone());
	
	
	var lampadario3 = new THREE.Object3D();
	lampadario3.position.set(33,16,9);
	lampadario3.add(bottone3);
	lampadario3.add(SpotLightBagni);
	//lampadario3.add(PointLight.clone());
	lampadario3.add(targetMesh.clone());
	
	var lampadario4 = new THREE.Object3D();
	lampadario4.position.set(32,26.5,9);
	lampadario4.add(bottone4);
	lampadario4.add(SpotLightBagni.clone());
	//lampadario4.add(PointLight.clone());
	lampadario4.add(targetMesh.clone());
	
	
	var lampadario5 = new THREE.Object3D();
	lampadario5.position.set(39,26.5,9);
	lampadario5.add(bottone5);
	lampadario5.add(SpotLightBagni.clone());
	//lampadario5.add(PointLight.clone());
	lampadario5.add(targetMesh.clone());
	
	
	var lampadario6 = new THREE.Object3D();
	lampadario6.position.set(52,23,9);
	lampadario6.add(bottone6);
	lampadario6.add(SpotLight.clone());
	//lampadario6.add(PointLight.clone());
	lampadario6.add(targetMesh.clone());
	
	
	var lampadario7 = new THREE.Object3D();
	lampadario7.position.set(50,7,9);
	lampadario7.add(bottone7);
	lampadario7.add(SpotLight.clone());
	//lampadario7.add(PointLight.clone());
	lampadario7.add(targetMesh.clone());
	
	var loader = new THREE.OBJLoader();
		loader.load("assets/models/lustreBoule.obj", function (obj) {

		global_o = obj;

		var material = new THREE.MeshLambertMaterial({color: 0xFFFFFF, transparent: true, opacity:1, side: THREE.BackSide});
		
		obj.children[0].material = material;
		mesh = obj.children[0];
		
		mesh.rotation.x = Math.PI;
			
		mesh.castShadow = true;
		mesh.receiveShadow = true;
			
		mesh.scale.set(0.04,0.04,0.04);
		mesh.rotation.z = Math.PI;
		
		//mesh.position.set(0,9,0);
		lampadario.add(mesh);
		lampadario.position.set(14,23,9);
		lampadario.rotation.x = Math.PI/2;
		
		
		lampadario2.add(mesh.clone());
		lampadario2.rotation.x = Math.PI/2;
		
		lampadario3.add(mesh.clone());
		lampadario3.rotation.x = Math.PI/2;

		lampadario4.add(mesh.clone());
		lampadario4.rotation.x = Math.PI/2;
		
		lampadario5.add(mesh.clone());
		lampadario5.rotation.x = Math.PI/2;
		
		lampadario6.add(mesh.clone());
		lampadario6.rotation.x = Math.PI/2;
		
		lampadario7.add(mesh.clone());
		lampadario7.rotation.x = Math.PI/2;
		
	
		
		
		});
		
		var SpotLightGiardino1 = SpotLightGiardino.clone();
		SpotLightGiardino1.position.x = -10;
		var SpotLightGiardino2 = SpotLightGiardino.clone();
		SpotLightGiardino2.position.set(50,-12,10);
		var SpotLightGiardino3 = SpotLightGiardino.clone();
		SpotLightGiardino3.position.set(40,50,10);
		var SpotLightGiardino4 = SpotLightGiardino.clone();
		SpotLightGiardino4.position.set(16,50,10);
		var SpotLightGiardino5 = SpotLightGiardino.clone();
		SpotLightGiardino5.position.set(63,50,10);		
		var SpotLightGiardino6 = SpotLightGiardino.clone();
		SpotLightGiardino6.position.set(-10,30,10);		
		var SpotLightGiardino7 = SpotLightGiardino.clone();
		SpotLightGiardino7.position.set(77,10,10);		
		
		luci.add(lampadario);
		luci.add(lampadario2);
		luci.add(lampadario3);
		luci.add(lampadario4);
		luci.add(lampadario5);
		luci.add(lampadario6);
		luci.add(lampadario7);
		luci.add(SpotLightGiardino);
		luci.add(SpotLightGiardino1);
		luci.add(SpotLightGiardino2);
		luci.add(SpotLightGiardino3);
		luci.add(SpotLightGiardino4);
		luci.add(SpotLightGiardino5);
		luci.add(SpotLightGiardino6);
		luci.add(SpotLightGiardino7);
			
		return luci;
	
};