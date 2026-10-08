# Week 1.2, Session 2: Task 6

import sys

try:
    machine_temp_c = int(input("Machine Temperature (C): "))
    machine_pressure_psi = int(input("Machine Pressure (PSI): "))
    machine_op_status_int = int(input("Machine Operational Status (1/0): "))
except ValueError:
    print("You idiot.")
    sys.exit()

safe = True

if machine_op_status_int == 1:
    machine_op_status = True
elif machine_op_status_int == 0:
    machine_op_status = False
else:
    print("You idiot 2.")
    sys.exit()

if machine_temp_c > 80:
    print("The temperature is too high.")
    safe = False
elif machine_temp_c >= 50:
    print("The temperature is within safe limits.")
else:
    print("The temperature is low; no action needed.")

if machine_pressure_psi > 100:
    print("High pressure is detected; maintenance recommended.")
    safe = False
elif machine_pressure_psi >= 70:
    print("The pressure is stable.")
else:
    print("The pressure is low; operating normally.")

if machine_op_status:
    if not safe:
        print("The machine is running in unsafe conditions; recommend shut down.")
    else:
        print("Everything normal; machine running normally.")
else:
    print("Machine not currently operating; no immediate action is needed.")
