# Removing spaces from beginning and at the end

name = "        Vivek   "
final_name = name.strip()
print("Name is : ",final_name)


# Removing left space and right space

left_space = name.lstrip()
print("The leftspace removed : ",left_space)

right_space = name.rstrip()
print("The rightspace removed : ",right_space)
