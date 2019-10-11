from nltk import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ngrams

pStemmer = PorterStemmer()
lStemmer = LancasterStemmer()
sStemmer = SnowballStemmer('english')
lemmetizer = WordNetLemmatizer()


def stem_each_word(tokens, lancaster_file, porter_file, snowball_file, lemmetizer_file, trigrams_file):
    lancaster_file_out = open(lancaster_file, "a+")
    porter_file_out = open(porter_file, "a+")
    snowball_file_out = open(snowball_file, "a+")
    lemmetizer_file_out = open(lemmetizer_file, "a+")
    trigrams_file_out = open(trigrams_file, "a+")
    for token in tokens:
        porter_file_out.write(str(pStemmer.stem(token)) + "\t")
        lancaster_file_out.write(str(lStemmer.stem(token)) + "\t")
        snowball_file_out.write(str(sStemmer.stem(token)) + "\t")
        lemmetizer_file_out.write(str(lemmetizer.lemmatize(token)) + "\t")
    trigrams_file_out.write(str(list(ngrams(tokens, 3))))
    porter_file_out.write("\n")
    lancaster_file_out.write("\n")
    snowball_file_out.write("\n")
    lemmetizer_file_out.write("\n")
    trigrams_file_out.write("\n")
