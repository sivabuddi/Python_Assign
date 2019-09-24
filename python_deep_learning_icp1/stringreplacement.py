# Replace Class  in Python
class Replace:
    def replace(self,input_string,original_word, replacement_word):
        output_string = ""
        temp_string = ""
        temp_counter = -1
        init = 0
        for char in input_string:
            # check if its starting with Original word for replacing
            if temp_counter < 0 and char == original_word[init]:
                temp_counter = init
                temp_counter += 1
                temp_string += char
            # its matching and still going.
            elif 0 < temp_counter < len(original_word) and char == original_word[temp_counter]:
                temp_counter += 1
                temp_string += char
                # Matching Complete
                if temp_string == original_word:
                    temp_counter = -1
                    temp_string = ""
                    output_string += replacement_word
            # Partially matched, but not entirely, so don't replace use the temp string formed so far.
            elif 0 < temp_counter < len(original_word) and char != original_word[temp_counter]:
                temp_string += char
                output_string += temp_string
                temp_counter = -1
                temp_string = ""
            elif temp_counter == -1:
                output_string += char

        return output_string
