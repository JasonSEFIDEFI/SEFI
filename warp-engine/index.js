/**
 * WARP-ENGINE: Dynamic Transformation Engine
 *
 * This module defines SEFI's dynamic behavior:
 * - Warp level
 * - Warp limits
 * - Warp stability influence
 * - Warp-surface behavior
 * - Nonlinear transformation (DEFI)
 *
 * Warp is the motion layer of SEFI.
 */

const core = require('../sefi-core/index');

// Canonical warp limit (from SEFI canon)
const WARP_LIMIT = 100;

/**
 * Ensures warp values always stay within canonical limits.
 */
function clampWarp(value) {
    if (value < 0) return 0;
    if (value > WARP_LIMIT) return WARP_LIMIT;
    return value;
}

/**
 * Returns the current warp-expression value.
 */
function getWarp() {
    return core.getState().warpExpression;
}

/**
 * Computes warp effect.
 * Warp effect increases nonlinearly as warp approaches the limit.
 */
function computeWarpEffect(warpExpression) {
    warpExpression = clampWarp(warpExpression);
    const normalized = warpExpression / WARP_LIMIT;
    return Math.pow(normalized, 2.2);
}

/**
 * Safely increases warp-expression.
 */
function increaseWarp(amount = 1) {
    const state = core.getState();
    let newWarp = clampWarp(state.warpExpression + amount);
    core.setWarp(newWarp);
    return newWarp;
}

/**
 * Safely decreases warp-expression.
 */
function decreaseWarp(amount = 1) {
    const state = core.getState();
    let newWarp = clampWarp(state.warpExpression - amount);
    core.setWarp(newWarp);
    return newWarp;
}

/**
 * Computes warp-surface distortion.
 * This affects visualizers and geometry.
 */
function computeWarpSurface(warpExpression) {
    warpExpression = clampWarp(warpExpression);
    return {
        distortion: warpExpression * 0.03,
        intensity: warpExpression * 0.02,
        resonance: Math.sin(warpExpression * 0.1) * 0.5
    };
}

/**
 * Computes warp stability influence.
 * Higher warp → lower stability.
 */
function computeWarpStability(warpExpression) {
    warpExpression = clampWarp(warpExpression);
    return 1 / (1 + warpExpression * 0.05);
}

/**
 * Returns a full warp-state snapshot.
 */
function getWarpState() {
    const warpExpression = getWarp();
    return {
        warpExpression,
        effect: computeWarpEffect(warpExpression),
        surface: computeWarpSurface(warpExpression),
        stability: computeWarpStability(warpExpression)
    };
}

module.exports = {
    WARP_LIMIT,
    clampWarp,
    getWarp,
    getWarpState,
    computeWarpEffect,
    computeWarpSurface,
    computeWarpStability,
    increaseWarp,
    decreaseWarp
};
