import nuke
import os



# ========================================================================== #
# This section defines color settings.
# ========================================================================== #

# Set color management -> OCIO
nuke.knobDefault('Root.colorManagement', 'OCIO')


# ========================================================================== #
# This section defines third party imports.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# NukeSurvivalToolkit v2.1.1
# https://github.com/CreativeLyons/NukeSurvivalToolkit_publicRelease

print("Importing NukeSurvivalToolkit:")
nuke.pluginAddPath('./repo/NukeSurvivalToolkit_2.1.1/NukeSurvivalToolkit', addToSysPath=True)

# -------------------------------------------------------------------------- #

# Pixelfudger v3.2 - Updated 2023/11/17
# https://github.com/xbourque/pixelfudger

print("Importing Pixelfudger:")
nuke.pluginAddPath('./repo/pixelfudger_3.2v1_nov_2023/pixelfudger3')

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section defines ofx and plugin imports.
# ========================================================================== #
