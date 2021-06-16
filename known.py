"""Catalog of known ROM chips.
"""

knownRom = {                # knownRom[lang][version][alg][chip] = value
    'fr': {
        '1.04': { # from diag cart ST 4.4 in real hw: crc x2-x0 are swapped!
            'checksum': { 'hi2': 0x0DC8, 'hi1': 0x34A4, 'hi0': 0xE03F,
                          'lo2': 0x8A0C, 'lo1': 0x4AF6, 'lo0': 0x5746 },
            'crc':      { 'hi2': 0x3D94, 'hi1': 0xDB06, 'hi0': 0xE4E9,
                          'lo2': 0x88A2, 'lo1': 0xBC68, 'lo0': 0xEF4C } },
        '1.02': { # from diag cart ST 4.4 in real hw: crc x2-x0 are swapped!
            'checksum': { 'hi2': 0x3158, 'hi1': 0x54C1, 'hi0': 0xF9E0,
                          'lo2': 0x82C4, 'lo1': 0x1BD3, 'lo0': 0x0C15 },
            'crc':      { 'hi2': 0xEB30, 'hi1': 0x201D, 'hi0': 0xB34E,
                          'lo2': 0xB217, 'lo1': 0x35DF, 'lo0': 0xDBAD } },
        '1.00': { # dump of Atari mask ROMs
            'checksum': { 'hi2': 0xEB83, 'hi1': 0xDF2B, 'hi0': 0xF0B9,
                          'lo2': 0x6C4C, 'lo1': 0x9AF3, 'lo0': 0x00D4 },
            'crc':      { 'hi2': 0x293D, 'hi1': 0x31EE, 'hi0': 0xB603,
                          'lo2': 0x9372, 'lo1': 0x8C69, 'lo0': 0xFD8E } },
    } }
