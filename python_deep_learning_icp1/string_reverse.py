class Reverse:
    def reverse_stip_characters(self,input_string,number_to_strip):
        output = ""
        try:
            i = len(input_string) - number_to_strip
            if i < 0:
                raise Exception('Input number Characters are not suitable to trim')
            while i > 0:
                i -= 1
                output = output + input_string[i]
            return output
        except Exception as exception:
            print(exception)