from math import gcd
from collections import Counter



def find_distances(current_set):
    arr = []
    sorted_arr = sorted(current_set)

    for i in range(len(sorted_arr) - 1):
        first = sorted_arr[i]
        second = sorted_arr[i+1]
        arr.append(second - first)

    return arr




def find_positions_of_trigraphs(encoded):
    positions = {}
    for i in range(len(encoded) - 2):
        newgraph = encoded[i:i + 3]
        if newgraph not in positions:
            positions[newgraph] = {i}
        else:
            current_set = positions[newgraph]
            current_set.add(i)
    return positions


def find_spacings(positions):
    distances = []
    for element in positions:
        if len(positions[element]) > 1:
            tmp_distance = find_distances(positions[element])
            distances.extend(tmp_distance)
    return  sorted(distances)


def key_length_by_kasiski(encoded):
    positions = find_positions_of_trigraphs(encoded)
    spacings =  find_spacings(positions)
    counter = Counter(spacings)
    most_common = counter.most_common(3)

    if not most_common:
        return 1
    res_gcd = most_common[0][0]
    for element in most_common:
        res_gcd = gcd(res_gcd, element[0])
    return res_gcd


def crack_vigenere(encoded, lang):
    key_len = key_length_by_kasiski(encoded)

    if key_len == 1:
        return None

    groups = split_on_groups_encoded_text(encoded, key_len)

    key = ''
    alphabet = lang.alphabet()
    frequency = lang.frequency()
    for group in groups:
        set_fr = frequency_analysis(group, alphabet)
        val = difference_frequency_amount(set_fr, frequency)
        letter = val.index(min(val))
        key += alphabet[letter]
    return key


def frequency_analysis(group, alphabet):
    frequency_set = []
    for letter in alphabet:
        amount_of_occurances = 0
        group_len = len(group)
        for i in range(group_len):
            if group[i] == letter:
                amount_of_occurances += 1
        frequency = amount_of_occurances / group_len
        frequency_set.append(frequency)

    return frequency_set

def difference_frequency_amount(actual, compared):
    shift = 0
    amount = len(compared)
    diff = []
    while shift < len(compared):
        res = 0
        for i in range(len(actual)):
            res += abs(actual[(i+ shift)%amount] - compared[i])
        diff.append(res)
        shift += 1
    return diff


def split_on_groups_encoded_text(encoded, key_len):
    groups = []
    for index in range(key_len):
        tmp_group = []
        i = index
        while i < len(encoded):
            tmp_group.append(encoded[i])
            i += key_len
        groups.append(tmp_group)
    return groups


