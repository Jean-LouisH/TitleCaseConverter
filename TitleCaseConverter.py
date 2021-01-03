def convert_to_title_case(entered_string):
    articles = ["the", "a", "an"]
    adpositions = ["in", "on", "under", "towards", "before", "of", "with", "without", "to", "as", "is", "are"]
    conjunctions = ["for", "and", "but", "or", "nor", "yet", "so", "either", "neither", "whether", "rather",
                    "after", "before", "though", "however", "because", "since", "unless" "until", "when",
                    "whenever", "where", "whereas", "wherever", "while"]
    lowercase_words = articles + adpositions + conjunctions
    words = entered_string.split(" ")
    output_string = ""
    word_count = len(words)

    #The first word is always capitalized.
    output_string += words[0].capitalize() + " "

    if word_count > 1:
        for i in range(1, word_count - 1, 1):
            first_character = words[i][0]
            
            if words[i] in lowercase_words and "." not in words[i - 1]:
                output_string += words[i].lower() + " "
            elif any(x.isupper() for x in words[i]): #Capitalized or has any capital letters
                output_string += words[i] + " "
            elif (first_character == "(" or 
                first_character == "\"" or 
                first_character == "'"):
                    other_characters = words[i][1:]
                    output_string += first_character + other_characters.capitalize() + " "
            else:
                output_string += words[i].capitalize() + " "

        #The last word is always capitalized
        output_string += words[word_count - 1].capitalize()

    return output_string

def write_conversion_to_file(output_string):
    f_out = open("title_case_output.txt", "w")
    f_out.write(output_string)
    f_out.close()    

def main():    
    print("\t\tTitle Case Converter")
    print("\nThis converts a regular string like\n"
          "'Local man marries a pole in Toronto' to 'Local Man Marries a Pole in Toronto'")

    option_input = ""
    is_exiting = False
    while not is_exiting:

        print("\n-----------------------------------------")
        print("Select one of the following options\n")
        print("1: Convert from entered string"
              "\n2: Convert from text file"
              "\nexit: Exit")
        
        option_input = input("\nEnter Option -> ")
        output_string = ""
        
        if option_input == "1":
            entered_string = input("\nEnter string -> ")
            output_string = convert_to_title_case(entered_string)
            print("\n" + output_string)
            write_conversion_to_file(output_string)
        elif option_input == "2":
            entered_filepath = input("\nEnter filepath -> ")
            try:
                f_in = open(entered_filepath, "r")
                file_string = f_in.read()
                f_in.close()
                output_string = convert_to_title_case(file_string)
                print("\n" + output_string)
                write_conversion_to_file(output_string)
            except:
                print("Filepath '" + entered_filepath + "' cannot be opened or is missing.")
        elif option_input == "3" or option_input == "exit":
            is_exiting = True
        else:
            print("'" + option_input + "' is not a valid option")

    
if __name__ == "__main__":
    main()
