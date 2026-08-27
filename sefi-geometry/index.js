/**
 * SEFI-GEOMETRY: Field Geometry Engine
 *
 * This module defines the geometric behavior of the SEFI field:
 * - Tension
 * - Stability
 * - Distortion
 * - Routing
 * - Metric
 *
 * Geometry is the structural layer of SEFI.
 */

const core = require('../sefi-core/index');
const warp = require('../warp-engine/index');

/**
 * Calculates geometric tension based on warp-expression.
 */
function calculateTension(warpExpression) {
    return warpExpression * 0.1;
}

/**
 * Calculates stability from tension.
 * Higher tension → lower stability.
 */
function calculateStability(tension) {
    return 1 / (1 + Math.abs(tension));
}

/**
 * Calculates distortion from tension and warp-expression.
 */
function calculateDistortion(tension, warpExpression) {
    return tension * 0.5 + warpExpression * 0.2;
}

/**
 * Calculates routing vectors based on tension and distortion.
 */
function calculateRouting(tension, distortion) {
    return {
        direction: {
            x: tension * 0.1,
            y: distortion * -0.05,
            z: tension * distortion * 0.02
        },
        intensity: tension + distortion
    };
}

/**
 * Calculates geometric metric (scale + curvature).
 */
function calculateMetric(warpExpression, tension) {
    return {
        scale: 1 + warpExpression * 0.01 - tension * 0.005,
        curvature: warpExpression * 0.02 + tension * 0.01
    };
}

/**
 * Returns a full geometry-state snapshot.
 */
function getGeometryState() {
    const warpExpression = warp.getWarp();
    const tension = calculateTension(warpExpression);
    const stability = calculateStability(tension);
    const distortion = calculateDistortion(tension, warpExpression);
    const routing = calculateRouting(tension, distortion);
    const metric = calculateMetric(warpExpression, tension);

    return {
        warpExpression,
        tension,
        stability,
        distortion,
        routing,
        metric
    };
}

module.exports = {
    calculateTension,
    calculateStability,
    calculateDistortion,
    calculateRouting,
    calculateMetric,
    getGeometryState
};
