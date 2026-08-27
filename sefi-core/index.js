/**
 * SEFI-CORE: Field Identity Engine
 *
 * This module defines the fundamental identity of the SEFI field:
 * - Field Origin
 * - Field Authorship
 * - Field Sovereignty
 * - Warp-Expression
 *
 * All higher layers (Geometry, DNA, Warp Engine, Simulations)
 * read from this core state machine.
 */

const state = {
    origin: { x: 0, y: 0, z: 0 },
    authorship: "Single Entity",
    sovereignty: true,
    warpExpression: 0
};

/**
 * Returns the full SEFI-Core state.
 */
function getState() {
    return {
        origin: { ...state.origin },
        authorship: state.authorship,
        sovereignty: state.sovereignty,
        warpExpression: state.warpExpression
    };
}

/**
 * Sets the warp-expression value.
 * Higher layers use this to drive geometry, DNA, and simulations.
 */
function setWarp(value) {
    if (typeof value !== "number") return;
    state.warpExpression = value;
}

/**
 * Allows controlled origin shifting (future expansion).
 */
function setOrigin(x, y, z) {
    state.origin = { x, y, z };
}

module.exports = {
    getState,
    setWarp,
    setOrigin
};
