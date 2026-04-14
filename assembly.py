# assembly.py

import time
from motor_control import (
    update_speed,
    return_to_origin,
    stop_motor_control,
    move_linear_stage,
)
from print import (
    glue_sequence,
    print_pcb,
    fill_electrode_pads,
    calibrate,
    x_home,
    y_home,
    z_home,
    x, y, z,
)
from image_recognition import (
    extrude,
    x_align,
    r_align
)

def run_full_assembly():
    """
    Full assembly sequence:
    1. Calibrate and print traces
    2. Return to home
    3. Rotate -90 to placement station
    4. Wait 20 minutes
    5. Adjust axes slightly
    6. Rotate +90 back
    7. Repeat placement
    8. Fill electrode pads
    """
    print("Starting full assembly...")

    # Step 1 — calibrate and print traces
    calibrate()
    print_pcb()

    # Step 2 — return to home
    update_speed(100)
    x_home()
    y_home()
    z_home()

    # Step 3 — rotate -90 to placement station
    update_speed(50)
    move_linear_stage('r', '-', 90, wait_for_stop=True, max_wait=30.0)

    # Step 4 — wait 20 minutes
    print("Waiting 20 minutes for placement...")
    time.sleep(1200)

    # Step 5 — adjust axes slightly (test values)
    move_linear_stage(x, '-', 5000, wait_for_stop=True, max_wait=30.0)
    move_linear_stage(y, '-', 5000, wait_for_stop=True, max_wait=30.0)
    move_linear_stage(z, '+', 5000, wait_for_stop=True, max_wait=30.0)

    # Step 6 — rotate +90 back to print station
    move_linear_stage('r', '+', 90, wait_for_stop=True, max_wait=30.0)

    # Step 7 — repeat placement
    calibrate()
    print_pcb()

    # Step 8 — fill electrode pads
    fill_electrode_pads()

    print("Full assembly complete.")
