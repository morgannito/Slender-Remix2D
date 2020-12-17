import os
import sys
from tkinter import *
import gobject
import gst

def on_sync_message(bus, message, window_id):
    if not message.structure is None:
        if message.structure.get_name() == 'prepare-xwindow-id':
            image_sink = message.src
            image_sink.set_property('force-aspect-ratio', True)
            image_sink.set_xwindow_id(window_id)


def lose(fenetre):
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    gobject.threads_init()
    video = tkinter.Frame(fenetre, bg='#000000')
    video.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
    window_id = video.winfo_id()
    player = gst.element_factory_make('playbin2', 'player')
    player.set_property('video-sink', None)
    player.set_property('uri', 'ressources/video/lose.mp4')
    player.set_state(gst.STATE_PLAYING)
    bus = player.get_bus()
    bus.add_signal_watch()
    bus.enable_sync_message_emission()
    bus.connect('sync-message::element', on_sync_message, window_id)

    fenetre.mainloop()