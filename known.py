"""Catalog of known ROM chips.
"""

knownRom = {    # knownRom[version][alg][chip] = value
    '1.00fr': { # dump of Atari mask ROMs
        'checksum': { 'hi2': 0xEB83, 'hi1': 0xDF2B, 'hi0': 0xF0B9,
                      'lo2': 0x6C4C, 'lo1': 0x9AF3, 'lo0': 0x00D4 },
        'crc':      { 'hi2': 0x293D, 'hi1': 0x31EE, 'hi0': 0xB603,
                      'lo2': 0x9372, 'lo1': 0x8C69, 'lo0': 0xFD8E } },
    '1.02fr': { # from diag cart ST 4.4 in real hw: crc x2-x0 are swapped!
        'checksum': { 'hi2': 0x3158, 'hi1': 0x54C1, 'hi0': 0xF9E0,
                      'lo2': 0x82C4, 'lo1': 0x1BD3, 'lo0': 0x0C15 },
        'crc':      { 'hi2': 0xEB30, 'hi1': 0x201D, 'hi0': 0xB34E,
                      'lo2': 0xB217, 'lo1': 0x35DF, 'lo0': 0xDBAD } },
    '1.04fr': { # from diag cart ST 4.4 in real hw: crc x2-x0 are swapped!
        'checksum': { 'hi2': 0x0DC8, 'hi1': 0x34A4, 'hi0': 0xE03F,
                      'lo2': 0x8A0C, 'lo1': 0x4AF6, 'lo0': 0x5746 },
        'crc':      { 'hi2': 0x3D94, 'hi1': 0xDB06, 'hi0': 0xE4E9,
                      'lo2': 0x88A2, 'lo1': 0xBC68, 'lo0': 0xEF4C } },
    '1.62fr': {
        'checksum': { 'hi': 0xC0C4,
                      'lo': 0xD536 },
        'crc':      { 'hi': 0xD9A0,
                      'lo': 0x360B } },
    '2.06fr': {
        'checksum': { 'hi': 0x4755,
                      'lo': 0x03AE },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '3.06fr': {
            'checksum': { 'ee': 0x327E,
                          'oe': 0x0190,
                          'eo': 0x54A4,
                          'oo': 0x2552 },
            'crc':      { 'ee': 0x0000,
                          'oe': 0x0000,
                          'eo': 0x0000,
                          'oo': 0x0000 } },
    '3.06uk': {
            'checksum': { 'ee': 0xC0A1,
                          'oe': 0xB810,
                          'eo': 0xA89A,
                          'oo': 0x72BB },
            'crc':      { 'ee': 0x0000,
                          'oe': 0x0000,
                          'eo': 0x0000,
                          'oo': 0x0000 } },
    'EmuTOS 1.01fr ST': {
        'checksum': { 'hi2': 0xEA7B, 'hi1': 0x43D2, 'hi0': 0x016F,
                      'lo2': 0xEB71, 'lo1': 0x9126, 'lo0': 0x5587 },
        'crc':      { 'hi2': 0xEFCF, 'hi1': 0x2D5E, 'hi0': 0x9D98,
                      'lo2': 0x2F88, 'lo1': 0x274C, 'lo0': 0xB0C6 } },
    'EmuTOS 1.01fr STe': {
            'checksum': { 'hi': 0xC84F,
                          'lo': 0xB4D8 },
            'crc':      { 'hi': 0xC4DA,
                          'lo': 0x84D0 } },
    }
