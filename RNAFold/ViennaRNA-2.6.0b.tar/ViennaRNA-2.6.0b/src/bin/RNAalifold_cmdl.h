/** @file RNAalifold_cmdl.h
 *  @brief The header file for the command line option parser
 *  generated by GNU Gengetopt version 2.23
 *  http://www.gnu.org/software/gengetopt.
 *  DO NOT modify this file, since it can be overwritten
 *  @author GNU Gengetopt */

#ifndef RNAALIFOLD_CMDL_H
#define RNAALIFOLD_CMDL_H

/* If we use autoconf.  */
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <stdio.h> /* for FILE */

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

#ifndef RNAALIFOLD_CMDLINE_PARSER_PACKAGE
/** @brief the program name (used for printing errors) */
#define RNAALIFOLD_CMDLINE_PARSER_PACKAGE "RNAalifold"
#endif

#ifndef RNAALIFOLD_CMDLINE_PARSER_PACKAGE_NAME
/** @brief the complete program name (used for help and version) */
#define RNAALIFOLD_CMDLINE_PARSER_PACKAGE_NAME "RNAalifold"
#endif

#ifndef RNAALIFOLD_CMDLINE_PARSER_VERSION
/** @brief the program version */
#define RNAALIFOLD_CMDLINE_PARSER_VERSION VERSION
#endif

