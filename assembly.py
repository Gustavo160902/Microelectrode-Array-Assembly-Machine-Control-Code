# assembly.py

import time
from motor_control import (
    update_speed,
    return_to_origin,
    stop_motor_control,
    move_linear_stage,
)
from relay_control import (
    laser_relay_on,
    laser_relay_off,
)
from Print import (
    glue_sequence,
    print_pcb,
    print_pad,
    pad_types,
)
from image_recognition import (
    extrude,
    x_align,
    r_align
)

# Sequence flags — set to True to enable in full assembly run
print_traces_seq =  ("print",      False)  # print traces + connector pads
rotate_neg_seq =    ("rotate_neg", False)  # rotate -90 to placement station
placement_seq =     ("placement",  False)  # extrude + align + place microwires
rotate_pos_seq =    ("rotate_pos", False)  # rotate +90 back to print station
fill_pads_seq =     ("fill",       False)  # fill electrode pads with metal ink

sequences = (print_traces_seq, rotate_neg_seq, placement_seq, rotate_pos_seq, fill_pads_seq)

def fill_electrode_pads():
    """Fill all 8 electrode pads with metal ink after wire placement."""
    # to be implemented — print only electrode pads
    pass

def sequence_handler(seq):
    name = seq[0]
    if name == "print":
        print_pcb()
    elif name == "rotate_neg":
        # rotate -90 to placement station
        update_speed(50)
        move_linear_stage('r', '-', 90, wait_for_stop=True, max_wait=30.0)
    elif name == "placement":
        # extrude + align + place — to be implemented
        pass
    elif name == "rotate_pos":
        # rotate +90 back to print station
        update_speed(50)
        move_linear_stage('r', '+', 90, wait_for_stop=True, max_wait=30.0)
    elif name == "fill":
        fill_electrode_pads()

def run_full_assembly():
    for seq in sequences:
        if seq[1] == True:
            print(f"Running sequence: {seq[0]}")
            sequence_handler(seq)
    print("Full assembly complete.")
