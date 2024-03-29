from utility.oscilloscopes.scope_readers import GwInstekReader
import numpy as np
import matplotlib.pyplot as plt

# FPGA version v0.5.2
# Data generated using 'single_pulse_testing' function within 'pulse_testing.py'
pulses = np.array([10, 20, 30, 40, 50, 100, 150, 200, 250, 500, 750, 1000])
filenames = [f"pulse_test_data/double_pulse_test_data_v052/{i}us_single_pulse.CSV" for i in pulses]

for f in filenames:
    dataset = GwInstekReader(f)
    #dataset.plot_data()

# Data generated using 'double_pulse_testing' function within 'pulse_testing.py'
filenames = np.array([f"pulse_test_data/double_pulse_test_data_v052/20_10_20_double_pulse.CSV",
                      f"pulse_test_data/double_pulse_test_data_v052/200_100_200_double_pulse.CSV",
                      f"pulse_test_data/double_pulse_test_data_v052/2000_1000_2000_double_pulse.CSV"])

for f in filenames:
    dataset = GwInstekReader(f)
    dataset.plot_data()

# Data generated using 'repeat_testing' function within 'pulse_testing.py'
filepath = r"pulse_test_data/double_pulse_test_data_v052/20_10_20_repeat_testing.csv"
data = np.genfromtxt(filepath, delimiter=",")

# Get parameters
N = data[0, 1].astype(int)
Ts = data[2, 1].astype(int)
num_frames = data[6, 1].astype(int)
y = data[:, 4]

# Generate t
t = np.arange(0, N*Ts, Ts)
plt.figure()
lbls = np.array(["Record 1, t = 0s", "Record 2, t = 15s", "Record 3, t = 30s"])
# Split y
for y_data, l in zip(np.split(y, num_frames), lbls):
    plt.plot(t/1000, y_data, label=l)

plt.title("3 repeats of 20us-10us-20us pulse sequence")
plt.xlabel("t (us)")
plt.ylabel("V (V)")
plt.legend(title="Trigger times relative to record 1")
