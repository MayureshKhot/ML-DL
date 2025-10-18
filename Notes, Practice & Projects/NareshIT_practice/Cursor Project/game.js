// 3D Airplane Simulation Game
class AirplaneSimulation {
    constructor() {
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.airplane = null;
        this.clouds = [];
        this.terrain = null;
        
        // Airplane physics
        this.velocity = new THREE.Vector3(0, 0, 0);
        this.rotation = new THREE.Euler(0, 0, 0);
        this.speed = 0;
        this.maxSpeed = 500;
        this.throttle = 0;
        this.altitude = 0;
        
        // Controls
        this.keys = {};
        this.controls = {
            pitch: 0,
            roll: 0,
            yaw: 0
        };
        
        this.init();
        this.setupEventListeners();
        this.animate();
    }
    
    init() {
        // Create scene
        this.scene = new THREE.Scene();
        this.scene.fog = new THREE.Fog(0x87CEEB, 100, 2000);
        
        // Create camera
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10000);
        this.camera.position.set(0, 5, 10);
        
        // Create renderer
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setClearColor(0x87CEEB);
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        document.getElementById('gameContainer').appendChild(this.renderer.domElement);
        
        // Add lighting
        this.setupLighting();
        
        // Create airplane
        this.createAirplane();
        
        // Create environment
        this.createEnvironment();
        
        // Create clouds
        this.createClouds();
        
