# Kinetic Energy for a rolling ball given a certain speed
_Keep in mind this is a very simplified version of reality. For example the pendulum weight would also contribute to the total Mass of the ball but is here left out._

## **Known Parameters**
- `M_sphere` = Mass of the hollow sphere (kg)  
- `L` = Length of the pendulum arm to center of mass (m)  
- `g` = Gravitational acceleration = 9.81 m/s²  
- `v` = Desired speed (m/s) 

### The total kinetic energy of ball:
$$
E_{\text{kin}} = \frac{1}{2} M_{\text{sphere}} v^2 + \frac{1}{2} I \omega^2
$$

with, rolling ball without slipping:

$$
\omega = \frac{v}{R}
$$

and, for hollow sphere:

$$
I = \frac{2}{3} M_{\text{sphere}} R^2
$$

##### Simplifying formula

$$
E_{\text{kin}} = \frac{1}{2} M_{\text{sphere}} v^2 + \frac{1}{2} \left(\frac{2}{3} M_{\text{sphere}} R^2\right) \left(\frac{v}{R}\right)^2
$$

$$
\boxed{E_{\text{kin}} = \frac{5}{6} M_{\text{sphere}} v^2}
$$

This formula allows us to calculate the energy required to move the ball by rotation for a given total **mass** and **speed** of the ball.

---
### Potential energy for pendulum
The pendulum must be able to match the energy required by the ball’s kinetic energy.  
For this we want to know the weight it needs to be for a given arm length and swing angle.

When the pendulum swings to an angle `θ` from vertical, its center of mass rises by a vertical distance `Δh`:

\[
\Delta h = L(1 - \cos\theta)
\]

Therefore, the potential energy at that point is:

\[
E_{\text{pend}} = M_{\text{pend}} g \Delta h = M_{\text{pend}} g L (1 - \cos\theta)
\]

---

#### Solve for M of pendulum
We equate pendulum potential energy to the ball kinetic energy:

\[
E_{\text{pend}} = E_{\text{kin}}
\]

\[
M_{\text{pend}} g L (1 - \cos\theta) = \frac{5}{6} M_{\text{sphere}} v^2
\]

\[
\boxed{M_{\text{pend}} = \frac{\frac{5}{6} M_{\text{sphere}} v^2}{g L (1 - \cos\theta)}}
\]

This formula allows us to calculate the pendulum mass needed for a **target speed**, **ball mass**, **arm length**, and **maximum swing angle θ**.

---

# Going from Energy to Torque
The motor will require a certain torque to move the given pendulum mass and arm.

## **Known Parameters**
- `m` = Mass of the pendulum (kg)  
- `L` = Length of the pendulum arm to center of mass (m)  
- `g` = Gravitational acceleration = 9.81 m/s²  
- `α` = Desired angular acceleration (rad/s²)
- `θ_max` = Maximum angular displacement from vertical (rad)  
- `SF` = Safety factor (typically 1.5–2)

---

### **Step 1: Moment of Inertia**
For a point mass at the end of a massless rod:
\[
I = m \cdot L^2
\]

---

### **Step 2: Torque due to Angular Acceleration**
\[
\tau_\text{inertia} = I \cdot \alpha = m L^2 \alpha
\]

---

### **Step 3: Torque due to Gravity**
\[
\tau_\text{gravity} = m g L \sin\theta
\]

Maximum torque occurs at maximum deflection angle `θ_max`:
\[
\tau_\text{gravity, max} = m g L \sin\theta_\text{max}
\]

---

### **Step 4: Total Torque Required**
\[
\tau_\text{total} = \tau_\text{inertia} + \tau_\text{gravity} = m L^2 \alpha + m g L \sin\theta_\text{max}
\]

---

### **Step 5: Torque with Safety Factor**
\[
\tau_\text{motor} = SF \cdot \tau_\text{total}
\]

\[
\boxed{\tau_\text{motor} = SF \cdot ( m L^2 \alpha + m g L \sin\theta_\text{max} )}
\]

Adding a safety factor is crucial because of motor and mechanical efficiency losses!

---

# Taking rotational speed into account
Besides torque, our motor will need to reach a certain **RPM** to deliver the required energy.

#### The pendulum’s rotational kinetic energy is:

\[
E_{\rm pend,rot} = \frac{1}{2} I \omega_{\rm pend}^2
\]

with, for a point mass at the end of a massless rod:

\[
I = M_{\rm pend} L^2
\]

so:

\[
E_{\rm pend,rot} = \frac{1}{2} M_{\rm pend} L^2 \omega_{\rm pend}^2
\]

#### Equate pendulum rotational energy to ball kinetic energy:
\[
E_{\rm pend,rot} = E_{\rm kin}
\]

