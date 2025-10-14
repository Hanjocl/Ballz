from designVals import *
from Pendulum_Calculator import *

''' Estimation on power requirements and respective capacity required'''
def estimate_power(KV, V, eff_motor, eff_esc, run_time_min):
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
    M_pend = calculate_pendulum_mass(M_sphere, D, L, v_ball, 45)  # Using 45 degrees as a reference angle
    tau_motor, a_ball, rpm_motor = calculate_pendulum_torque(M_sphere, D, L, 45, M_pend, v_ball)  # Using 45 degrees as a reference angle
    P_out = tau_motor * omega_motor
    P_in = P_out / (eff_motor * eff_esc)
    I_in = P_in / V
    capacity_Ah = (I_in * run_time_min) / 60
    return P_out, P_in, I_in, capacity_Ah