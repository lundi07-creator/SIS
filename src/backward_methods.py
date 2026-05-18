"""Backward estimation methods for extracting line impedance.

Implements three methods for estimating line resistance/impedance from
Two-end phasor measurements: Singh, SI (voltage drop), and Effect methods.
"""

import numpy as np


def singh_method(U_s, U_r, I_s, I_r):
    """Singh method for line impedance estimation.
    
    Uses both sending and receiving end phasor measurements.
    
    Args:
        U_s: Sending-end voltage (phasor)
        U_r: Receiving-end voltage (phasor)
        I_s: Sending-end current (phasor)
        I_r: Receiving-end current (phasor)
    
    Returns:
        Z_estimate: Estimated line impedance (complex)
        R_estimate: Estimated line resistance (ohms)
    """
    # Singh uses averaged voltage and current
    U_avg = (U_s + U_r) / 2
    I_avg = (I_s + I_r) / 2
    
    Z_estimate = (U_s - U_r) / I_avg
    R_estimate = np.real(Z_estimate)
    
    return Z_estimate, R_estimate


def si_method(U_s, U_r, I_avg):
    """Voltage drop-based impedance method (SI).
    
    Direct calculation from voltage difference and average current.
    
    Args:
        U_s: Sending-end voltage (phasor)
        U_r: Receiving-end voltage (phasor)
        I_avg: Average current (phasor)
    
    Returns:
        Z_estimate: Estimated line impedance (complex)
        R_estimate: Estimated line resistance (ohms)
    """
    Z_estimate = (U_s - U_r) / I_avg
    R_estimate = np.real(Z_estimate)
    
    return Z_estimate, R_estimate


def effect_method(P_loss, I):
    """Power loss-based resistance estimation (Effect method).
    
    Estimates resistance from measured 3-phase power loss and current.
    
    Args:
        P_loss: 3-phase power loss (watts)
        I: Current magnitude (RMS)
    
    Returns:
        R_estimate: Estimated line resistance (ohms)
    """
    if np.isscalar(I):
        R_estimate = P_loss / (3 * (I ** 2))
    else:
        R_estimate = P_loss / (3 * (np.abs(I) ** 2))
    
    return R_estimate


def estimate_temperature(R_estimate, R_ref, T_ref=20, alpha=0.00403):
    """Estimate conductor temperature from resistance estimate.
    
    Uses temperature-dependent resistance model: R(T) = R_ref * (1 + alpha * (T - T_ref))
    
    Args:
        R_estimate: Estimated resistance (ohms)
        R_ref: Reference resistance at T_ref (ohms)
        T_ref: Reference temperature (°C), default 20°C
        alpha: Temperature coefficient for copper/aluminum
    
    Returns:
        T_estimate: Estimated temperature (°C)
    """
    if R_ref <= 0:
        return np.nan
    
    T_estimate = T_ref + (R_estimate / R_ref - 1) / alpha
    
    return T_estimate