/** @brief Where the command line options are stored */
struct RNAalifold_args_info
{
  const char *help_help; /**< @brief Print help and exit help description.  */
  const char *detailed_help_help; /**< @brief Print help, including all details and hidden options, and exit help description.  */
  const char *full_help_help; /**< @brief Print help, including hidden options, and exit help description.  */
  const char *version_help; /**< @brief Print version and exit help description.  */
  int verbose_flag;	/**< @brief Be verbose.
  
 (default=off).  */
  const char *verbose_help; /**< @brief Be verbose.
  
 help description.  */
  int quiet_flag;	/**< @brief Be quiet.
 (default=off).  */
  const char *quiet_help; /**< @brief Be quiet.
 help description.  */
  int jobs_arg;	/**< @brief Split batch input into jobs and start processing in parallel using multiple threads. A value of 0 indicates to use as many parallel threads as computation cores are available.
 (default='0').  */
  char * jobs_orig;	/**< @brief Split batch input into jobs and start processing in parallel using multiple threads. A value of 0 indicates to use as many parallel threads as computation cores are available.
 original value given at command line.  */
  const char *jobs_help; /**< @brief Split batch input into jobs and start processing in parallel using multiple threads. A value of 0 indicates to use as many parallel threads as computation cores are available.
 help description.  */
  int unordered_flag;	/**< @brief Do not try to keep output in order with input while parallel processing is in place.
 (default=off).  */
  const char *unordered_help; /**< @brief Do not try to keep output in order with input while parallel processing is in place.
 help description.  */
  int noconv_flag;	/**< @brief Do not automatically substitute nucleotide \"T\" with \"U\"
  
 (default=off).  */
  const char *noconv_help; /**< @brief Do not automatically substitute nucleotide \"T\" with \"U\"
  
 help description.  */
  int color_flag;	/**< @brief Produce a colored version of the consensus structure plot \"alirna.ps\" (default b&w only)
  
 (default=off).  */
  const char *color_help; /**< @brief Produce a colored version of the consensus structure plot \"alirna.ps\" (default b&w only)
  
 help description.  */
  int aln_flag;	/**< @brief Produce a colored and structure annotated alignment in PostScript format in the file \"aln.ps\" in the current directory.
  
 (default=off).  */
  const char *aln_help; /**< @brief Produce a colored and structure annotated alignment in PostScript format in the file \"aln.ps\" in the current directory.
  
 help description.  */
  int aln_EPS_cols_arg;	/**< @brief Number of columns in colored EPS alignment output.
 (default='60').  */
  char * aln_EPS_cols_orig;	/**< @brief Number of columns in colored EPS alignment output.
 original value given at command line.  */
  const char *aln_EPS_cols_help; /**< @brief Number of columns in colored EPS alignment output.
 help description.  */
  char * aln_stk_arg;	/**< @brief Create a multi-Stockholm formatted output file.
 (default='RNAalifold_results').  */
  char * aln_stk_orig;	/**< @brief Create a multi-Stockholm formatted output file.
 original value given at command line.  */
  const char *aln_stk_help; /**< @brief Create a multi-Stockholm formatted output file.
 help description.  */
  int layout_type_arg;	/**< @brief Choose the layout algorithm. Simple radial layout if 0, or naview if 1
  
 (default='1').  */
  char * layout_type_orig;	/**< @brief Choose the layout algorithm. Simple radial layout if 0, or naview if 1
  
 original value given at command line.  */
  const char *layout_type_help; /**< @brief Choose the layout algorithm. Simple radial layout if 0, or naview if 1
  
 help description.  */
  int noPS_flag;	/**< @brief Do not produce postscript drawing of the mfe structure.
  
 (default=off).  */
  const char *noPS_help; /**< @brief Do not produce postscript drawing of the mfe structure.
  
 help description.  */
  int noDP_flag;	/**< @brief Do not produce dot-plot postscript file containing base pair or stack probabilitities.
 (default=off).  */
  const char *noDP_help; /**< @brief Do not produce dot-plot postscript file containing base pair or stack probabilitities.
 help description.  */
  char * input_format_arg;	/**< @brief File format of the input multiple sequence alignment (MSA).
.  */
  char * input_format_orig;	/**< @brief File format of the input multiple sequence alignment (MSA).
 original value given at command line.  */
  const char *input_format_help; /**< @brief File format of the input multiple sequence alignment (MSA).
 help description.  */
  int continuous_ids_flag;	/**< @brief Use continuous alignment ID numbering when no alignment ID can be retrieved from input data.
 (default=off).  */
  const char *continuous_ids_help; /**< @brief Use continuous alignment ID numbering when no alignment ID can be retrieved from input data.
 help description.  */
  int auto_id_flag;	/**< @brief Automatically generate an ID for each alignment.
 (default=off).  */
  const char *auto_id_help; /**< @brief Automatically generate an ID for each alignment.
 help description.  */
  char * id_prefix_arg;	/**< @brief Prefix for automatically generated IDs (as used in output file names)
  
 (default='alignment').  */
  char * id_prefix_orig;	/**< @brief Prefix for automatically generated IDs (as used in output file names)
  
 original value given at command line.  */
  const char *id_prefix_help; /**< @brief Prefix for automatically generated IDs (as used in output file names)
  
 help description.  */
  char * id_delim_arg;	/**< @brief Change the delimiter between prefix and increasing number for automatically generated IDs (as used in output file names)
  
 (default='_').  */
  char * id_delim_orig;	/**< @brief Change the delimiter between prefix and increasing number for automatically generated IDs (as used in output file names)
  
 original value given at command line.  */
  const char *id_delim_help; /**< @brief Change the delimiter between prefix and increasing number for automatically generated IDs (as used in output file names)
  
 help description.  */
  int id_digits_arg;	/**< @brief Specify the number of digits of the counter in automatically generated alignment IDs.
 (default='4').  */
  char * id_digits_orig;	/**< @brief Specify the number of digits of the counter in automatically generated alignment IDs.
 original value given at command line.  */
  const char *id_digits_help; /**< @brief Specify the number of digits of the counter in automatically generated alignment IDs.
 help description.  */
  long id_start_arg;	/**< @brief Specify the first number in automatically generated alignment IDs.
 (default='1').  */
  char * id_start_orig;	/**< @brief Specify the first number in automatically generated alignment IDs.
 original value given at command line.  */
  const char *id_start_help; /**< @brief Specify the first number in automatically generated alignment IDs.
 help description.  */
  char * filename_delim_arg;	/**< @brief Change the delimiting character that is used for sanitized filenames
  
 (default='ID-delimiter').  */
  char * filename_delim_orig;	/**< @brief Change the delimiting character that is used for sanitized filenames
  
 original value given at command line.  */
  const char *filename_delim_help; /**< @brief Change the delimiting character that is used for sanitized filenames
  
 help description.  */
  int maxBPspan_arg;	/**< @brief Set the maximum base pair span
  
 (default='-1').  */
  char * maxBPspan_orig;	/**< @brief Set the maximum base pair span
  
 original value given at command line.  */
  const char *maxBPspan_help; /**< @brief Set the maximum base pair span
  
 help description.  */
  char * constraint_arg;	/**< @brief Calculate structures subject to constraints.
  The constraining structure will be read from 'stdin', the alignment has to be given as a file name on the command line.
 (default='').  */
  char * constraint_orig;	/**< @brief Calculate structures subject to constraints.
  The constraining structure will be read from 'stdin', the alignment has to be given as a file name on the command line.
 original value given at command line.  */
  const char *constraint_help; /**< @brief Calculate structures subject to constraints.
  The constraining structure will be read from 'stdin', the alignment has to be given as a file name on the command line.
 help description.  */
  int batch_flag;	/**< @brief Use constraints for all alignment records.
 (default=off).  */
  const char *batch_help; /**< @brief Use constraints for all alignment records.
 help description.  */
  int enforceConstraint_flag;	/**< @brief Enforce base pairs given by round brackets ( ) in structure constraint
  
 (default=off).  */
  const char *enforceConstraint_help; /**< @brief Enforce base pairs given by round brackets ( ) in structure constraint
  
 help description.  */
  int SS_cons_flag;	/**< @brief Use consensus structures from Stockholm file (#=GF SS_cons) as constraint
 (default=off).  */
  const char *SS_cons_help; /**< @brief Use consensus structures from Stockholm file (#=GF SS_cons) as constraint
 help description.  */
  char ** shape_arg;	/**< @brief Use SHAPE reactivity data to guide structure predictions
.  */
  char ** shape_orig;	/**< @brief Use SHAPE reactivity data to guide structure predictions
 original value given at command line.  */
  unsigned int shape_min; /**< @brief Use SHAPE reactivity data to guide structure predictions
's minimum occurreces */
  unsigned int shape_max; /**< @brief Use SHAPE reactivity data to guide structure predictions
's maximum occurreces */
  const char *shape_help; /**< @brief Use SHAPE reactivity data to guide structure predictions
 help description.  */
  char * shapeMethod_arg;	/**< @brief Specify the method how to convert SHAPE reactivity data to pseudo energy contributions
 (default='D').  */
  char * shapeMethod_orig;	/**< @brief Specify the method how to convert SHAPE reactivity data to pseudo energy contributions
 original value given at command line.  */
  const char *shapeMethod_help; /**< @brief Specify the method how to convert SHAPE reactivity data to pseudo energy contributions
 help description.  */
  int partfunc_arg;	/**< @brief Calculate the partition function and base pairing probability matrix in addition to the mfe structure. Default is calculation of mfe structure only.
 (default='1').  */
  char * partfunc_orig;	/**< @brief Calculate the partition function and base pairing probability matrix in addition to the mfe structure. Default is calculation of mfe structure only.
 original value given at command line.  */
  const char *partfunc_help; /**< @brief Calculate the partition function and base pairing probability matrix in addition to the mfe structure. Default is calculation of mfe structure only.
 help description.  */
  float MEA_arg;	/**< @brief Calculate an MEA (maximum expected accuracy) structure, where the expected accuracy is computed from the pair probabilities: each base pair (i,j) gets a score 2*gamma*p_ij and the score of an unpaired base is given by the probability of not forming a pair.
 (default='1.').  */
  char * MEA_orig;	/**< @brief Calculate an MEA (maximum expected accuracy) structure, where the expected accuracy is computed from the pair probabilities: each base pair (i,j) gets a score 2*gamma*p_ij and the score of an unpaired base is given by the probability of not forming a pair.
 original value given at command line.  */
  const char *MEA_help; /**< @brief Calculate an MEA (maximum expected accuracy) structure, where the expected accuracy is computed from the pair probabilities: each base pair (i,j) gets a score 2*gamma*p_ij and the score of an unpaired base is given by the probability of not forming a pair.
 help description.  */
  int mis_flag;	/**< @brief Output \"most informative sequence\" instead of simple consensus: For each column of the alignment output the set of nucleotides with frequency greater than average in IUPAC notation.
  
 (default=off).  */
  const char *mis_help; /**< @brief Output \"most informative sequence\" instead of simple consensus: For each column of the alignment output the set of nucleotides with frequency greater than average in IUPAC notation.
  
 help description.  */
  int stochBT_arg;	/**< @brief Stochastic backtrack. Compute a certain number of random structures with a probability dependend on the partition function. See -p option in RNAsubopt.
  
.  */
  char * stochBT_orig;	/**< @brief Stochastic backtrack. Compute a certain number of random structures with a probability dependend on the partition function. See -p option in RNAsubopt.
  
 original value given at command line.  */
  const char *stochBT_help; /**< @brief Stochastic backtrack. Compute a certain number of random structures with a probability dependend on the partition function. See -p option in RNAsubopt.
  
 help description.  */
  int stochBT_en_arg;	/**< @brief same as \"-s\" but also print out the energies and probabilities of the backtraced structures.
  
.  */
  char * stochBT_en_orig;	/**< @brief same as \"-s\" but also print out the energies and probabilities of the backtraced structures.
  
 original value given at command line.  */
  const char *stochBT_en_help; /**< @brief same as \"-s\" but also print out the energies and probabilities of the backtraced structures.
  
 help description.  */
  int nonRedundant_flag;	/**< @brief Enable non-redundant sampling strategy.
  
 (default=off).  */
  const char *nonRedundant_help; /**< @brief Enable non-redundant sampling strategy.
  
 help description.  */
  double pfScale_arg;	/**< @brief In the calculation of the pf use scale*mfe as an estimate for the ensemble free energy (used to avoid overflows).
.  */
  char * pfScale_orig;	/**< @brief In the calculation of the pf use scale*mfe as an estimate for the ensemble free energy (used to avoid overflows).
 original value given at command line.  */
  const char *pfScale_help; /**< @brief In the calculation of the pf use scale*mfe as an estimate for the ensemble free energy (used to avoid overflows).
 help description.  */
  int circ_flag;	/**< @brief Assume a circular (instead of linear) RNA molecule.
  
 (default=off).  */
  const char *circ_help; /**< @brief Assume a circular (instead of linear) RNA molecule.
  
 help description.  */
  double bppmThreshold_arg;	/**< @brief Set the threshold for base pair probabilities included in the postscript output
 (default='1e-6').  */
  char * bppmThreshold_orig;	/**< @brief Set the threshold for base pair probabilities included in the postscript output
 original value given at command line.  */
  const char *bppmThreshold_help; /**< @brief Set the threshold for base pair probabilities included in the postscript output
 help description.  */
  int gquad_flag;	/**< @brief Incoorporate G-Quadruplex formation into the structure prediction algorithm.
  
 (default=off).  */
  const char *gquad_help; /**< @brief Incoorporate G-Quadruplex formation into the structure prediction algorithm.
  
 help description.  */
  int sci_flag;	/**< @brief Compute the structure conservation index (SCI) for the MFE consensus structure of the alignment
  
 (default=off).  */
  const char *sci_help; /**< @brief Compute the structure conservation index (SCI) for the MFE consensus structure of the alignment
  
 help description.  */
  double temp_arg;	/**< @brief Rescale energy parameters to a temperature of temp C. Default is 37C.
  
.  */
  char * temp_orig;	/**< @brief Rescale energy parameters to a temperature of temp C. Default is 37C.
  
 original value given at command line.  */
  const char *temp_help; /**< @brief Rescale energy parameters to a temperature of temp C. Default is 37C.
  
 help description.  */
  int noTetra_flag;	/**< @brief Do not include special tabulated stabilizing energies for tri-, tetra- and hexaloop hairpins.
  
 (default=off).  */
  const char *noTetra_help; /**< @brief Do not include special tabulated stabilizing energies for tri-, tetra- and hexaloop hairpins.
  
 help description.  */
  int dangles_arg;	/**< @brief How to treat \"dangling end\" energies for bases adjacent to helices in free ends and multi-loops
 (default='2').  */
  char * dangles_orig;	/**< @brief How to treat \"dangling end\" energies for bases adjacent to helices in free ends and multi-loops
 original value given at command line.  */
  const char *dangles_help; /**< @brief How to treat \"dangling end\" energies for bases adjacent to helices in free ends and multi-loops
 help description.  */
  int noLP_flag;	/**< @brief Produce structures without lonely pairs (helices of length 1).
 (default=off).  */
  const char *noLP_help; /**< @brief Produce structures without lonely pairs (helices of length 1).
 help description.  */
  int noGU_flag;	/**< @brief Do not allow GU pairs
  
 (default=off).  */
  const char *noGU_help; /**< @brief Do not allow GU pairs
  
 help description.  */
  int noClosingGU_flag;	/**< @brief Do not allow GU pairs at the end of helices
  
 (default=off).  */
  const char *noClosingGU_help; /**< @brief Do not allow GU pairs at the end of helices
  
 help description.  */
  double salt_arg;	/**< @brief Set salt concentration in molar (M). Default is 1.021M.
  
.  */
  char * salt_orig;	/**< @brief Set salt concentration in molar (M). Default is 1.021M.
  
 original value given at command line.  */
  const char *salt_help; /**< @brief Set salt concentration in molar (M). Default is 1.021M.
  
 help description.  */
  double cfactor_arg;	/**< @brief Set the weight of the covariance term in the energy function
  
 (default='1.0').  */
  char * cfactor_orig;	/**< @brief Set the weight of the covariance term in the energy function
  
 original value given at command line.  */
  const char *cfactor_help; /**< @brief Set the weight of the covariance term in the energy function
  
 help description.  */
  double nfactor_arg;	/**< @brief Set the penalty for non-compatible sequences in the covariance term of the energy function
  
 (default='1.0').  */
  char * nfactor_orig;	/**< @brief Set the penalty for non-compatible sequences in the covariance term of the energy function
  
 original value given at command line.  */
  const char *nfactor_help; /**< @brief Set the penalty for non-compatible sequences in the covariance term of the energy function
  
 help description.  */
  int endgaps_flag;	/**< @brief Score pairs with endgaps same as gap-gap pairs.
  
 (default=off).  */
  const char *endgaps_help; /**< @brief Score pairs with endgaps same as gap-gap pairs.
  
 help description.  */
  char * ribosum_file_arg;	/**< @brief use specified Ribosum Matrix instead of normal energy model. Matrixes to use should be 6x6 matrices, the order of the terms is AU, CG, GC, GU, UA, UG.
  
.  */
  char * ribosum_file_orig;	/**< @brief use specified Ribosum Matrix instead of normal energy model. Matrixes to use should be 6x6 matrices, the order of the terms is AU, CG, GC, GU, UA, UG.
  
 original value given at command line.  */
  const char *ribosum_file_help; /**< @brief use specified Ribosum Matrix instead of normal energy model. Matrixes to use should be 6x6 matrices, the order of the terms is AU, CG, GC, GU, UA, UG.
  
 help description.  */
  int ribosum_scoring_flag;	/**< @brief use ribosum scoring matrix. The matrix is chosen according to the minimal and maximal pairwise identities of the sequences in the file.
  
 (default=off).  */
  const char *ribosum_scoring_help; /**< @brief use ribosum scoring matrix. The matrix is chosen according to the minimal and maximal pairwise identities of the sequences in the file.
  
 help description.  */
  int old_flag;	/**< @brief use old energy evaluation, treating gaps as characters.
  
 (default=off).  */
  const char *old_help; /**< @brief use old energy evaluation, treating gaps as characters.
  
 help description.  */
  char * paramFile_arg;	/**< @brief Read energy parameters from paramfile, instead of using the default parameter set.
.  */
  char * paramFile_orig;	/**< @brief Read energy parameters from paramfile, instead of using the default parameter set.
 original value given at command line.  */
  const char *paramFile_help; /**< @brief Read energy parameters from paramfile, instead of using the default parameter set.
 help description.  */
  char * nsp_arg;	/**< @brief Allow other pairs in addition to the usual AU,GC,and GU pairs.
.  */
  char * nsp_orig;	/**< @brief Allow other pairs in addition to the usual AU,GC,and GU pairs.
 original value given at command line.  */
  const char *nsp_help; /**< @brief Allow other pairs in addition to the usual AU,GC,and GU pairs.
 help description.  */
  int energyModel_arg;	/**< @brief Rarely used option to fold sequences from the artificial ABCD... alphabet, where A pairs B, C-D etc.  Use the energy parameters for GC (-e 1) or AU (-e 2) pairs.
  
.  */
  char * energyModel_orig;	/**< @brief Rarely used option to fold sequences from the artificial ABCD... alphabet, where A pairs B, C-D etc.  Use the energy parameters for GC (-e 1) or AU (-e 2) pairs.
  
 original value given at command line.  */
  const char *energyModel_help; /**< @brief Rarely used option to fold sequences from the artificial ABCD... alphabet, where A pairs B, C-D etc.  Use the energy parameters for GC (-e 1) or AU (-e 2) pairs.
  
 help description.  */
  double betaScale_arg;	/**< @brief Set the scaling of the Boltzmann factors
 (default='1.').  */
  char * betaScale_orig;	/**< @brief Set the scaling of the Boltzmann factors
 original value given at command line.  */
  const char *betaScale_help; /**< @brief Set the scaling of the Boltzmann factors
 help description.  */
  
