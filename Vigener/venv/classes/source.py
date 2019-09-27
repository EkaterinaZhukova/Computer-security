from main_logic.language_info import Language
from main_logic.Vigenere import Vigenere
from main_logic.Kasiski import *
import random
import string

def load_data_from_file(file_name):
    f = open(file_name, encoding='utf-8', errors='surrogateescape')
    data = f.readlines()
    if len(data) != 3:
        print ('incorrect input data')
        return
    lang_text = data[0]
    key = data[1]
    string_to_encrypt = data[2]


    if lang_text == 'ru\n':
        lang = Language.RU
    elif lang_text == 'en\n':
        lang = Language.EN
    else:
        print('Incorrect language')
        return

    source_text = process_source_text(string_to_encrypt.lower(), lang)
    print('Current language is: ', lang_text)
    return key, source_text, lang


def process_source_text(text, lang):
    alphabet = [i for i in lang.alphabet()]
    res = text
    for letter in res:
        if letter not in alphabet:
            res = res.replace(letter, "")
    return res

def test_with_filename(file_name):
    print('\n***************LOAD DATA***************')
    print ('Start working....\nLoading data from file: ' + file_name)
    source_key, source_text, lang = load_data_from_file(file_name)

    source_key = source_key.replace('\n', '')
    print ('Source text is: ' +  source_text + '\n')
    print ('Length of source text is: ' + str(len(source_text)))
    print ('Key is: ' + source_key)
    run(lang, source_text, source_key)

def run(lang, source_text, source_key):
    ## Encode
    print('\n***************ENCODING***************')
    vigenere = Vigenere(lang)
    ciphered_text = "".join(vigenere.encode(source_text, source_key))
    print('Encoded text is: ' + ciphered_text)

    ## Decode
    print('\n***************DECODING***************')
    decoded_text = vigenere.decode(ciphered_text, source_key)
    print('Decoded text is: ' + "".join(decoded_text))

    ##Attack
    print('\n***************ATTACK***************')
    key_found_by_attack = crack_vigenere(ciphered_text, lang)
    if key_found_by_attack is None:
        print('Key wasn\'t found\n')
        return

    print('Key found by Kasiski examination: ' + key_found_by_attack)
    hacked_text = vigenere.decode(ciphered_text, key_found_by_attack)
    print('Text found by attack: ' + "".join(hacked_text))

    if hacked_text == decoded_text:
        print('Attack was succeed! Hacked and decoded texts are the same')
    else:
        print('Something went wrong! Attack was not succeed :(')

def main():
    test_files = ['test3_1.txt', 'test3_2.txt', 'test3_3.txt',
                  'test4_1.txt','test4_2.txt', 'test4_3.txt',
                  'test4_4.txt', 'test4_5.txt']
    for file in test_files:
        print('\n===========================================================================')
        test_with_filename(file)
        print('===========================================================================\n')


main()


