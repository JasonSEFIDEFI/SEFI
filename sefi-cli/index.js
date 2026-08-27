#!/usr/bin/env node

/**
 * SEFI CLI
 * Command-line interface for interacting with the SEFI engine.
 */

const sefi = require('../sefi/index');

const args = process.argv.slice(2);
const command = args[0];

function help() {
    console.log(`
SEFI CLI Commands:

  sefi snapshot       Print a single SEFI field snapshot
  sefi loop           Stream continuous snapshots
  sefi core           Show core state
  sefi warp           Show warp state
  sefi geometry       Show geometry state
  sefi dna            Show DNA state
  sefi help           Show this help menu
`);
}

switch (command) {
    case 'snapshot':
        console.log(JSON.stringify(sefi.snapshot(), null, 2));
        break;

    case 'loop':
        setInterval(() => {
            console.log(JSON.stringify(sefi.snapshot(), null, 2));
        }, 1000);
        break;

    case 'core':
        console.log(JSON.stringify(sefi.core.getState(), null, 2));
        break;

    case 'warp':
        console.log(JSON.stringify(sefi.warp.getWarpState(), null, 2));
        break;

    case 'geometry':
        console.log(JSON.stringify(sefi.geometry.getGeometryState(), null, 2));
        break;

    case 'dna':
        console.log(JSON.stringify(sefi.dna.getDNAState(), null, 2));
        break;

    default:
        help();
        break;
}