  unsigned int help_given ;	/**< @brief Whether help was given.  */
  unsigned int detailed_help_given ;	/**< @brief Whether detailed-help was given.  */
  unsigned int full_help_given ;	/**< @brief Whether full-help was given.  */
  unsigned int version_given ;	/**< @brief Whether version was given.  */
  unsigned int verbose_given ;	/**< @brief Whether verbose was given.  */
  unsigned int quiet_given ;	/**< @brief Whether quiet was given.  */
  unsigned int jobs_given ;	/**< @brief Whether jobs was given.  */
  unsigned int unordered_given ;	/**< @brief Whether unordered was given.  */
  unsigned int noconv_given ;	/**< @brief Whether noconv was given.  */
  unsigned int color_given ;	/**< @brief Whether color was given.  */
  unsigned int aln_given ;	/**< @brief Whether aln was given.  */
  unsigned int aln_EPS_cols_given ;	/**< @brief Whether aln-EPS-cols was given.  */
  unsigned int aln_stk_given ;	/**< @brief Whether aln-stk was given.  */
  unsigned int layout_type_given ;	/**< @brief Whether layout-type was given.  */
  unsigned int noPS_given ;	/**< @brief Whether noPS was given.  */
  unsigned int noDP_given ;	/**< @brief Whether noDP was given.  */
  unsigned int input_format_given ;	/**< @brief Whether input-format was given.  */
  unsigned int continuous_ids_given ;	/**< @brief Whether continuous-ids was given.  */
  unsigned int auto_id_given ;	/**< @brief Whether auto-id was given.  */
  unsigned int id_prefix_given ;	/**< @brief Whether id-prefix was given.  */
  unsigned int id_delim_given ;	/**< @brief Whether id-delim was given.  */
  unsigned int id_digits_given ;	/**< @brief Whether id-digits was given.  */
  unsigned int id_start_given ;	/**< @brief Whether id-start was given.  */
  unsigned int filename_delim_given ;	/**< @brief Whether filename-delim was given.  */
  unsigned int maxBPspan_given ;	/**< @brief Whether maxBPspan was given.  */
  unsigned int constraint_given ;	/**< @brief Whether constraint was given.  */
  unsigned int batch_given ;	/**< @brief Whether batch was given.  */
  unsigned int enforceConstraint_given ;	/**< @brief Whether enforceConstraint was given.  */
  unsigned int SS_cons_given ;	/**< @brief Whether SS_cons was given.  */
  unsigned int shape_given ;	/**< @brief Whether shape was given.  */
  unsigned int shapeMethod_given ;	/**< @brief Whether shapeMethod was given.  */
  unsigned int partfunc_given ;	/**< @brief Whether partfunc was given.  */
  unsigned int MEA_given ;	/**< @brief Whether MEA was given.  */
  unsigned int mis_given ;	/**< @brief Whether mis was given.  */
  unsigned int stochBT_given ;	/**< @brief Whether stochBT was given.  */
  unsigned int stochBT_en_given ;	/**< @brief Whether stochBT_en was given.  */
  unsigned int nonRedundant_given ;	/**< @brief Whether nonRedundant was given.  */
  unsigned int pfScale_given ;	/**< @brief Whether pfScale was given.  */
  unsigned int circ_given ;	/**< @brief Whether circ was given.  */
  unsigned int bppmThreshold_given ;	/**< @brief Whether bppmThreshold was given.  */
  unsigned int gquad_given ;	/**< @brief Whether gquad was given.  */
  unsigned int sci_given ;	/**< @brief Whether sci was given.  */
  unsigned int temp_given ;	/**< @brief Whether temp was given.  */
  unsigned int noTetra_given ;	/**< @brief Whether noTetra was given.  */
  unsigned int dangles_given ;	/**< @brief Whether dangles was given.  */
  unsigned int noLP_given ;	/**< @brief Whether noLP was given.  */
  unsigned int noGU_given ;	/**< @brief Whether noGU was given.  */
  unsigned int noClosingGU_given ;	/**< @brief Whether noClosingGU was given.  */
  unsigned int salt_given ;	/**< @brief Whether salt was given.  */
  unsigned int cfactor_given ;	/**< @brief Whether cfactor was given.  */
  unsigned int nfactor_given ;	/**< @brief Whether nfactor was given.  */
  unsigned int endgaps_given ;	/**< @brief Whether endgaps was given.  */
  unsigned int ribosum_file_given ;	/**< @brief Whether ribosum_file was given.  */
  unsigned int ribosum_scoring_given ;	/**< @brief Whether ribosum_scoring was given.  */
  unsigned int old_given ;	/**< @brief Whether old was given.  */
  unsigned int paramFile_given ;	/**< @brief Whether paramFile was given.  */
  unsigned int nsp_given ;	/**< @brief Whether nsp was given.  */
  unsigned int energyModel_given ;	/**< @brief Whether energyModel was given.  */
  unsigned int betaScale_given ;	/**< @brief Whether betaScale was given.  */

