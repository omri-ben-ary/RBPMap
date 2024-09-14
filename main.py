from prepareData import *

'''Prepare Bed file with relevant windows around center'''
# prepare_bed_file("C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\312_01.basedon_312_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode.bed",
#               "C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\312_01.basedon_312_01_sorted.bed")
# prepare_bed_file("C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\SRSF1_hg38_K562_02_eCLIP.bed",
#                "C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\SRSF1_hg38_K562_02_eCLIP_fixed_coordinates.bed")

'''Prepare dataset using bed file and generated fasta file'''
# prepare_data(bed_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\SRSF1_hg38_HepG2_02_eCLIP_fixed_coordinates.bed",
#              fasta_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\SRSF1_hg38_HepG2_02_eCLIP_fixed_coordinates_FASTA.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\HepG2_dataset.txt", threshold=0)

# prepare_data(bed_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\SRSF1_hg38_K562_02_eCLIP_fixed_coordinates.bed",
#              fasta_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\SRSF1_hg38_K562_02_eCLIP_fixed_coordinates_FASTA.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\K562_dataset.txt", threshold=0)

'''Shuffle dataset so it is unordered'''
# shuffle_dataset(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\combined_data_ordered.txt",
#                 output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\combined_data_shuffled.txt")

####################################################################################################

# label_rbp_map_results(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResults.txt",
#                       output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResultsLabeled.txt")

# order = shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\combined_data_ordered.txt",
#                      output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\combined_data_shuffled_2.txt")
#
# shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResultsLabeled.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResultsLabeledShuffled.txt",
#              order=order)




# label_rbp_map_results(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResults_fifth.txt",
#                        output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResultsLabeled_fifth.txt")

# order = shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\combined_data_ordered_fifth_positive.txt",
#                     output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\combined_data_shuffled_fifth_positive.txt")
#
# shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResultsLabeled_fifth.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\dataset\\unprocessed\\RefrenceRBPMapResultsLabeledShuffled_fifth.txt",
#              order=order)

####################################################################################################

# prepare_data(bed_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\312.01v02.IDR.out.0102merged_sorted.bed",
#              fasta_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\312.01v02.IDR.out.0102merged_sorted_fasta.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\merged_dataset_all_ones.txt", threshold=0)
#
# prepare_data(bed_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\312_01.basedon_312_01_sorted.bed",
#              fasta_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\312_01.basedon_312_01_sorted_fasta.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\dataset_all_zeroes.txt", threshold=500)



# label_rbp_map_results(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_half_positive_rbp_results.txt",
#                       output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_half_positive_labled.txt")
#
# label_rbp_map_results(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_fifth_positive_rbp_results.txt",
#                       output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_fifth_positive_labled.txt")



# order = shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\clean_data_half_positive.txt",
#                     output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\clean_data_half_positive_shuffled.txt")
#
# shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_half_positive_labled.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_half_positive_labled_shuffled.txt",
#              order=order)
#
# order = shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\clean_data_fifth_positive.txt",
#                     output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\clean_data_fifth_positive_shuffled.txt")
#
# shuffle_file(input_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_fifth_positive_labled.txt",
#              output_filepath="C:\\Users\\User\\Desktop\\RBPMap\\raw_data\\chosen_files\\RefrenceRBPMapCleanData_fifth_positive_labled_shuffled.txt",
#              order=order)

####################################################################################################


