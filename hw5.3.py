import string

text = input("Введіть текст: ")

text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()
capitalized = [word.capitalize() for word in words]
hashtag = '#' + ''.join(capitalized)
hashtag = hashtag[:140]

print(hashtag)
