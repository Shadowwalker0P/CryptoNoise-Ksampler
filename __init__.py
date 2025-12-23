"""
CryptoNoise KSampler - Cryptographic Artist Authentication for AI-Generated Art

Version: 1.0.0
Author: Shadowwalker
License: Creative Commons Attribution-NonCommercial 4.0 International (BY-NC)

For more information, see README.md and LICENSE
"""

__version__ = "1.0.0"
__author__ = "Shadowwalker"
__license__ = "BY-NC 4.0"

from .cryptonoise_ksampler import CryptoNoise_KSampler, NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = [
    "CryptoNoise_KSampler",
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
