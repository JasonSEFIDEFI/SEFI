// ---------- SEFI 3D ENGINE ----------

let scene, camera, renderer;
let worldline3D, originLayer3D, authLayer3D, warpLayer3D;

function init3D() {
  scene = new THREE.Scene();

  camera = new THREE.PerspectiveCamera(
    60,
    (window.innerWidth - 300) / window.innerHeight,
    0.1,
    5000
  );
  camera.position.set(0, 0, 600);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth - 300, window.innerHeight);
  renderer.setClearColor(0x000000);

  const container = document.getElementById("fieldCanvas").parentNode;
  const canvas3d = renderer.domElement;
  canvas3d.id = "threeCanvas";
  container.appendChild(canvas3d);

  // Basic lighting
  const light = new THREE.PointLight(0xffffff, 1);
  light.position.set(200, 200, 300);
  scene.add(light);

  build3DWorldline();
  animate3D();
}

