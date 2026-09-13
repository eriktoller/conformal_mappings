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
    big_z = (2 * z - (z1 + z2)) / (z2 - z1)
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
    big_z = (chi + 1 / chi) / 2
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


def chi_to_circle(chi, center, radius):
    """
    Map a point on the unit circle back to a circle defined by its center and radius using the inverse conformal mapping.

    Parameters
    ----------
    chi : complex
        The complex coordinate on the unit circle to be mapped back.
    center : complex
        The center of the circle.
    radius : float
        The radius of the circle.

    Returns
    -------
    z : complex
        The mapped complex coordinate on the circle.
    """
    z = chi * radius + center
    return z


def square_to_chi(z, vertices):
    """
    Map a square defined by its vertices to a unit circle using a conformal mapping.

    Parameters
    ----------
    z : complex
        The complex coordinate to be mapped.
    vertices : np.ndarray(complex)
        A numpy array containing four complex numbers representing the vertices of the square in order.

    Returns
    -------
    chi : complex
        The mapped complex coordinate on the unit circle.
    """
    chi = 1
    return chi


def xi_to_ramp(xi, h):
    """
    Map a ramp defined by its height to the upper half-plane using Schwarz-Christoffel transformation.

    Parameters
    ----------
    xi : complex
        The complex coordinate to be mapped.
    h : float
        The height of the ramp.

    Returns
    -------
    chi : complex
        The mapped complex coordinate on the upper half-plane.
    """
    z = (
        h
        / np.pi
        * (
            np.sqrt(xi - 1) * np.sqrt(xi + 1)
            + np.log(xi + np.sqrt(xi - 1) * np.sqrt(xi + 1))
        )
    )
    return z


def arc_to_chi(z, center, radius, start_angle, end_angle):
    """
    Map an arc defined by its center, radius, and start/end angles to a unit circle using a conformal mapping.

    Parameters
    ----------
    z : complex
        The complex coordinate to be mapped.
    center : complex
        The center of the arc.
    radius : float
        The radius of the arc.
    start_angle : float
        The starting angle of the arc in radians.
    end_angle : float
        The ending angle of the arc in radians.

    Returns
    -------
    chi : complex
        The mapped complex coordinate on the unit circle.
    """
    # Map the arc to a line segment using a Möbius transformation
    strt = center + radius * np.exp(1j * start_angle)
    end = center + radius * np.exp(1j * end_angle)
    endpoints = np.array([strt, end])

    # Send the start to infinity and the end to 0
    def mobius(w):
        return (w - strt) / (w - end)

    # Apply the Möbius transformation to z
    w = mobius(z)
    # Map the line segment to the unit circle
    chi = w

    return chi
