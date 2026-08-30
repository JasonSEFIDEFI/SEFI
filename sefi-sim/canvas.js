export function createCanvas(width, height) {
    const canvas = document.createElement("canvas");
    canvas.width = width;
    canvas.height = height;
    document.body.appendChild(canvas);
    return canvas.getContext("2d");
}
