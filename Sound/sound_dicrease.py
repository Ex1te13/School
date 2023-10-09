import wave
import struct


def increase(frame, count):
    frame //= count
    if frame >= 32767:
        return 32767
    elif frame <= -32768:
        return -32768
    return frame


num = 25
source = wave.open("in.wav", mode="rb")
dest = wave.open("dicreased.wav", mode="wb")
dest.setparams(source.getparams())
frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
newdata = list(map(lambda frame: increase(frame, num), data))
newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
dest.writeframes(newframes)
source.close()
dest.close()
