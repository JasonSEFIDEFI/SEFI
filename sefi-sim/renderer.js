// renderer.js

// Draw a single frame of the field + worldline
export function renderFrame(ctx, frame) {
    // Clear previous frame
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

    // Draw field grid (simple baseline visual)
    ctx.strokeStyle = "#222";
    ctx.lineWidth = 1;

    for (let x = 0; x < ctx.canvas.width; x += 40) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, ctx.canvas.height);
        ctx.stroke();
    }

    for (let y = 0; y < ctx.canvas.height; y += 40) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(ctx.canvas.width, y);
        ctx.stroke();
    }

    // Draw worldline point
    ctx.fillStyle = "#0ff";
    ctx.beginPath();
    ctx.arc(frame.x, frame.y, 5, 0, Math.PI * 2);
    ctx.fill();
}
