import os
import json
import glob
import sys
import subprocess
from django.http import HttpResponse
import settings

last = None

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
    args = ["timidity", path]
    #args = ["aplaymidi", "-p", "20:0", path]
    #subprocess.call(["aplaymidi", "-p", "20:0", path])
    if last is not None:
        last.kill()
    last = subprocess.Popen(args)
    return HttpResponse("You're welcome", content_type="application/json")

def stop(req):
    if last is not None:
        last.kill()
    return HttpResponse("Stopped")
