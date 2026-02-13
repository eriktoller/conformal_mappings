from elements import omega_well
from mappings import line_to_chi
from plotter import contour_flow_net, make_arrow_gif

import numpy as np

if __name__ == "__main__":
    print("This is the model module.")

    # Well
    q = 10.0  # Strength of the well
    endpoints = np.array([-1 + 0j, 1 + 1j])  # Endpoints of the line segment
    def omega(z):
        return omega_well(z, q, lambda z: line_to_chi(z, endpoints))

    well = omega

    # plot the well
    ccs_phi, cs_psi = contour_flow_net(
        (-3, 3),
        (-3, 3),
        well,
        levels=50,
        xgrid_points=400,
        ygrid_points=400,
    )
    # add_steamline_arrows(cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5)
    make_arrow_gif(
        cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5, filename="well_flow.gif"
    )
    import matplotlib.pyplot as plt

    plt.title("Well Flow")
    plt.show()
