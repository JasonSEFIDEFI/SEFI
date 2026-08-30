export function startLoop(ctx, engine) {
    let t = 0;

    const width = ctx.canvas.width;
    const height = ctx.canvas.height;

    const stars = [];
    for (let i = 0; i < 400; i++) {
        stars.push({
            x: Math.random() * width,
            y: Math.random() * height,
            brightness: Math.random() * 0.8 + 0.2
        });
    }

    function frame() {
        t += 0.016;

        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, width, height);

        stars.forEach(star => {
            const p = engine.distortPoint(star.x, star.y, t);
            ctx.fillStyle = `rgba(255,255,255,${star.brightness})`;
            ctx.fillRect(p.x, p.y, 2, 2);
        });

        ctx.fillStyle = "cyan";
        ctx.beginPath();
        ctx.arc(engine.origin.x, engine.origin.y, 6, 0, Math.PI * 2);
        ctx.fill();

        requestAnimationFrame(frame);
    }

    frame();
}
