import math
import numpy as np
import matplotlib.pyplot as plt
from designVals import *
from mpl_toolkits.mplot3d import Axes3D

def sphere_I(M_sphere, D):
    '''Calculate the moment of inertia of a hollow sphere.
    Inputs:
    M_sphere : Mass of the sphere (kg)
    D        : Diameter of the sphere (m)
    Returns:
    I        : Moment of inertia (kg·m²)
    '''
    R = D / 2
    I = (2/3) * M_sphere * R**2
    return I

def calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg):
    '''Calculate the minimum pendulum mass required to achieve a target ball speed.
    Function uses energy conservation and rotational dynamics principles, assuming no energy losses.
    Inputs:
    M_sphere : Mass of the sphere (kg)
    D        : Diameter of the sphere (m)
    L        : Length of the pendulum arm (m)
    v_ball   : Target ball speed (m/s)
    theta_deg: Pendulum release angle (degrees)
    Returns:
    M_pend   : Minimum pendulum mass (kg)

    '''
    theta_rad = np.radians(theta_deg)
    E_kin_v = (5/6) * M_sphere * v_ball**2
    E_kin_rot = 0.5 * sphere_I(M_sphere, D) * (v_ball / (D/2))**2

    E_kin = E_kin_v + E_kin_rot

    M_pend = E_kin / (9.81 * L * np.sin(theta_rad))
    return M_pend

def calculate_pendulum_torque(M_sphere, D, L, theta_deg, M_pend, v_ball, SF=1.5):
    '''Calculate the torque exerted by the pendulum on the motor shaft, the ball's acceleration, and the motor RPM, assumes no losses.
    Inputs:
    M_sphere : Mass of the sphere (kg)
    D        : Diameter of the sphere (m)
    L        : Length of the pendulum arm (m)
    theta_deg: Pendulum release angle (degrees)
    M_pend   : Mass of the pendulum (kg)
    v_ball   : Target ball speed (m/s)
    SF       : Safety factor (default=1.5)
    Returns:
    tau_motor: Torque on the motor shaft (N·m)
    a_ball   : Ball acceleration (m/s²)
    rpm_motor: Motor speed (RPM)
    '''
    R = D / 2
    theta_rad = np.radians(theta_deg)


    tau_motor_array = SF + M_pend * 9.81 * L * np.sin(theta_rad)
    a_ball_array = (3 * tau_motor_array) / (5 * M_sphere * R)
    omega_motor_array = v_ball / R
    rpm_motor_array = (omega_motor_array * 60) / (2 * np.pi)

    return tau_motor_array, a_ball_array, rpm_motor_array


def print_table(title, angles, M_sphere, D, L, M_pend, v_ball):
    print(f"\n=== {title} ===")
    print(f"{'Angle (deg)':>12} | {'Torque (N·m)':>15} | {'Ball Accel (m/s²)':>20} | {'Motor RPM':>10}")
    print("-" * 65)
    for angle in angles:
        tau, a, rpm = calculate_pendulum_torque(M_sphere, D, L, angle, M_pend, v_ball)
        print(f"{angle:12.1f} | {tau:15.3f} | {a:20.3f} | {rpm:10.3f}")

# --- Example usage ---
if __name__ == "__main__":


    angles = np.arange(10, 60, 1)
    m_pend_array = np.array(calculate_pendulum_mass(M_sphere, D, L, v_ball, angles) )

    m_pend_array_generated = np.linspace(0.5, 15, 15)
    tau_array_opt = np.array(calculate_pendulum_torque(M_sphere, D, L, angles, M_pend=m_pend_array, v_ball=v_ball)[0] )

    tau_matrix = np.zeros((len(m_pend_array_generated), len(angles)))
    for i, m_pend in enumerate(m_pend_array_generated):
        for j, angle in enumerate(angles):
            tau_matrix[i, j], _, _ = calculate_pendulum_torque(M_sphere, D, L, angle, m_pend, v_ball)

    # Replace the previous 1x2 subplot block with a 1x3 layout:
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    ax1.plot(angles, m_pend_array)
    ax1.set_xlabel("Angle (deg)")
    ax1.set_ylabel("Pendulum Mass (kg)")
    ax1.set_title("Pendulum Mass vs Angle")
    ax1.grid(True)
    
    ax2.plot(angles, tau_array_opt, color='orange')
    ax2.set_xlabel("Angle (deg)")
    ax2.set_ylabel("Torque (N·m)")
    ax2.set_title("Torque vs Optimal Angle for Given Mass")
    ax2.grid(True)
    
    cax = ax3.imshow(tau_matrix, extent=[angles[0], angles[-1], m_pend_array_generated[0], m_pend_array_generated[-1]],
                     aspect='auto', origin='lower', cmap='viridis')
    ax3.set_xlabel("Angle (deg)")
    ax3.set_ylabel("Pendulum Mass (kg)")
    ax3.set_title("Torque vs Angle and Pendulum Mass")
    fig.colorbar(cax, ax=ax3, label="Torque (N·m)")



    plt.tight_layout()
    plt.show()
