Schwarz-Christoffel Mapping
=================================

The Schwarz-Christoffel formula gives a conformal map from the upper half-plane
to the interior of a polygon. It is especially useful because the polygon's
corners correspond to points on the real axis, called *prevertices*. Conformal
maps preserve angles locally, and the formula encodes each polygon corner's
interior angle in the behavior of the map near its prevertex.

Let

.. math::

   \mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}

be the upper half-plane. For a polygon with vertices having interior angles
:math:`\pi\alpha_1,\ldots,\pi\alpha_n`, choose real prevertices
:math:`x_1 < \cdots < x_{n-1}`, with the remaining prevertex at infinity. The
Schwarz-Christoffel map has the form

.. math::

   f(z) = A + C \int_{z_0}^{z}
   \prod_{j=1}^{n-1} (\zeta - x_j)^{\alpha_j - 1}\,d\zeta,
   \qquad z \in \mathbb{H},

where :math:`A` and :math:`C` are complex constants, and the powers are defined
using branches analytic in :math:`\mathbb{H}`. Equivalently,

.. math::

   f'(z) = C\prod_{j=1}^{n-1}(z-x_j)^{\alpha_j-1}.

Each exponent :math:`\alpha_j-1` determines the angle at the corresponding
polygon vertex. The angles satisfy
:math:`\sum_{j=1}^{n}\alpha_j=n-2`, as required for a polygon, and the constant
and prevertices are chosen to match its size, position, and side lengths.
