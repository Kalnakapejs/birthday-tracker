def clean_file(input_filename, output_filename):
    input_file = open(input_filename, "r", encoding = "utf-8")
    output_file = open(output_filename, "w", encoding = "utf-8")

    for line in input_file.readlines():
        line = line.encode("ascii", "ignore").decode()
        remove = [".", ",", "?", "!", ";", ":", "-", "*", "_", "#", "(", ")", "{", "}", "[", "]", "%", "/", "+", "-", "$"]
        
        for symbol in remove:
            line = line.replace(symbol, " ")
        line = line.lower()
        output_file.write(line)
    input_file.close()
    output_file.close()

