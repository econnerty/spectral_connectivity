# flake8: noqa
import logging
import os
logging.basicConfig(level=logging.DEBUG)
os.environ["SPECTRAL_CONNECTIVITY_ENABLE_GPU"] = "true"
from spectral_connectivity.connectivity import Connectivity
from spectral_connectivity.transforms import Multitaper
from spectral_connectivity.wrapper import multitaper_connectivity

__version__ = "1.1.2"
