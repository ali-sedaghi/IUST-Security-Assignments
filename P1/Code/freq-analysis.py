alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

order_of_alphabet = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'


def getfirstItem(items):
    return items[0]


def FreqOrder(message):
    main_message = message.upper()
    letter_counter = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                   'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                   'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
                   'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    for char in main_message:
        if char in alphabet:
            letter_counter[char] += 1
    char_to_freq = letter_counter
    freq_to_letter = {}
    for char in alphabet:
        if char_to_freq[char] not in freq_to_letter:
            freq_to_letter[char_to_freq[char]] = [char]
        else:
            freq_to_letter[char_to_freq[char]].append(char)
    for frequence in freq_to_letter:
        freq_to_letter[frequence].sort(reverse=True, key=order_of_alphabet.find)
        freq_to_letter[frequence] = ''.join(freq_to_letter[frequence])
    list_of_freq = list(freq_to_letter.items())
    list_of_freq.sort(reverse=True, key=getfirstItem)
    order = []
    for ind in list_of_freq:
        order.append(ind[1])
    return ''.join(order)


def MatchScore(message):
    order = FreqOrder(message)
    score = 0
    for char in order_of_alphabet[-6:]:
        if char in order[-6:]:
            score += 1
    for char in order_of_alphabet[:6]:
        if char in order[:6]:
            score += 1
    return score
