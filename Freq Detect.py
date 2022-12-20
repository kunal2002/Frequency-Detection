import wave
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
# Open the wave file
with wave.open('1000Hz.wav', 'r') as f:
    # Read the wave file properties
    num_channels = f.getnchannels()
    sample_width = f.getsampwidth()
    frame_rate = f.getframerate()
    num_frames = f.getnframes()

    # Read the wave file data
    data = f.readframes(num_frames)

# Close the wave file
f.close()

# Convert the wave data to a numpy array
wave_data = np.frombuffer(data, dtype=np.int16)

# Compute the FFT of the wave data
frequencies = fft(wave_data)

# Get the absolute value of the complex FFT data
magnitudes = np.abs(frequencies)

# Get the frequencies corresponding to the FFT data
frequencies = np.fft.fftfreq(wave_data.size, 1/frame_rate)
frequencies *= sample_width
times = np.arange(len(wave_data)) / frame_rate

maxfreq = np.max(magnitudes)
peak_indices = np.argwhere(magnitudes == maxfreq)
peak_frequencies = frequencies[peak_indices]
print(peak_frequencies[0])
plt.plot(frequencies, magnitudes)
# Times vs Wave_data = Time Domain
# plt.plot(times, wave_data)
# plt.xlabel('Time')
# plt.ylabel('Magnitude')
# For freq vs Magnitude = Frequency Domain
# plt.xlim(0, 10000)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()