# SRSF1_ENCSR432XUP_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR432XUP\\raw\\"
# SRSF1_ENCSR432XUP_positive_filename = "312.01v02.IDR.out.0102merged.bed.blacklist_removed.bed.narrowPeak.encode_no_random.bed"
# SRSF1_ENCSR432XUP_negative_filename = "312_01.basedon_312_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode_no_random.bed"
# SRSF1_ENCSR432XUP_output_filename = "SRSF1_ENCSR432XUP_raw_bed_file.bed"
# prepare_bed_file(SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_positive_filename, SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_negative_filename
#                  , SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_output_filename, num_of_positive_samples=2000, shuffle=True)
#
#
# SRSF1_ENCSR321PWZ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR321PWZ\\raw\\"
# SRSF1_ENCSR321PWZ_positive_filename = "4045_CLIP1_rep1.vs.4045_CLIP2_rep2.sorted.nh.narrowPeak_no_random.bed"
# SRSF1_ENCSR321PWZ_negative_filename = "encode4_batch11b.4045_CLIP1_CLIP.umi.r1.fq.genome-mappedSoSo.rmDupSo.peakClusters.normed.compressed.sorted.blacklist-removed.nh.narrowPeak_no_random.bed"
# SRSF1_ENCSR321PWZ_output_filename = "SRSF1_ENCSR321PWZ_raw_bed_file.bed"
# prepare_bed_file(SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_positive_filename, SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_negative_filename
#                  , SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_output_filename, num_of_positive_samples=2000, shuffle=True)
#
#
# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\raw\\"
# PUM2_ENCSR661ICQ_positive_filename = "441.01v02.IDR.out.0102merged.bed.blacklist_removed.bed.narrowPeak.encode.bed"
# PUM2_ENCSR661ICQ_negative_filename = "441_01.basedon_441_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode_no_random.bed"
# PUM2_ENCSR661ICQ_output_filename = "PUM2_ENCSR661ICQ_raw_bed_file.bed"
# prepare_bed_file(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_positive_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_negative_filename
#                  , PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_output_filename, num_of_positive_samples=2000, shuffle=True)
#
#
# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\raw\\"
# QKI_ENCSR366YOG_positive_filename = "466.01v02.IDR.out.0102merged.bed.blacklist_removed.bed.narrowPeak.encode_no_random.bed"
# QKI_ENCSR366YOG_negative_filename = "466_01.basedon_466_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode_no_random.bed"
# QKI_ENCSR366YOG_output_filename = "QKI_ENCSR366YOG_raw_bed_file.bed"
# prepare_bed_file(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_positive_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_negative_filename
#                  , QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_output_filename, num_of_positive_samples=2000, shuffle=True)
#
#
# QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\raw\\"
# QKI_ENCSR570WLM_positive_filename = "478.01v02.IDR.out.0102merged.bed.blacklist_removed.bed.narrowPeak.encode_no_random.bed"
# QKI_ENCSR570WLM_negative_filename = "478_01.basedon_478_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode_no_random.bed"
# QKI_ENCSR570WLM_output_filename = "QKI_ENCSR570WLM_raw_bed_file.bed"
# prepare_bed_file(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_positive_filename, QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_negative_filename
#                  , QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_output_filename, num_of_positive_samples=2000, shuffle=True)
#
#
# RBM5_ENCSR489ABS_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\RBM5\\ENCSR489ABS\\raw\\"
# RBM5_ENCSR489ABS_positive_filename = "501.01v02.IDR.out.0102merged.bed.blacklist_removed.bed.narrowPeak.encode.bed"
# RBM5_ENCSR489ABS_negative_filename = "501_01.basedon_501_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode_no_random.bed"
# RBM5_ENCSR489ABS_output_filename = "RBM5_ENCSR489ABS_raw_bed_file.bed"
# prepare_bed_file(RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_positive_filename, RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_negative_filename
#                  , RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_output_filename, num_of_positive_samples=2000, shuffle=True)
#
#
# hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\raw\\"
# hnRNPL_ENCSR724RDN_positive_filename = "678.01v02.IDR.out.0102merged.bed.blacklist_removed.bed.narrowPeak.encode.bed"
# hnRNPL_ENCSR724RDN_negative_filename = "678_01.basedon_678_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode_no_random.bed"
# hnRNPL_ENCSR724RDN_output_filename = "hnRNPL_ENCSR724RDN_raw_bed_file.bed"
# prepare_bed_file(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_positive_filename, hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_negative_filename
#                  , hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_output_filename, num_of_positive_samples=2000, shuffle=True)
#
#
# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\raw\\"
# hnRNPL_ENCSR795CAI_positive_filename = "560.01v02.IDR.out.0102merged.bed.blacklist_removed.bed.narrowPeak.encode.bed"
# hnRNPL_ENCSR795CAI_negative_filename = "560_01.basedon_560_01.peaks.l2inputnormnew.bed.compressed.bed.narrowPeak.encode_no_random.bed"
# hnRNPL_ENCSR795CAI_output_filename = "hnRNPL_ENCSR795CAI_raw_bed_file.bed"
# prepare_bed_file(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_positive_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_negative_filename
#                  , hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_output_filename, num_of_positive_samples=2000, shuffle=True)





