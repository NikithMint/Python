import math
import matplotlib.pyplot as plt
def area_ratio(mach, gamma, area_throat, area_exit):
    """Returns the area ratio A/A* for a converging-diverging nozzle"""
    if mach < 1.0:
        # Subsonic flow
        ratio = (1.0/gamma)*(1.0 + (gamma-1.0)/2.0*mach*2)**(gamma/(gamma-1.0))
    else:
        # Supersonic flow
        ratio = (1.0/gamma)*(1.0 + (gamma-1.0)/2.0*mach*2)**(1.0/(1.0-gamma/2.0))
    return area_exit/area_throat*ratio
# Inputs
gamma = 1.4  # Specific heat ratio
area_throat = 1.0  # Throat area
area_exit = 3.0  # Exit area
# Calculate area ratio for Mach numbers between 0.1 and 3.0
mach_numbers = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
area_ratios = [area_ratio(mach, gamma, area_throat, area_exit) for mach in mach_numbers]
# Print results
for i in range(len(mach_numbers)):
    print("Mach number: {mach_numbers[i]}, Area ratio: {area_ratios[i]}")
plt.plot(area_ratio,mach_numbers,linewidth=2,color='blue')
plt.xlabel('Area Ratio')
plt.ylabel('Mach Number')
plt.title('Area Mach Number Relation')
plt.grid()
plt.show()
