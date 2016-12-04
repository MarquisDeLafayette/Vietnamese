from string import punctuation
import codecs


def sort_items(x, y):
    """Sort by value first, and by key (reverted) second."""
    return cmp(x[1], y[1]) or cmp(y[0], x[0])

N = 50
words = {}

words_gen = (word.strip(punctuation).lower() for line in codecs.open("dialogue.txt", encoding = 'utf-8') 
                                             for word in line.split())
                                          
for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(words.iteritems(), cmp=sort_items, reverse=True)[:N]

for word, frequency in top_words:
    print "%s: %d" % (word, frequency)
