# This program computes the volume in litres of a six-pack of soda cans and the total volume of a six pack and a two-litres bottle
# 
# Mihai Gheorghe
# 2019

#
CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2.0

# Calculate the total volume in the cans
cans_per_pack = 6

six_pack_volume = cans_per_pack * CAN_VOLUME
print("Total volume in a", cans_per_pack, "pack is", six_pack_volume)

# the total volume of a six pack and a two-litres bottle

total_soda_volume = six_pack_volume + BOTTLE_VOLUME
print("Total volume is", total_soda_volume)
