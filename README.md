# Interactive WebGL Narrative Experience ✨

![WebGL](https://img.shields.io/badge/WebGL-Custom%20Engine-blue?style=for-the-badge&logo=webgl)
![Node.js](https://img.shields.io/badge/Node.js-Express%20Proxy-green?style=for-the-badge&logo=node.js)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript)

Welcome to an immersive, browser-based 3D storytelling experience. This project pushes the boundaries of modern web development by combining hardware-accelerated 3D graphics, dynamic audio synchronization, and complex DOM manipulations into a seamless narrative journey.

## 🚀 Key Features

* **Custom 3D WebGL Engine**: Built utilizing custom shaders and `nanogl` for high-performance browser rendering.
* **Dynamic Audio Synchronization**: Features an advanced subtitle engine (`.srt` parsing) that seamlessly hooks into engine events to synchronize voiceovers with background stem layers.
* **Interactive DOM Overlays**: A sophisticated floating-element system built with CSS3 3D Transforms and Vanilla JavaScript, perfectly synced to in-engine narrative triggers.
* **Responsive Architecture**: Fully fluid and optimized layout that scales from 4K desktop monitors down to mobile devices, gracefully adjusting texture sizes and element constraints.
* **Custom Proxied Environment**: Powered by a local Node.js/Express server configured with proxy middleware to bypass CORS restrictions for remote glTF binary asset resolution.

## 🛠️ Technical Stack

- **Core**: Vanilla JavaScript (ES6+), HTML5, CSS3
- **Rendering**: WebGL, NanoGL, Custom GLSL Shaders
- **Animation**: GSAP (GreenSock) for fluid UI transitions and camera interpolation
- **Backend/Tooling**: Node.js, Express, `http-proxy-middleware`

## ⚙️ Local Development

To run this project locally and explore the environment:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/agam263/Special-One-.git
   cd Special-One-
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the local proxy server:**
   ```bash
   node server.js
   ```

4. **Experience the narrative:**
   Open your browser and navigate to `http://localhost:8081`

## 🧠 System Architecture Highlights

- **Asset Pipeline**: The engine leverages dynamic XHR loading to fetch textures, JSON definitions, and glTF models asynchronously, ensuring rapid initial load times.
- **Event-Driven UI**: The floating overlay elements are completely decoupled from the WebGL render loop. They listen to an event bus (`window.GLXP.audio.onSubtitles`) to react directly to audio cues, ensuring strict separation of concerns.

---
*This repository showcases advanced capabilities in frontend creative development, graphics programming, and immersive web design.*
