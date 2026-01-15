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
        result += coef[i] * (chi ** i)
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
        result += coef[i] / (chi ** i)
    return result