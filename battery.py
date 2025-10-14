from designVals import *
from Pendulum_Calculator import *
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


''' Estimation on power requirements and respective capacity required'''

def estimate_power(KV, V, eff_motor, eff_esc, run_time_min, angle):
    '''Estimate the power requirements and battery capacity needed for the motor setup.
    Inputs:
    KV         : Motor KV rating (RPM/V)
    V          : Battery voltage (V)
    eff_motor  : Motor efficiency (0 < eff_motor <= 1)
    eff_esc    : ESC efficiency (0 < eff_esc <= 1)
    run_time_min: Desired run time (minutes)
    Returns:
    P_out      : Output power required (W)
    P_in       : Input power required (W)
    I_in       : Input current required (A)
    capacity_Ah: Required battery capacity (Ah)
    '''
    rpm_motor = KV * V
    omega_motor = (rpm_motor * 2 * math.pi) / 60
    R = D / 2
    v_ball = omega_motor * R
    M_pend = calculate_pendulum_mass(M_sphere, D, L, v_ball, angle) 
    tau_motor, a_ball, rpm_motor = calculate_pendulum_torque(M_sphere, D, L, angle, M_pend, v_ball) 
    P_out = tau_motor * omega_motor
    P_in = P_out / (eff_motor * eff_esc)
    I_in = P_in / V
    capacity_Ah = (I_in * run_time_min) / 60
    return P_out, P_in, I_in, capacity_Ah


if __name__ == "__main__":
    angles = np.arange(10, 60, 1)
    pd_motor = pd_motor
    P_out, P_in, I_in, capacity_Ah = estimate_power(pd_motor.loc[0, "KV (RPM/V)"], V_nom, 0.85, 0.95, desired_run_time, angles)


    plt.figure()
    plt.plot(angles, capacity_Ah, marker='o')
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Battery Capacity (Ah)')
    plt.title('Angle vs. Battery Capacity')
    plt.grid(True)
    plt.show()