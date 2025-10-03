# Kinetic Energy for a rolling ball given a certain speed
_Keep in mind this is a very simplified version of reality. For example the pendulum weight would also contribute to the total Mass of the ball but is here left out._

## **Known Parameters**
- `M_sphere` = Mass of the hollow sphere (kg)  
- `L` = Length of the pendulum arm to center of mass (m)  
- `g` = Gravitational acceleration = 9.81 m/s²  
- `v` = Desired speed (m/s) 

#### The total kinetic energy of ball:
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

---
##### Simplified formula

$$
E_{\text{kin}} = \frac{1}{2} M_{\text{sphere}} v^2 + \frac{1}{2} \left(\frac{2}{3} M_{\text{sphere}} R^2\right) \left(\frac{v}{R}\right)^2
$$

$$
\boxed{E_{\text{kin}} = \frac{5}{6} M_{\text{sphere}} v^2}
$$

---
#### Potential energy for pendulum
$$
E_{\text{pend}} = M g r
$$

---
##### Solve for M of pendulum
$$
E_{\text{pend}} = E_{\text{kin}}
$$

$$
M g r = \frac{5}{6} M_{\text{sphere}} v^2
$$

---
##### Solving for M of pendulum
$$
M = \frac{\frac{5}{6} M_{\text{sphere}} v^2}{g r}
$$

---

# Going from Energy to Torque
The motor will require a certain torque to move the given mass and arm of the pendulum.

## **Known Parameters**
- `m` = Mass of the pendulum (kg)  
- `L` = Length of the pendulum arm to center of mass (m)  
- `g` = Gravitational acceleration = 9.81 m/s²  
- `α` = Desired angular acceleration (rad/s²)

> Maximum linear acceleration of the ball:

$$
a_{\rm ball, max} = \frac{\tau_{\rm pend,max} \cdot R}{I_{\rm ball} + M R^2} 
= \frac{m g L \cdot R}{\frac{2}{3} M R^2 + M R^2} 
= \frac{3 m g L}{5 M R}
$$

- `θ_max` = Maximum angular displacement from vertical (rad)  
- `SF` = Safety factor (typically 1.5–2)

#### **Step 1: Moment of Inertia**
For a point mass at the end of a massless rod:
$$
I = m \cdot L^2
$$


#### **Step 2: Torque due to Angular Acceleration**
$$
\tau_\text{inertia} = I \cdot \alpha = m L^2 \alpha
$$

---

#### **Step 3: Torque due to Gravity**
$$
\tau_\text{gravity} = m \cdot g \cdot L \cdot \sin\theta
$$

- Maximum torque occurs at horizontal position:  
$$
\tau_\text{gravity, max} = m g L
$$

---

#### **Step 4: Total Torque Required**
$$
\tau_\text{total} = \tau_\text{inertia} + \tau_\text{gravity} = m L^2 \alpha + m g L \sin\theta
$$

---

#### **Step 5: Torque with Safety Factor**
$$
\tau_\text{motor} = \text{SF} \cdot \tau_\text{total} 
$$

$$
\tau_\text{motor} = \text{SF} \cdot ( m L^2 \alpha + m g L \sin\theta_\text{max} )
$$

---
# Example calculation
We want to calculate the required pendulum mass \(M_{\rm pend}\) to roll a hollow sphere to a desired speed.

---
## Calculate kinetic energy required

##### **step 0: Given Parameters**

- Mass of hollow sphere: \(M_{\rm sphere} = 6\ \text{kg}\)  
- Radius of sphere: \(R = 0.45\ \text{m}\)  
- Pendulum lever arm: \(L = 0.30\ \text{m}\)  
- Desired ball speed: \(v = 1\ \text{m/s}\)  
- Gravitational acceleration: \(g = 9.81\ \text{m/s²}\)  


##### **Step 1: Calculate Ball Kinetic Energy**
Using:
$$
E_{\text{kin}} = \frac{5}{6} M_{\text{sphere}} v^2
$$

plug in numbers:

$$
E_{\rm kin} = \frac{5}{6} \cdot 6 \cdot 1^2 = 5.0\ \text{J}
$$

---

##### **Step 2: Solve for Pendulum Mass**

Maximum potential energy of the pendulum:

$$
E_{\rm pend} = M_{\rm pend} g L
$$

Set \(E_{\rm pend} = E_{\rm kin}\) to provide enough energy:

$$
M_{\rm pend} = \frac{E_{\rm kin}}{g L} = \frac{5.0}{9.81 \cdot 0.30} \approx 1.70\ \text{kg}
$$

---

## Calculate motor torque & rotational speed

##### **Given Parameters**

- Mass of hollow sphere: \(M_{\rm sphere} = 6\ \text{kg}\)  
- Pendulum lever arm: \(L = 0.30\ \text{m}\)  
- Desired ball speed: \(v = 1\ \text{m/s}\)  
- Gravitational acceleration: \(g = 9.81\ \text{m/s²}\)  
- Desired pendulum angular acceleration: \(\alpha = 3.7\ \text{rad/s²}\) (example)  
- Maximum pendulum angle from vertical: \(\theta = 90^\circ = \pi/2\) rad  
- Safety factor: \(SF = 1.5\)  

---

##### **Step 3: Calculate Total Torque Required**

Using the total torque formula:

$$
\tau_\text{total} = \tau_\text{inertia} + \tau_\text{gravity}
$$

$$
\tau_\text{total} = m L^2 \alpha + m g L \sin\theta
$$

$$
\tau_{\rm total} = 1.70 \cdot 0.30^2 \cdot 3.7 + 1.70 \cdot 9.81 \cdot 0.30 \approx 5.565 \text{Nm}
$$

---

##### **Step 4: Apply Safety Factor**

$$
\tau_\text{motor} = SF \cdot \tau_\text{total} = 1.5 \cdot 5.57 \approx 8.36\ \text{Nm}
$$

---


# Relevant links

- [Rolling ball intertia](http://hyperphysics.phy-astr.gsu.edu/hbase/rotwe.html)
- [Hollow ball Interia](https://images.squarespace-cdn.com/content/v1/58757ed7f5e231cc32494a1b/1507333885709-Y85UDFNJZNJOU1YR52MJ/rotational+inertiaimg.jpg)
- []()