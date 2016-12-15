SYMBOL_SIZE = 50


def get_symbol_by_index(idx):
    symbol = None
    if idx is 0:
        # DOT
        symbol = SymbolsDot()
    elif idx is 1:
        # ACCIDENTAL_SHARP
        symbol = SymbolsAccidental('ACCIDENTAL_SHARP', 'sharp')
    elif idx is 2:
        # NOTE_QUARTER_UP
        symbol = SymbolsNote('NOTE_QUARTER_UP', 1, 4, 'up', 37, False)
    elif idx is 3:
        # NOTE_HALF_UP
        symbol = SymbolsNote('NOTE_HALF_UP', 1, 2, 'up', 37, False)
    elif idx is 4:
        # TIME_SIGNATURE_3_4
        symbol = SymbolsTimeSignature('TIME_SIGNATURE_3_4', '3_4')
    elif idx is 5:
        # BAR
        symbol = SymbolsBar('BAR', 'normal')
    elif idx is 6:
        # NOTE_QUARTER_DOWN
        symbol = SymbolsNote('NOTE_QUARTER_DOWN', 1, 4, 'down', 0, False)
    elif idx is 7:
        # BEAM_2_EIGHTH_NOTES_UP
        symbol = SymbolsNote('BEAM_2_EIGHTH_NOTES_UP', 2, 8, 'up', 36, False)
    elif idx is 8:
        # BEAM_2_EIGHTH_NOTES_DOWN
        symbol = SymbolsNote('BEAM_2_EIGHTH_NOTES_DOWN', 2, 8, 'down', 0, False)
    elif idx is 9:
        # FINAL_BAR
        symbol = SymbolsBar('FINAL_BAR', 'final')
    elif idx is 10:
        # REST_QUARTER
        symbol = SymbolsRest('REST_QUARTER', 4)
    elif idx is 11:
        # NOTE_HALF_DOWN
        symbol = SymbolsNote('NOTE_HALF_DOWN', 1, 2, 'down', 0, False)
    elif idx is 12:
        # NOTE_EIGHTH_DOWN
        symbol = SymbolsNote('NOTE_EIGHTH_DOWN', 1, 8, 'down', 0, False)
    elif idx is 13:
        # KEY_SIGNATURE_DOUBLE_#
        symbol = SymbolsKeySignature('KEY_SIGNATURE_DOUBLE_#', 'double_#')
    elif idx is 14:
        # CLEF_TREBLE
        symbol = SymbolsClef('CLEF_TREBLE', 'treble')
    elif idx is 15:
        # NOTE_EIGHTH_UP
        symbol = SymbolsNote('NOTE_EIGHTH_UP', 1, 8, 'up', 37, False)
    elif idx is 16:
        # NOTE_HALF_UP_WITH_DOT
        symbol = SymbolsNote('NOTE_HALF_UP_WITH_DOT', 1, 2, 'up', 37, True)
    elif idx is 17:
        # TIE
        symbol = SymbolsTie()
    elif idx is 18:
        # TIME_SIGNATURE_4_4
        symbol = SymbolsTimeSignature('TIME_SIGNATURE_4_4', '4_4')
    elif idx is 19:
        # NOTE_QUARTER_UP_WITH_DOT
        symbol = SymbolsNote('NOTE_QUARTER_UP_WITH_DOT', 1, 4, 'up', 37, True)
    elif idx is 20:
        # NOTE_WHOLE
        symbol = SymbolsNote('NOTE_WHOLE', 1, 1, 'up', 0, False)
    return symbol


class Symbols:
    @staticmethod
    def get(index):
        return get_symbol_by_index(index)

    def __init__(self, class_name):
        self.class_name = class_name
        self.name = 'DEFAULT_NAME'

    def get_name(self):
        return self.name


class SymbolsDot(Symbols):
    def __init__(self):
        super().__init__('dot')
        self.name = 'DOT'


class SymbolsAccidental(Symbols):
    def __init__(self, name, s_type):
        super().__init__('accidental')
        self.name = name
        self.type = s_type  # sharp, flat, double_sharp, double_flat


class SymbolsNote(Symbols):
    def __init__(self, name, number_of_notes, duration, direction, offset, with_dot):
        super().__init__('note')
        self.name = name
        self.number_of_notes = number_of_notes
        self.duration = duration
        self.direction = direction
        self.offset = offset
        self.pitch_step = None
        self.pitch_octave = None
        self.with_dot = with_dot

    def set_pitch(self, step, octave):
        self.pitch_step = step
        self.pitch_octave = octave


class SymbolsTimeSignature(Symbols):
    def __init__(self, name, time_signature_type):
        super().__init__('time_signature')
        self.name = name
        self.type = time_signature_type


class SymbolsBar(Symbols):
    def __init__(self, name, bar_type):
        super().__init__('bar')
        self.name = name
        self.type = bar_type


class SymbolsRest(Symbols):
    def __init__(self, name, duration):
        super().__init__('rest')
        self.name = name
        self.duration = duration


class SymbolsKeySignature(Symbols):
    def __init__(self, name, key_signature_type):
        super().__init__('key_signature')
        self.name = name
        self.type = key_signature_type


class SymbolsClef(Symbols):
    def __init__(self, name, clef_type):
        super().__init__('clef')
        self.name = name
        self.type = clef_type


class SymbolsTie(Symbols):
    def __init__(self):
        super().__init__('tie')
        self.name = 'TIE'
