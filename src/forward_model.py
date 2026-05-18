"""Forward model implementations for transmission line analysis.

Implements equations (9)-(12) from the thesis for calculating voltage drop,
current flow, and power loss in transmission lines.
"""

import numpy as np


def forward_voltage_drop(Vs, Z, I):
    """Calculate voltage drop across line impedance.
    
    Args:
        Vs: Sending-end voltage (phasor)
        Z: Line impedance (complex)
        I: Current through line (phasor)
    
    Returns:
        Vr: Receiving-end voltage (phasor)
    """
    return Vs - Z * I


def forward_fixed_load(Vs, Z, Z_load):
    """Calculate current and voltage in fixed load scenario.
    
    Args:
        Vs: Sending-end voltage (phasor)
        Z: Line impedance (complex)
        Z_load: Load impedance (complex)
    
    Returns:
        I: Current through line (phasor)
        Vr: Receiving-end voltage (phasor)
    """
    I = Vs / (Z + Z_load)
    Vr = I * Z_load
    return I, Vr


def power_loss(I, R):
    """Calculate 3-phase power loss in line.
    
    Args:
        I: Current magnitude (RMS)
        R: Line resistance (ohms)
    
    Returns:
        P_loss: 3-phase power loss (watts)
    """
    return 3 * (I ** 2) * R


def angle_change(Vs, Vr, Z, I):
    """Calculate phase angle change across line.
    
    Args:
        Vs: Sending-end voltage (phasor)
        Vr: Receiving-end voltage (phasor)
        Z: Line impedance (complex)
        I: Current through line (phasor)
    
    Returns:
        angle_rad: Phase angle change (radians)
    """
    delta_V = Vs - Vr
    return np.angle(delta_V) - np.angle(I)