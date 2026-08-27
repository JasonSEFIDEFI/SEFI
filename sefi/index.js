/**
 * SEFI: Root Engine
 *
 * This module provides the main entry point for the SEFI system.
 * It ties together:
 * - Core
 * - Warp Engine
 * - Geometry Engine
 * - DNA Engine
 * - Simulation Engine
 *
 * This is the file you run with: node sefi/index.js
 */

const core = require('../sefi-core/index');
const warp = require('../warp-engine/index');
const geometry = require('../sefi-geometry/index');
const dna = require('../sefi-dna/index');
const sim = require('../sefi-sim/index');

/**
 * Produces a full SEFI snapshot.
 */
function snapshot() {
    return sim.simulateField();
}

/**
 * Runs SEFI and prints a snapshot to the console.
 */
function run() {
    const field = snapshot();
    console.log("=== SEFI FIELD SNAPSHOT ===");
    console.log(JSON.stringify(field, null, 2));
}

/**
 * Expose SEFI API.
 */
module.exports = {
    snapshot,
    run,
    core,
    warp,
    geometry,
    dna,
    sim
};

// Auto-run if executed directly
if (require.main === module) {
    run();
}
