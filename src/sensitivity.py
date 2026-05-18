"""Sensitivity analysis tools for phasor measurement perturbations.

Tools for applying angle and magnitude errors to phasors and analyzing
impact on backward method estimates.
"""

import numpy as np


def apply_angle_offset(phasor, deg):
    """Apply angular offset to phasor.
    
    Args:
        phasor: Input phasor (complex)
        deg: Angular offset (degrees)
    
    Returns:
        phasor_offset: Rotated phasor
    """
    if np.isscalar(phasor):
        return phasor * np.exp(1j * np.deg2rad(deg))
    else:
        return phasor * np.exp(1j * np.deg2rad(deg))


def apply_magnitude_error(phasor, pct):
    """Apply percentage magnitude error to phasor.
    
    Args:
        phasor: Input phasor (complex)
        pct: Magnitude error (percent)
    
    Returns:
        phasor_error: Phasor with magnitude error
    """
    return phasor * (1 + pct / 100)


def apply_combined_error(phasor, angle_deg, magnitude_pct):
    """Apply combined angle and magnitude error to phasor.
    
    Args:
        phasor: Input phasor (complex)
        angle_deg: Angular offset (degrees)
        magnitude_pct: Magnitude error (percent)
    
    Returns:
        phasor_error: Phasor with combined errors
    """
    return apply_angle_offset(
        apply_magnitude_error(phasor, magnitude_pct),
        angle_deg
    )


def sensitivity_slope(base_estimate, perturbed_estimates, perturbations):
    """Calculate sensitivity slope (derivative) numerically.
    
    Args:
        base_estimate: Estimate at zero perturbation
        perturbed_estimates: Array of estimates with perturbations
        perturbations: Array of applied perturbations
    
    Returns:
        slope: Sensitivity slope (change in estimate per unit perturbation)
    """
    perturbations = np.asarray(perturbations)
    perturbed_estimates = np.asarray(perturbed_estimates)
    
    # Linear regression near zero
    mask = np.abs(perturbations) < 1e-6  # Near-zero mask
    if np.sum(mask) > 1:
        slope = np.polyfit(perturbations[mask], perturbed_estimates[mask], 1)[0]
    else:
        slope = np.mean(np.diff(perturbed_estimates) / np.diff(perturbations))
    
    return slope


def error_propagation(sensitivity, measurement_uncertainty):
    """Estimate error propagation through method.
    
    Args:
        sensitivity: Method sensitivity (change per unit error)
        measurement_uncertainty: Measurement uncertainty (same units as perturbation)
    
    Returns:
        estimate_uncertainty: Resulting estimate uncertainty
    """
    return np.abs(sensitivity) * measurement_uncertainty