"""Catalog of known ROM chips.
"""

knownRom = {    # knownRom[version][alg][chip] = value
    '1.0fr': { # dump of Atari mask ROMs
        'checksum': { 'hi2': 0xEB83, 'hi1': 0xDF2B, 'hi0': 0xF0B9,
                      'lo2': 0x6C4C, 'lo1': 0x9AF3, 'lo0': 0x00D4 },
        'crc':      { 'hi2': 0x293D, 'hi1': 0x31EE, 'hi0': 0xB603,
                      'lo2': 0x9372, 'lo1': 0x8C69, 'lo0': 0xFD8E } },
    '1.02fr': { # from diag cart ST 4.4 in real hw: crc x2-x0 were swapped!
        'checksum': { 'hi2': 0x3158, 'hi1': 0x54C1, 'hi0': 0xF9E0,
                      'lo2': 0x82C4, 'lo1': 0x1BD3, 'lo0': 0x0C15 },
        'crc':      { 'hi2': 0xB34E, 'hi1': 0x201D, 'hi0': 0xEB30,
                      'lo2': 0xDBAD, 'lo1': 0x35DF, 'lo0': 0xB217 } },
    '1.04fr': { # from diag cart ST 4.4 in real hw: crc x2-x0 were swapped!
        'checksum': { 'hi2': 0x0DC8, 'hi1': 0x34A4, 'hi0': 0xE03F,
                      'lo2': 0x8A0C, 'lo1': 0x4AF6, 'lo0': 0x5746 },
        'crc':      { 'hi2': 0xE4E9, 'hi1': 0xDB06, 'hi0': 0x3D94,
                      'lo2': 0xEF4C, 'lo1': 0xBC68, 'lo0': 0x88A2 } },
    '1.06fr': {
        'checksum': { 'hi': 0x0B23,
                      'lo': 0x6FF8 },
        'crc':      { 'hi': 0x05E2,
                      'lo': 0xAB90 } },
    '1.62fr': {
        'checksum': { 'hi': 0xC0C4,
                      'lo': 0xD536 },
        'crc':      { 'hi': 0xD9A0,
                      'lo': 0x360B } },
    '2.05fr': {
        'checksum': { 'hi': 0xA041,
                      'lo': 0xFA3B },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
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

    '1.0uk': {
        'checksum': { 'hi2': 0xFBF1, 'hi1': 0x6E55, 'hi0': 0xFB97,
                      'lo2': 0x95D8, 'lo1': 0xA85B, 'lo0': 0x29DE },
        'crc':      { 'hi2': 0x2BB5, 'hi1': 0xC759, 'hi0': 0xC5AE,
                      'lo2': 0x956B, 'lo1': 0xDCA1, 'lo0': 0xE78D } },
    '1.02uk': {
        'checksum': { 'hi2': 0x268A, 'hi1': 0x61D1, 'hi0': 0xFDFB,
                      'lo2': 0x6671, 'lo1': 0x1C29, 'lo0': 0x0C8E },
        'crc':      { 'hi2': 0xA8D5, 'hi1': 0x4A87, 'hi0': 0xF1EF,
                      'lo2': 0x0B82, 'lo1': 0x16B5, 'lo0': 0xE560 } },
    '1.04uk': {
        'checksum': { 'hi2': 0x2097, 'hi1': 0x2AAA, 'hi0': 0xF6F2,
                      'lo2': 0x9FC5, 'lo1': 0x305D, 'lo0': 0x648B },
        'crc':      { 'hi2': 0xA147, 'hi1': 0xFC91, 'hi0': 0xC8D0,
                      'lo2': 0xBBF2, 'lo1': 0x962A, 'lo0': 0xCA69 } },
    '1.06uk': {
        'checksum': { 'hi': 0x27FB,
                      'lo': 0x2DBA },
        'crc':      { 'hi': 0x6444,
                      'lo': 0xD0C5 } },
    '1.62uk': {
        'checksum': { 'hi': 0xE24D,
                      'lo': 0xE42B },
        'crc':      { 'hi': 0xCE48,
                      'lo': 0x9DDB } },
    '2.05uk': {
        'checksum': { 'hi': 0x8D31,
                      'lo': 0x0B76 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '2.06uk': {
        'checksum': { 'hi': 0x294C,
                      'lo': 0xA629 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '3.06uk': {
            'checksum': { 'ee': 0xC0A1,
                          'oe': 0xB810,
                          'eo': 0xA89A,
                          'oo': 0x72BB },
            'crc':      { 'ee': 0x0000,
                          'oe': 0x0000,
                          'eo': 0x0000,
                          'oo': 0x0000 } },

    '1.0us': {
        'checksum': { 'hi2': 0xFBF1, 'hi1': 0x6E55, 'hi0': 0xF9CC,
                      'lo2': 0x95D8, 'lo1': 0xA85B, 'lo0': 0x29E4 },
        'crc':      { 'hi2': 0x2BB5, 'hi1': 0x9A86, 'hi0': 0x95DE,
                      'lo2': 0x956B, 'lo1': 0x661E, 'lo0': 0x1C78 } },
    '1.02us': {
        'checksum': { 'hi2': 0x268A, 'hi1': 0x61D1, 'hi0': 0xFC30,
                      'lo2': 0x6671, 'lo1': 0x1C29, 'lo0': 0x0C94 },
        'crc':      { 'hi2': 0xA8D5, 'hi1': 0xBF1D, 'hi0': 0xBC39,
                      'lo2': 0x0B82, 'lo1': 0x0AA3, 'lo0': 0xD55D } },
    '1.04us': {
        'checksum': { 'hi2': 0x1ECC, 'hi1': 0x2ACA, 'hi0': 0xF6F2,
                      'lo2': 0x9FD2, 'lo1': 0x307D, 'lo0': 0x6484 },
        'crc':      { 'hi2': 0xA922, 'hi1': 0xC355, 'hi0': 0xC8D0,
                      'lo2': 0x99B0, 'lo1': 0x6B2C, 'lo0': 0x3BFF } },
    '1.06us': {
        'checksum': { 'hi': 0x2630,
                      'lo': 0x2DB0 },
        'crc':      { 'hi': 0x0F28,
                      'lo': 0x9463 } },
    '1.62us': {
        'checksum': { 'hi': 0xE082,
                      'lo': 0xE421 },
        'crc':      { 'hi': 0x4ACD,
                      'lo': 0xC295 } },
    '2.05us': {
        'checksum': { 'hi': 0x8BC7,
                      'lo': 0x0B26 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '2.06us': {
        'checksum': { 'hi': 0x27C2,
                      'lo': 0xA695 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '3.0us': {
        'checksum': { 'ee': 0x8A89,
                      'oe': 0x47FE,
                      'eo': 0xFE86,
                      'oo': 0x5C9E },
        'crc':      { 'ee': 0x1D0F,
                      'oe': 0x0000,
                      'eo': 0x1D0F,
                      'oo': 0x0000 } },
    '3.05us': {
        'checksum': { 'ee': 0x9235,
                      'oe': 0xA686,
                      'eo': 0xB299,
                      'oo': 0x1A7A },
        'crc':      { 'ee': 0x0000,
                      'oe': 0x0000,
                      'eo': 0x0000,
                      'oo': 0x0000 } },
    '3.06us': {
        'checksum': { 'ee': 0xBD53,
                      'oe': 0xB6B8,
                      'eo': 0xA97F,
                      'oo': 0x73DD },
        'crc':      { 'ee': 0x0000,
                      'oe': 0x0000,
                      'eo': 0x0000,
                      'oo': 0x0000 } },

    '1.0de': {
        'checksum': { 'hi2': 0x5B93, 'hi1': 0x0B34, 'hi0': 0xF5C4,
                      'lo2': 0xD07A, 'lo1': 0xA2CF, 'lo0': 0x071A },
        'crc':      { 'hi2': 0x108A, 'hi1': 0xE23B, 'hi0': 0x2084,
                      'lo2': 0xCCD8, 'lo1': 0x1332, 'lo0': 0x4BFB } },
    '1.02de': {
        'checksum': { 'hi2': 0x7EF5, 'hi1': 0x4448, 'hi0': 0xFA34,
                      'lo2': 0xBEC6, 'lo1': 0x1027, 'lo0': 0x0D1E },
        'crc':      { 'hi2': 0x756F, 'hi1': 0x6F57, 'hi0': 0xFC39,
                      'lo2': 0x9F49, 'lo1': 0xC2F8, 'lo0': 0xBF64 } },
    '1.04de': {
        'checksum': { 'hi2': 0xEA64, 'hi1': 0x34E9, 'hi0': 0xE375,
                      'lo2': 0x4F1D, 'lo1': 0x4799, 'lo0': 0x3D4F },
        'crc':      { 'hi2': 0xC9A2, 'hi1': 0x390E, 'hi0': 0x2CC5,
                      'lo2': 0xE68A, 'lo1': 0xA48F, 'lo0': 0xD3E6 } },
    '1.06de': {
        'checksum': { 'hi': 0xE9E5,
                      'lo': 0xFB24 },
        'crc':      { 'hi': 0x0B63,
                      'lo': 0xA65B } },
    '1.62de': {
        'checksum': { 'hi': 0x9F32,
                      'lo': 0xB49E },
        'crc':      { 'hi': 0xA174,
                      'lo': 0xC0E4 } },
    '2.05de': {
        'checksum': { 'hi': 0x9A68,
                      'lo': 0x5CB0 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '2.06de': {
        'checksum': { 'hi': 0x2B8F,
                      'lo': 0xDE5F },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '3.01de': {
        'checksum': { 'ee': 0x46AC,
                      'oe': 0xCBB7,
                      'eo': 0xC9E7,
                      'oo': 0xB1DB },
        'crc':      { 'ee': 0x71E8,
                      'oe': 0x2539,
                      'eo': 0x63B2,
                      'oo': 0x8366 } },
    '3.06de': {
        'checksum': { 'ee': 0x02E6,
                      'oe': 0x4F50,
                      'eo': 0x694E,
                      'oo': 0x4AD1 },
        'crc':      { 'ee': 0x0000,
                      'oe': 0x0000,
                      'eo': 0x0000,
                      'oo': 0x0000 } },

    '1.02es': {
        'checksum': { 'hi2': 0x0A4B, 'hi1': 0x2C14, 'hi0': 0x2599,
                      'lo2': 0x6DF9, 'lo1': 0xC584, 'lo0': 0x56F4 },
        'crc':      { 'hi2': 0x94CE, 'hi1': 0x078D, 'hi0': 0xB228,
                      'lo2': 0xA5FA, 'lo1': 0xCD73, 'lo0': 0xDF4C } },
    '1.04es': {
        'checksum': { 'hi2': 0xDFDB, 'hi1': 0x368E, 'hi0': 0xDE57,
                      'lo2': 0x65D6, 'lo1': 0x5103, 'lo0': 0x3D63 },
        'crc':      { 'hi2': 0x5659, 'hi1': 0xE69B, 'hi0': 0x9FC6,
                      'lo2': 0x3C57, 'lo1': 0x97F9, 'lo0': 0x2E2A } },
    '1.06es': {
        'checksum': { 'hi': 0x2A76,
                      'lo': 0x7697 },
        'crc':      { 'hi': 0xB970,
                      'lo': 0x68E0 } },
    '2.05es': {
        'checksum': { 'hi': 0xBE1E,
                      'lo': 0xA964 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '2.06es': {
        'checksum': { 'hi': 0x6217,
                      'lo': 0x4E88 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '3.06es': {
        'checksum': { 'ee': 0x7713,
                      'oe': 0xCE12,
                      'eo': 0x2765,
                      'oo': 0xA195 },
        'crc':      { 'ee': 0x0000,
                      'oe': 0x0000,
                      'eo': 0x0000,
                      'oo': 0x0000 } },

    '1.02sv': {
        'checksum': { 'hi2': 0xBA8E, 'hi1': 0x2ED9, 'hi0': 0x17AE,
                      'lo2': 0x1988, 'lo1': 0xF5A9, 'lo0': 0x3B66 },
        'crc':      { 'hi2': 0x0C01, 'hi1': 0xA9C0, 'hi0': 0x4766,
                      'lo2': 0x0C54, 'lo1': 0x7B57, 'lo0': 0xF7B6 } },
    '1.04sv': {
        'checksum': { 'hi2': 0x9E9F, 'hi1': 0x3484, 'hi0': 0xE042,
                      'lo2': 0x298A, 'lo1': 0x4AD6, 'lo0': 0x579D },
        'crc':      { 'hi2': 0x2B3A, 'hi1': 0x7572, 'hi0': 0x0776,
                      'lo2': 0x6FAB, 'lo1': 0xCEC9, 'lo0': 0x70BC } },
    '1.62sv': {
        'checksum': { 'hi': 0x509D,
                      'lo': 0x739A },
        'crc':      { 'hi': 0x2312,
                      'lo': 0xA285 } },
    '2.05sv': {
        'checksum': { 'hi': 0xEB36,
                      'lo': 0x6EB9 },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '2.06sv': {
        'checksum': { 'hi': 0x8DAE,
                      'lo': 0x7CDB },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '3.06sv': {
        'checksum': { 'ee': 0x114C,
                      'oe': 0x8A5A,
                      'eo': 0xBCEE,
                      'oo': 0xD6DD },
        'crc':      { 'ee': 0x0000,
                      'oe': 0x0000,
                      'eo': 0x0000,
                      'oo': 0x0000 } },

    '1.02sg': {
        'checksum': { 'hi2': 0x8A51, 'hi1': 0x25C6, 'hi0': 0x141E,
                      'lo2': 0xD1CC, 'lo1': 0xD59E, 'lo0': 0x442D },
        'crc':      { 'hi2': 0x526C, 'hi1': 0xF3E4, 'hi0': 0x7FA1,
                      'lo2': 0x1A52, 'lo1': 0x79FA, 'lo0': 0x03B4 } },
    '1.06sg': {
        'checksum': { 'hi': 0xD76F,
                      'lo': 0x1479 },
        'crc':      { 'hi': 0xE873,
                      'lo': 0xC2DC } },
    '2.05sg': {
        'checksum': { 'hi': 0x817E,
                      'lo': 0x5D6A },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },
    '2.06sg': {
        'checksum': { 'hi': 0x188C,
                      'lo': 0x163F },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },

    '1.04nl': {
        'checksum': { 'hi2': 0x7B99, 'hi1': 0x2A05, 'hi0': 0xF797,
                      'lo2': 0x20BD, 'lo1': 0x2D6B, 'lo0': 0x62F8 },
        'crc':      { 'hi2': 0x0511, 'hi1': 0x09A1, 'hi0': 0x9AEF,
                      'lo2': 0xA064, 'lo1': 0x3499, 'lo0': 0x427A } },

    '1.06it': {
        'checksum': { 'hi': 0x6878,
                      'lo': 0xD984 },
        'crc':      { 'hi': 0x337F,
                      'lo': 0x71EF } },
    '2.05it': {
        'checksum': { 'hi': 0x5089,
                      'lo': 0xB92B },
        'crc':      { 'hi': 0x0000,
                      'lo': 0x0000 } },

    'EmuTOS 1.01fr ST': {
        'checksum': { 'hi2': 0xEA7B, 'hi1': 0x43D2, 'hi0': 0x016F,
                      'lo2': 0xEB71, 'lo1': 0x9126, 'lo0': 0x5587 },
        'crc':      { 'hi2': 0xEFCF, 'hi1': 0x2D5E, 'hi0': 0x9D98,
                      'lo2': 0x2F88, 'lo1': 0x274C, 'lo0': 0xB0C6 } },
    'EmuTOS 1.01cz ST': {
        'checksum': { 'hi2': 0xACF7, 'hi1': 0x4B2E, 'hi0': 0x9C47,
                      'lo2': 0x72C0, 'lo1': 0x91F3, 'lo0': 0x1DC9 },
        'crc':      { 'hi2': 0xDD09, 'hi1': 0x87D2, 'hi0': 0xD283,
                      'lo2': 0xCC8E, 'lo1': 0x9806, 'lo0': 0xF9A2 } },
    'EmuTOS 1.01de ST': {
        'checksum': { 'hi2': 0xA94C, 'hi1': 0x4961, 'hi0': 0xF7C7,
                      'lo2': 0x98B3, 'lo1': 0x8300, 'lo0': 0x4CBB },
        'crc':      { 'hi2': 0x866F, 'hi1': 0xAE34, 'hi0': 0xA89D,
                      'lo2': 0x349F, 'lo1': 0xD00B, 'lo0': 0xDE7A } },
    'EmuTOS 1.01es ST': {
        'checksum': { 'hi2': 0xC11E, 'hi1': 0x4585, 'hi0': 0xFB34,
                      'lo2': 0xE34A, 'lo1': 0x8D48, 'lo0': 0x4693 },
        'crc':      { 'hi2': 0xB8FC, 'hi1': 0x47A9, 'hi0': 0x1178,
                      'lo2': 0x5299, 'lo1': 0x0186, 'lo0': 0xBF34 } },
    'EmuTOS 1.01fi ST': {
        'checksum': { 'hi2': 0x4ADF, 'hi1': 0x48C5, 'hi0': 0xFA77,
                      'lo2': 0x701A, 'lo1': 0x71E1, 'lo0': 0x4832 },
        'crc':      { 'hi2': 0x3B44, 'hi1': 0xC10E, 'hi0': 0xB621,
                      'lo2': 0x8BEC, 'lo1': 0xC28D, 'lo0': 0x9E4D } },
    'EmuTOS 1.01fr ST': {
        'checksum': { 'hi2': 0xEA7B, 'hi1': 0x43D2, 'hi0': 0x016F,
                      'lo2': 0xEB71, 'lo1': 0x9126, 'lo0': 0x5587 },
        'crc':      { 'hi2': 0xEFCF, 'hi1': 0x2D5E, 'hi0': 0x9D98,
                      'lo2': 0x2F88, 'lo1': 0x274C, 'lo0': 0xB0C6 } },
    'EmuTOS 1.01gr ST': {
        'checksum': { 'hi2': 0xAD6A, 'hi1': 0x2FB9, 'hi0': 0xF66E,
                      'lo2': 0xEF60, 'lo1': 0x62AB, 'lo0': 0x6EF3 },
        'crc':      { 'hi2': 0xFA33, 'hi1': 0x3E55, 'hi0': 0x68DE,
                      'lo2': 0xCB99, 'lo1': 0xD838, 'lo0': 0x4E81 } },
    'EmuTOS 1.01it ST': {
        'checksum': { 'hi2': 0x9F40, 'hi1': 0x4960, 'hi0': 0xF55A,
                      'lo2': 0x9027, 'lo1': 0x8250, 'lo0': 0x4D4A },
        'crc':      { 'hi2': 0x3203, 'hi1': 0x1E15, 'hi0': 0x5448,
                      'lo2': 0x2C59, 'lo1': 0x4AEA, 'lo0': 0x57A7 } },
    'EmuTOS 1.01nl ST': {
        'checksum': { 'hi2': 0x8E09, 'hi1': 0x4752, 'hi0': 0xFA4E,
                      'lo2': 0x7F10, 'lo1': 0x869B, 'lo0': 0x556E },
        'crc':      { 'hi2': 0xD838, 'hi1': 0xA583, 'hi0': 0x24EC,
                      'lo2': 0x0F0A, 'lo1': 0xC567, 'lo0': 0x8F0B } },
    'EmuTOS 1.01no ST': {
        'checksum': { 'hi2': 0x4278, 'hi1': 0x4B1B, 'hi0': 0xF46E,
                      'lo2': 0x2C43, 'lo1': 0x8CA9, 'lo0': 0x3EE3 },
        'crc':      { 'hi2': 0xFE38, 'hi1': 0xC31A, 'hi0': 0x373B,
                      'lo2': 0xA4C4, 'lo1': 0xAD9B, 'lo0': 0x1318 } },
    'EmuTOS 1.01pl ST': {
        'checksum': { 'hi2': 0xA2FA, 'hi1': 0x438D, 'hi0': 0x9A7F,
                      'lo2': 0xA64D, 'lo1': 0x8659, 'lo0': 0x2F21 },
        'crc':      { 'hi2': 0x2359, 'hi1': 0x394E, 'hi0': 0xAB40,
                      'lo2': 0x5250, 'lo1': 0xAB8D, 'lo0': 0xC7CC } },
    'EmuTOS 1.01ru ST': {
        'checksum': { 'hi2': 0xFE12, 'hi1': 0x367A, 'hi0': 0xD23C,
                      'lo2': 0x2CC6, 'lo1': 0x692D, 'lo0': 0x0FD8 },
        'crc':      { 'hi2': 0x76EA, 'hi1': 0x6201, 'hi0': 0x2592,
                      'lo2': 0x228D, 'lo1': 0x0110, 'lo0': 0x9E6A } },
    'EmuTOS 1.01se ST': {
        'checksum': { 'hi2': 0x4278, 'hi1': 0x4B1B, 'hi0': 0xF459,
                      'lo2': 0x2C43, 'lo1': 0x8CA9, 'lo0': 0x3E83 },
        'crc':      { 'hi2': 0xFE38, 'hi1': 0xC31A, 'hi0': 0x645A,
                      'lo2': 0xA4C4, 'lo1': 0xAD9B, 'lo0': 0xE37B } },
    'EmuTOS 1.01sg ST': {
        'checksum': { 'hi2': 0xAA01, 'hi1': 0x4914, 'hi0': 0xF5BE,
                      'lo2': 0x942B, 'lo1': 0x7189, 'lo0': 0x3F39 },
        'crc':      { 'hi2': 0xB33B, 'hi1': 0xBD1E, 'hi0': 0x923D,
                      'lo2': 0x937E, 'lo1': 0xB3B0, 'lo0': 0xBD2D } },
    'EmuTOS 1.01uk ST': {
        'checksum': { 'hi2': 0x3E16, 'hi1': 0x4C11, 'hi0': 0xF42D,
                      'lo2': 0x2194, 'lo1': 0x8492, 'lo0': 0x351E },
        'crc':      { 'hi2': 0xB4DD, 'hi1': 0xADB6, 'hi0': 0x2A58,
                      'lo2': 0x5774, 'lo1': 0x8522, 'lo0': 0xCF59 } },
    'EmuTOS 1.01us ST': {
        'checksum': { 'hi2': 0x3E16, 'hi1': 0x4C11, 'hi0': 0xF2A1,
                      'lo2': 0x2194, 'lo1': 0x8492, 'lo0': 0x3518 },
        'crc':      { 'hi2': 0xB4DD, 'hi1': 0xADB6, 'hi0': 0x3287,
                      'lo2': 0x5774, 'lo1': 0x8522, 'lo0': 0x48B9 } },
    'EmuTOS 1.01fr STe': {
            'checksum': { 'hi': 0xC84F,
                          'lo': 0xB4D8 },
            'crc':      { 'hi': 0xC4DA,
                          'lo': 0x84D0 } },
    'EmuTOS 1.01cz STe': {
        'checksum': { 'hi': 0xA6D5,
                      'lo': 0xCC25 },
        'crc':      { 'hi': 0x5AA9,
                      'lo': 0x9E8A } },
    'EmuTOS 1.01de STe': {
        'checksum': { 'hi': 0x5781,
                      'lo': 0x0B29 },
        'crc':      { 'hi': 0x07C9,
                      'lo': 0x7CBE } },
    'EmuTOS 1.01es STe': {
        'checksum': { 'hi': 0x7BAF,
                      'lo': 0x53E2 },
        'crc':      { 'hi': 0xD77C,
                      'lo': 0x6940 } },
    'EmuTOS 1.01fi STe': {
        'checksum': { 'hi': 0x9503,
                      'lo': 0x4143 },
        'crc':      { 'hi': 0xF3BE,
                      'lo': 0x6C75 } },
    'EmuTOS 1.01gr STe': {
        'checksum': { 'hi': 0x547D,
                      'lo': 0xCEB7 },
        'crc':      { 'hi': 0xE003,
                      'lo': 0xBA14 } },
    'EmuTOS 1.01it STe': {
        'checksum': { 'hi': 0x1145,
                      'lo': 0xD6EC },
        'crc':      { 'hi': 0xA386,
                      'lo': 0x99B8 } },
    'EmuTOS 1.01nl STe': {
        'checksum': { 'hi': 0xFAEB,
                      'lo': 0xC585 },
        'crc':      { 'hi': 0x163A,
                      'lo': 0x2644 } },
    'EmuTOS 1.01no STe': {
        'checksum': { 'hi': 0x71A8,
                      'lo': 0x768C },
        'crc':      { 'hi': 0x995D,
                      'lo': 0xA49B } },
    'EmuTOS 1.01pl STe': {
        'checksum': { 'hi': 0xE53D,
                      'lo': 0x28FF },
        'crc':      { 'hi': 0x70BA,
                      'lo': 0xA2E3 } },
    'EmuTOS 1.01ru STe': {
        'checksum': { 'hi': 0xFF17,
                      'lo': 0x2D7B },
        'crc':      { 'hi': 0x4F8A,
                      'lo': 0xC7B5 } },
    'EmuTOS 1.01se STe': {
        'checksum': { 'hi': 0x7193,
                      'lo': 0x762C },
        'crc':      { 'hi': 0x50AF,
                      'lo': 0x8C01 } },
    'EmuTOS 1.01sg STe': {
        'checksum': { 'hi': 0x55BF,
                      'lo': 0x15A0 },
        'crc':      { 'hi': 0x9ED8,
                      'lo': 0x3EAC } },
    'EmuTOS 1.01uk STe': {
        'checksum': { 'hi': 0x6DBE,
                      'lo': 0x4931 },
        'crc':      { 'hi': 0x318D,
                      'lo': 0x0F79 } },
    'EmuTOS 1.01us STe': {
        'checksum': { 'hi': 0x6C32,
                      'lo': 0x492B },
        'crc':      { 'hi': 0x065F,
                      'lo': 0x5E05 } },
    }
