class Wordcounter:
    def __init__(self, path: str) -> None:
        self.path = path

    def __repr__(self) -> str:
        return f"Word counter of file: {self.path}"

    @property
    def script_length(self):
        return f"Length of script is {len(self.getScript())}"

    @property
    def script(self):
        file = self.path
        words = []
        with open(file, "r") as f:
            content = f.readlines()
            for line in content:
                for word in line.split():
                    words.append(word)
        return words

    @property
    def word_counter(self):
        word_counter = {}
        for word in self.script:
            word_counter[word] = word_counter.setdefault(word, 0) + 1
        return word_counter

    @property
    def top_word(self):
        word = max(self.word_counter, key=lambda x: self.word_counter[x])
        score = self.word_counter[word]
        return f"Top word is {word} with score of {score} repetitions"

    def printTopWords(self, count=5):
        ans = []
        temp_dict = self.word_counter
        for _ in range(count):
            word = max(temp_dict, key=lambda x: temp_dict[x])
            ans.append((word, temp_dict[word]))
            temp_dict.pop(word)
        for key, value in ans:
            print(f"Word: {key}, score: {value}")
        return ans


bee = Wordcounter("beemovie.txt")
bee.printTopWords(5)