  char **inputs ; /**< @brief unnamed options (options without names) */
  unsigned inputs_num ; /**< @brief unnamed options number */
} ;

/** @brief The additional parameters to pass to parser functions */
struct RNAalifold_cmdline_parser_params
{
  int override; /**< @brief whether to override possibly already present options (default 0) */
  int initialize; /**< @brief whether to initialize the option structure RNAalifold_args_info (default 1) */
  int check_required; /**< @brief whether to check that all required options were provided (default 1) */
  int check_ambiguity; /**< @brief whether to check for options already specified in the option structure RNAalifold_args_info (default 0) */
  int print_errors; /**< @brief whether getopt_long should print an error message for a bad option (default 1) */
} ;

/** @brief the purpose string of the program */
extern const char *RNAalifold_args_info_purpose;
/** @brief the usage string of the program */
extern const char *RNAalifold_args_info_usage;
/** @brief the description string of the program */
extern const char *RNAalifold_args_info_description;
/** @brief all the lines making the help output */
extern const char *RNAalifold_args_info_help[];
/** @brief all the lines making the full help output (including hidden options) */
extern const char *RNAalifold_args_info_full_help[];
/** @brief all the lines making the detailed help output (including hidden options and details) */
extern const char *RNAalifold_args_info_detailed_help[];

