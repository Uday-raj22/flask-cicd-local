import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def generate_lorenz_plot(output_file):
    def lorenz_system(t, state, sigma, rho, beta):
        x, y, z = state
        return [
            sigma * (y - x),
            x * (rho - z) - y,
            x * y - beta * z
        ]

    sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
    t_span = (0, 40)
    t_eval = np.linspace(*t_span, 10000)

    sol1 = solve_ivp(lorenz_system, t_span, [1, 1, 1],
                     args=(sigma, rho, beta), t_eval=t_eval)
    sol2 = solve_ivp(lorenz_system, t_span, [1.0001, 1, 1],
                     args=(sigma, rho, beta), t_eval=t_eval)

    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    labels = ['x(t)', 'y(t)', 'z(t)']
    for i in range(3):
        axs[i].plot(sol1.t, sol1.y[i])
        axs[i].plot(sol2.t, sol2.y[i], linestyle='--')
        axs[i].set_ylabel(labels[i])
        axs[i].grid(True)

    axs[2].set_xlabel('Time')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

