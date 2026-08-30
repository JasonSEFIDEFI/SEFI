export class WarpEngine {
    constructor(config = {}) {
        this.origin = config.origin || { x: 450, y: 300 };
        this.strength = config.strength || 1.0;
    }

    getResonance(t) {
        return Math.sin(t * 0.4) * Math.cos(t * 0.17);
    }

    distortPoint(x, y, t) {
        const dx = x - this.origin.x;
        const dy = y - this.origin.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        const falloff = Math.exp(-dist * 0.005);

        const warp = (
            Math.sin(t * 0.7) * 1.2 +
            Math.cos(t * 0.13) * 0.9
        ) * this.strength * falloff;

        const resonance = this.getResonance(t);
        const angle = Math.atan2(dy, dx);

        const radial = warp * (1 + resonance * 0.8);
        const newDist = dist + radial;

        return {
            x: this.origin.x + Math.cos(angle) * newDist,
            y: this.origin.y + Math.sin(angle) * newDist
        };
    }
}