# SRSF1_ENCSR432XUP_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR432XUP\\"
# SRSF1_ENCSR432XUP_bed_filename = "SRSF1_ENCSR432XUP_raw_bed_file.bed"
# SRSF1_ENCSR432XUP_fasta_filename = "SRSF1_ENCSR432XUP_raw_fasta_file.fasta"
# SRSF1_ENCSR432XUP_output_filename = "SRSF1_ENCSR432XUP_dataset.txt"
# prepare_data(SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_bed_filename, SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_fasta_filename,
#              SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_output_filename)
#
#
# SRSF1_ENCSR321PWZ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR321PWZ\\"
# SRSF1_ENCSR321PWZ_bed_filename = "SRSF1_ENCSR321PWZ_raw_bed_file.bed"
# SRSF1_ENCSR321PWZ_fasta_filename = "SRSF1_ENCSR321PWZ_raw_fasta_file.fasta"
# SRSF1_ENCSR321PWZ_output_filename = "SRSF1_ENCSR321PWZ_dataset.txt"
# prepare_data(SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_bed_filename, SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_fasta_filename,
#              SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_output_filename)
#
#
# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
# PUM2_ENCSR661ICQ_bed_filename = "PUM2_ENCSR661ICQ_raw_bed_file.bed"
# PUM2_ENCSR661ICQ_fasta_filename = "PUM2_ENCSR661ICQ_raw_fasta_file.fasta"
# PUM2_ENCSR661ICQ_output_filename = "PUM2_ENCSR661ICQ_dataset.txt"
# prepare_data(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_bed_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_fasta_filename,
#              PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_output_filename)
#
#
# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
# QKI_ENCSR366YOG_bed_filename = "QKI_ENCSR366YOG_raw_bed_file.bed"
# QKI_ENCSR366YOG_fasta_filename = "QKI_ENCSR366YOG_raw_fasta_file.fasta"
# QKI_ENCSR366YOG_output_filename = "QKI_ENCSR366YOG_dataset.txt"
# prepare_data(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_bed_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_fasta_filename,
#              QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_output_filename)
#
#
# QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\"
# QKI_ENCSR570WLM_bed_filename = "QKI_ENCSR570WLM_raw_bed_file.bed"
# QKI_ENCSR570WLM_fasta_filename = "QKI_ENCSR570WLM_raw_fasta_file.fasta"
# QKI_ENCSR570WLM_output_filename = "QKI_ENCSR570WLM_dataset.txt"
# prepare_data(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_bed_filename, QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_fasta_filename,
#              QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_output_filename)
#
#
# RBM5_ENCSR489ABS_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\RBM5\\ENCSR489ABS\\"
# RBM5_ENCSR489ABS_bed_filename = "RBM5_ENCSR489ABS_raw_bed_file.bed"
# RBM5_ENCSR489ABS_fasta_filename = "RBM5_ENCSR489ABS_raw_fasta_file.fasta"
# RBM5_ENCSR489ABS_output_filename = "RBM5_ENCSR489ABS_dataset.txt"
# prepare_data(RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_bed_filename, RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_fasta_filename,
#              RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_output_filename)
#
#
# hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\"
# hnRNPL_ENCSR724RDN_bed_filename = "hnRNPL_ENCSR724RDN_raw_bed_file.bed"
# hnRNPL_ENCSR724RDN_fasta_filename = "hnRNPL_ENCSR724RDN_raw_fasta_file.fasta"
# hnRNPL_ENCSR724RDN_output_filename = "hnRNPL_ENCSR724RDN_dataset.txt"
# prepare_data(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_bed_filename, hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_fasta_filename,
#              hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_output_filename)
#
#
# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
# hnRNPL_ENCSR795CAI_bed_filename = "hnRNPL_ENCSR795CAI_raw_bed_file.bed"
# hnRNPL_ENCSR795CAI_fasta_filename = "hnRNPL_ENCSR795CAI_raw_fasta_file.fasta"
# hnRNPL_ENCSR795CAI_output_filename = "hnRNPL_ENCSR795CAI_dataset.txt"
# prepare_data(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_bed_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_fasta_filename,
#              hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_output_filename)


