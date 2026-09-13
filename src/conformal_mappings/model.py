from conformal_mappings.elements import omega_well
from conformal_mappings.mappings import arc_to_chi
from conformal_mappings.plotter import contour_flow_net, make_arrow_gif

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("This is the model module.")

    # Well
    q = 10.0  # Strength of the well
    zw = 1 + 1j  # Location of the well
    zw2 = 1 - 2j  # Location of the image well
    zw3 = -1 + 3j  # Location of the image well
    center = 0 + 0j  # Center of the arc
    radius = 1.0  # Radius of the arc
    start_angle = 0.0  # Start angle of the arc in radians
    end_angle = np.pi / 2 * 2  # End angle of the arc in radians

    def omega(z):
        return omega_well(
            z, q, lambda z: arc_to_chi(z, center, radius, start_angle, end_angle)
        )
        # return 2*np.log(2+z**2)+np.log(3+(z+2)**2)-.5*np.log(8+(z-3)**2)# Creates an image well with an impermeable boundary at the real axis
        # return np.log(z-zw) + np.log(z-zw2) + np.log(z-zw3) + np.log(z-np.conj(zw)) + np.log(z-np.conj(zw2)) + np.log(z-np.conj(zw3))

    well = omega

    # plot the well
    ccs_phi, cs_psi = contour_flow_net(
        (-4, 4),
        (-4, 4),
        well,
        levels=50,
        xgrid_points=400,
        ygrid_points=400,
    )
    # add_steamline_arrows(cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5)
    # make_arrow_gif(
    #    cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5, filename="well_flow.gif"
    # )

    plt.title("Well Flow")
    plt.show()
