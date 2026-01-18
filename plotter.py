import matplotlib.pyplot as plt
import numpy as np


def contour_flow_net(
    xrange, yrange, flow_func, levels=50, xgrid_points=400, ygrid_points=400
):
    """
    Plot the contour of a complex flow function over a specified range.

    Parameters
    ----------
    xrange : tuple
        A tuple specifying the range of x values (xmin, xmax).
    yrange : tuple
        A tuple specifying the range of y values (ymin, ymax).
    flow_func : function
        A function that takes a complex number and returns a complex number representing the flow.
    levels : int
        The number of contour levels to plot.
    xgrid_points : int
        The number of grid points in the x direction.
    ygrid_points : int
        The number of grid points in the y direction.

    Returns
    -------
    cs_phi : QuadContourSet
        The contour set for the potential function (real part).
    cs_psi : QuadContourSet
        The contour set for the stream function (imaginary part).
    """
    # Create grid points
    x = np.linspace(xrange[0], xrange[1], xgrid_points)
    y = np.linspace(yrange[0], yrange[1], ygrid_points)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Compute the complex potential
    OMEGA = np.vectorize(flow_func)(Z)

    # Extract potential and stream functions and determine contour levels
    PHI = OMEGA.real
    PSI = OMEGA.imag
    dphi = max(PHI.max() - PHI.min(), PSI.max() - PSI.min()) / levels
    phi_levels = np.arange(PHI.min(), PHI.max(), dphi)
    psi_levels = np.arange(PSI.min(), PSI.max(), dphi)

    # Plot contours
    cs_psi = plt.contour(
        X, Y, PSI, levels=psi_levels, colors="blue", linestyles="solid", linewidths=0.5
    )
    cs_phi = plt.contour(
        X, Y, PHI, levels=phi_levels, colors="red", linestyles="solid", linewidths=0.5
    )
    plt.axis("equal")

    return cs_phi, cs_psi
