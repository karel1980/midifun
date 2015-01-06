# What's this?

A web service for sending midi events.
You can play songs from file, play one tone at a time or send raw midi events.

Note: this is not a good idea(TM). I merely wanted to toy around.

# Configuration

To configure the midi outputs: See midifun/views.py

hint: devices are listed on stdout when this thing starts, or you can
see them using `aplaymidi -l` if your system has that command

# Usage

python manage.py runserver

# API

## List available songs

    http://localhost:8000/

## Play a song

    http://localhost:8000/play/happy_birthday.mid

## Play a tone:

    http://localhost:8000/tone/{note}/{duration}

E.g. play tone '40' for half a second:

    http://localhost:8000/tone/40/0.5

## Send a raw midi event

    http://localhost:8000/event/{status}
    http://localhost:8000/event/{status}/{data1}
    http://localhost:8000/event/{status}/{data1}/{data2}

E.g. press key '40'

    http://localhost:8000/event/0x90/40/50

Don't forget to 'unpress' it:

    http://localhost:8000/event/0x80/40
