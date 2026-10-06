Complex potential
================

In two-dimensional incompressible, irrotational flow, the flow can often be
represented by a complex potential

.. math::

   \Omega(z) = \Phi(x,y) + i\Psi(x,y),

where :math:`z = x + iy`, :math:`\Phi` is the velocity potential, and
:math:`\Psi` is the stream function.

The complex potential is an analytic function of :math:`z` in the flow domain,
so it satisfies the Cauchy-Riemann equations

.. math::

   \frac{\partial \Phi}{\partial x}
   = \frac{\partial \Psi}{\partial y},
   \qquad
   \frac{\partial \Phi}{\partial y}
   = -\frac{\partial \Psi}{\partial x}.

These equations imply that both :math:`\Phi` and :math:`\Psi` are harmonic,
so they satisfy Laplace's equation,

.. math::

   \nabla^2 \Phi = 0,
   \qquad
   \nabla^2 \Psi = 0.

Basic flow equations
--------------------

The complex velocity is obtained by differentiating the complex potential,

.. math::

   -\frac{d\Omega}{dz} = q_x + iq_y,

where :math:`q_x` and :math:`q_y` are the velocity components in the :math:`x` and
:math:`y` directions. Equivalently,

.. math::

   u = \frac{\partial \Phi}{\partial x}
   = \frac{\partial \Psi}{\partial y},
   \qquad
   v = \frac{\partial \Phi}{\partial y}
   = -\frac{\partial \Psi}{\partial x}.

The streamlines are the level curves of :math:`\Psi`, while the equipotential
curves are the level curves of :math:`\Phi`. Since the flow is incompressible
and irrotational, these curves intersect orthogonally, and the velocity field is
invariant under a conformal change of variables.

This is the key idea behind conformal mapping in fluid mechanics: a complicated
flow domain can be mapped to a simpler one, such as the upper half-plane or the
unit disk, where the complex potential is easier to write down.
