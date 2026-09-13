import numpy as np


def omega_well(z, q, map_z_to_chi):
    """
    Model a well using conformal mappings.

    Parameters
    ----------
    q : float
        The strength of the well.
    map_z_to_chi : function
        A function that maps complex coordinate z to chi.

    Returns
    -------
    function
        A function that takes a complex coordinate z and returns the complex potential omega due to the well.
    """

    chi = map_z_to_chi(z)
    omega = (q / (2 * np.pi)) * np.log(chi)
    return omega


def omega_uni_flow(z, w, map_z_to_chi=None, map_chi_to_z=None):
    """
    Model of a unform flow unsing conformal mappings.

    Paramters
    ---------
    z : complex
        The complex point, either in z or chi
    w : complex
        The strength and dirction of the unform flow of the form w = wx + 1j*wy
    map_z_to_chi : function, optional
        The function that maps z to chi
    map_chi_to_z : funciton, optional
        The function that maps chi to z

    Returns
    -------
    omega : complex
        The complex potential for the unform flow at the given point.
    z : complex
        The coplex point z
    """

    if map_chi_to_z is None and map_z_to_chi is None:
        return w * z

    if map_chi_to_z is not None:
        omega = w * z
        zout = map_chi_to_z(z)

        return omega, zout

    if map_z_to_chi is not None:
        chi = map_z_to_chi(z)
        omega = chi * w

        return omega, z