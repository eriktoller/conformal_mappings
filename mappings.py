import numpy as np

def line_to_chi(z, endpoints):
    """
    Map a line segment defined by its endpoints to a unit circle using a conformal mapping.

    Parameters
    ----------
    z : complex
        The complex coordinate to be mapped.
    endpoints : np.ndarray(complex)
        A numpy array containing two complex numbers representing the endpoints of the line segment.

    Returns
    -------
    chi : complex
        The mapped complex coordinate on the unit circle.
    """
    z1, z2 = endpoints
    big_z = ( 2*z - (z1 + z2) ) / (z2 - z1)
    chi = big_z + np.sqrt(big_z - 1) * np.sqrt(big_z + 1)
    return chi

def chi_to_line(chi, endpoints):
    """
    Map a point on the unit circle back to a line segment defined by its endpoints using the inverse conformal mapping.

    Parameters
    ----------
    chi : complex
        The complex coordinate on the unit circle to be mapped back.
    endpoints : np.ndarray(complex)
        A numpy array containing two complex numbers representing the endpoints of the line segment.

    Returns
    -------
    z : complex
        The mapped complex coordinate on the line segment.
    """
    z1, z2 = endpoints
    big_z = (chi + 1/chi) / 2
    z = ((z2 - z1) * big_z + (z1 + z2)) / 2
    return z

def circle_to_chi(z, center, radius):
    """
    Map a circle defined by its center and radius to a unit circle using a conformal mapping.

    Parameters
    ----------
    z : complex
        The complex coordinate to be mapped.
    center : complex
        The center of the circle.
    radius : float
        The radius of the circle.

    Returns
    -------
    chi : complex
        The mapped complex coordinate on the unit circle.
    """
    chi = (z - center) / radius
    return chi

