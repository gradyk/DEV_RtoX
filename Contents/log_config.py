# #############################################################################
#  Copyright (c) 2019. Kenneth A. Grady                                       #
#                                                                             #
#  Redistribution and use in source and binary forms, with or without         #
#  modification, are permitted provided that the following conditions are met:#
#                                                                             #
#  1. Redistributions of source code must retain the above copyright          #
#  notice, this list of conditions and the following disclaimer.              #
#                                                                             #
#  2. Redistributions in binary form must reproduce the above copyright       #
#  notice, this list of conditions and the following disclaimer in the        #
#  documentation and/or other materials provided with the distribution.       #
#                                                                             #
#  3. Neither the name of the copyright holder nor the names of its           #
#  contributors may be used to endorse or promote products derived            #
#  from this software without specific prior written permission.              #
#                                                                             #
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS    #
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,  #
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR     #
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR          #
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,      #
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,        #
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR         #
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF     #
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING       #
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF              #
#  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.          #
# #############################################################################

# CRITICAL 50
# ERROR 40
# WARNING 30
# INFO 20
# DEBUG 10
# NOTSET 0

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-22"
__name__ = "Contents.log_config"

import logging
import os
import sys
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=30)
logging.propagate=False
logger = logging.getLogger(__name__)


# Create Handlers
conhandler = logging.StreamHandler()
conhandler.setLevel(logging.INFO)

base_dir_pre = os.path.dirname(os.path.abspath(sys.argv[0]))
base_dir = base_dir_pre + "/logs"

filehandler_debug = logging.handlers.RotatingFileHandler(
    filename=os.path.join(base_dir, "rtox.log"),  mode="w",  maxBytes=8000,
    backupCount=20)
filehandler_debug.setLevel(logging.DEBUG)

# Create Formatters
conformat = logging.Formatter(fmt='%(asctime)s | %(name)s | %(levelname)s '
                              '| %(filename)s | %(lineno)d |%(message)s')
fileformat = logging.Formatter(fmt='%(asctime)s | %(name)s | %(levelname)s '
                               '| %(filename)s | %(lineno)d | %(message)s')

# Set Formatters
conhandler.setFormatter(conformat)
filehandler_debug.setFormatter(fileformat)

# Add handlers to the logger
logger.addHandler(conhandler)
logger.addHandler(filehandler_debug)