\[
\frac{1}{2} M_{\rm pend} L^2 \omega_{\rm pend}^2 = E_{\rm kin}
\]

Solve symbolically for angular speed:

\[
\boxed{\omega_{\rm pend} = \sqrt{\frac{2 E_{\rm kin}}{M_{\rm pend} L^2}}}
\]

#### Convert to RPM:
\[
\text{RPM} = \frac{60}{2 \pi} \, \omega_{\rm pend} = \frac{60}{2 \pi} \sqrt{\frac{2 E_{\rm kin}}{M_{\rm pend} L^2}}
\]


---

# Example calculation: Comparison for 45° vs 90° pendulum swing

We want to calculate the required pendulum mass \(M_{\rm pend}\) to roll a hollow sphere to a desired speed,
considering **two swing angles**: 45° and 90°.

---

## Step 0: Given Parameters

- Mass of hollow sphere: \(M_{\rm sphere} = 6\ \rm kg\)  
- Radius of sphere: \(R = 0.45\ \rm m\)  
- Pendulum arm length: \(L = 0.30\ \rm m\)  
- Desired ball speed: \(v = 1\ \rm m/s\)  
- Gravitational acceleration: \(g = 9.81\ \rm m/s^2\)  
- Desired angular acceleration: \(\alpha = 3.7\ \rm rad/s^2\)  
- Safety factor: \(SF = 1.5\)

---

## Step 1: Ball Kinetic Energy

\[
E_{\rm kin} = \frac{5}{6} M_{\rm sphere} v^2 = \frac{5}{6} \cdot 6 \cdot 1^2 = 5.0\ \rm J
\]

---

## Step 2: Pendulum Height Change

\[
\Delta h = L (1 - \cos\theta)
\]

| Angle | θ [deg] | θ [rad] | Δh [m] |
|-------|----------|----------|---------|
| 45°   | 45       | π/4      | 0.30(1-0.7071)=0.0879 |
| 90°   | 90       | π/2      | 0.30(1-0)=0.30 |

---

## Step 3: Required Pendulum Mass

\[
M_{\rm pend} = \frac{E_{\rm kin}}{g \Delta h}
\]

| Angle | Δh [m] | M_pend [kg] |
|-------|---------|--------------|
| 45°   | 0.0879  | 5.8          |
| 90°   | 0.30    | 1.70         |

> Smaller swing angles require **larger pendulum mass**, because less height change reduces potential energy.

---

## Step 4: Total Torque Required

\[
\tau_\text{total} = M_{\rm pend} L^2 \alpha + M_{\rm pend} g L \sin\theta
\]

| Angle | τ_inertia [N·m] | τ_gravity [N·m] | τ_total [N·m] | τ_motor (SF=1.5) [N·m] |
|-------|-----------------|-----------------|---------------|------------------------|
| 45°   | 5.8·0.3²·3.7 ≈ 1.94 | 5.8·9.81·0.3·sin45° ≈ 12.1 | 14.0 | 21.0 |
| 90°   | 1.70·0.3²·3.7 ≈ 0.57 | 1.70·9.81·0.3·sin90° ≈ 5.0 | 5.57 | 8.35 |

---

## Step 5: Pendulum Angular Speed

\[
\omega_{\rm pend} = \sqrt{\frac{2 E_{\rm kin}}{M_{\rm pend} L^2}}
\]

| Angle | ω [rad/s] | RPM |
|-------|------------|-----|
| 45°   | √(2·5 / (5.8·0.3²)) ≈ 2.83 | 27 |
| 90°   | √(2·5 / (1.7·0.3²)) ≈ 8.09 | 77 |

---

## ✅ Summary Table

| Parameter | 45° Swing | 90° Swing |
|-----------|-----------|-----------|
| Pendulum Mass \(M_{\rm pend}\) | 5.8 kg | 1.70 kg |
| Motor Torque (with SF) | 21.0 N·m | 8.35 N·m |
| Pendulum Angular Speed \(ω_{\rm pend}\) | 2.83 rad/s | 8.09 rad/s |
| Equivalent RPM | 27 RPM | 77 RPM |

> 🔹 **Insight:**  
> - Smaller swing angles → need larger mass and higher torque, but slower angular speed.  
> - Full horizontal swing (90°) → smaller mass, smaller torque, faster angular speed.


# Relevant links

- [Rolling ball intertia](http://hyperphysics.phy-astr.gsu.edu/hbase/rotwe.html)
- [Hollow ball Interia](https://images.squarespace-cdn.com/content/v1/58757ed7f5e231cc32494a1b/1507333885709-Y85UDFNJZNJOU1YR52MJ/rotational+inertiaimg.jpg)
- []()