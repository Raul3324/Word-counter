import requests, nltk
from operator import itemgetter
from nltk.probability import FreqDist
nltk.download('punkt_tab')
fdist = FreqDist()

link_to_book = input("Link to book: ")
request = requests.get(link_to_book)

with open("book.txt", 'w') as file:
    file.write(request.text)


file = open("book.txt")
content = file.read()

for sentence in nltk.tokenize.sent_tokenize(content):
    for word in nltk.tokenize.word_tokenize(sentence):
        if word.isalpha():
            fdist[word.lower()] += 1


word_list = fdist.most_common()
result = sorted(word_list, key=itemgetter(1), reverse=True)

with open("word_count.txt", 'w') as file:
    for item in result:
        file.write(str(item) + '\n')