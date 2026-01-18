from elements import omega_well
from mappings import line_to_chi
from plotter import contour_flow_net

import numpy as np

if __name__ == "__main__":
    print("This is the model module.")

    # Well
    q = 10.0  # Strength of the well
    endpoints = np.array([-1 + 0j, 1 + 1j])  # Endpoints of the line segment
    well = lambda z: omega_well(z, q, lambda z: line_to_chi(z, endpoints))

    # plot the well
    contour_flow_net(
        (-3, 3),
        (-3, 3),
        well,
        levels=50,
        xgrid_points=400,
        ygrid_points=400,
    )
    import matplotlib.pyplot as plt
    plt.title("Well Flow")
    plt.show()