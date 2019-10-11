from nltk import pos_tag, ne_chunk


def pos_tagger_named_entity(tokens, post_tag_file, named_chunk_file):
    pos_tagged_file = open(post_tag_file, "a+")
    name_chunked_file = open(named_chunk_file, "a+")
    pos_tagged_file.write(str(pos_tag(tokens)))
    name_chunked_file.write(str(ne_chunk(pos_tag(tokens))))
