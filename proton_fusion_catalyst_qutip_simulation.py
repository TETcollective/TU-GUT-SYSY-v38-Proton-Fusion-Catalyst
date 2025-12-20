# proton_fusion_catalyst_qutip_simulation.py
# TU-GUT-SYSY v38 – Design 12: Proton Fusion Entanglement Catalyst
# QuTiP few-body simulation of anyonic phase enhancement in p-p fusion
# Author: Simon Soliman
# Date: December 2025
# License: CC BY-NC 4.0
# DOI (paper): https://doi.org/10.5281/zenodo.xxxxxx (da aggiornare)

# Installa QuTiP (una sola volta)
!pip install qutip

# Codice simulazione
import numpy as np
from qutip import *
import matplotlib.pyplot as plt

theta = 6 * np.pi / 5
beta = 0.32

r = np.linspace(0.01, 5, 200)
V_coul = 1.44 / r
V_eff = V_coul * (1 - beta * np.sin(theta / 2))

plt.figure(figsize=(10, 6))
plt.plot(r, V_coul, label='Coulomb standard', linewidth=3)
plt.plot(r, V_eff, label=f'Catalyzed (β={beta}, θ=6π/5)', linewidth=3, linestyle='--')
plt.xlabel('Distanza relativa r (fm)')
plt.ylabel('Potenziale effettivo (MeV)')
plt.title('Proton Fusion Entanglement Catalyst – Potenziale modificato')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(0, 3)
plt.xlim(0, 3)
plt.show()