/**
 * The command line parser
 * @param argc the number of command line options
 * @param argv the command line options
 * @param args_info the structure where option information will be stored
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNAalifold_cmdline_parser (int argc, char **argv,
  struct RNAalifold_args_info *args_info);

/**
 * The command line parser (version with additional parameters - deprecated)
 * @param argc the number of command line options
 * @param argv the command line options
 * @param args_info the structure where option information will be stored
 * @param override whether to override possibly already present options
 * @param initialize whether to initialize the option structure my_args_info
 * @param check_required whether to check that all required options were provided
 * @return 0 if everything went fine, NON 0 if an error took place
 * @deprecated use RNAalifold_cmdline_parser_ext() instead
 */
int RNAalifold_cmdline_parser2 (int argc, char **argv,
  struct RNAalifold_args_info *args_info,
  int override, int initialize, int check_required);

/**
 * The command line parser (version with additional parameters)
 * @param argc the number of command line options
 * @param argv the command line options
 * @param args_info the structure where option information will be stored
 * @param params additional parameters for the parser
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNAalifold_cmdline_parser_ext (int argc, char **argv,
  struct RNAalifold_args_info *args_info,
  struct RNAalifold_cmdline_parser_params *params);

/**
 * Save the contents of the option struct into an already open FILE stream.
 * @param outfile the stream where to dump options
 * @param args_info the option struct to dump
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNAalifold_cmdline_parser_dump(FILE *outfile,
  struct RNAalifold_args_info *args_info);

/**
 * Save the contents of the option struct into a (text) file.
 * This file can be read by the config file parser (if generated by gengetopt)
 * @param filename the file where to save
 * @param args_info the option struct to save
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNAalifold_cmdline_parser_file_save(const char *filename,
  struct RNAalifold_args_info *args_info);

/**
 * Print the help
 */
