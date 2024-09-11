"""
------------------------------------------------------------------------
[CP164]
------------------------------------------------------------------------
Author: Gurshan bhogal
ID:     169052062
Email:  bhog2062@mylaurier.ca
__updated__ = "2024-01-11"
------------------------------------------------------------------------
"""
from functions import reroute

opstring = "SSSSXXXX"
values_in = [1, 2, 3, 4]
values_out = reroute(opstring, values_in)
print(f"Opstring: {opstring}")
print(f"Order: {values_in}")
print(f"New order: {values_out}")