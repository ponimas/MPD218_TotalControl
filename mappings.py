from MIDI import Note, CC

mappings = {
    "volume": CC(0),
    "pan": CC(1),
    "send_a": CC(2),
    "send_b": CC(3),
    "send_c": CC(4),
    "send_d": CC(5),

    "macro_1": CC(6),
    "macro_2": CC(7),
    "macro_5": CC(8),
    "macro_6": CC(9),
    "scroll_tracks": CC(10),
    "scroll_scenes": CC(11),

    "macro_3": CC(12),
    "macro_4": CC(13),
    "macro_7": CC(14),
    "macro_8": CC(15),
    "scrub_by": CC(16),
    "midi_recording_quantization": CC(17),

    "stop": Note(0),
    "play_pause": Note(1),
    "overdub": Note(2),
    "metronome": Note(3),
    "undo": Note(4),
    "redo": Note(5),
    "session_automation_rec": Note(6),
    "arm": Note(7),
    "select_instrument": Note(8),
    "toggle_lock": Note(9),
    "delete_clip": Note(10),
    "solo": Note(11),
    "prev_track": Note(12),
    "next_track": Note(13),
    "duplicate_clip": Note(14),
    "mute": Note(15),
    "fire_next_scene": Note(16)
}
