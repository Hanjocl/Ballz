import math

def calculate_pendulum_parameters_energy(M_sphere, D, L, v_ball, theta_deg, SF=1.5):
    """
    Calculate pendulum parameters based on kinetic energy required to roll the ball.

    Parameters:
    - M_sphere: mass of the sphere (kg)
    - D: diameter of the sphere (m)
    - L: length of the pendulum arm (m)
    - v_ball: target ball speed (m/s)
    - theta_deg: pendulum angle from vertical (degrees)
    - SF: safety factor for torque

    Returns:
    Dictionary with pendulum mass, torque, resulting ball acceleration, and motor RPM.
    """
    print("\n=== Input Parameters ===")
    print(f"Sphere Mass (kg): {M_sphere}")
    print(f"Sphere Diameter (m): {D}")
    print(f"Pendulum Arm Length (m): {L}")
    print(f"Pendulum Angle (deg): {theta_deg}")
    print(f"Safety Factor: {SF}")
    print(f"Target Ball Speed (m/s): {v_ball}")

    R = D / 2
    theta_rad = math.radians(theta_deg)

    # Calculate kinetic energy of rolling ball
    E_kin = (5/6) * M_sphere * v_ball**2

    # Pendulum mass based on energy
    M_pend = E_kin / (9.81 * L * math.sin(theta_rad))

    # Torque required with safety factor
    tau_motor = SF * M_pend * 9.81 * L * math.sin(theta_rad)

    # Resulting ball acceleration from torque
    a_ball = (3 * tau_motor) / (5 * M_sphere * R)

    # Motor angular speed to hold pendulum fixed (rad/s)
    omega_motor = v_ball / R

    # Convert to RPM
    rpm_motor = (60 / (2 * math.pi)) * omega_motor

    results = {
        'Pendulum Mass (kg)': M_pend,
        'Torque Required (N·m)': tau_motor,
        'Resulting Ball Acceleration (m/s²)': a_ball,
        'Motor RPM': rpm_motor
    }

    print("\n=== Calculated Results ===")
    for key, value in results.items():
        print(f"{key}: {value:.3f}")

    return results

# Example usage
if __name__ == "__main__":
    calculate_pendulum_parameters_energy(
        M_sphere=6,     # kg
        D=0.45,         # m
        L=0.3,          # m
        v_ball=1.0,     # m/s
        theta_deg=45,   # degrees
        SF=1.5
    )