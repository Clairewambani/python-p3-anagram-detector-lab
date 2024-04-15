class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        anagrams = []
        for w in word_list:
            if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word:
                anagrams.append(w)
        return anagrams

# Example usage:
listen = Anagram("listen")
matches = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(matches)  # Output: ['inlets']
