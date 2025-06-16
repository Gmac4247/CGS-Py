""" Insert this line into the legacy code to import functions from the module. """

import basic_geometry 

""" Usage example of functions """
""" Replacy legacy expressions by the exact ones where the output is. """

print(basic_geometry.exact_circle_area(r))   
print(basic_geometry.exact_circumference(r)) 
print(basic_geometry.exact_sphere_volume(r))   
print(basic_geometry.exact_cone_volume(r, h))  
print("sin(30):", approx_sin(30))
print("cos(60):", approx_cos(60))
print("tan(45):", approx_tan(45))
print("asin(0.5):", approx_asin(0.5))
print("acos(0.5):", approx_acos(0.5))
print("atan(1):", approx_atan(1))
