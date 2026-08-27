const sefi = require('./index');

setInterval(() => {
    const field = sefi.snapshot();
    console.log(JSON.stringify(field, null, 2));
}, 1000);
