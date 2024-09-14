def prepareDataRBP(input_filepath, output_filepath='output.txt'):
    file = open(input_filepath, 'r')
    lines = file.readlines()
    file.close()
    new_file = open(output_filepath, 'w')
    for line in lines:
        elements = line.split('\t')
        new_line = elements[0] + ':' + elements[1] + '-' + elements[2] + ':' + elements[-1]
        new_file.write(new_line)
    new_file.close()
