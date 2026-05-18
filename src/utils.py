"""Utility functions for phasor calculations and data handling."""

import numpy as np


def to_phasor(magnitude, angle_deg):
    """Convert magnitude and angle to complex phasor.
    
    Args:
        magnitude: Phasor magnitude
        angle_deg: Phasor angle (degrees)
    
    Returns:
        phasor: Complex phasor representation
    """
    return magnitude * np.exp(1j * np.deg2rad(angle_deg))


def from_phasor(phasor):
    """Convert complex phasor to magnitude and angle.
    
    Args:
        phasor: Complex phasor
    
    Returns:
        magnitude: Phasor magnitude
        angle_deg: Phasor angle (degrees)
    """
    magnitude = np.abs(phasor)
    angle_deg = np.rad2deg(np.angle(phasor))
    return magnitude, angle_deg


def phasor_error(true_phasor, estimated_phasor):
    """Calculate error between true and estimated phasor.
    
    Args:
        true_phasor: True phasor (complex)
        estimated_phasor: Estimated phasor (complex)
    
    Returns:
        magnitude_error: Magnitude error (absolute)
        angle_error_deg: Angle error (degrees)
    """
    magnitude_error = np.abs(np.abs(estimated_phasor) - np.abs(true_phasor))
    angle_error_rad = np.angle(estimated_phasor) - np.angle(true_phasor)
    angle_error_deg = np.rad2deg(angle_error_rad)
    
    return magnitude_error, angle_error_deg


def rms_to_peak(rms_value):
    """Convert RMS value to peak value.
    
    Args:
        rms_value: RMS value
    
    Returns:
        peak_value: Peak value
    """
    return rms_value * np.sqrt(2)


def peak_to_rms(peak_value):
    """Convert peak value to RMS value.
    
    Args:
        peak_value: Peak value
    
    Returns:
        rms_value: RMS value
    """
    return peak_value / np.sqrt(2)


def normalize_angle(angle_deg):
    """Normalize angle to [-180, 180] degrees.
    
    Args:
        angle_deg: Input angle (degrees)
    
    Returns:
        normalized_angle: Angle in [-180, 180] range
    """
    return (angle_deg + 180) % 360 - 180