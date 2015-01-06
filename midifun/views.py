import os
import json
import glob
import sys
import subprocess
from django.http import HttpResponse
import settings
import pypm
from threading import Timer

#APLAYMIDI_P_OPT = "20:0"
APLAYMIDI_P_OPT = "128:0"
PYPM_DEVICE_NUM=2

last = None

pypm.Initialize()
for i in range(pypm.CountDevices()):
    print pypm.GetDeviceInfo(i)
midiout = pypm.Output(PYPM_DEVICE_NUM,0.0)

def list_songs(req):
    print settings.MIDI_DIR
    names = [ os.path.basename(x) for x in glob.glob(os.path.join(settings.MIDI_DIR, "*.mid")) ]
    return HttpResponse(json.dumps(names), content_type="application/json")

def play(req, something):
    global last
    names = [ os.path.basename(x) for x in glob.glob(os.path.join(settings.MIDI_DIR, "*.mid")) ]
    if something not in names:
        return HttpResponse("Nope", content_type="application/json")

    path = os.path.join(settings.MIDI_DIR, something)
    #args = ["timidity", path]
    args = ["aplaymidi", "-p", APLAYMIDI_P_OPT, path]
    if last is not None:
        last.kill()
    last = subprocess.Popen(args)
    return HttpResponse("You're welcome", content_type="application/json")

def tone(req, note_s, duration_s):
    note,duration = int(note_s),float(duration_s)

    def on():
        midiout.WriteShort(0x90,note,50)
    def off():
        midiout.WriteShort(0x90,note,0)

    on()
    Timer(duration, off).start()
    return HttpResponse("Gee, thanks for your request Buddy")

def event0(req, s_status):
    status = int(s_status,16)
    midiout.WriteShort(status)

    return HttpResponse("Gee, thanks for your request Buddy")

def event1(req, s_status, s_data1):
    status,data1 = int(s_status,16), int(s_data1)
    midiout.WriteShort(status,data1)

    return HttpResponse("Gee, thanks for your request Buddy")

def event2(req, s_status, s_data1, s_data2):
    status,data1,data2 = int(s_status,16), int(s_data1), int(s_data2)
    midiout.WriteShort(status,data1,data2)

    return HttpResponse("Gee, thanks for your request Buddy")

def stop(req):
    if last is not None:
        last.kill()
    return HttpResponse("Stopped")
