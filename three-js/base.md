```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Hello Three.js!</title>
 <script src="https://cdn.rawgit.com/mrdoob/three.js/r102/build/three.js"></script>
<script src="https://cdn.rawgit.com/mrdoob/three.js/r102/examples/js/controls/OrbitControls.js"></script>
</head>
 
<body>
  <canvas id="canvas"></canvas>
<body>
</html>
```

```js
const width = 480;
const height = 480;
const fov = 60;
const aspect = width / height;
const near = 1;
const far = 1000;

const main = () => {
  //シーン
  const scene = new THREE.Scene();
  const axis = new THREE.AxisHelper(50);
  scene.add(axis);
  
  //カメラ
  const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
  camera.position.set(100, 100, 100);
  camera.up.set(0,0,1);
  
  //スクロール
  const controls = new THREE.OrbitControls(camera);
  
　//光源
  const directionalLight = new THREE.DirectionalLight(0xffffff);
  directionalLight.position.set(1, 1, 1);
  scene.add(directionalLight);
  
  //オブジェクト
  const geometry = new THREE.CubeGeometry(30, 30, 30);
  const material = new THREE.MeshPhongMaterial({ color: 0xff0000});
  const mesh = new THREE.Mesh(geometry, material);
  mesh.rotation.set(0.7, 0.7, 0);
  scene.add(mesh);
  
  // 描画
  const renderer = new THREE.WebGLRenderer({
    canvas: document.getElementById("canvas")
  });
  renderer.setSize(width, height);
  
  (function loop () {
    window.requestAnimationFrame(loop)
    renderer.render(scene, camera);
  })();
};

document.addEventListener("DOMContentLoaded", main); 
```
![image](https://raw.githubusercontent.com/youya66/til/master/three-js/images/base_result.png)
