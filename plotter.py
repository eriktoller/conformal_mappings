import matplotlib.pyplot as plt
import numpy as np
import imageio
import tempfile
import os


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


def add_steamline_arrows(cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5):
    """
    Add arrows to the streamlines to indicate flow direction.

    Parameters
    ----------
    cs_psi : QuadContourSet
        The contour set for the stream function.
    n_arrows : int
        The number of arrows to add along each streamline.
    arrow_style : str
        The style of the arrows.

    Returns
    -------
    None
    """
    arrows = []
    for collection in cs_psi.allsegs:
        segments = collection
        for segment in segments:
            if len(segment) < 2:
                continue
            indices = np.linspace(0, len(segment) - 2, n_arrows, dtype=int)
            for idx in indices:
                start = segment[int(idx)]
                end = segment[int(idx) + 1]
                arrow = plt.annotate(
                    "",
                    xy=end,
                    xytext=start,
                    arrowprops=dict(arrowstyle=arrow_style, color="blue", lw=1.0),
                )
                arrows.append(arrow)
    return arrows


def make_arrow_gif(
    cs_psi, n_arrows=10, arrow_style="->", arrow_size=1.5, filename="arrows.gif"
):
    """
    Create an animated GIF of arrows moving along the streamlines.

    Parameters
    ----------
    cs_psi : QuadContourSet
        The contour set for the stream function.
    n_arrows : int
        The number of arrows to add along each streamline.
    arrow_style : str
        The style of the arrows.
    filename : str
        The name of the output GIF file.

    Returns
    -------
    None
    """

    frames = []
    frames_str = []
    for i in range(n_arrows):
        arrows = add_steamline_arrows(cs_psi, n_arrows=i + 1, arrow_style=arrow_style)
        plt.axis("equal")
        plt.title(f"Streamlines with {i + 1} Arrows")
        plt.draw()
        # Save the current frame as an image
        # At the start of the function, create a temp directory
        temp_dir = tempfile.mkdtemp()

        # Then replace the placeholder with:
        frame_filename = os.path.join(temp_dir, f"frame_{i}.png")
        plt.savefig(frame_filename)
        frames.append(imageio.imread(frame_filename))
        frames_str.append(frame_filename)

        # Remove the arrows for the next frame
        for arrow in arrows:
            arrow.remove()

    # Create GIF
    imageio.mimsave(filename, frames, duration=5.0 / n_arrows, loop=0)

    # Clean up temporary files
    for frame_file in frames_str:
        os.remove(frame_file)
    os.rmdir(temp_dir)

    print(f"Animated GIF saved as {filename}")
