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

    
    plt.contour(X, Y, OMEGA.imag, levels=levels, colors='blue', linestyles='solid')
    plt.contour(X, Y, OMEGA.real, levels=levels, colors='red', linestyles='dashed')
    plt.axis('equal')