

# count the frequency of each word in a sentence

def frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

sentence =  "I am a programmer and I am learning Python and Django"
print(frequency(sentence))
