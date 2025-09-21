import matplotlib.pyplot as plt
import numpy as np

# ---------------- Data ----------------
processes = np.array([1, 4, 8, 16, 32, 64])
times = np.array([0.1632, 0.0442, 0.0234, 0.0164, 0.0193, 0.0043])
speedup = times[0] / times
efficiency = speedup / processes

n = np.array([10**2, 10**4, 10**6, 10**8])
time_1 = np.array([0.0000, 0.0000, 0.0016, 0.1632])
time_64 = np.array([0.0014, 0.0004, 0.0009, 0.0034])
error_64 = np.array([2.65e-6, 2.65e-10, 2.63e-14, 0.0])
epsilon = 1e-6
speedup_problem_size = (time_1 + epsilon) / time_64

ntasks_per_node = np.array([2, 4, 8, 16, 32, 48])
execution_times_ntasks = np.array([0.2676, 0.2672, 0.2761, 0.2767, 0.2823, 0.2875])

subplot_labels = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']

# ---------------- Plotting Subplots ----------------
fig, axs = plt.subplots(3, 2, figsize=(16, 8))
axs = axs.flatten()

# (a) Execution time vs processes
axs[0].plot(processes, times, marker='o', color='b')
axs[0].set_yscale('log')
axs[0].set_xlabel('Processes (P)')
axs[0].set_ylabel('Time (sec, log scale)')
axs[0].set_title(f'{subplot_labels[0]} Execution Time vs Processes')
axs[0].grid(True, which='both', ls='--')

# (b) Speedup vs processes
axs[1].plot(processes, speedup, marker='o', color='r')
axs[1].set_xlabel('Processes (P)')
axs[1].set_ylabel('Speedup')
axs[1].set_title(f'{subplot_labels[1]} Speedup vs Processes')
axs[1].grid(True, ls='--')

# (c) Efficiency vs processes
axs[2].plot(processes, efficiency, marker='s', linestyle='--', color='g')
axs[2].set_xlabel('Processes (P)')
axs[2].set_ylabel('Efficiency')
axs[2].set_title(f'{subplot_labels[2]} Efficiency vs Processes')
axs[2].set_ylim(0, 1.1)
axs[2].grid(True, ls='--')

# (d) Speedup vs problem size
axs[3].plot(n, speedup_problem_size, marker='o', color='m')
axs[3].set_xscale('log')
axs[3].set_yscale('log')
axs[3].set_xlabel('Problem size n')
axs[3].set_ylabel('Speedup')
axs[3].set_title(f'{subplot_labels[3]} Speedup vs Problem Size (p=1 vs p=64)')
axs[3].grid(True, which='both', ls='--')
axs[3].set_xticks(n)
axs[3].set_xticklabels([r'$10^2$', r'$10^4$', r'$10^6$', r'$10^8$'])

# (e) Relative error vs problem size
axs[4].plot(n, error_64, marker='s', linestyle='--', color='c')
axs[4].set_xscale('log')
axs[4].set_yscale('log')
axs[4].set_xlabel('Problem size n')
axs[4].set_ylabel('Relative Error')
axs[4].set_title(f'{subplot_labels[4]} Relative Error vs Problem Size (p=64)')
axs[4].grid(True, which='both', ls='--')
axs[4].set_xticks(n)
axs[4].set_xticklabels([r'$10^2$', r'$10^4$', r'$10^6$', r'$10^8$'])

# (f) Execution time vs ntasks-per-node
axs[5].plot(ntasks_per_node, execution_times_ntasks, marker='o', color='orange')
axs[5].set_xscale('linear')
axs[5].set_yscale('log')
axs[5].set_xlabel('Number of Tasks per Node')
axs[5].set_ylabel('Execution Time (sec, log scale)')
axs[5].set_title(f'{subplot_labels[5]} Execution Time vs Tasks per Node')
axs[5].grid(True, which='both', ls='--')
axs[5].set_xticks(ntasks_per_node)

plt.tight_layout()
plt.show()
