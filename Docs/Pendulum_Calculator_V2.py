import math
import matplotlib.pyplot as plt

def calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg):
    theta_rad = math.radians(theta_deg)
    E_kin = (5/6) * M_sphere * v_ball**2
    M_pend = E_kin / (9.81 * L * math.sin(theta_rad))
    return M_pend

def calculate_pendulum_torque(M_sphere, D, L, theta_deg, M_pend, v_ball, SF=1.5):
    theta_rad = math.radians(theta_deg)
    tau_pendulum = M_pend * 9.81 * L * math.sin(theta_rad)
    return tau_pendulum, None, None

# --- Example usage ---
if __name__ == "__main__":
    M_sphere = 6
    D = 0.45
    L = 0.3
    v_ball = 1.0

    angles = list(range(10, 61, 1))
    m_pend_list = []
    torque_list = []

    # First, calculate pendulum mass for each angle and store it
    for angle in angles:
        m_pend = calculate_pendulum_mass(M_sphere, D, L, v_ball, angle)
        m_pend_list.append(m_pend)

    # Now, use the calculated mass for each angle to compute torque
    for angle, m_pend in zip(angles, m_pend_list):
        tau, _, _ = calculate_pendulum_torque(M_sphere, D, L, angle, m_pend, v_ball)
        theta_rad = math.radians(angle)
        print(f"Angle: {angle} deg | M_pend: {m_pend:.4f} kg | sin(theta): {math.sin(theta_rad):.4f} | Torque: {tau:.4f} Nm")
        torque_list.append(tau)

    # Plotting
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(angles, m_pend_list, label="Pendulum Mass (kg)")
    plt.xlabel("Angle (deg)")
    plt.ylabel("Pendulum Mass (kg)")
    plt.title("Angle vs Pendulum Mass")
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(angles, torque_list, color='orange', label="Torque (N·m)")
    plt.xlabel("Angle (deg)")
    plt.ylabel("Torque (N·m)")
    plt.title("Angle vs Torque")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()