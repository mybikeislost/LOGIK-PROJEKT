import nuke
import re
import os



# ========================================================================== #
# This section defines core projekt tools.
# ========================================================================== #

nuke.pluginAddPath('./repo/projekt-core_v0.0.1')

# -------------------------------------------------------------------------- #

# Node defaults
#import defaults

# -------------------------------------------------------------------------- #

# Toggle Viewer Pipes
import viewerOps
nuke.menu("Nuke").addCommand('Viewer/Toggle Viewer Pipes', 
                             viewerOps.toggleViewerPipes, 
                             'alt+t')


# -------------------------------------------------------------------------- #

# ReadFromWrite
import readFromWrite
nuke.menu('Nuke').addCommand('Edit/Node/Read from Write',
                             'readFromWrite.ReadFromWrite()',
                             'alt+r')

# -------------------------------------------------------------------------- #



# ========================================================================== #
# This section defines third party tool packages.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Stamps v1.1.0
# https://github.com/adrianpueyo/Stamps

print("Importing Stamps:")
nuke.pluginAddPath("./repo/Stamps_v1.1.0/stamps")

try:
    import stamps
    print("Stamps imported successfully.")
except ImportError:
    print("Failed to import Stamps... Continuing without it.")

# -------------------------------------------------------------------------- #

# KnobScripter v3.1.0
# https://github.com/adrianpueyo/KnobScripter

print("Importing KnobScripter:")
nuke.pluginAddPath("./repo/KnobScripter-3.1.0")
try:
    import KnobScripter
except ImportError:
    print("Failed to import KnobScripter... Continuing without it.")


# -------------------------------------------------------------------------- #