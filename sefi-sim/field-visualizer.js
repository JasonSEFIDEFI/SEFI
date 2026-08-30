console.log("VISUALIZER LOADED");

import { createCanvas } from "./canvas.js";
import { startLoop } from "./loop.js";
import { WarpEngine } from "./warp-engine.js";

console.log("IMPORTS OK");

const ctx = createCanvas(900, 600);
console.log("CANVAS OK");

const engine = new WarpEngine({
    origin: { x: 450, y: 300 },
    strength: 1.0
});
console.log("ENGINE OK");

window.engine = engine;

console.log("CALLING LOOP");
startLoop(ctx, engine);
console.log("LOOP CALLED");
