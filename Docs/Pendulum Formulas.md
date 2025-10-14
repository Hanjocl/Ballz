# Formulas Used for Pendulum-Driven Rolling Ball

This document provides explanations for all formulas used in designing a motor-stabilized pendulum inside a rolling hollow sphere.

---

## 1. Ball Kinetic Energy

The total kinetic energy of a rolling hollow sphere:

\[
E_{\rm kin} = \frac{1}{2} M_{\rm sphere} v^2 + \frac{1}{2} I \omega^2
\]

Where:
- $M_{\mathrm{sphere}}$ = mass of the hollow sphere  
- $v$ = linear speed of the sphere  
- $I$ = rotational inertia of the sphere  
- $\omega = v/R$ for rolling without slipping  

For a hollow sphere, $I = \frac{2}{3} M_{\mathrm{sphere}} R^2$, so:

$$
E_{\mathrm{kin}} = \frac{1}{2} M_{\mathrm{sphere}} v^2 + \frac{1}{2} \left(\frac{2}{3} M_{\mathrm{sphere}} R^2\right) \left(\frac{v}{R}\right)^2 = \frac{5}{6} M_{\mathrm{sphere}} v^2
$$

> This gives the energy needed to roll the ball at a given speed.

---

## 2. Potential Energy of Pendulum

Potential energy of a pendulum mass raised to height $\Delta h$:

$$
E_{\mathrm{pend}} = M_{\mathrm{pend}} g \Delta h = M_{\mathrm{pend}} g L (1 - \cos\theta)
$$

Where:
- $M_{\mathrm{pend}}$ = pendulum mass  
- $L$ = pendulum arm length  
- $\theta$ = angle from vertical  
- $g$ = gravitational acceleration

> This is used to determine the pendulum mass needed for a target energy.

---

## 3. Pendulum Mass for Desired Ball Acceleration

The linear acceleration of the ball caused by a pendulum at fixed angle $\theta$ is:

$$
a_{\mathrm{ball}} = \frac{3 M_{\mathrm{pend}} g L \sin\theta}{5 M_{\mathrm{sphere}} R}
$$

Solve for pendulum mass:

$$
M_{\mathrm{pend}} = \frac{5 M_{\mathrm{sphere}} R \ a_{\mathrm{ball}}}{3 g L \sin\theta}
$$

> This formula allows calculation of the pendulum mass required for a desired acceleration.

---

## 4. Motor Torque Required

The motor must provide torque to hold the pendulum at angle $\theta$:

$$
	au_{\mathrm{motor}} = SF \cdot M_{\mathrm{pend}} g L \sin\theta
$$

Where $SF$ is a safety factor to account for mechanical losses.

---

## 5. Ball Acceleration from Pendulum Torque

The torque applied to the ball produces linear acceleration:

$$
a_{\mathrm{ball}} = \frac{3 \tau_{\mathrm{pend}}}{5 M_{\mathrm{sphere}} R}
$$

> For a hollow sphere, $I_{\mathrm{ball}} = \frac{2}{3} M_{\mathrm{sphere}} R^2$ and total rotational + translational inertia = $I + M R^2 = \tfrac{5}{3} M R^2$.

---

## 6. Motor Angular Speed to Hold Pendulum Fixed

To keep the pendulum stationary relative to the floor while the ball rolls:

$$
\omega_{\mathrm{motor}} = \frac{v_{\mathrm{ball}}}{R}, \quad \text{RPM} = \frac{60}{2\pi} \omega_{\mathrm{motor}}
$$

> Motor RPM depends on ball speed and radius, independent of pendulum angle.

---

## 7. Summary

- **Kinetic energy** formula gives energy of rolling ball.  
- **Potential energy** gives energy stored in pendulum.  
- **Pendulum mass formula** allows calculation for target acceleration.  
- **Torque formula** sizes motor.  
- **Motor RPM formula** ensures pendulum stays fixed relative to floor.

