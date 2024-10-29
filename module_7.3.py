
class WordsFinder:
    def __init__(self, *filenames):
        self.filenames = filenames

    def get_all_words(self):
        all_words = {}

        for filename in self.filenames:
            with open(filename, encoding='utf-8') as f:
                words = []
                for line in f:
                    for x in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(x, '')
                    words.extend(line.lower().split())
                all_words[filename] = words

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            if word.lower() in words:
                return {
                    filename : words.index(word.lower()) + 1
                }

    def count(self, word):
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            if word.lower() in words:
                return {
                    filename : words.count(word.lower())
                }


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('его')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего