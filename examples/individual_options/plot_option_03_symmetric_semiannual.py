"""
03. MSIS Option 3: Symmetric Semiannual
=======================================

This example demonstrates the analysis of MSIS Option 3,
which controls Semiannual atmospheric oscillations. This option represents a key
physical process that affects atmospheric density variations.

Understanding how this option affects atmospheric structure is important for
atmospheric modeling, satellite operations, and space weather applications.
"""

import matplotlib.pyplot as plt
from msis_options_utils import create_option_analysis_figure


# %%
# Option 3 controls Semiannual atmospheric oscillations
# =====================================================
#
# This atmospheric effect includes:
#
# * Twice-yearly atmospheric oscillations
# * Semiannual density and temperature variations
# * Atmospheric response to semiannual solar forcing
# * Global atmospheric circulation effects
#
# This analysis shows how enabling ONLY this option affects atmospheric density
# compared to a baseline with all options disabled.

option_index = 3
option_name = "Symmetric Semiannual"

fig = create_option_analysis_figure(option_index, option_name)

# %%
# Understanding the Results
# =========================
#
# **Panel A (Altitude Profiles)**: Shows how this effect varies with altitude
# and between different seasonal and diurnal conditions. Look for differences
# between the four curves to understand temporal variability.
#
# **Panel B (Geographic Map)**: Reveals the global pattern of this atmospheric
# effect. The contour plot shows percentage changes when ONLY this option is enabled
# compared to the baseline (all options OFF).
#
# **Panel C (Diurnal Cycle)**: Demonstrates how this effect varies throughout
# a 24-hour period at a fixed location (45°N, 0°E, 300 km altitude).
#
# **Panel D (Seasonal Cycle)**: Shows how the strength of this effect
# varies throughout the year, revealing seasonal dependencies.

plt.show()

# %%
# Physical Importance
# ===================
#
# This atmospheric effect is important because:
#
# * Captures important semiannual density variations
# * Affects satellite drag twice per year
# * Important for atmospheric dynamics understanding
# * Contributes to seasonal atmospheric modeling accuracy
#
# When this option is enabled (starting from a baseline with all options OFF),
# these physical processes are added to the atmospheric model, demonstrating
# their specific contribution to atmospheric density variations.
