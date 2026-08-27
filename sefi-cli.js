/**
 * SEFI Command-Line Interface
 *
 * This file allows you to run SEFI engine functions directly
 * from the terminal using Node.js.
 *
 * Examples:
 *   node sefi-cli.js state
 *   node sefi-cli.js warp 20
 *   node sefi-cli.js warpUp
 *   node sefi-cli.js slit
 *   node sefi-cli.js visualize
 */

const SEFI = require('./sefi/index');

// Read command + argument
const command = process.argv[2];
const arg = process.argv[3];

function run() {
    switch (command) {
        case "state":
            console.log(SEFI.state());
            break;

        case "warp":
            SEFI.setWarp(Number(arg));
            console.log("Warp set to:", SEFI.state().warpExpression);
            break;

        case "warpUp":
            console.log("Warp increased to:", SEFI.warpUp(Number(arg) || 1));
            break;

        case "warpDown":
            console.log("Warp decreased to:", SEFI.warpDown(Number(arg) || 1));
            break;

        case "slit":
            console.log(SEFI.sim.slit());
            break;

        case "origin":
            console.log(SEFI.sim.origin());
            break;

        case "warpTest":
            console.log(SEFI.sim.warp());
            break;

        case "geometry":
            console.log(SEFI.sim.geometry());
            break;

        case "dna":
            console.log(SEFI.sim.dna());
            break;

        case "visualize":
            console.log(SEFI.sim.visualize());
            break;

        default:
            console.log("Unknown command:", command);
            console.log("Available commands:");
            console.log(" state");
            console.log(" warp <value>");
            console.log(" warpUp <amount>");
            console.log(" warpDown <amount>");
            console.log(" slit");
            console.log(" origin");
            console.log(" warpTest");
            console.log(" geometry");
            console.log(" dna");
            console.log(" visualize");
            break;
    }
}

run();
