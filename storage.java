
function compare(word1, word2):
    // this should return True if value 1 is alphabetically before value 2
    letter_index = 0;
    while letter_index < word1.length():
        letter_index += 1
        letter1 = word1.get_character_at(letter_index)
        letter2 = word2.get_character_at(letter_index)

        if alphabet.indexOf(letter1) > alphabet.indexOf(letter2)
            return True
        else if alphabet.indexOf(letter2) > alphabet.indexOf(letter1)
            return False

    return True