# SRSF1_ENCSR432XUP_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR432XUP\\"
# SRSF1_ENCSR432XUP_ds_input_filename = "SRSF1_ENCSR432XUP_dataset.txt"
# SRSF1_ENCSR432XUP_bed_input_filename = "SRSF1_ENCSR432XUP_raw_bed_file.bed"
# SRSF1_ENCSR432XUP_rbp_input_filename = "SRSF1_ENCSR432XUP_RBPmap_no_conservation.txt"
# SRSF1_ENCSR432XUP_rbp_output_filename = "SRSF1_ENCSR432XUP_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_rbp_input_filename,
#                       SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_ds_input_filename,
#                       SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_bed_input_filename,
#                       SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_rbp_output_filename)
# SRSF1_ENCSR432XUP_rbp_input_filename = "SRSF1_ENCSR432XUP_RBPmap_with_conservation.txt"
# SRSF1_ENCSR432XUP_rbp_output_filename = "SRSF1_ENCSR432XUP_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_rbp_input_filename,
#                       SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_ds_input_filename,
#                       SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_bed_input_filename,
#                       SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_rbp_output_filename)
#
# SRSF1_ENCSR321PWZ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR321PWZ\\"
# SRSF1_ENCSR321PWZ_ds_input_filename = "SRSF1_ENCSR321PWZ_dataset.txt"
# SRSF1_ENCSR321PWZ_bed_input_filename = "SRSF1_ENCSR321PWZ_raw_bed_file.bed"
# SRSF1_ENCSR321PWZ_rbp_input_filename = "SRSF1_ENCSR321PWZ_RBPmap_no_conservation.txt"
# SRSF1_ENCSR321PWZ_rbp_output_filename = "SRSF1_ENCSR321PWZ_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_rbp_input_filename,
#                       SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_ds_input_filename,
#                       SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_bed_input_filename,
#                       SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_rbp_output_filename)
# SRSF1_ENCSR321PWZ_rbp_input_filename = "SRSF1_ENCSR321PWZ_RBPmap_with_conservation.txt"
# SRSF1_ENCSR321PWZ_rbp_output_filename = "SRSF1_ENCSR321PWZ_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_rbp_input_filename,
#                       SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_ds_input_filename,
#                       SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_bed_input_filename,
#                       SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_rbp_output_filename)
#
# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
# PUM2_ENCSR661ICQ_ds_input_filename = "PUM2_ENCSR661ICQ_dataset.txt"
# PUM2_ENCSR661ICQ_bed_input_filename = "PUM2_ENCSR661ICQ_raw_bed_file.bed"
# PUM2_ENCSR661ICQ_rbp_input_filename = "PUM2_ENCSR661ICQ_RBPmap_no_conservation.txt"
# PUM2_ENCSR661ICQ_rbp_output_filename = "PUM2_ENCSR661ICQ_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_rbp_input_filename,
#                       PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_ds_input_filename,
#                       PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_bed_input_filename,
#                       PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_rbp_output_filename)
# PUM2_ENCSR661ICQ_rbp_input_filename = "PUM2_ENCSR661ICQ_RBPmap_with_conservation.txt"
# PUM2_ENCSR661ICQ_rbp_output_filename = "PUM2_ENCSR661ICQ_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_rbp_input_filename,
#                       PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_ds_input_filename,
#                       PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_bed_input_filename,
#                       PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_rbp_output_filename)
#
# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
# QKI_ENCSR366YOG_ds_input_filename = "QKI_ENCSR366YOG_dataset.txt"
# QKI_ENCSR366YOG_bed_input_filename = "QKI_ENCSR366YOG_raw_bed_file.bed"
# QKI_ENCSR366YOG_rbp_input_filename = "QKI_ENCSR366YOG_RBPmap_no_conservation.txt"
# QKI_ENCSR366YOG_rbp_output_filename = "QKI_ENCSR366YOG_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_rbp_input_filename,
#                       QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_ds_input_filename,
#                       QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_bed_input_filename,
#                       QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_rbp_output_filename)
# QKI_ENCSR366YOG_rbp_input_filename = "QKI_ENCSR366YOG_RBPmap_with_conservation.txt"
# QKI_ENCSR366YOG_rbp_output_filename = "QKI_ENCSR366YOG_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_rbp_input_filename,
#                       QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_ds_input_filename,
#                       QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_bed_input_filename,
#                       QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_rbp_output_filename)
#
# QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\"
# QKI_ENCSR570WLM_ds_input_filename = "QKI_ENCSR570WLM_dataset.txt"
# QKI_ENCSR570WLM_bed_input_filename = "QKI_ENCSR570WLM_raw_bed_file.bed"
# QKI_ENCSR570WLM_rbp_input_filename = "QKI_ENCSR570WLM_RBPmap_no_conservation.txt"
# QKI_ENCSR570WLM_rbp_output_filename = "QKI_ENCSR570WLM_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_rbp_input_filename,
#                       QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_ds_input_filename,
#                       QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_bed_input_filename,
#                       QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_rbp_output_filename)
# QKI_ENCSR570WLM_rbp_input_filename = "QKI_ENCSR570WLM_RBPmap_with_conservation.txt"
# QKI_ENCSR570WLM_rbp_output_filename = "QKI_ENCSR570WLM_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_rbp_input_filename,
#                       QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_ds_input_filename,
#                       QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_bed_input_filename,
#                       QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_rbp_output_filename)
#
# RBM5_ENCSR489ABS_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\RBM5\\ENCSR489ABS\\"
# RBM5_ENCSR489ABS_ds_input_filename = "RBM5_ENCSR489ABS_dataset.txt"
# RBM5_ENCSR489ABS_bed_input_filename = "RBM5_ENCSR489ABS_raw_bed_file.bed"
# RBM5_ENCSR489ABS_rbp_input_filename = "RBM5_ENCSR489ABS_RBPmap_no_conservation.txt"
# RBM5_ENCSR489ABS_rbp_output_filename = "RBM5_ENCSR489ABS_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_rbp_input_filename,
#                       RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_ds_input_filename,
#                       RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_bed_input_filename,
#                       RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_rbp_output_filename)
# RBM5_ENCSR489ABS_rbp_input_filename = "RBM5_ENCSR489ABS_RBPmap_with_conservation.txt"
# RBM5_ENCSR489ABS_rbp_output_filename = "RBM5_ENCSR489ABS_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_rbp_input_filename,
#                       RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_ds_input_filename,
#                       RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_bed_input_filename,
#                       RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_rbp_output_filename)
#
# hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\"
# hnRNPL_ENCSR724RDN_ds_input_filename = "hnRNPL_ENCSR724RDN_dataset.txt"
# hnRNPL_ENCSR724RDN_bed_input_filename = "hnRNPL_ENCSR724RDN_raw_bed_file.bed"
# hnRNPL_ENCSR724RDN_rbp_input_filename = "hnRNPL_ENCSR724RDN_RBPmap_no_conservation.txt"
# hnRNPL_ENCSR724RDN_rbp_output_filename = "hnRNPL_ENCSR724RDN_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_rbp_input_filename,
#                       hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_ds_input_filename,
#                       hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_bed_input_filename,
#                       hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_rbp_output_filename)
# hnRNPL_ENCSR724RDN_rbp_input_filename = "hnRNPL_ENCSR724RDN_RBPmap_with_conservation.txt"
# hnRNPL_ENCSR724RDN_rbp_output_filename = "hnRNPL_ENCSR724RDN_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_rbp_input_filename,
#                       hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_ds_input_filename,
#                       hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_bed_input_filename,
#                       hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_rbp_output_filename)
#
# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
# hnRNPL_ENCSR795CAI_ds_input_filename = "hnRNPL_ENCSR795CAI_dataset.txt"
# hnRNPL_ENCSR795CAI_bed_input_filename = "hnRNPL_ENCSR795CAI_raw_bed_file.bed"
# hnRNPL_ENCSR795CAI_rbp_input_filename = "hnRNPL_ENCSR795CAI_RBPmap_no_conservation.txt"
# hnRNPL_ENCSR795CAI_rbp_output_filename = "hnRNPL_ENCSR795CAI_rbp_predictions_no_conservation.txt"
# label_rbp_map_results(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_rbp_input_filename,
#                       hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_ds_input_filename,
#                       hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_bed_input_filename,
#                       hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_rbp_output_filename)
# hnRNPL_ENCSR795CAI_rbp_input_filename = "hnRNPL_ENCSR795CAI_RBPmap_with_conservation.txt"
# hnRNPL_ENCSR795CAI_rbp_output_filename = "hnRNPL_ENCSR795CAI_rbp_predictions_with_conservation.txt"
# label_rbp_map_results(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_rbp_input_filename,
#                       hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_ds_input_filename,
#                       hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_bed_input_filename,
#                       hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_rbp_output_filename)


