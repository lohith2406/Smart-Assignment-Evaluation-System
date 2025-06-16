import nltk
from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

word = "revolutionize"
synonyms = get_synonyms(word)
print("Synonyms :", synonyms)
from nltk.corpus import wordnet

def get_synonyms(keywords):
    for i in range(len(keywords)):
        synonyms = []
        for syn in wordnet.synsets(keywords[i][0]):  # Fetching synonyms for the first element of each sublist
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        keywords[i].extend(synonyms)

# Example usage
keywords = [["save"], ["innovate"], ["transform"]]
get_synonyms(keywords)

# Printing the modified keywords list
for item in keywords:
    print("Keyword:", item[0])
    print("Synonyms:", item[1:])
