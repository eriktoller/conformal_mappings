import matplotlib.pyplot as plt
import numpy as np

def contour_flow_net(xrange, yrange, flow_func, levels=50):
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

    Returns
    -------
    None
    """
    x = np.linspace(xrange[0], xrange[1], 400)
    y = np.linspace(yrange[0], yrange[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Compute the flow function values
    OMEGA = np.vectorize(flow_func)(Z)

    PHI = OMEGA.real
    PSI = OMEGA.imag
    dphi = max(PHI.max() - PHI.min(), PSI.max() - PSI.min()) / levels
    phi_levels = np.arange(PHI.min(), PHI.max(), dphi)
    psi_levels = np.arange(PSI.min(), PSI.max(), dphi)


    plt.contour(X, Y, PSI, levels=psi_levels, colors='blue', linestyles='solid', linewidths=0.5)
    plt.contour(X, Y, PHI, levels=phi_levels, colors='red', linestyles='solid', linewidths=0.5)
    plt.axis('equal')