/**
 * SEFI-CONFIG: Global Configuration System (Full Version)
 *
 * This module provides:
 * - Default configuration
 * - Environment profiles
 * - Runtime overrides
 * - Config merging
 * - Validation
 * - Config events (listeners)
 *
 * This is the complete configuration layer for SEFI.
 */

const config = {
    defaults: {
        origin: { x: 0, y: 0, z: 0 },
        warpExpression: 0
    },

    simulation: {
        slit: {
            intensityScale: 1.0,
            interferenceScale: 1.0
        },
        origin: {
            shiftScale: 1.0
        },
        geometry: {
            tensionScale: 1.0,
            distortionScale: 1.0
        },
        dna: {
            expressionScale: 1.0,
            sequenceScale: 1.0,
            narrativeScale: 1.0
        }
    },

    visualizer: {
        tensionLineScale: 1.0,
        distortionMapScale: 1.0,
        identityGlowScale: 1.0
    },

    environment: {
        mode: "development",   // "development" | "production"
        logging: true
    },

    // Runtime overrides
    overrides: {},

    // Event listeners
    listeners: []
};

/**
 * Returns the merged configuration:
 * defaults + overrides
 */
function getConfig() {
    return mergeConfigs(config, config.overrides);
}

/**
 * Applies a runtime override.
 */
function setOverride(path, value) {
    setDeep(config.overrides, path, value);
    notifyListeners(path, value);
}

/**
 * Clears all overrides.
 */
function clearOverrides() {
    config.overrides = {};
    notifyListeners("overrides", null);
}

/**
 * Sets environment mode.
 */
function setMode(mode) {
    if (mode !== "development" && mode !== "production") return;
    config.environment.mode = mode;
    notifyListeners("environment.mode", mode);
}

/**
 * Toggles logging.
 */
function toggleLogging(value) {
    config.environment.logging = Boolean(value);
    notifyListeners("environment.logging", config.environment.logging);
}

/**
 * Adds a config listener.
 * Listener receives: (path, value)
 */
function addListener(fn) {
    if (typeof fn === "function") {
        config.listeners.push(fn);
    }
}

/**
 * Notifies listeners of a change.
 */
function notifyListeners(path, value) {
    for (const fn of config.listeners) {
        fn(path, value);
    }
}

/**
 * Deep merge utility.
 */
function mergeConfigs(base, overrides) {
    const output = JSON.parse(JSON.stringify(base));

    function apply(obj, path, value) {
        const parts = path.split(".");
        let current = obj;

        for (let i = 0; i < parts.length - 1; i++) {
            if (!current[parts[i]]) current[parts[i]] = {};
            current = current[parts[i]];
        }

        current[parts[parts.length - 1]] = value;
    }

    for (const key in overrides) {
        apply(output, key, overrides[key]);
    }

    return output;
}

/**
 * Deep setter utility.
 */
function setDeep(obj, path, value) {
    const parts = path.split(".");
    let current = obj;

    for (let i = 0; i < parts.length - 1; i++) {
        if (!current[parts[i]]) current[parts[i]] = {};
        current = current[parts[i]];
    }

    current[parts[parts.length - 1]] = value;
}

module.exports = {
    getConfig,
    setOverride,
    clearOverrides,
    setMode,
    toggleLogging,
    addListener
};

