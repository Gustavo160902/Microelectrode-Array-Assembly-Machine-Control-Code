# assembly.py

import time
from motor_control import (
    update_speed,
    move_linear_stage,
)
from print import (
    print_pcb,
    fill_electrode_pads,
    calibrate,
    x_home,
    y_home,
    z_home,
    x, y, z,
)

def run_full_assembly():
    """
    Full assembly sequence:
    1. Calibrate and print traces
    2. Return to home
    3. Rotate -90 to placement station
    4. Wait 20 seconds (test value)
    5. Adjust axes slightly
    6. Rotate +90 back
    7. Calibrate and print again
    8. Fill electrode pads
    """
    print("Starting full assembly...")

    # Step 1 — calibrate and print traces
    calibrate()
    print_pcb()

    # Step 2 — return to home
    update_speed(100)
    z_home()
    y_home()
    x_home()

    # Step 3 — rotate -90 to placement station
    update_speed(50)
    move_linear_stage('r', '-', 90, wait_for_stop=True, max_wait=30.0)

    # Step 4 — wait 20 seconds for testing
    print("Waiting 20 seconds...")
    time.sleep(20)

    # Step 5 — adjust axes slightly (test values)
    move_linear_stage(x, '-', 5000, wait_for_stop=True, max_wait=30.0)
    move_linear_stage(y, '-', 5000, wait_for_stop=True, max_wait=30.0)
    move_linear_stage(z, '+', 5000, wait_for_stop=True, max_wait=30.0)

    # Step 6 — rotate +90 back to print station
    move_linear_stage('r', '+', 90, wait_for_stop=True, max_wait=30.0)

    # Step 7 — calibrate and print again
    calibrate()
    print_pcb()

    # Step 8 — fill electrode pads
    fill_electrode_pads()

    print("Full assembly complete.")


# # assembly.py

# from print import full_sequence

# def run_full_assembly():
#     full_sequence()
