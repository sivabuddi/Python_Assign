from nltk import wordpunct_tokenize
from apps.pos_tagger import pos_tagger_named_entity
from apps.stemmer import stem_each_word


def tokenize(input_file, output_file):
    in_file = open(input_file, "r")
    out_file = open(output_file, "w")
    for statement in in_file:
        tokens = wordpunct_tokenize(str(statement))
        out_file.write(str(tokens) + "\n")
        pos_tagger_named_entity(tokens, "pos_tag.txt", "ne_chunk.txt")
        stem_each_word(tokens, "lancaster.txt", "porter.txt", "snowball.txt", "lemmetize.txt","trigrams.txt")
