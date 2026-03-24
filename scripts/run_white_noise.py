"""
play each burst individually so DIO can be toggled per burst.
The Player is initialized once (stream opened, buffers allocated) and
reused for every burst; only the seek-to-zero + Play call happens in the
loop, keeping re-trigger latency relatively low
"""
import time

import audiomath as am
from radiens_core import AllegoClient
from radiens_core.models import StreamMode, StreamStateRequest

# from radiens_core.models import RecordMode, RecordStateRequest

# Stimulus parameters
NUM_BURSTS = 10
DURATION_MS = 200
RAMP_SEC = 0.005       # 5 ms cosine on/off ramps
ISI_SEC = 0.5          # inter-stimulus interval (silence between bursts)
SAMPLE_RATE = 100_000  # Hz; 100 kHz → Nyquist = 50 kHz = upper bound of stimulus band
# dB SPL is a physical scale: 0 dB SPL = 20 µPa (threshold of human hearing).
# dBFS is a digital scale: 0 dBFS = peak amplitude of 1.0 (digital full scale / clipping point).
# To convert between them we need DB_REF: the dB SPL that corresponds to 0 dBFS on this rig.
#
# DB_REF = 94 follows the professional audio convention that a signal at 0 dBFS produces
# 94 dB SPL (= 1 Pa; 20·log10(1 Pa / 20 µPa) ≈ 94 dB). This is just an assumption —
# the true value depends on the audio interface output level, amplifier gain, speaker
# sensitivity, and distance to the subject's ear.
#
# To calibrate properly: play a tone at a known dBFS level, measure the output with a
# sound level meter at the subject's ear, and solve for DB_REF = measured_dB_SPL - dBFS_level.
DB_SPL = 75
DB_REF = 94            # ← verify against your hardware with a sound level meter

TARGET_AMP = 10 ** ((DB_SPL - DB_REF) / 20)  # ~0.112 linear amplitude

# Generate a single broadband white noise burst.
# Signal.Noise draws independent uniform samples, producing a flat spectrum
# from 0 Hz to Nyquist (50 kHz) by construction — no filtering needed.
burst = am.Sound().GenerateWaveform(
    waveform=am.Signal.Noise,
    duration_msec=DURATION_MS,
    samplingfreq_hz=SAMPLE_RATE,
)
burst.AutoScale(TARGET_AMP)
burst.Fade(risetime=RAMP_SEC, falltime=RAMP_SEC, hann=True)

# Open the stream once; reuse for every burst
player = am.Player(burst)

client = AllegoClient()

# ensure stream is on before the loop
client.set_stream_state(StreamStateRequest(mode=StreamMode.ON))

# (optional) set recording state to ON
# client.set_record_state(RecordStateRequest(mode=RecordMode.ON))

# ensure DIO is in manual mode and starts low before the loop
client.set_dio_manual(0, False)

for _ in range(NUM_BURSTS):
    client.set_dio_manual(0, True)
    player.Play(position=0, wait=True)  # seek to start, then block until done
    client.set_dio_manual(0, False)
    time.sleep(ISI_SEC)
