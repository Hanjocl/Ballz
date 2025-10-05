import math

def calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg):
    theta_rad = math.radians(theta_deg)
    E_kin = (5/6) * M_sphere * v_ball**2
    M_pend = E_kin / (9.81 * L * math.sin(theta_rad))
    return M_pend

def calculate_pendulum_torque(M_sphere, D, L, theta_deg, M_pend, v_ball, SF=1.5):
    R = D / 2
    theta_rad = math.radians(theta_deg)
    tau_motor = SF * M_pend * 9.81 * L * math.sin(theta_rad)
    a_ball = (3 * tau_motor) / (5 * M_sphere * R)
    omega_motor = v_ball / R
    rpm_motor = (60 / (2 * math.pi)) * omega_motor
    return tau_motor, a_ball, rpm_motor

def print_table(title, angles, M_sphere, D, L, M_pend, v_ball):
    print(f"\n=== {title} ===")
    print(f"{'Angle (deg)':>12} | {'Torque (N·m)':>15} | {'Ball Accel (m/s²)':>20} | {'Motor RPM':>10}")
    print("-" * 65)
    for angle in angles:
        tau, a, rpm = calculate_pendulum_torque(M_sphere, D, L, angle, M_pend, v_ball)
        print(f"{angle:12.1f} | {tau:15.3f} | {a:20.3f} | {rpm:10.3f}")

# --- Example usage ---
if __name__ == "__main__":
    M_sphere = 6
    D = 0.45
    L = 0.3
    v_ball = 1.0

    # Case 1: theta = 90°
    theta_deg_case1 = 90
    M_pend_90 = calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg_case1)
    print(f"\nInput Values: Sphere Mass={M_sphere} kg, Diameter={D} m, Arm Length={L} m, Target Ball Speed={v_ball} m/s")
    print(f"Minimum Pendulum Mass for theta={theta_deg_case1}°: {M_pend_90:.3f} kg")

    print_table("Torque & Motor Requirements (Using Min Mass at 90°)", [45, 90], M_sphere, D, L, M_pend_90, v_ball)

    print("\n" + "-"*65)

    # Case 2: theta = 45°
    theta_deg_case2 = 45
    M_pend_45 = calculate_pendulum_mass(M_sphere, D, L, v_ball, theta_deg_case2)
    print(f"\nInput Values: Sphere Mass={M_sphere} kg, Diameter={D} m, Arm Length={L} m, Target Ball Speed={v_ball} m/s")
    print(f"Minimum Pendulum Mass for theta={theta_deg_case2}°: {M_pend_45:.3f} kg")

    print_table("Torque & Motor Requirements (Using Min Mass at 45°)", [45, 90], M_sphere, D, L, M_pend_45, v_ball)