# SRSF1_ENCSR432XUP_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR432XUP\\"
# SRSF1_ENCSR432XUP_ds_input_filename = "SRSF1_ENCSR432XUP_dataset.txt"
# SRSF1_ENCSR432XUP_output_filename_1 = "SRSF1_ENCSR432XUP_dataset_all_uppercase.txt"
# SRSF1_ENCSR432XUP_output_filename_2 = "SRSF1_ENCSR432XUP_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_ds_input_filename, SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_output_filename_1)
# classify_file_uppercase_lowercase(SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_ds_input_filename, SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_output_filename_2)
#
# SRSF1_ENCSR321PWZ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR321PWZ\\"
# SRSF1_ENCSR321PWZ_ds_input_filename = "SRSF1_ENCSR321PWZ_dataset.txt"
# SRSF1_ENCSR321PWZ_output_filename_1 = "SRSF1_ENCSR321PWZ_dataset_all_uppercase.txt"
# SRSF1_ENCSR321PWZ_output_filename_2 = "SRSF1_ENCSR321PWZ_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_ds_input_filename, SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_output_filename_1)
# classify_file_uppercase_lowercase(SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_ds_input_filename, SRSF1_ENCSR321PWZ_path+SRSF1_ENCSR321PWZ_output_filename_2)
#
#
# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
# PUM2_ENCSR661ICQ_ds_input_filename = "PUM2_ENCSR661ICQ_dataset.txt"
# PUM2_ENCSR661ICQ_output_filename_1 = "PUM2_ENCSR661ICQ_dataset_all_uppercase.txt"
# PUM2_ENCSR661ICQ_output_filename_2 = "PUM2_ENCSR661ICQ_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_ds_input_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_output_filename_1)
# classify_file_uppercase_lowercase(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_ds_input_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_output_filename_2)
#
#
# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
# QKI_ENCSR366YOG_ds_input_filename = "QKI_ENCSR366YOG_dataset.txt"
# QKI_ENCSR366YOG_output_filename_1 = "QKI_ENCSR366YOG_dataset_all_uppercase.txt"
# QKI_ENCSR366YOG_output_filename_2 = "QKI_ENCSR366YOG_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_ds_input_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_output_filename_1)
# classify_file_uppercase_lowercase(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_ds_input_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_output_filename_2)
#
# QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\"
# QKI_ENCSR570WLM_ds_input_filename = "QKI_ENCSR570WLM_dataset.txt"
# QKI_ENCSR570WLM_output_filename_1 = "QKI_ENCSR570WLM_dataset_all_uppercase.txt"
# QKI_ENCSR570WLM_output_filename_2 = "QKI_ENCSR570WLM_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_ds_input_filename, QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_output_filename_1)
# classify_file_uppercase_lowercase(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_ds_input_filename, QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_output_filename_2)
#
#
# RBM5_ENCSR489ABS_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\RBM5\\ENCSR489ABS\\"
# RBM5_ENCSR489ABS_ds_input_filename = "RBM5_ENCSR489ABS_dataset.txt"
# RBM5_ENCSR489ABS_output_filename_1 = "RBM5_ENCSR489ABS_dataset_all_uppercase.txt"
# RBM5_ENCSR489ABS_output_filename_2 = "RBM5_ENCSR489ABS_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_ds_input_filename, RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_output_filename_1)
# classify_file_uppercase_lowercase(RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_ds_input_filename, RBM5_ENCSR489ABS_path+RBM5_ENCSR489ABS_output_filename_2)
#
#
# hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\"
# hnRNPL_ENCSR724RDN_ds_input_filename = "hnRNPL_ENCSR724RDN_dataset.txt"
# hnRNPL_ENCSR724RDN_output_filename_1 = "hnRNPL_ENCSR724RDN_dataset_all_uppercase.txt"
# hnRNPL_ENCSR724RDN_output_filename_2 = "hnRNPL_ENCSR724RDN_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_ds_input_filename, hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_output_filename_1)
# classify_file_uppercase_lowercase(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_ds_input_filename, hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_output_filename_2)
#
# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
# hnRNPL_ENCSR795CAI_ds_input_filename = "hnRNPL_ENCSR795CAI_dataset.txt"
# hnRNPL_ENCSR795CAI_output_filename_1 = "hnRNPL_ENCSR795CAI_dataset_all_uppercase.txt"
# hnRNPL_ENCSR795CAI_output_filename_2 = "hnRNPL_ENCSR795CAI_dataset_classify_uppercase_lowercase.txt"
# make_file_uppercase(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_ds_input_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_output_filename_1)
# classify_file_uppercase_lowercase(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_ds_input_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_output_filename_2)


