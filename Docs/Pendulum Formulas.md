# Formulas Used for Pendulum-Driven Rolling Ball

This document provides explanations for all formulas used in designing a motor-stabilized pendulum inside a rolling hollow sphere.

---

## 1. Ball Kinetic Energy

The total kinetic energy of a rolling hollow sphere:

\[
E_{\rm kin} = \frac{1}{2} M_{\rm sphere} v^2 + \frac{1}{2} I \omega^2
\]

Where:
- \(M_{\rm sphere}\) = mass of the hollow sphere  
- \(v\) = linear speed of the sphere  
- \(I\) = rotational inertia of the sphere  
- \(\omega = v/R\) for rolling without slipping  

For a hollow sphere, \(I = \frac{2}{3} M_{\rm sphere} R^2\), so:

\[
E_{\rm kin} = \frac{1}{2} M_{\rm sphere} v^2 + \frac{1}{2} \left(\frac{2}{3} M_{\rm sphere} R^2\right) \left(\frac{v}{R}\right)^2 = \frac{5}{6} M_{\rm sphere} v^2
\]

> This gives the energy needed to roll the ball at a given speed.

---

## 2. Potential Energy of Pendulum

Potential energy of a pendulum mass raised to height \(\Delta h\):

\[
E_{\rm pend} = M_{\rm pend} g \Delta h = M_{\rm pend} g L (1 - \cos\theta)
\]

Where:
- \(M_{\rm pend}\) = pendulum mass  
- \(L\) = pendulum arm length  
- \(\theta\) = angle from vertical  
- \(g\) = gravitational acceleration

> This is used to determine the pendulum mass needed for a target energy.

---

## 3. Pendulum Mass for Desired Ball Acceleration

The linear acceleration of the ball caused by a pendulum at fixed angle \(\theta\) is:

\[
a_{\rm ball} = \frac{3 M_{\rm pend} g L \sin\theta}{5 M_{\rm sphere} R}
\]

Solve for pendulum mass:

\[
M_{\rm pend} = \frac{5 M_{\rm sphere} R \ a_{\rm ball}}{3 g L \sin\theta}
\]

> This formula allows calculation of the pendulum mass required for a desired acceleration.

---

## 4. Motor Torque Required

The motor must provide torque to hold the pendulum at angle \(\theta\):

\[
\tau_{\rm motor} = SF \cdot M_{\rm pend} g L \sin\theta
\]

Where \(SF\) is a safety factor to account for mechanical losses.

---

## 5. Ball Acceleration from Pendulum Torque

The torque applied to the ball produces linear acceleration:

\[
a_{\rm ball} = \frac{3 \tau_{\rm pend}}{5 M_{\rm sphere} R}
\]

> For a hollow sphere, \(I_{\rm ball} = \frac{2}{3} M_{\rm sphere} R^2\) and total rotational + translational inertia = \(I + M R^2 = 5/3 M R^2\).

---

## 6. Motor Angular Speed to Hold Pendulum Fixed

To keep the pendulum stationary relative to the floor while the ball rolls:

\[
\omega_{\rm motor} = \frac{v_{\rm ball}}{R}, \quad \text{RPM} = \frac{60}{2\pi} \omega_{\rm motor}
\]

> Motor RPM depends on ball speed and radius, independent of pendulum angle.

---

## 7. Summary

- **Kinetic energy** formula gives energy of rolling ball.  
- **Potential energy** gives energy stored in pendulum.  
- **Pendulum mass formula** allows calculation for target acceleration.  
- **Torque formula** sizes motor.  
- **Motor RPM formula** ensures pendulum stays fixed relative to floor.

