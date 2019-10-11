from nltk import PorterStemmer, LancasterStemmer, SnowballStemmer

pStemmer = PorterStemmer()
lStemmer = LancasterStemmer()
sStemmer = SnowballStemmer('english')

print(pStemmer.stem("Playing"))
print(lStemmer.stem("Dancing"))
print(sStemmer.stem("Killing"))

from nltk.stem import WordNetLemmatizer

lemmetizer = WordNetLemmatizer()
print(lemmetizer.lemmatize("Playing"))
print(lemmetizer.lemmatize("Dancing"))
print(lemmetizer.lemmatize("Killing"))
print(lemmetizer.lemmatize("geese"))

from nltk import wordpunct_tokenize, pos_tag, ne_chunk

sentence = "Mark and John are working at google"
print(wordpunct_tokenize(sentence), '\n')
print(pos_tag(wordpunct_tokenize(sentence)), '\n')
print(ne_chunk(pos_tag(wordpunct_tokenize(sentence))))
