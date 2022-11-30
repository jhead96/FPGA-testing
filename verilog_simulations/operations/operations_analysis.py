import numpy as np
import matplotlib.pyplot as plt



dir_path = r"simulation_outputs\\"
ph = np.array([0, 9, 18, 27])

# RF output
RF_file_names = [dir_path+f"10MHz_RF_output_decimal_TX{p}_RX0.txt" for p in ph]
fig1, fig1_ax1 = plt.subplots()

for f, p in zip(RF_file_names, ph):
    data = np.loadtxt(f, delimiter=",",skiprows=6)
    fig1_ax1.plot(data[0, :], data[1, :], label=f"TX phase = {p}")

fig1_ax1.set_title("10MHz RF output for varying TX phase, RX phase = 0")
fig1_ax1.set_ylabel("signal")
fig1_ax1.set_xlabel("t (s)")
fig1_ax1.legend()

# LO output
fig2, (fig2_ax1, fig2_ax2) = plt.subplots(1, 2)

LO_I_filenames = [dir_path+f"10MHz_LO_I_decimal_TX0_RX{p}.txt" for p in ph]
LO_Q_filenames = [dir_path+f"10MHz_LO_Q_decimal_TX0_RX{p}.txt" for p in ph]

for i, q, p in zip(LO_I_filenames, LO_Q_filenames, ph):
    data_I = np.loadtxt(i, delimiter=",", skiprows=6)
    data_Q = np.loadtxt(q, delimiter=",", skiprows=6)

    fig2_ax1.plot(data_I[0, :], data_I[1, :], label=f"RX phase = {p}")
    fig2_ax2.plot(data_Q[0, :], data_Q[1, :], label=f"RX phase = {p}")

fig2.suptitle("10MHz LO signals with varying RX phase, TX phase = 0")

fig2_ax1.set_title("I")
fig2_ax1.set_ylabel("signal")
fig2_ax1.set_xlabel("t (s)")
fig2_ax1.legend()

fig2_ax2.set_title("Q")
fig2_ax2.set_ylabel("signal")
fig2_ax2.set_xlabel("t (s)")
fig2_ax2.legend()




