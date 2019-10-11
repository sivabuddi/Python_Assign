class StringOperations:

    def string_alternative(self,input_string):
        output = ""
        for counter in range(0,len(input_string),2):
            output+=input_string[counter]
        return output
