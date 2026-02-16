from elements import omega_well
from mappings import xi_to_ramp
from plotter import contour_flow_net, make_arrow_gif

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("This is the model module.")

    # Well
    w = 10.0 # uniform flow
    zw = 0 + 2.01j  # Location of the well
    zw = 1 + 2.01j  # Location of the well
    h = 1.0  # Height of the ramp
    q = 10.0  # Strength of the well
    def omega(z):
        return (q / (2 * np.pi)) * np.log(z-zw) - (q / (2 * np.pi)) * np.log(z-np.conj(zw))

    well = omega

    # plot the well
    num = 1000
    ccs_phi, cs_psi = contour_flow_net(
        (-10, 5),
        (0, 10),
        well,
        levels=50,
        xgrid_points=num,
        ygrid_points=num,
        mapping_func=lambda z: xi_to_ramp(z, h)
    )
    plt.plot([-100, 0, 0, 100], [3, 1, 0, 0], color="black", linewidth=1)
    plt.xlim(-2, 2)
    plt.ylim(0, 2)
    # remove the x and y ticks
    plt.xticks([])
    plt.yticks([])
    # remove the outer box
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    # add_steamline_arrows(cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5)
    #make_arrow_gif(
    #    cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5, filename="well_flow.gif"
    #)
    
    plt.tight_layout()
    plt.show()