void RNAalifold_cmdline_parser_print_help(void);
/**
 * Print the full help (including hidden options)
 */
void RNAalifold_cmdline_parser_print_full_help(void);
/**
 * Print the detailed help (including hidden options and details)
 */
void RNAalifold_cmdline_parser_print_detailed_help(void);
/**
 * Print the version
 */
void RNAalifold_cmdline_parser_print_version(void);

/**
 * Initializes all the fields a RNAalifold_cmdline_parser_params structure 
 * to their default values
 * @param params the structure to initialize
 */
void RNAalifold_cmdline_parser_params_init(struct RNAalifold_cmdline_parser_params *params);

/**
 * Allocates dynamically a RNAalifold_cmdline_parser_params structure and initializes
 * all its fields to their default values
 * @return the created and initialized RNAalifold_cmdline_parser_params structure
 */
struct RNAalifold_cmdline_parser_params *RNAalifold_cmdline_parser_params_create(void);

/**
 * Initializes the passed RNAalifold_args_info structure's fields
 * (also set default values for options that have a default)
 * @param args_info the structure to initialize
 */
void RNAalifold_cmdline_parser_init (struct RNAalifold_args_info *args_info);
/**
 * Deallocates the string fields of the RNAalifold_args_info structure
 * (but does not deallocate the structure itself)
 * @param args_info the structure to deallocate
 */
void RNAalifold_cmdline_parser_free (struct RNAalifold_args_info *args_info);

/**
 * Checks that all the required options were specified
 * @param args_info the structure to check
 * @param prog_name the name of the program that will be used to print
 *   possible errors
 * @return
 */
int RNAalifold_cmdline_parser_required (struct RNAalifold_args_info *args_info,
  const char *prog_name);


#ifdef __cplusplus
}
#endif /* __cplusplus */
#endif /* RNAALIFOLD_CMDL_H */
