import numpy as np
import matplotlib.pyplot as plt

def prepare_bed_file(input_filepath_positive, input_filepath_negative, output_filepath='output.txt', num_of_positive_samples=2000, shuffle=True):
    positive_file = open(input_filepath_positive, 'r')
    positive_lines = positive_file.readlines()
    num_of_positive_samples = min(num_of_positive_samples, len(positive_lines))
    positive_file.close()
    positive_lines = sort_and_clean_data(positive_lines)

    negative_file = open(input_filepath_negative, 'r')
    negative_lines = negative_file.readlines()
    negative_file.close()
    negative_lines = sort_and_clean_data(negative_lines)

    top_lines = positive_lines[:num_of_positive_samples]
    bottom_lines = np.flip(np.flip(negative_lines)[:num_of_positive_samples])
    dataset_lines = np.concatenate([top_lines, bottom_lines])
    if shuffle:
        order = np.array(range(len(dataset_lines)))
        np.random.shuffle(order)
        dataset_lines = [dataset_lines[index] for index in order]

    new_file = open(output_filepath, 'w')
    new_file.writelines(dataset_lines)
    new_file.close()


def sort_and_clean_data(lines):
    lines_to_write = []
    q_values = []
    for line in lines:
        elements = line.split('\t')
        location = int(elements[1]) + (int(elements[2]) - int(elements[1])) // 2
        elements[1] = str(location-100)
        elements[2] = str(location + 100)
        q_values.append(float(elements[7]))
        new_line = '\t'.join(elements)
        lines_to_write.append(new_line)
    order = np.flip(np.argsort(q_values))
    sorted_lines_to_write = np.array([lines_to_write[index] for index in order])
    return sorted_lines_to_write

def prepare_data(bed_filepath, fasta_filepath, output_filepath='output.txt', threshold=0):
    bed_file = open(bed_filepath, 'r')
    bed_lines = bed_file.readlines()
    bed_file.close()

    fasta_file = open(fasta_filepath, 'r')
    fasta_lines = fasta_file.readlines()
    fasta_lines = [line for line in fasta_lines if not line.startswith(">")]
    fasta_file.close()

    new_file = open(output_filepath, 'w')

    for bed_line, fasta_line in zip(bed_lines, fasta_lines):
        bed_elements = bed_line.split('\t')
        label = int(float(bed_elements[7]) > threshold)
        new_line = str(label) + '\t' + fasta_line
        new_file.write(new_line)
    new_file.close()


def label_rbp_map_results(input_rbp_filepath, input_ds_filepath, input_bed_filepath, output_filepath='output.txt', threshhold=1e-4):
    bed_file = open(input_bed_filepath, 'r')
    bed_lines = bed_file.readlines()
    bed_lines = [bed_lines[i].split('\t')[1] for i in range(len(bed_lines))]
    bed_file.close()

    ds_file = open(input_ds_filepath, 'r')
    ds_lines = ds_file.readlines()
    true_labels = [ds_lines[i].split('\t')[0] for i in range(len(ds_lines))]
    ds_file.close()

    rbp_file = open(input_rbp_filepath, 'r')
    rbp_lines = rbp_file.readlines()
    rbp_file.close()
    rbp_filtered_lines = [line for line in rbp_lines if
                          (line.startswith(("chr", "No motifs found")) or line[0].isdigit())]
    coordinates = []
    labels = []
    min_p_value = 1
    for line in rbp_filtered_lines:
        if line.startswith("chr"):
            if coordinates:
                labels.append(int(min_p_value < threshhold))
                min_p_value = 1
            start = line.find(':') + 1
            end = line.find('-', start)
            if start == 0 or end == -1:
                coordinates.append(-1)
            else:
                coordinates.append(line[start:end].strip())
        elif line.startswith("No motifs found"):
            continue
        else:
            elements = line.split('\t')
            min_p_value = min(min_p_value, float(elements[5]))
    labels.append(int(min_p_value < threshhold))

    new_file = open(output_filepath, 'w')
    new_file.write('RBPmap\tTrue\n')
    for (line, true_label) in zip(bed_lines, true_labels):
        try:
            index = coordinates.index(line)
            new_file.write(str(labels[index]) + '\t' + true_label + '\n')
        except ValueError:
            new_file.write('0\t' + true_label + '\n')
    new_file.close()

def make_file_uppercase(input_filepath, output_filepath):
    file = open(input_filepath, 'r')
    lines = file.readlines()
    lines = [line.upper() for line in lines]
    file.close()

    new_file = open(output_filepath, 'w')
    new_file.writelines(lines)
    new_file.close()

def classify_file_uppercase_lowercase(input_filepath, output_filepath):
    file = open(input_filepath, 'r')
    lines = file.readlines()
    lines = [transform_string(line) for line in lines]
    file.close()

    new_file = open(output_filepath, 'w')
    new_file.writelines(lines)
    new_file.close()

def transform_char(char):
    if char.isupper():
        return 'X'
    elif char.islower():
        return 'x'
    else:
        return char

def transform_string(s):
    return ''.join(transform_char(char) for char in s)

def add_secondary_structure(dataset_filepath, secondary_sruct_filepath, output_filepath):
    secondary_sruct_file = open(secondary_sruct_filepath, 'r')
    secondary_sruct_lines = secondary_sruct_file.readlines()
    secondary_sruct_lines = [line[0:200] for line in secondary_sruct_lines if (line.startswith(".") or line.startswith("("))]
    secondary_sruct_file.close()

    ds_file = open(dataset_filepath, 'r')
    lines = ds_file.readlines()
    lines = [add_secondary_struct_internal(line_pair) for line_pair in zip(lines,secondary_sruct_lines)]
    ds_file.close()

    new_file = open(output_filepath, 'w')
    new_file.writelines(lines)
    new_file.close()


