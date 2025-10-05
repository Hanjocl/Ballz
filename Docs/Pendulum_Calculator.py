import math

def calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg):
    """
    Calculate the minimum pendulum mass required to deliver the target ball speed.

    Parameters:
    - M_sphere: mass of the sphere (kg)
    - D: diameter of the sphere (m)
    - L: length of the pendulum arm (m)
    - v_ball: target ball speed (m/s)
    - theta_deg: pendulum angle from vertical (degrees)

    Returns:
    - Minimum pendulum mass (kg)
    """
    theta_rad = math.radians(theta_deg)
    # Kinetic energy of the rolling ball
    E_kin = (5/6) * M_sphere * v_ball**2
    # Pendulum mass from potential energy
    M_pend = E_kin / (9.81 * L * math.sin(theta_rad))
    return M_pend

def calculate_pendulum_torque(M_sphere, D, L, theta_deg, M_pend, SF=1.5):
    """
    Calculate torque and resulting ball acceleration for a given pendulum mass.

    Parameters:
    - M_sphere: mass of the sphere (kg)
    - D: diameter of the sphere (m)
    - L: length of the pendulum arm (m)
    - theta_deg: pendulum angle from vertical (degrees)
    - M_pend: mass of the pendulum (kg)
    - SF: safety factor

    Returns:
    Dictionary with torque and ball acceleration.
    """
    R = D / 2
    theta_rad = math.radians(theta_deg)

    # Torque required to hold pendulum at angle theta
    tau_motor = SF * M_pend * 9.81 * L * math.sin(theta_rad)

    # Ball acceleration from torque
    a_ball = (3 * tau_motor) / (5 * M_sphere * R)

    results = {
        'Torque Required (N·m)': tau_motor,
        'Resulting Ball Acceleration (m/s²)': a_ball
    }

    return results

# Example usage
if __name__ == "__main__":
    # --- First case: theta = 90° ---
    M_sphere = 6
    D = 0.45
    L = 0.3
    v_ball = 1.0
    theta_deg_case1 = 90

    print("\n=== Case 1: Theta = 90° ===")
    print(f"Sphere Mass (kg): {M_sphere}")
    print(f"Sphere Diameter (m): {D}")
    print(f"Pendulum Arm Length (m): {L}")
    print(f"Target Ball Speed (m/s): {v_ball}")
    print(f"Pendulum Angle (deg): {theta_deg_case1}")
    print(f"===============>")

    # Calculate minimum pendulum mass
    M_pend_90 = calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg_case1)
    print(f"Minimum Pendulum Mass: {M_pend_90:.3f} kg")

    # Torque for fixed mass
    torque_90 = calculate_pendulum_torque(M_sphere, D, L, theta_deg_case1, M_pend_90)
    print(f"Torque Required (N·m): {torque_90['Torque Required (N·m)']:.3f}")
    print(f"Resulting Ball Acceleration (m/s²): {torque_90['Resulting Ball Acceleration (m/s²)']:.3f}")


    torque_45 = calculate_pendulum_torque(M_sphere, D, L, 45, M_pend_90)
    print(f"Torque Required (N·m): {torque_45['Torque Required (N·m)']:.3f}")
    print(f"Resulting Ball Acceleration (m/s²): {torque_45['Resulting Ball Acceleration (m/s²)']:.3f}")

    print("\n---------------------------")

    # --- Second case: theta = 45° ---
    theta_deg_case2 = 45

    print("\n=== Case 2: Theta = 45° ===")
    print(f"Sphere Mass (kg): {M_sphere}")
    print(f"Sphere Diameter (m): {D}")
    print(f"Pendulum Arm Length (m): {L}")
    print(f"Target Ball Speed (m/s): {v_ball}")
    print(f"Pendulum Angle (deg): {theta_deg_case2}")
    print(f"===============>")

    # Calculate minimum pendulum mass
    M_pend_45 = calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg_case2)
    print(f"Minimum Pendulum Mass: {M_pend_45:.3f} kg")

    # Torque for fixed mass
    torque_90_case2 = calculate_pendulum_torque(M_sphere, D, L, 90, M_pend_45)
    print(f"Torque Required (N·m): {torque_90_case2['Torque Required (N·m)']:.3f}")
    print(f"Resulting Ball Acceleration (m/s²): {torque_90_case2['Resulting Ball Acceleration (m/s²)']:.3f}")

    torque_45_case2 = calculate_pendulum_torque(M_sphere, D, L, theta_deg_case2, M_pend_45)
    print(f"Torque Required (N·m): {torque_45_case2['Torque Required (N·m)']:.3f}")
    print(f"Resulting Ball Acceleration (m/s²): {torque_45_case2['Resulting Ball Acceleration (m/s²)']:.3f}")
