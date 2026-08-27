/**
 * SEFI-DNA: Identity Expression Engine
 *
 * This module defines the identity behavior of the SEFI field:
 * - Identity Expression
 * - Identity Sequencing
 * - Identity Narrative
 *
 * DNA is the identity layer of SEFI.
 */

const core = require('../sefi-core/index');
const warp = require('../warp-engine/index');
const geometry = require('../sefi-geometry/index');

/**
 * Computes identity expression intensity and mode.
 */
function expressIdentity(stability, distortion) {
    const intensity = (1 - stability) + distortion * 0.3;

    return {
        intensity,
        mode: determineExpressionMode(intensity)
    };
}

/**
 * Determines identity expression mode.
 */
function determineExpressionMode(intensity) {
    if (intensity < 0.3) return "stable";
    if (intensity < 0.7) return "adaptive";
    if (intensity < 1.2) return "distorted";
    return "warp-expression";
}

/**
 * Computes identity sequence progression and state.
 */
function sequenceIdentity(stability, warpEffect) {
    const progression = warpEffect * 0.5 + (1 - stability) * 0.2;

    return {
        progression,
        state: determineSequenceState(progression)
    };
}

/**
 * Determines identity sequence state.
 */
function determineSequenceState(progress) {
    if (progress < 0.3) return "baseline";
    if (progress < 0.7) return "shifted";
    if (progress < 1.2) return "transforming";
    return "nonlinear";
}

/**
 * Computes identity narrative depth and arc.
 */
function narrateIdentity(sequenceState, distortion, warpEffect) {
    const depth = distortion * 0.4 + warpEffect * 0.3;

    return {
        depth,
        arc: determineNarrativeArc(sequenceState, depth)
    };
}

/**
 * Determines identity narrative arc.
 */
function determineNarrativeArc(sequenceState, depth) {
    if (sequenceState === "baseline") return "origin";
    if (sequenceState === "shifted") return "stability";
    if (sequenceState === "transforming") return "distortion";
    if (depth > 1.0) return "warp";
    return "recovery";
}

/**
 * Returns a full DNA-state snapshot.
 */
function getDNAState() {
    const warpExpression = warp.getWarp();
    const warpEffect = warp.computeWarpEffect(warpExpression);

    const tension = geometry.calculateTension(warpExpression);
    const stability = geometry.calculateStability(tension);
    const distortion = geometry.calculateDistortion(tension, warpExpression);

    const expression = expressIdentity(stability, distortion);
    const sequence = sequenceIdentity(stability, warpEffect);
    const narrative = narrateIdentity(sequence.state, distortion, warpEffect);

    return {
        warpExpression,
        warpEffect,
        tension,
        stability,
        distortion,
        expression,
        sequence,
        narrative
    };
}

module.exports = {
    expressIdentity,
    sequenceIdentity,
    narrateIdentity,
    getDNAState
};
