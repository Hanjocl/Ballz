# Motor-Stabilized Pendulum in a Rolling Hollow Sphere

This document explains how to design a pendulum inside a rolling hollow sphere to **control ball acceleration** and **ensure stable motion**. It covers pendulum mass calculation, torque requirements, motor RPM, and ball acceleration for different swing angles.

---

## 1. Given Parameters

| Parameter | Symbol | Value / Unit | Description |
|-----------|--------|--------------|-------------|
| Ball mass | \(M_{\rm sphere}\) | 6 kg | Hollow sphere mass |
| Ball diameter | \(D\) | 45 cm | Sphere diameter |
| Ball radius | \(R\) | 0.225 m | Sphere radius (D/2) |
| Pendulum arm | \(L\) | 0.30 m | Distance from pivot to pendulum mass |
| Gravity | \(g\) | 9.81 m/s² | Gravitational acceleration |
| Pendulum angle | \(\theta\) | 45° or 90° | Angle from vertical |
| Safety factor | \(SF\) | 1.5 | Motor torque safety factor |
| Target ball speed | \(v_{\rm ball}\) | 1.0 m/s | Ball linear speed |

---

## 2. Calculate Required Pendulum Mass

The pendulum mass required to provide the energy needed for a given ball speed **depends on the swing angle**:

\[
M_{\rm pend} = \frac{E_{\rm kin}}{g L \sin\theta}, \quad E_{\rm kin} = \frac{5}{6} M_{\rm sphere} v_{\rm ball}^2
\]

### Example: Target ball speed = 1.0 m/s

| Pendulum Angle | Pendulum Mass [kg] |
|----------------|------------------|
| 45°            | 2.40             |
| 90°            | 1.53             |

> Smaller angles require heavier pendulum mass to deliver the same energy.

---

## 3. Torque Required to Hold Pendulum

Motor torque needed to hold the pendulum at a fixed angle relative to the floor:

\[
\tau_{\rm motor} = SF \cdot M_{\rm pend} g L \sin\theta
\]

| Pendulum Angle | Torque [N·m] |
|----------------|--------------|
| 45°            | 7.50         |
| 90°            | 6.73         |

---

## 4. Resulting Ball Acceleration

The torque produces ball acceleration:

\[
a_{\rm ball} = \frac{3 \tau_{\rm motor}}{5 M_{\rm sphere} R}
\]

| Pendulum Angle | Ball Acceleration [m/s²] |
|----------------|--------------------------|
| 45°            | 3.33                     |
| 90°            | 1.00                     |

> Using a smaller angle increases required mass, which also increases torque and can produce higher acceleration.

---

## 5. Motor Angular Speed (RPM) to Hold Pendulum Fixed

The motor must rotate the pendulum relative to the ball to keep it fixed to the floor:

\[
\omega_{\rm motor} = \frac{v_{\rm ball}}{R}, \quad \text{RPM} = \frac{60}{2\pi} \omega
\]

- Example: \(v_{\rm ball} = 1.0\ \rm m/s, R = 0.225\ m\) → \(\text{RPM} \approx 42.44\)  

> Motor RPM is the same for all angles at a given ball speed.

---

## 6. Summary Table

| Pendulum Angle | Pendulum Mass [kg] | Torque [N·m] | Ball Acceleration [m/s²] | Motor RPM |
|----------------|------------------|--------------|--------------------------|-----------|
| 45°            | 2.40             | 7.50         | 3.33                     | 42.44     |
| 90°            | 1.53             | 6.73         | 1.00                     | 42.44     |

### Notes

- Smaller angles require heavier pendulum mass.  
- Torque depends on pendulum mass, length, and angle.  
- Motor RPM depends only on ball speed.  
- Safety factor ensures motor and mechanical efficiency.

---

## 7. Conceptual Diagram

```
   Floor
     |
     v
    ----- Ball rolling
   /     \
  |       |  <- Motor keeps pendulum fixed
  |  o    |  <- Pendulum mass inside ball
   \     /
    -----
```
- Motor rotates pendulum **inside the rolling ball** at ~42 RPM to hold it fixed relative to the floor.

