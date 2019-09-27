from enum import Enum

class Language(Enum):
    EN = 1
    RU = 2



    def info(self):
        if self == Language.EN:
            return 97,26
        elif self == Language.RU:
            return 1072, 32
        else:
            return nil

    def alphabet(self):
        if self == Language.EN:
            return 'abcdefghijklmnopqrstuvwxyz'
        elif self == Language.RU:
            return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        else:
            return nil

    def alphabet_arr(self):
        if self == Language.EN:
            return ['a', 'b', 'c', 'd', 'e',
                    'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y',
                    'z']
        elif self == Language.RU:
            return ['а', 'б', 'в', 'г', 'д',
                    'е', 'ё', 'ж', 'з', 'и',
                    'й', 'к', 'л', 'м', 'н',
                    'о', 'п', 'р', 'с', 'т',
                    'у', 'ф', 'х', 'ц', 'ч',
                    'ш', 'щ', 'ъ', 'ы', 'ь',
                    'э', 'ю', 'я']
        else:
            return nil


    def frequency(self):
        if self == Language.EN:
            return [0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
                    0.0228, 0.02015, 0.06094, 0.06966, 0.00153,
                    0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
                    0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                    0.02758, 0.00978, 0.0236, 0.0015, 0.01974,
                    0.00074]
        elif self == Language.RU:
            return [.07821, .01732, .0449, .01698,
                    .03103, .08567, .0007, .01082,
                    .01647, .06777, .01041, .03215,
                    .04813, .03139, .0685, .11394,
                    .02754, .04234, .05382, .06443,
                    .02882, .00132, .00833, .00333,
                    .01645, .00775, .00331, .00023,
                    .01854, .02106, .0031, .00544,
                    .01979]
        else:
            return nil