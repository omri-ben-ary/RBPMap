def prepare_data_for_training(rbp_input_filepath, experiment_input_file, output_filepath='output.txt', rbp_p_value_threshold=1e-3, experiment_threshold=0):
    rbp_file = open(rbp_input_filepath, 'r')
    rbp_lines = rbp_file.readlines()
    rbp_file.close()
    rbp_filtered_lines = [line for line in rbp_lines if
                          (line.startswith(("Protein:", "No motifs found", "Error:")) or line[0].isdigit())]
    experiment_file = open(experiment_input_file, 'r')
    experiment_lines = experiment_file.readlines()
    experiment_file.close()
    new_file = open(output_filepath, 'w')
    i = 1
    rbp_line = rbp_filtered_lines[i]
    for exp_line in experiment_lines:
        exp_label = 0
        exp_elements = exp_line.split('\t')
        if float(exp_elements[6]) > experiment_threshold:
            exp_label = 1
        while not rbp_line.startswith(("Protein:", "No motifs found", "Error:")):
            rbp_elements = rbp_line.split('\t')
            p_value = float(rbp_elements[-1][:-1])
            if p_value < rbp_p_value_threshold:
                new_line = rbp_elements[1] + '\t' + '\t1' + '\t' + str(exp_label) + '\n'
            else:
                new_line = rbp_elements[1] + '\t' + '\t0' + '\t' + str(exp_label) + '\n'
            new_file.write(new_line)
            i += 1
            if i >= len(rbp_filtered_lines):
                break
            rbp_line = rbp_filtered_lines[i]
        i += 1
        if i >= len(rbp_filtered_lines):
            break
        rbp_line = rbp_filtered_lines[i]
    new_file.close()
