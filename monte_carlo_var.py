import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Configuration des Paramètres (Inputs)
# ==========================================
S0 = 100          # Prix initial de l'action (€)
mu = 0.05         # Rendement annuel attendu (5%)
sigma = 0.20      # Volatilité annuelle (20%)
T = 30 / 365      # Horizon temporel : 30 jours (en années)
N_sim = 10000     # Nombre de simulations de Monte Carlo

# ==========================================
# 2. Mouvement Mouvement Brownien Géométrique
# Equation : S_T = S0 * exp((mu - 0.5 * sigma^2)*T + sigma * sqrt(T) * Z)
# ==========================================
np.random.seed(42) # Pour rendre les résultats réproductibles
Z = np.random.normal(0, 1, N_sim) # Variable aléatoire gaussienne N(0,1)
S_T = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

# ==========================================
# 3. Calcul des Pertes et de la VaR (Value at Risk)
# ==========================================
pertes = S0 - S_T

# Calcul de la VaR à 95% et 99%
var_95 = np.percentile(pertes, 95)
var_99 = np.percentile(pertes, 99)

print(f"Prix initial du titre : {S0} €")
print(f"Value at Risk (VaR 95%) sur 30 jours : {var_95:.2f} €")
print(f"Value at Risk (VaR 99%) sur 30 jours : {var_99:.2f} €")

# ==========================================
# 4. Visualisation des Résultats (Matplotlib)
# ==========================================
plt.figure(figsize=(10, 6))
plt.hist(pertes, bins=50, color='#2b5c8f', edgecolor='black', alpha=0.7)

# Lignes représentant la VaR
plt.axvline(var_95, color='orange', linestyle='--', linewidth=2, label=f'VaR 95% : {var_95:.2f} €')
plt.axvline(var_99, color='red', linestyle='--', linewidth=2, label=f'VaR 99% : {var_99:.2f} €')

plt.title('Simulation de Monte Carlo - Distribution des Pertes (VaR)', fontsize=14)
plt.xlabel('Pertes / Gains (€)', fontsize=12)
plt.ylabel('Fréquence', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)

# Sauvegarde du graphique pour le rapport LaTeX
plt.savefig('monte_carlo_var_results.png', dpi=300, bbox_inches='tight')
plt.show()