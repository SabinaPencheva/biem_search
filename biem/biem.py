import pyaudio
import wave


def biem():
    f = wave.open(__file__[:-7]+'/biem.wav')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(), rate=f.getframerate(), output=True)
    data = f.readframes(1024)
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(1024)
    stream.stop_stream()
    stream.close()
    p.terminate()