# SRSF1_ENCSR432XUP_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\SRSF1\\ENCSR432XUP\\"
# SRSF1_ENCSR432XUP_ds_input_filename = "SRSF1_ENCSR432XUP_dataset_all_uppercase.txt"
# SRSF1_ENCSR432XUP_secondary_structure_filename = "SRSF1_ENCSR432XUP_secondary_struct.txt"
# SRSF1_ENCSR432XUP_output_filename = "SRSF1_ENCSR432XUP_dataset_secondary_structure.txt"
# add_secondary_structure(SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_ds_input_filename, SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_secondary_structure_filename
#                         , SRSF1_ENCSR432XUP_path+SRSF1_ENCSR432XUP_output_filename)
#
# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
# PUM2_ENCSR661ICQ_ds_input_filename = "PUM2_ENCSR661ICQ_dataset_all_uppercase.txt"
# PUM2_ENCSR661ICQ_secondary_structure_filename = "PUM2_ENCSR661ICQ_secondary_struct.txt"
# PUM2_ENCSR661ICQ_output_filename = "PUM2_ENCSR661ICQ_dataset_secondary_structure.txt"
# add_secondary_structure(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_ds_input_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_secondary_structure_filename
#                         , PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_output_filename)
#
# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
# QKI_ENCSR366YOG_ds_input_filename = "QKI_ENCSR366YOG_dataset_all_uppercase.txt"
# QKI_ENCSR366YOG_secondary_structure_filename = "QKI_ENCSR366YOG_secondary_struct.txt"
# QKI_ENCSR366YOG_output_filename = "QKI_ENCSR366YOG_dataset_secondary_structure.txt"
# add_secondary_structure(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_ds_input_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_secondary_structure_filename
#                         , QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_output_filename)
#
# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
# hnRNPL_ENCSR795CAI_ds_input_filename = "hnRNPL_ENCSR795CAI_dataset_all_uppercase.txt"
# hnRNPL_ENCSR795CAI_secondary_structure_filename = "hnRNPL_ENCSR795CAI_secondary_struct.txt"
# hnRNPL_ENCSR795CAI_output_filename = "hnRNPL_ENCSR795CAI_dataset_secondary_structure.txt"
# add_secondary_structure(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_ds_input_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_secondary_structure_filename
#                         , hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_output_filename)


# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
# PUM2_ENCSR661ICQ_ds_input_filename = "PUM2_ENCSR661ICQ_test_ds.txt"
# PUM2_ENCSR661ICQ_ds_output_filename = "PUM2_ENCSR661ICQ_ds_test_fasta_format.txt"
# format_file_to_fasta(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_ds_input_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_ds_output_filename)

# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
# PUM2_ENCSR661ICQ_rbp_filename = "PUM2_ENCSR661ICQ_test_RBPmap_results.txt"
# PUM2_ENCSR661ICQ_labels_filename = "PUM2_ENCSR661ICQ_test_SVM_predictions.txt"
# PUM2_ENCSR661ICQ_name = "PUM2 ENCSR661ICQ"
# calc_seq_motif_avg_location_by_label(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_rbp_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_labels_filename, PUM2_ENCSR661ICQ_name)

# hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\"
# hnRNPL_ENCSR724RDN_ds_input_filename = "hnRNPL_ENCSR724RDN_test_ds.txt"
# hnRNPL_ENCSR724RDN_ds_output_filename = "hnRNPL_ENCSR724RDN_ds_test_fasta_format.txt"
# format_file_to_fasta(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_ds_input_filename, hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_ds_output_filename)

# hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\"
# hnRNPL_ENCSR724RDN_rbp_filename = "hnRNPL_ENCSR724RDN_test_RBPmap_results.txt"
# hnRNPL_ENCSR724RDN_labels_filename = "hnRNPL_ENCSR724RDN_test_SVM_predictions.txt"
# hnRNPL_ENCSR724RDN_name = "hnRNPL ENCSR724RDN"
# calc_seq_motif_avg_location_by_label(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_rbp_filename, hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_labels_filename,
#                                       hnRNPL_ENCSR724RDN_name)

# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
# hnRNPL_ENCSR795CAI_ds_input_filename = "hnRNPL_ENCSR795CAI_test_ds.txt"
# hnRNPL_ENCSR795CAI_ds_output_filename = "hnRNPL_ENCSR795CAI_ds_test_fasta_format.txt"
# format_file_to_fasta(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_ds_input_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_ds_output_filename)

# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
# hnRNPL_ENCSR795CAI_rbp_filename = "hnRNPL_ENCSR795CAI_test_RBPmap_results.txt"
# hnRNPL_ENCSR795CAI_labels_filename = "hnRNPL_ENCSR795CAI_test_SVM_predictions.txt"
# hnRNPL_ENCSR795CAI_name = "hnRNPL ENCSR795CAI"
# calc_seq_motif_avg_location_by_label(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_rbp_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_labels_filename,
#                                       hnRNPL_ENCSR795CAI_name)

# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
# QKI_ENCSR366YOG_ds_input_filename = "QKI_ENCSR366YOG_test_ds.txt"
# QKI_ENCSR366YOG_ds_output_filename = "QKI_ENCSR366YOG_ds_test_fasta_format.txt"
# format_file_to_fasta(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_ds_input_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_ds_output_filename)

# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
# QKI_ENCSR366YOG_rbp_filename = "QKI_ENCSR366YOG_test_RBPmap_results.txt"
# QKI_ENCSR366YOG_labels_filename = "QKI_ENCSR366YOG_test_SVM_predictions.txt"
# QKI_ENCSR366YOG_name = "QKI ENCSR366YOG"
# calc_seq_motif_avg_location_by_label(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_rbp_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_labels_filename,
#                                       QKI_ENCSR366YOG_name)

# QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\"
# QKI_ENCSR570WLM_ds_input_filename = "QKI_ENCSR570WLM_test_ds.txt"
# QKI_ENCSR570WLM_ds_output_filename = "QKI_ENCSR570WLM_ds_test_fasta_format.txt"
# format_file_to_fasta(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_ds_input_filename, QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_ds_output_filename)

# QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\"
# QKI_ENCSR570WLM_rbp_filename = "QKI_ENCSR570WLM_test_RBPmap_results.txt"
# QKI_ENCSR570WLM_labels_filename = "QKI_ENCSR570WLM_test_SVM_predictions.txt"
# QKI_ENCSR570WLM_name = "QKI ENCSR570WLM"
# calc_seq_motif_avg_location_by_label(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_rbp_filename, QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_labels_filename,
#                                       QKI_ENCSR570WLM_name)


PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
PUM2_ENCSR661ICQ_rbp_filename = "PUM2_ENCSR661ICQ_RBPmap_with_conservation.txt"
PUM2_ENCSR661ICQ_labels_filename = "PUM2_ENCSR661ICQ_ds_SVM_predictions.txt"
PUM2_ENCSR661ICQ_name = "PUM2 ENCSR661ICQ"
calc_seq_motif_avg_location_by_label(PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_rbp_filename, PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_labels_filename, PUM2_ENCSR661ICQ_name)


QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
QKI_ENCSR366YOG_rbp_filename = "QKI_ENCSR366YOG_RBPmap_with_conservation.txt"
QKI_ENCSR366YOG_labels_filename = "QKI_ENCSR366YOG_ds_SVM_predictions.txt"
QKI_ENCSR366YOG_name = "QKI ENCSR366YOG"
calc_seq_motif_avg_location_by_label(QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_rbp_filename, QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_labels_filename,
                                      QKI_ENCSR366YOG_name)


QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\"
QKI_ENCSR570WLM_rbp_filename = "QKI_ENCSR570WLM_RBPmap_with_conservation.txt"
QKI_ENCSR570WLM_labels_filename = "QKI_ENCSR570WLM_ds_SVM_predictions.txt"
QKI_ENCSR570WLM_name = "QKI ENCSR570WLM"
calc_seq_motif_avg_location_by_label(QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_rbp_filename, QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_labels_filename,
                                      QKI_ENCSR570WLM_name)


hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\"
hnRNPL_ENCSR724RDN_rbp_filename = "hnRNPL_ENCSR724RDN_RBPmap_with_conservation.txt"
hnRNPL_ENCSR724RDN_labels_filename = "hnRNPL_ENCSR724RDN_ds_SVM_predictions.txt"
hnRNPL_ENCSR724RDN_name = "hnRNPL ENCSR724RDN"
calc_seq_motif_avg_location_by_label(hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_rbp_filename, hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_labels_filename,
                                      hnRNPL_ENCSR724RDN_name)

hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
hnRNPL_ENCSR795CAI_rbp_filename = "hnRNPL_ENCSR795CAI_RBPmap_with_conservation.txt"
hnRNPL_ENCSR795CAI_labels_filename = "hnRNPL_ENCSR795CAI_ds_SVM_predictions.txt"
hnRNPL_ENCSR795CAI_name = "hnRNPL ENCSR795CAI"
calc_seq_motif_avg_location_by_label(hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_rbp_filename, hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_labels_filename,
                                      hnRNPL_ENCSR795CAI_name)

# PUM2_ENCSR661ICQ_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\PUM2\\ENCSR661ICQ\\"
# PUM2_ENCSR661ICQ_rbp_filename = "PUM2_ENCSR661ICQ_RBPmap_with_conservation.txt"
# PUM2_ENCSR661ICQ_secondary_filename = "PUM2_ENCSR661ICQ_dataset_secondary_structure.txt"
# PUM2_ENCSR661ICQ_output_filename = "PUM2_ENCSR661ICQ_dataset_secondary_structure_motif.txt"
# create_dataset_with_secondary_struct_and_motif(rbp_filepath=PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_rbp_filename,
#                                                secondary_sruct_filepath=PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_secondary_filename,
#                                                output_filepath=PUM2_ENCSR661ICQ_path+PUM2_ENCSR661ICQ_output_filename)

# QKI_ENCSR366YOG_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR366YOG\\"
# QKI_ENCSR366YOG_rbp_filename = "QKI_ENCSR366YOG_RBPmap_with_conservation.txt"
# QKI_ENCSR366YOG_secondary_filename = "QKI_ENCSR366YOG_dataset_secondary_structure.txt"
# QKI_ENCSR366YOG_output_filename = "QKI_ENCSR366YOG_dataset_secondary_structure_motif.txt"
# create_dataset_with_secondary_struct_and_motif(rbp_filepath=QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_rbp_filename,
#                                                secondary_sruct_filepath=QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_secondary_filename,
#                                                output_filepath=QKI_ENCSR366YOG_path+QKI_ENCSR366YOG_output_filename)

# hnRNPL_ENCSR795CAI_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR795CAI\\"
# hnRNPL_ENCSR795CAI_rbp_filename = "hnRNPL_ENCSR795CAI_RBPmap_with_conservation.txt"
# hnRNPL_ENCSR795CAI_secondary_filename = "hnRNPL_ENCSR795CAI_dataset_secondary_structure.txt"
# hnRNPL_ENCSR795CAI_output_filename = "hnRNPL_ENCSR795CAI_dataset_secondary_structure_motif.txt"
# create_dataset_with_secondary_struct_and_motif(rbp_filepath=hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_rbp_filename,
#                                                secondary_sruct_filepath=hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_secondary_filename,
#                                                output_filepath=hnRNPL_ENCSR795CAI_path+hnRNPL_ENCSR795CAI_output_filename)

# QKI_ENCSR570WLM_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\QKI\\ENCSR570WLM\\"
# QKI_ENCSR570WLM_rbp_filename = "QKI_ENCSR570WLM_RBPmap_with_conservation.txt"
# QKI_ENCSR570WLM_secondary_filename = "QKI_ENCSR570WLM_dataset_all_uppercase.txt"
# QKI_ENCSR570WLM_output_filename = "QKI_ENCSR570WLM_dataset_motif.txt"
# create_dataset_with_secondary_struct_and_motif(rbp_filepath=QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_rbp_filename,
#                                                secondary_sruct_filepath=QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_secondary_filename,
#                                                output_filepath=QKI_ENCSR570WLM_path+QKI_ENCSR570WLM_output_filename)
#
# hnRNPL_ENCSR724RDN_path = "C:\\Users\\User\\Desktop\\RBPMap\\data\\hnRNPL\\ENCSR724RDN\\"
# hnRNPL_ENCSR724RDN_rbp_filename = "hnRNPL_ENCSR724RDN_RBPmap_with_conservation.txt"
# hnRNPL_ENCSR724RDN_secondary_filename = "hnRNPL_ENCSR724RDN_dataset_all_uppercase.txt"
# hnRNPL_ENCSR724RDN_output_filename = "hnRNPL_ENCSR724RDN_dataset_motif.txt"
# create_dataset_with_secondary_struct_and_motif(rbp_filepath=hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_rbp_filename,
#                                                secondary_sruct_filepath=hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_secondary_filename,
#                                                output_filepath=hnRNPL_ENCSR724RDN_path+hnRNPL_ENCSR724RDN_output_filename)