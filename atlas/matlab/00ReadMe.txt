siminos/froehlich/matlab/00ReadMe.txt
$Author: predrag $
$Date:2010-04-21 18:36:47 -0400 (Wed, 21 Apr 2010) $
----------------------------------------------------------------------------

ComplexLorenz.m is just the function for the complex Lorenz
equations used for ode45 in PlotCL.m and FiniteTimeStep.m.

PlotCL.m takes in the initial value and length of time you want
to integrate over, and plots the trajectory of the system.

FiniteTimeStep.m takes in the initial value, length of the time
interval before it is rotated back into the x1=0 slice, and the
number of intervals this is to be done one. It outputs the
values of the system after each rotation and displays these in
a graph (this is not a graph of the entire trajectory).

CL4D.m is the function used in ode45 for the reduced complex
Lorenz equations for Infinitesimal.m.

Infinitesimal.m takes in the initial value and length of time
you want to integrate over. It rotates the initial point into
the x1=0 hyperplane and then calculates the trajectory using
the reduced equations you get in the method of moving frames.

HilbEq.m is the function used in ode45 for a Hilbert basis
version of the system.

Hilbert1.m calculates the trajectory of the flow in the
coordinates of a Hilbert basis.

Hilbert2.m calculates the trajectory of the flow in standard
coordinates then converts the resulting flow into the
coordinates of a Hilbert basis.

reqstability.m calculates the stability matrix of the relative
equilibrium when a slice is used to restrict the flow to the 4D
hyperplane perpendicular to the vector [1 0 0 0 0].

reqstability2.m takes in a theta value and calculates the
stability of the relative equilibrium when the flow is
restricted to a 4D hyperplane. The slice used is the hyperplane
normal to the group tangent at the point in the relative
equilibrium orbit that is rotated by theta from a set point.

Jacobian.m takes in the initial value and time and then
calculates the Jacobian of the trajectory at that time by using
the system of differential equations, d/dt J^t(x) = A(x) J^t(x)
with initial condition J^0(x) = I. This is the most accurate of
the three programs for calculating the Jacobian.

Jacobian2.m takes in the initial value and time and then
calculates the Jacobian of the trajectory at that time by
multiplying the infinitesimal Jacobians between successive
points and using the approximation e ^(dt A(x_n)) for the
infinitesimal Jacobians

Jacobian3.m takes in the initial value and time and then
calculates the Jacobian of the trajectory at that time by
multiplying the infinitesimal Jacobians between successive
points and using the approximation I + dt A(x_n) for the
infinitesimal Jacobians

JacEq.m calculates the derivatives of the Jacobian and
trajectory for use by the ode45 function used in Jacobian.m

ReducedAttractor.m takes in an initial point and length of
time, It calculates the trajectory for 2* the length of time
given, and then rotates the second half of the trajectory into
the slice and plots it.

rpoNewton.m takes in an initial guess for the angular shift,
period, and point on a relative periodic orbit, then performs
Newton's method to find one.
