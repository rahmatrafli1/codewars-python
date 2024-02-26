FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'E': 'Energy', 'F': 'Function', 'G': 'Glitch',
              'H': 'Half-life', 'I': 'Ice', 'J': 'Java', 'K': 'Keystroke', 'L': 'Logic', 'M': 'Malware', 'N': 'Nagware',
              'O': 'OS', 'P': 'Phishing', 'Q': 'Quantum', 'R': 'RAD', 'S': 'Strike', 'T': 'Trojan', 'U': 'Ultraviolet',
              'V': 'Vanilla', 'W': 'WiFi', 'X': 'Xerox', 'Y': 'Y', 'Z': 'Zero'}

SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'D': 'Discharge', 'E': 'Electron', 'F': 'Faraday', 'G': 'Gig',
           'H': 'Hacker', 'I': 'IP', 'J': 'Jabber', 'K': 'Killer', 'L': 'Lazer', 'M': 'Mike', 'N': 'n00b',
           'O': 'Overclock', 'P': 'Payload', 'Q': 'Quark', 'R': 'Roy', 'S': 'Spy', 'T': 'T-Rex', 'U': 'Unit',
           'V': 'Virus', 'W': 'Worm', 'X': 'X', 'Y': 'Yob', 'Z': 'Zombie'}

def alias_gen(f_name, l_name):
    if f_name and l_name and f_name[0].isalpha() and l_name[0].isalpha():
        first_name_word = FIRST_NAME.get(f_name[0].upper(), '')
        surname_word = SURNAME.get(l_name[0].upper(), '')

        if first_name_word and surname_word:
            return f'{first_name_word} {surname_word}'
        else:
            return "Your name must start with a letter from A - Z."
    else:
        return "Your name must start with a letter from A - Z."