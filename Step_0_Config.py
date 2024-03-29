import numpy as np

#--------------------------------------------------
# GLOBAL
#--------------------------------------------------

number_of_images = 1000
train_fraction = 0.7
validation_fraction = 0.2
# test fraction = 1 - train_fraction - validation_fraction

path = "data"#"data/dataset/"
filename_format = "{N}x{N}_with_{n}_stars"
# Parameters:
# - {i}: image number
# - {N}: size of the image
# - {n}: star number
# - {f}: fwhm
# - {s}: sky magnitude
# - {M}: maximum magnitud star
# - {m}: minimum magnitude star

#--------------------------------------------------
# SKY
#--------------------------------------------------

N = 1000 # Image size (in pixels)
nb_stars = 100 # Number of stars
fwhm = 3 # fwhm of all stars
noise_intensity = 4 # mean of the gaussian noise
noise_std = 0.1 # standard deviation of the gaussian noise

def intensity_prob(I:float) -> float:
    """Probability p in [0,1] of generating a star ith intensity I, with I in [0,1]"""
    return 1

#--------------------------------------------------
# TELESCOPE
#--------------------------------------------------

pupil_radius = N/4 # Pupil radius (in pixels)
obstruction_radius = N/20 # Obstruction radius (in pixels)
arms_count = 3 # Number of arms
arms_size = 5 # Arms size (in pixels)
arms_angle = 3 # Arms angle (in degrees)