import pandas as pd

#Interial 
M_sphere = 6 # [kg]
D = 0.45 # [m]
L = 0.3 # [m]
v_ball = 1.0 # [m/s]

#Power
V_nom = 24 # [Volts]
desired_run_time = 60*4  # [minutes]


motor_data = {
    "Name": [
        "ODrive S1 and M8325s Motor Kit",
        "Rctimer GBM5010-150T 90KV",
        "Eaglepower LA8308 130kv",
        "C4250 Outrunner",
        "Motor 5065"
    ],
    "Mass (kg)": [6.62, 0.15, 3.5, 2.0, 0.65],
    "KV (RPM/V)": [100, 90, 130, 560, 270],
    "Torque Constant (Nm/A)": [1.13, 50.00, 2.14, 3.75, 11.54],
    "Resistance (Ω)": [13.24, 7.50, 10.50, 8.00, 7.80],
    "Power (W)": [1200, 43, 1040, 3360, 540],
    "Price (€)": [117.71, 15.80, 55.77, 37.34, None]  # None for missing value
}

pd_motor = pd.DataFrame(motor_data)

