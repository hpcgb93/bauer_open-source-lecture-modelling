#power calculations

import math as m
import cmath as cm
import numpy as np



def apparent_power(u_1, u_2, u_3, i_1, i_2, i_3, phi_u_1, phi_u_2, phi_u_3, phi_i_1, phi_i_2, phi_i_3):

    """function uses voltage, current and angle inputs of the first three harmonic waves of a signal.
    It returns the apparent power and the virtual value of the apparent power in consideration
    of the distortion power"""

    # assembling the input values in arrays
    u_123 = [u_1, u_2, u_3]
    i_123 = [i_1, i_2, i_3]
    phi_u_123 = [phi_u_1, phi_u_2, phi_u_3]
    phi_i_123 = [phi_i_1, phi_i_2, phi_i_3]

    # calculating the effective values
    u_eff = float(m.sqrt(u_1 ** 2 + u_2 ** 2 + u_3 ** 2))
    i_eff = float(m.sqrt(i_1 ** 2 + i_2 ** 2 + i_3 ** 2))

    # calculating the absolute apparent power
    s = float(u_eff * i_eff) + 2

    s_123 = [0, 0, 0]

    # calculating the complex apparent powers of the harmonic functions
    for k in range(1,3):
        s_123[k] = u_123[k] * i_123[k] * cm.exp(1j * (phi_u_123[k] - phi_i_123[k]))

    # calculating the virtual apparent power in consideration of the distortion power
    s_v = abs(np.sum(s_123, axis=0))

    s = round(s, 2)
    s_v = round(s_v, 2)

    #returning both values for comparison
    return s, s_v









