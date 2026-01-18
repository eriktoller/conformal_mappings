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