text1 = "Weeds were not the only things Frank had to contend with either. Boys from the village made a habit of throwing stones through the windows of the Riddle House. They rode their bicycles over the lawns Frank worked so hard to keep smooth. Once or twice, they broke into the old house for a dare. They knew that old Frank's devotion to the house and the grounds amounted almost to an obsession, and it amused them to see him limping across the garden"
text2 = "Young Cowperwood was making a rapid calculation. If, as the auctioneer said, coffee was worth seven dollars and thirty-two cents a bag in the open market, and this buyer was getting this coffee for seventy-five dollars, he was making then and there eighty-six dollars and four cents, to say nothing of what his profit would be if he sold it at retail. As he recalled, his mother was paying twenty-eight cents a pound. He drew nearer, his books tucked under his arm, and watched these operations closely. The starch, as he soon heard, was valued at ten dollars a barrel, and it only brought six. Some kegs of vinegar were knocked down at one-third their value, and so on. He began to wish he could bid; but he had no money, just a little pocket change. The auctioneer noticed him standing almost directly under his nose, and was impressed with the stolidity — solidity — of the boy’s expression."
text3 = "Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn't think they could bear it if anyone found out about the Potters. Mrs. Potter was Mrs. Dursley's sister, but they hadn't met for several years; in fact, Mrs. Dursley pretended she didn't have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn't want Dudley mixing with a child like that."
text4 = "It was on the corner of the street that he noticed the first sign of something peculiar -- a cat reading a map. For a second, Mr. Dursley didn't realize what he had seen -- then he jerked his head around to look again. There was a tabby cat standing on the corner of Privet Drive, but there wasn't a map in sight. What could he have been thinking of? It must have been a trick of the light. Mr. Dursley blinked and stared at the cat. It stared back. As Mr. Dursley drove around the corner and up the road, he watched the cat in his mirror. It was now reading the sign that said Privet Drive -- no, looking at the sign; cats couldn't read maps or signs. Mr. Dursley gave himself a little shake and put the cat out of his mind. As he drove toward town he thought of nothing except a large order of drills he was hoping to get that day.But on the edge of town, drills were driven out of his mind by something else. As he sat in the usual morning traffic jam, he couldn't help noticing that there seemed to be a lot of strangely dressed people about. People in cloaks. Mr. Dursley couldn't bear people who dressed in funny clothes -- the getups you saw on young people! He supposed this was some stupid new fashion. He drummed his fingers on the steering wheel and his eyes fell on a huddle of these weirdos standing quite close by. They were whispering excitedly together. Mr. Dursley was enraged to see that a couple of them weren't young at all; why, that man had to be older than he was, and wearing an emerald-green cloak! The nerve of him! But then it struck Mr. Dursley that this was probably some silly stunt -- these people were obviously collecting for something. . . yes, that would be it. The traffic moved on and a few minutes later, Mr. Dursley arrived in the Grunnings parking lot, his mind back on drills."
text5 = "Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn't think they could bear it if anyone found out about the Potters. Mrs. Potter was Mrs. Dursley's sister, but they hadn't met for several years; in fact, Mrs. Dursley pretended she didn't have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn't want Dudley mixing with a child like that.When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr. Dursley hummed as he picked out his most boring tie for work, and Mrs. Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.None of them noticed a large, tawny owl flutter past the window.At half past eight, Mr. Dursley picked up his briefcase, pecked Mrs. Dursley on the cheek, and tried to kiss Dudley good-bye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. chortled Mr. Dursley as he left the house. He got into his car and backed out of number four's drive.It was on the corner of the street that he noticed the first sign of something peculiar -- a cat reading a map. For a second, Mr. Dursley didn't realize what he had seen -- then he jerked his head around to look again. There was a tabby cat standing on the corner of Privet Drive, but there wasn't a map in sight. What could he have been thinking of? It must have been a trick of the light. Mr. Dursley blinked and stared at the cat. It stared back. As Mr. Dursley drove around the corner and up the road, he watched the cat in his mirror. It was now reading the sign that said Privet Drive -- no, looking at the sign; cats couldn't read maps or signs. Mr. Dursley gave himself a little shake and put the cat out of his mind. As he drove toward town he thought of nothing except a large order of drills he was hoping to get that day.But on the edge of town, drills were driven out of his mind by something else. As he sat in the usual morning traffic jam, he couldn't help noticing that there seemed to be a lot of strangely dressed people about. People in cloaks. Mr. Dursley couldn't bear people who dressed in funny clothes -- the getups you saw on young people! He supposed this was some stupid new fashion. He drummed his fingers on the steering wheel and his eyes fell on a huddle of these weirdos standing quite close by. They were whispering excitedly together. Mr. Dursley was enraged to see that a couple of them weren't young at all; why, that man had to be older than he was, and wearing an emerald-green cloak! The nerve of him! But then it struck Mr. Dursley that this was probably some silly stunt -- these people were obviously collecting for something. . . yes, that would be it. The traffic moved on and a few minutes later, Mr. Dursley arrived in the Grunnings parking lot, his mind back on drills."
text6 = "He purchased a horse and buggy about this time — the most attractive-looking animal and vehicle he could find — the combination cost him five hundred dollars — and invited Mrs. Semple to drive with him. She refused at first, but later consented. He had told her of his success, his prospects, his windfall of fifteen thousand dollars, his intention of going into the note-brokerage business. She knew his father was likely to succeed to the position of vice-president in the Third National Bank, and she liked the Cowperwoods. Now she began to realize that there was something more than mere friendship here."
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def hack_test(key_len):
    lang = Language.EN
    source_texts = [text1, text2, text3, text4, text5,text6]
    for text in source_texts:
        success = 0
        preccessed = process_source_text(text, lang)
        for i in range (100):
            key = randomString(key_len)
            vigenere = Vigenere(lang)
            ciphered_text = "".join(vigenere.encode(preccessed, key))
            key_found_by_attack = crack_vigenere(ciphered_text, lang)
            if key_found_by_attack == key:
                success += 1
        print("For text of length " +str(len(preccessed)) + " with key of length " + str(key_len) + " num of success is: " + str(success))

def test():
    arr_len = [5, 10, 15, 20, 25, 40, 60]
    for length in arr_len:
        print("\n================================================================")
        hack_test(length)
        print("\n================================================================")

# test()