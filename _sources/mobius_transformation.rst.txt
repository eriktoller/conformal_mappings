Möbius transformation
=====================

A Möbius transformation is a fractional linear map of the complex plane,

.. math::

   w = \frac{az + b}{cz + d}, \qquad ad - bc \neq 0.

Here :math:`a, b, c, d` are complex constants. The condition
:math:`ad - bc \neq 0` ensures that the map is invertible.

Properties
----------

Möbius transformations are conformal everywhere they are defined. They map
lines and circles in the :math:`z`-plane to lines and circles in the
:math:`w`-plane. In particular, they preserve angles and map the extended
complex plane to itself.

This makes them especially useful in complex analysis and fluid dynamics, where
one often wants to transform a complicated boundary into a simpler one, such as
a half-plane, a circle, or a wedge.

A simple example is the inversion

.. math::

   w = \frac{1}{z},

which sends a line or circle not passing through the origin to another line or
circle. More generally, a Möbius transformation can be composed with shifts,
rotations, dilations, and inversions to build a wide range of useful mappings.

Relation to boundary-value problems
-----------------------------------

In conformal mapping, a Möbius transform is often used as a preliminary change
of variables. It can simplify a boundary geometry before applying a more
specialized transform, such as the Schwarz-Christoffel mapping or a wedge map.
The important point is that the transformation preserves local shape and angle,
while changing the global geometry in a controlled way.
