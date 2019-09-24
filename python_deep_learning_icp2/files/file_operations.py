
class FileOperations:
    def count_words(self, input_file, output_file):
        f = open(input_file, "r")
        output = open(output_file, "w")
        final = ""
        input_line = f.read()
        word_count = {}

        for word in input_line.split():
            if word_count.get(word) is None:
                word_count[word] = 1
            else:
                count = word_count[word]
                count += 1
                word_count[word] = count
        f.close()

        for key, value in word_count.items():
            final = final + key + " " + str(value) + "\n"
        output.write(final)
        output.close()
