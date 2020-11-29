#!/usr/bin/env python
#
# Tom's Pong
# A simple pong game with realistic physics and AI
#
# Released under the GNU General Public License

VERSION = "0.4"

try:
    import sys
    import random
    import math
    import os
    import getopt
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print("couldn't load module:", err)
    sys.exit(2)