from designVals import *
from Pendulum_Calculator import *
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


''' Estimation on power requirements and respective capacity required'''

# def estimate_current(torque, rpm, V, eff_motor, eff_esc, run_time_min):
#     '''TBD'''
#     return P_out, P_in, I_in, capacity_Ah

def battery_sizing(I_nom, V_nom, max_discharge_sys, max_discharge_batt, battV, battC, run_time_min):
    '''Estimate cells in series and parallel per battery pack and total number of packs.'''
    # Cells 
    Nseries = np.ceil(V_nom / battV)
    Nparallel = np.ceil(max_discharge_sys / max_discharge_batt)

    cellsperpack = Nseries * Nparallel
    # Packs
    reqC = I_nom*run_time_min/60/0.8  # [Ah]
    
    total_packs = np.ceil(reqC / (Nparallel * battC))

    total_cells = total_packs * Nparallel * Nseries
    return cellsperpack, total_packs, reqC, total_cells



def battery_comparison(pd_battery, V_nom, I_nom, run_time_min):
    """Compare different battery types based on total cells required and plot."""
    # Use the correct name column
    name_col = "battery_name" if "battery_name" in pd_battery.columns else "name"


    

    # Create two subplots: one for Total Packs vs Total Cells and one for Cells per Pack vs Total Cells
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Reset legend handles for each subplot by re-iterating through the battery data
    for _, row in pd_battery.iterrows():
        cellsperpack, total_packs, total_Ah, total_cells = battery_sizing(
            I_nom,
            V_nom,
            80,
            row["max_continuous_discharge_A"],
            row["nominal_voltage_V"],
            row["capacity_Ah"],
            run_time_min,
        )
        label = row.get("battery_name", row.get("name", "Unnamed"))
        axs[0].scatter(total_cells, total_packs, marker="o", label=label)
        axs[1].scatter(total_cells, cellsperpack, marker="o", label=label)
        axs[2].scatter(total_packs, cellsperpack, marker="o", label=label)

    axs[0].set_xlabel("Total Cells")
    axs[0].set_ylabel("Total Packs")
    axs[0].set_title("Total Packs vs Total Cells")
    axs[0].legend(title="Battery")

    axs[1].set_xlabel("Total Cells")
    axs[1].set_ylabel("Cells per Pack")
    axs[1].set_title("Cells per Pack vs Total Cells")
    axs[1].legend(title="Battery")

    axs[2].set_xlabel("Total Packs")
    axs[2].set_ylabel("cellsperpack")
    axs[2].set_title("Total Cells vs cellsperpack")
    axs[2].legend(title="Battery")

    plt.tight_layout()
    plt.show()





if __name__ == "__main__":
    battery_comparison(pd_battery, V_nom, 2, desired_run_time)

    # I_nom = np.linspace(1, 10, 100)  # [Ah]


    # cellsperpack, total_packs, total_Ah, total_cells = battery_sizing(I_nom, V_nom, 5, 3.7, 3.3, desired_run_time)

    # plt.figure(figsize=(10, 5))

    # plt.subplot(1, 2, 1) 
    # plt.plot(I_nom, total_packs, marker='o')
    # plt.xlabel("Nominal Current (Ah)")
    # plt.ylabel("Total Packs")
    # plt.title("Total Packs vs Nominal Current")

    # plt.subplot(1, 2, 2)
    # plt.plot(I_nom, total_cells, marker='o', color="orange")
    # plt.xlabel("Nominal Current (Ah)")
    # plt.ylabel("Total Cells")
    # plt.title("Total Cells vs Nominal Capacity")

    # plt.tight_layout()
    # plt.show()


    