def add_secondary_struct_internal(line_pair):
    return line_pair[0][0:2] + ''.join(line_pair[0][i+2].lower() if line_pair[1][i] == '.' else line_pair[0][i+2]for i in range(len(line_pair[1]))) + '\n'

def format_file_to_fasta(in_filepath, out_filepath):
    file = open(in_filepath, 'r')
    lines = file.readlines()
    file.close()

    new_file = open(out_filepath, 'w')
    for i, line in enumerate(lines):
        new_file.write('>seq' + str(i) + '\n')
        new_file.write(line)
    new_file.close()

def calc_seq_motif_avg_location_by_label(rbp_filepath, label_filepath, name):
    rbp_file = open(rbp_filepath, 'r')
    rbp_lines = rbp_file.readlines()
    rbp_lines = [line for line in rbp_lines if
                          (line.startswith(("Sequence", "No motifs found")) or line[0].isdigit())]
    rbp_file.close()

    #iterate through rbp lines and extract motif locations
    motif_locations = []
    min_p_value = 1
    coordinate_default = -100
    coordinate = coordinate_default
    last_line = "A"
    for line in rbp_lines:
        line_elements = line.split('\t')
        if line.startswith("No motifs found"):
            if last_line[0].isdigit():
                motif_locations.append(coordinate)
            motif_locations.append(coordinate_default)
            min_p_value = 1
            coordinate = coordinate_default
        elif line.startswith("Sequence"):
            if last_line[0].isdigit():
                motif_locations.append(coordinate)
            min_p_value = 1
            coordinate = coordinate_default
        elif float(line_elements[5]) < min_p_value:
            min_p_value = float(line_elements[5])
            coordinate = int(line_elements[0])
        last_line = line

    if coordinate != coordinate_default:
        motif_locations.append(coordinate)

    label_filepath = open(label_filepath, 'r')
    labels = label_filepath.readlines()
    labels = [int(label[0]) for label in labels]
    label_filepath.close()

    motif_locations_0 = []
    motif_locations_1 = []
    for label in labels:
        if label == 0:
            motif_locations_0.append(motif_locations.pop(0))
        else:
            motif_locations_1.append(motif_locations.pop(0))

    filtered_motif_locations_0 = [location for location in motif_locations_0 if location != coordinate_default]
    filtered_motif_locations_1 = [location for location in motif_locations_1 if location != coordinate_default]

    print(name + ':')
    print("Average motif location for label 0: ", np.mean(filtered_motif_locations_0))
    print("Average motif location for label 1: ", np.mean(filtered_motif_locations_1))
    print(f"Number of filtered out results for label 0: {len(motif_locations_0)-len(filtered_motif_locations_0)} out of {len(motif_locations_0)}")
    print(f"Number of filtered out results for label 1: {len(motif_locations_1)-len(filtered_motif_locations_1)} out of {len(motif_locations_1)}")
    print('**********************************************************')


    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    axs[0].hist(filtered_motif_locations_0, bins=200)
    axs[0].set_title(name+' Motif locations for label 0')
    axs[1].hist(filtered_motif_locations_1, bins=200)
    axs[1].set_title(name+' Motif locations for label 1')

    plt.show()


def create_dataset_with_secondary_struct_and_motif(rbp_filepath, secondary_sruct_filepath, output_filepath):
    rbp_file = open(rbp_filepath, 'r')
    rbp_lines = rbp_file.readlines()
    rbp_lines = [line for line in rbp_lines if
                          (line.startswith(("Sequence", "No motifs found")) or line[0].isdigit())]
    rbp_file.close()

    #iterate through rbp lines and extract motif locations
    motif_locations = []
    min_p_value = 1
    coordinate_default = -100
    coordinate = coordinate_default
    last_line = "A"
    for line in rbp_lines:
        line_elements = line.split('\t')
        if line.startswith("No motifs found"):
            if last_line[0].isdigit():
                motif_locations.append(coordinate)
            motif_locations.append(coordinate_default)
            min_p_value = 1
            coordinate = coordinate_default
        elif line.startswith("Sequence"):
            if last_line[0].isdigit():
                motif_locations.append(coordinate)
            min_p_value = 1
            coordinate = coordinate_default
        elif float(line_elements[5]) < min_p_value:
            min_p_value = float(line_elements[5])
            coordinate = int(line_elements[0])
        last_line = line

    if coordinate != coordinate_default:
        motif_locations.append(coordinate)

    secondary_sruct_file = open(secondary_sruct_filepath, 'r')
    secondary_sruct_lines = secondary_sruct_file.readlines()
    secondary_sruct_file.close()

    new_file = open(output_filepath, 'w')

    for i, line in enumerate(secondary_sruct_lines):
        if motif_locations[i] < 0:
            new_file.write(line)
            continue
        new_line = line[:2] + transform_substring(line[2:], motif_locations[i])    # lines are with the form: [label]\t[sequence]
        new_file.write(new_line)
    new_file.close()

def transform_substring(s, index, size=10):
    real_size = min(size, len(s) - index - 1)
    if index < 0:
        raise ValueError("Index out of range or substring exceeds string length")

    # Extract the substring to be transformed
    substring = s[index:index + real_size]

    # Transform each character in the substring to the following character in the ASCII order
    transformed_substring = ''.join(chr(ord(char) + 1) for char in substring)

    # Replace the original substring with the transformed substring
    new_string = s[:index] + transformed_substring + s[index + real_size:]

    return new_string
