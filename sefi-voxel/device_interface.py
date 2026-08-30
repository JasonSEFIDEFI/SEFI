# sefi-voxel/device_interface.py
import serial
import struct
import numpy as np

def send_phase_sequence(port: str,
                        phases: np.ndarray,
                        baudrate: int = 115200) -> None:
    """
    Send a sequence of phase frames to the hardware over serial.
    phases: (N, M) array of phase values (radians).
    """
    ser = serial.Serial(port, baudrate=baudrate)
    try:
        for frame in phases:
            payload = struct.pack(f'{len(frame)}f', *frame)
            ser.write(payload)
    finally:
        ser.close()
