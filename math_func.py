import numpy as np


def taylor_series(chi, coef):
    """
    Compute the Taylor series expansion for a given chi value and coefficients.

    Parameters
    ----------
    chi : complex
        The point at which to evaluate the Taylor series.
    coef : np.ndarray(complex)
        The coefficients of the Taylor series, where coef[i] corresponds to the
        coefficient of (chi^i).

    Returns
    -------
    complex
        The value of the Taylor series evaluated at chi.
    """
    result = 0 + 0j
    for i in range(len(coef)):
        result += coef[i] * (chi**i)
    return result


def asym_exp(chi, coef):
    """
    Compute the asymptotic expansion for a given chi value and coefficients.

    Parameters
    ----------
    chi : complex
        The point at which to evaluate the asymptotic expansion.
    coef : np.ndarray(complex)
        The coefficients of the asymptotic expansion, where coef[i] corresponds to the
        coefficient of (1/chi^i).

    Returns
    -------
    complex
        The value of the asymptotic expansion evaluated at chi.
    """
    result = 0 + 0j
    for i in range(len(coef)):
        result += coef[i] / (chi**i)
    return result


def cauchy_integral(func_omega, func_chi, degrees, num_points=1000):
    """
    Compute the Cauchy integral of a given function around the unit circle.

    Parameters
    ----------
    func_omega : function
        A function that takes a complex number chi and returns the complex potential omega.
    func_chi : function
        A function that takes a complex number z and returns the corresponding chi value.
    degrees : int
        The number of degrees of freedom for the integral.
    num_points : int
        The number of points to use for the numerical integration.

    Returns
    -------
    complex
        The value of the Cauchy integral.
    """
    theta = np.linspace(0, 2 * np.pi, num_points)
    zs = np.exp(1j * theta)  # Points on the unit circle
    omegas = np.zeros(num_points, dtype=complex)
    for i, z in enumerate(zs):
        chi = func_chi(z)
        omegas[i] = func_omega(chi)

    integral = 0 + 0j
    for j in range(degrees):
        for i in range(num_points):
            integral += omegas[i] * np.exp(1j * j * theta[i]) * (2 * np.pi / num_points)

    return integral / (2j * np.pi)