        // Handle window resize
        window.addEventListener('resize', () => this.onWindowResize());
    }
    
    setupLighting() {
        // Ambient light
        const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
        this.scene.add(ambientLight);
        
        // Directional light (sun)
        const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
        directionalLight.position.set(100, 100, 50);
        directionalLight.castShadow = true;
        directionalLight.shadow.mapSize.width = 2048;
        directionalLight.shadow.mapSize.height = 2048;
        directionalLight.shadow.camera.near = 0.5;
        directionalLight.shadow.camera.far = 500;
        directionalLight.shadow.camera.left = -100;
        directionalLight.shadow.camera.right = 100;
        directionalLight.shadow.camera.top = 100;
        directionalLight.shadow.camera.bottom = -100;
        this.scene.add(directionalLight);
    }
    
    createAirplane() {
        const airplaneGroup = new THREE.Group();
        
        // Fuselage (main body)
        const fuselageGeometry = new THREE.CylinderGeometry(0.5, 0.3, 8, 8);
        const fuselageMaterial = new THREE.MeshLambertMaterial({ color: 0xffffff });
        const fuselage = new THREE.Mesh(fuselageGeometry, fuselageMaterial);
        fuselage.castShadow = true;
        fuselage.receiveShadow = true;
        airplaneGroup.add(fuselage);
        
        // Wings
        const wingGeometry = new THREE.BoxGeometry(12, 0.2, 2);
        const wingMaterial = new THREE.MeshLambertMaterial({ color: 0xcccccc });
        const wings = new THREE.Mesh(wingGeometry, wingMaterial);
        wings.position.set(0, 0, 0);
        wings.castShadow = true;
        wings.receiveShadow = true;
        airplaneGroup.add(wings);
        
        // Tail
        const tailGeometry = new THREE.BoxGeometry(0.1, 2, 1);
        const tailMaterial = new THREE.MeshLambertMaterial({ color: 0xcccccc });
        const tail = new THREE.Mesh(tailGeometry, tailMaterial);
        tail.position.set(0, 1, -3.5);
        tail.castShadow = true;
        tail.receiveShadow = true;
        airplaneGroup.add(tail);
        
        // Horizontal stabilizer
        const stabilizerGeometry = new THREE.BoxGeometry(4, 0.1, 0.5);
        const stabilizerMaterial = new THREE.MeshLambertMaterial({ color: 0xcccccc });
        const stabilizer = new THREE.Mesh(stabilizerGeometry, stabilizerMaterial);
        stabilizer.position.set(0, 0.5, -3.5);
        stabilizer.castShadow = true;
        stabilizer.receiveShadow = true;
        airplaneGroup.add(stabilizer);
        
        // Cockpit
        const cockpitGeometry = new THREE.SphereGeometry(0.8, 8, 6);
        const cockpitMaterial = new THREE.MeshLambertMaterial({ color: 0x87CEEB, transparent: true, opacity: 0.7 });
        const cockpit = new THREE.Mesh(cockpitGeometry, cockpitMaterial);
        cockpit.position.set(0, 0.5, 2);
        cockpit.castShadow = true;
        cockpit.receiveShadow = true;
        airplaneGroup.add(cockpit);
        
        // Propeller
        const propellerGeometry = new THREE.BoxGeometry(0.1, 0.1, 4);
        const propellerMaterial = new THREE.MeshLambertMaterial({ color: 0x333333 });
        const propeller = new THREE.Mesh(propellerGeometry, propellerMaterial);
        propeller.position.set(0, 0, 4.5);
        propeller.castShadow = true;
        propeller.receiveShadow = true;
        airplaneGroup.add(propeller);
        
        this.airplane = airplaneGroup;
        this.airplane.position.set(0, 100, 0);
        this.scene.add(this.airplane);
    }
    
    createEnvironment() {
        // Create ground
        const groundGeometry = new THREE.PlaneGeometry(2000, 2000, 100, 100);
        const groundMaterial = new THREE.MeshLambertMaterial({ 
            color: 0x90EE90,
            side: THREE.DoubleSide
        });
        this.terrain = new THREE.Mesh(groundGeometry, groundMaterial);
        this.terrain.rotation.x = -Math.PI / 2;
        this.terrain.receiveShadow = true;
        this.scene.add(this.terrain);
        
        // Add some mountains in the distance
        for (let i = 0; i < 20; i++) {
            const mountainGeometry = new THREE.ConeGeometry(
                Math.random() * 50 + 20,
                Math.random() * 100 + 50,
                8
            );
            const mountainMaterial = new THREE.MeshLambertMaterial({ 
                color: 0x8B4513 
            });
            const mountain = new THREE.Mesh(mountainGeometry, mountainMaterial);
            mountain.position.set(
                (Math.random() - 0.5) * 1000,
                Math.random() * 50 + 25,
                (Math.random() - 0.5) * 1000
            );
            mountain.castShadow = true;
            mountain.receiveShadow = true;
            this.scene.add(mountain);
        }
    }
    
    createClouds() {
        for (let i = 0; i < 50; i++) {
            const cloudGroup = new THREE.Group();
            
            // Create multiple spheres to form a cloud
            for (let j = 0; j < 5; j++) {
                const cloudGeometry = new THREE.SphereGeometry(
                    Math.random() * 10 + 5,
                    8,
                    6
                );
                const cloudMaterial = new THREE.MeshLambertMaterial({ 
                    color: 0xffffff,
                    transparent: true,
                    opacity: 0.8
                });
                const cloudPart = new THREE.Mesh(cloudGeometry, cloudMaterial);
                cloudPart.position.set(
                    (Math.random() - 0.5) * 20,
                    (Math.random() - 0.5) * 10,
                    (Math.random() - 0.5) * 20
                );
                cloudGroup.add(cloudPart);
            }
            
            cloudGroup.position.set(
                (Math.random() - 0.5) * 2000,
                Math.random() * 300 + 100,
                (Math.random() - 0.5) * 2000
            );
            
            this.clouds.push(cloudGroup);
            this.scene.add(cloudGroup);
        }
    }
    
    setupEventListeners() {
        document.addEventListener('keydown', (event) => {
            this.keys[event.code] = true;
        });
        
        document.addEventListener('keyup', (event) => {
            this.keys[event.code] = false;
        });
    }
    
    handleControls() {
        // Throttle control
        if (this.keys['ArrowUp']) {
            this.throttle = Math.min(this.throttle + 0.005, 1);
        }
        if (this.keys['ArrowDown']) {
            this.throttle = Math.max(this.throttle - 0.005, 0);
        }
        
        // Pitch control
        if (this.keys['KeyW']) {
            this.controls.pitch += 0.005;
        }
        if (this.keys['KeyS']) {
            this.controls.pitch -= 0.005;
        }
        
        // Roll control
        if (this.keys['KeyA']) {
            this.controls.roll -= 0.005;
        }
        if (this.keys['KeyD']) {
            this.controls.roll += 0.005;
        }
        
        // Yaw control
        if (this.keys['KeyQ']) {
            this.controls.yaw -= 0.005;
        }
        if (this.keys['KeyE']) {
            this.controls.yaw += 0.005;
        }
        
        // Reset position
        if (this.keys['Space']) {
            this.resetPosition();
        }
        
        // Apply damping to controls
        this.controls.pitch *= 0.95;
        this.controls.roll *= 0.95;
        this.controls.yaw *= 0.95;
    }
    
    updatePhysics() {
        // Update speed based on throttle
        this.speed = this.throttle * this.maxSpeed;
        
        // Calculate velocity vector
        const direction = new THREE.Vector3(0, 0, -1);
        direction.applyEuler(this.airplane.rotation);
        this.velocity.copy(direction.multiplyScalar(this.speed * 0.01));
        
        // Apply gravity
        this.velocity.y -= 0.1;
        
        // Update position
        this.airplane.position.add(this.velocity);
        
        // Update rotation based on controls
        this.airplane.rotation.x += this.controls.pitch;
        this.airplane.rotation.z += this.controls.roll;
        this.airplane.rotation.y += this.controls.yaw;
        
        // Ground collision
        if (this.airplane.position.y < 5) {
            this.airplane.position.y = 5;
            this.velocity.y = 0;
        }
        
        // Update altitude
        this.altitude = Math.max(0, this.airplane.position.y - 5);
        
        // Update camera position (follow airplane)
        const cameraOffset = new THREE.Vector3(0, 10, 20);
        cameraOffset.applyEuler(this.airplane.rotation);
        this.camera.position.copy(this.airplane.position).add(cameraOffset);
        this.camera.lookAt(this.airplane.position);
        
        // Update UI
        this.updateUI();
    }
    
    updateUI() {
        document.getElementById('altitude').textContent = Math.round(this.altitude);
        document.getElementById('speed').textContent = Math.round(this.speed);
        document.getElementById('speedValue').textContent = Math.round(this.speed);
        document.getElementById('altitudeValue').textContent = Math.round(this.altitude);
    }
    
    resetPosition() {
        this.airplane.position.set(0, 100, 0);
        this.airplane.rotation.set(0, 0, 0);
        this.velocity.set(0, 0, 0);
        this.controls.pitch = 0;
        this.controls.roll = 0;
        this.controls.yaw = 0;
        this.throttle = 0;
    }
    
    animateClouds() {
        this.clouds.forEach(cloud => {
            cloud.position.x += 0.5;
            if (cloud.position.x > 1000) {
                cloud.position.x = -1000;
            }
        });
    }
    
    animate() {
        requestAnimationFrame(() => this.animate());
        
        this.handleControls();
        this.updatePhysics();
        this.animateClouds();
        
        this.renderer.render(this.scene, this.camera);
    }
    
    onWindowResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
}

// Start the simulation when the page loads
window.addEventListener('load', () => {
    new AirplaneSimulation();
}); 