import matplotlib.pyplot as plt

# --- Dataset 1: 100 million trials ---
threads_100M = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
time_100M = [0.9349,0.4694,0.2436,0.1261,0.0637,0.0329,0.0301,0.0256,
             0.0256,0.0292,0.0325,0.0634,0.1299,0.2613]

speedup_100M = [time_100M[0]/t for t in time_100M]
efficiency_100M = [s/p for s,p in zip(speedup_100M, threads_100M)]

# --- Dataset 2: 10 billion trials ---
threads_10B = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
time_10B = [93.3185,46.8691,24.4800,12.4698,6.3088,3.1582,2.4364,2.2104,
            2.2313,2.1924,2.2066,2.1953,2.2915,2.3529]

speedup_10B = [time_10B[0]/t for t in time_10B]
efficiency_10B = [s/p for s,p in zip(speedup_10B, threads_10B)]

# --- Create figure with 2 rows of 3 subplots each ---
fig, axs = plt.subplots(2, 3, figsize=(16,8))

# --- Row 1: 100M trials ---
axs[0,0].plot(threads_100M, time_100M, 'o-', color='blue')
axs[0,0].set_xscale('log', base=2)
axs[0,0].set_xlabel('Threads')
axs[0,0].set_ylabel('Time (s)')
axs[0,0].set_title('(a) Execution Time (100M trials)')
axs[0,0].grid(True, which="both", ls="--")

axs[0,1].plot(threads_100M, speedup_100M, 's-', color='green')
axs[0,1].set_xscale('log', base=2)
axs[0,1].set_xlabel('Threads')
axs[0,1].set_ylabel('Speedup')
axs[0,1].set_title('(b) Speedup (100M trials)')
axs[0,1].grid(True, which="both", ls="--")

axs[0,2].plot(threads_100M, efficiency_100M, 'd-', color='magenta')
axs[0,2].set_xscale('log', base=2)
axs[0,2].set_xlabel('Threads')
axs[0,2].set_ylabel('Efficiency')
axs[0,2].set_title('(c) Efficiency (100M trials)')
axs[0,2].grid(True, which="both", ls="--")

# --- Row 2: 10B trials ---
axs[1,0].plot(threads_10B, time_10B, 'o-', color='blue')
axs[1,0].set_xscale('log', base=2)
axs[1,0].set_xlabel('Threads')
axs[1,0].set_ylabel('Time (s)')
axs[1,0].set_title('(d) Execution Time (10B trials)')
axs[1,0].grid(True, which="both", ls="--")

axs[1,1].plot(threads_10B, speedup_10B, 's-', color='green')
axs[1,1].set_xscale('log', base=2)
axs[1,1].set_xlabel('Threads')
axs[1,1].set_ylabel('Speedup')
axs[1,1].set_title('(e) Speedup (10B trials)')
axs[1,1].grid(True, which="both", ls="--")

axs[1,2].plot(threads_10B, efficiency_10B, 'd-', color='magenta')
axs[1,2].set_xscale('log', base=2)
axs[1,2].set_xlabel('Threads')
axs[1,2].set_ylabel('Efficiency')
axs[1,2].set_title('(f) Efficiency (10B trials)')
axs[1,2].grid(True, which="both", ls="--")


import matplotlib.pyplot as plt

# Data
trials = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
error = [4.76e-02, 1.01e-02, 4.29e-03, 1.21e-03, 1.29e-03, 2.08e-04, 8.04e-06]

# Plot Error vs Number of Trials
plt.figure(figsize=(10,6))
plt.plot(trials, error, 'o-', color='orange')
plt.xscale('log')  # log scale for number of trials
plt.yscale('log')  # optional: log scale for error to better show small values
plt.xlabel('Number of Trials (n)')
plt.ylabel('Error')
plt.title('Monte Carlo Pi Approximation: Error vs Number of Trials')
plt.grid(True, which="both", ls="--")
#plt.show()


plt.tight_layout(w_pad=100000)
plt.show()
