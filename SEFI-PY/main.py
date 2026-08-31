# main.py

import sys

from demo_core import demo_core
from demo_sim import demo_sim
from demo_warp import demo_warp
from demo_quantum import demo_quantum


MENU = """
SEFI-PY MAIN MENU
-----------------
1. SEFI Core Pipeline Demo
2. SEFI-SIM World Simulation
3. Torsion Warp Simulation
4. Quantum Warp Superposition Demo
5. Exit
"""


def main():
    while True:
        print(MENU)
        choice = input("Select an option: ").strip()

        if choice == "1":
            demo_core()
        elif choice == "2":
            demo_sim()
        elif choice == "3":
            demo_warp()
        elif choice == "4":
            demo_quantum()
        elif choice == "5":
            print("Exiting SEFI-PY.")
            sys.exit(0)
        else:
            print("Invalid selection. Try again.\n")


if __name__ == "__main__":
    main()
