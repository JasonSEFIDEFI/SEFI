#!/usr/bin/env node

const { exec } = require('child_process');

console.log('--- SEFI Engine JS CLI Wrapper ---');
exec('python main.py', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing engine: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`Stderr: ${stderr}`);
        return;
    }
    console.log(stdout);
});