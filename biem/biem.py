import pyaudio
import wave
from ctypes import c_char_p, c_int, CFUNCTYPE, cdll

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass


def biem():
    c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
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
    asound.snd_lib_error_set_handler(None)