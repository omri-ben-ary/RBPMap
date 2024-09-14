/** @file RNALalifold_cmdl.h
 *  @brief The header file for the command line option parser
 *  generated by GNU Gengetopt version 2.23
 *  http://www.gnu.org/software/gengetopt.
 *  DO NOT modify this file, since it can be overwritten
 *  @author GNU Gengetopt */

#ifndef RNALALIFOLD_CMDL_H
#define RNALALIFOLD_CMDL_H

/* If we use autoconf.  */
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <stdio.h> /* for FILE */

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

#ifndef RNALALIFOLD_CMDLINE_PARSER_PACKAGE
/** @brief the program name (used for printing errors) */
#define RNALALIFOLD_CMDLINE_PARSER_PACKAGE "RNALalifold"
#endif

#ifndef RNALALIFOLD_CMDLINE_PARSER_PACKAGE_NAME
/** @brief the complete program name (used for help and version) */
#define RNALALIFOLD_CMDLINE_PARSER_PACKAGE_NAME "RNALalifold"
#endif

#ifndef RNALALIFOLD_CMDLINE_PARSER_VERSION
/** @brief the program version */
#define RNALALIFOLD_CMDLINE_PARSER_VERSION VERSION
#endif

/** @brief Where the command line options are stored */
struct RNALalifold_args_info
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
  int noconv_flag;	/**< @brief Do not automatically substitute nucleotide \"T\" with \"U\"
  
 (default=off).  */
  const char *noconv_help; /**< @brief Do not automatically substitute nucleotide \"T\" with \"U\"
  
 help description.  */
  char * input_format_arg;	/**< @brief File format of the input multiple sequence alignment (MSA).
.  */
  char * input_format_orig;	/**< @brief File format of the input multiple sequence alignment (MSA).
 original value given at command line.  */
  const char *input_format_help; /**< @brief File format of the input multiple sequence alignment (MSA).
 help description.  */
  int csv_flag;	/**< @brief Create comma separated output (csv)
  
 (default=off).  */
  const char *csv_help; /**< @brief Create comma separated output (csv)
  
 help description.  */
  char * aln_arg;	/**< @brief Produce output alignments and secondary structure plots for each hit found.
.  */
  char * aln_orig;	/**< @brief Produce output alignments and secondary structure plots for each hit found.
 original value given at command line.  */
  const char *aln_help; /**< @brief Produce output alignments and secondary structure plots for each hit found.
 help description.  */
  char * aln_EPS_arg;	/**< @brief Produce colored and structure annotated subalignment for each hit
.  */
  char * aln_EPS_orig;	/**< @brief Produce colored and structure annotated subalignment for each hit
 original value given at command line.  */
  const char *aln_EPS_help; /**< @brief Produce colored and structure annotated subalignment for each hit
 help description.  */
  int aln_EPS_cols_arg;	/**< @brief Number of columns in colored EPS alignment output.
 (default='60').  */
  char * aln_EPS_cols_orig;	/**< @brief Number of columns in colored EPS alignment output.
 original value given at command line.  */
  const char *aln_EPS_cols_help; /**< @brief Number of columns in colored EPS alignment output.
 help description.  */
  char * aln_EPS_ss_arg;	/**< @brief Produce colored consensus secondary structure plots in PostScript format
.  */
  char * aln_EPS_ss_orig;	/**< @brief Produce colored consensus secondary structure plots in PostScript format
 original value given at command line.  */
  const char *aln_EPS_ss_help; /**< @brief Produce colored consensus secondary structure plots in PostScript format
 help description.  */
  char * aln_stk_arg;	/**< @brief Add hits to a multi-Stockholm formatted output file.
 (default='RNALalifold_results').  */
  char * aln_stk_orig;	/**< @brief Add hits to a multi-Stockholm formatted output file.
 original value given at command line.  */
  const char *aln_stk_help; /**< @brief Add hits to a multi-Stockholm formatted output file.
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
  int split_contributions_flag;	/**< @brief Split the free energy contributions into separate parts
 (default=off).  */
  const char *split_contributions_help; /**< @brief Split the free energy contributions into separate parts
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
  int maxBPspan_arg;	/**< @brief Set the maximum allowed separation of a base pair to span. I.e. no pairs (i,j) with j-i>span will be allowed.
  
 (default='70').  */
  char * maxBPspan_orig;	/**< @brief Set the maximum allowed separation of a base pair to span. I.e. no pairs (i,j) with j-i>span will be allowed.
  
 original value given at command line.  */
  const char *maxBPspan_help; /**< @brief Set the maximum allowed separation of a base pair to span. I.e. no pairs (i,j) with j-i>span will be allowed.
  
 help description.  */
  double threshold_arg;	/**< @brief Energy threshold in kcal/mol per nucleotide above which secondary structure hits are omitted in the output.
  
 (default='-0.1').  */
  char * threshold_orig;	/**< @brief Energy threshold in kcal/mol per nucleotide above which secondary structure hits are omitted in the output.
  
 original value given at command line.  */
  const char *threshold_help; /**< @brief Energy threshold in kcal/mol per nucleotide above which secondary structure hits are omitted in the output.
  
 help description.  */
  int mis_flag;	/**< @brief Output \"most informative sequence\" instead of simple consensus: For each column of the alignment output the set of nucleotides with frequency greater than average in IUPAC notation.
  
 (default=off).  */
  const char *mis_help; /**< @brief Output \"most informative sequence\" instead of simple consensus: For each column of the alignment output the set of nucleotides with frequency greater than average in IUPAC notation.
  
 help description.  */
  int gquad_flag;	/**< @brief Incoorporate G-Quadruplex formation into the structure prediction algorithm
  
 (default=off).  */
  const char *gquad_help; /**< @brief Incoorporate G-Quadruplex formation into the structure prediction algorithm
  
 help description.  */
  double temp_arg;	/**< @brief Rescale energy parameters to a temperature of temp C. Default is 37C.
  
.  */
  char * temp_orig;	/**< @brief Rescale energy parameters to a temperature of temp C. Default is 37C.
  
 original value given at command line.  */
  const char *temp_help; /**< @brief Rescale energy parameters to a temperature of temp C. Default is 37C.
  
 help description.  */
  int noTetra_flag;	/**< @brief Do not include special tabulated stabilizing energies for tri-, tetra- and hexaloop hairpins. Mostly for testing.
  
 (default=off).  */
  const char *noTetra_help; /**< @brief Do not include special tabulated stabilizing energies for tri-, tetra- and hexaloop hairpins. Mostly for testing.
  
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
  
  unsigned int help_given ;	/**< @brief Whether help was given.  */
  unsigned int detailed_help_given ;	/**< @brief Whether detailed-help was given.  */
  unsigned int full_help_given ;	/**< @brief Whether full-help was given.  */
  unsigned int version_given ;	/**< @brief Whether version was given.  */
  unsigned int verbose_given ;	/**< @brief Whether verbose was given.  */
  unsigned int quiet_given ;	/**< @brief Whether quiet was given.  */
  unsigned int noconv_given ;	/**< @brief Whether noconv was given.  */
  unsigned int input_format_given ;	/**< @brief Whether input-format was given.  */
  unsigned int csv_given ;	/**< @brief Whether csv was given.  */
  unsigned int aln_given ;	/**< @brief Whether aln was given.  */
  unsigned int aln_EPS_given ;	/**< @brief Whether aln-EPS was given.  */
  unsigned int aln_EPS_cols_given ;	/**< @brief Whether aln-EPS-cols was given.  */
  unsigned int aln_EPS_ss_given ;	/**< @brief Whether aln-EPS-ss was given.  */
  unsigned int aln_stk_given ;	/**< @brief Whether aln-stk was given.  */
  unsigned int auto_id_given ;	/**< @brief Whether auto-id was given.  */
  unsigned int id_prefix_given ;	/**< @brief Whether id-prefix was given.  */
  unsigned int id_delim_given ;	/**< @brief Whether id-delim was given.  */
  unsigned int id_digits_given ;	/**< @brief Whether id-digits was given.  */
  unsigned int id_start_given ;	/**< @brief Whether id-start was given.  */
  unsigned int filename_delim_given ;	/**< @brief Whether filename-delim was given.  */
  unsigned int split_contributions_given ;	/**< @brief Whether split-contributions was given.  */
  unsigned int shape_given ;	/**< @brief Whether shape was given.  */
  unsigned int shapeMethod_given ;	/**< @brief Whether shapeMethod was given.  */
  unsigned int maxBPspan_given ;	/**< @brief Whether maxBPspan was given.  */
  unsigned int threshold_given ;	/**< @brief Whether threshold was given.  */
  unsigned int mis_given ;	/**< @brief Whether mis was given.  */
  unsigned int gquad_given ;	/**< @brief Whether gquad was given.  */
  unsigned int temp_given ;	/**< @brief Whether temp was given.  */
  unsigned int noTetra_given ;	/**< @brief Whether noTetra was given.  */
  unsigned int dangles_given ;	/**< @brief Whether dangles was given.  */
  unsigned int noLP_given ;	/**< @brief Whether noLP was given.  */
  unsigned int noGU_given ;	/**< @brief Whether noGU was given.  */
  unsigned int noClosingGU_given ;	/**< @brief Whether noClosingGU was given.  */
  unsigned int salt_given ;	/**< @brief Whether salt was given.  */
  unsigned int paramFile_given ;	/**< @brief Whether paramFile was given.  */
  unsigned int nsp_given ;	/**< @brief Whether nsp was given.  */
  unsigned int energyModel_given ;	/**< @brief Whether energyModel was given.  */
  unsigned int cfactor_given ;	/**< @brief Whether cfactor was given.  */
  unsigned int nfactor_given ;	/**< @brief Whether nfactor was given.  */
  unsigned int ribosum_file_given ;	/**< @brief Whether ribosum_file was given.  */
  unsigned int ribosum_scoring_given ;	/**< @brief Whether ribosum_scoring was given.  */

  char **inputs ; /**< @brief unnamed options (options without names) */
  unsigned inputs_num ; /**< @brief unnamed options number */
} ;

/** @brief The additional parameters to pass to parser functions */
struct RNALalifold_cmdline_parser_params
{
  int override; /**< @brief whether to override possibly already present options (default 0) */
  int initialize; /**< @brief whether to initialize the option structure RNALalifold_args_info (default 1) */
  int check_required; /**< @brief whether to check that all required options were provided (default 1) */
  int check_ambiguity; /**< @brief whether to check for options already specified in the option structure RNALalifold_args_info (default 0) */
  int print_errors; /**< @brief whether getopt_long should print an error message for a bad option (default 1) */
} ;

/** @brief the purpose string of the program */
extern const char *RNALalifold_args_info_purpose;
/** @brief the usage string of the program */
extern const char *RNALalifold_args_info_usage;
/** @brief the description string of the program */
extern const char *RNALalifold_args_info_description;
/** @brief all the lines making the help output */
extern const char *RNALalifold_args_info_help[];
/** @brief all the lines making the full help output (including hidden options) */
extern const char *RNALalifold_args_info_full_help[];
/** @brief all the lines making the detailed help output (including hidden options and details) */
extern const char *RNALalifold_args_info_detailed_help[];

/**
 * The command line parser
 * @param argc the number of command line options
 * @param argv the command line options
 * @param args_info the structure where option information will be stored
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNALalifold_cmdline_parser (int argc, char **argv,
  struct RNALalifold_args_info *args_info);

/**
 * The command line parser (version with additional parameters - deprecated)
 * @param argc the number of command line options
 * @param argv the command line options
 * @param args_info the structure where option information will be stored
 * @param override whether to override possibly already present options
 * @param initialize whether to initialize the option structure my_args_info
 * @param check_required whether to check that all required options were provided
 * @return 0 if everything went fine, NON 0 if an error took place
 * @deprecated use RNALalifold_cmdline_parser_ext() instead
 */
int RNALalifold_cmdline_parser2 (int argc, char **argv,
  struct RNALalifold_args_info *args_info,
  int override, int initialize, int check_required);

/**
 * The command line parser (version with additional parameters)
 * @param argc the number of command line options
 * @param argv the command line options
 * @param args_info the structure where option information will be stored
 * @param params additional parameters for the parser
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNALalifold_cmdline_parser_ext (int argc, char **argv,
  struct RNALalifold_args_info *args_info,
  struct RNALalifold_cmdline_parser_params *params);

/**
 * Save the contents of the option struct into an already open FILE stream.
 * @param outfile the stream where to dump options
 * @param args_info the option struct to dump
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNALalifold_cmdline_parser_dump(FILE *outfile,
  struct RNALalifold_args_info *args_info);

/**
 * Save the contents of the option struct into a (text) file.
 * This file can be read by the config file parser (if generated by gengetopt)
 * @param filename the file where to save
 * @param args_info the option struct to save
 * @return 0 if everything went fine, NON 0 if an error took place
 */
int RNALalifold_cmdline_parser_file_save(const char *filename,
  struct RNALalifold_args_info *args_info);

/**
 * Print the help
 */
void RNALalifold_cmdline_parser_print_help(void);
/**
 * Print the full help (including hidden options)
 */
void RNALalifold_cmdline_parser_print_full_help(void);
/**
 * Print the detailed help (including hidden options and details)
 */
void RNALalifold_cmdline_parser_print_detailed_help(void);
/**
 * Print the version
 */
void RNALalifold_cmdline_parser_print_version(void);

/**
 * Initializes all the fields a RNALalifold_cmdline_parser_params structure 
 * to their default values
 * @param params the structure to initialize
 */
void RNALalifold_cmdline_parser_params_init(struct RNALalifold_cmdline_parser_params *params);

/**
 * Allocates dynamically a RNALalifold_cmdline_parser_params structure and initializes
 * all its fields to their default values
 * @return the created and initialized RNALalifold_cmdline_parser_params structure
 */
struct RNALalifold_cmdline_parser_params *RNALalifold_cmdline_parser_params_create(void);

/**
 * Initializes the passed RNALalifold_args_info structure's fields
 * (also set default values for options that have a default)
 * @param args_info the structure to initialize
 */
void RNALalifold_cmdline_parser_init (struct RNALalifold_args_info *args_info);
/**
 * Deallocates the string fields of the RNALalifold_args_info structure
 * (but does not deallocate the structure itself)
 * @param args_info the structure to deallocate
 */
void RNALalifold_cmdline_parser_free (struct RNALalifold_args_info *args_info);

/**
 * Checks that all the required options were specified
 * @param args_info the structure to check
 * @param prog_name the name of the program that will be used to print
 *   possible errors
 * @return
 */
int RNALalifold_cmdline_parser_required (struct RNALalifold_args_info *args_info,
  const char *prog_name);


#ifdef __cplusplus
}
#endif /* __cplusplus */
#endif /* RNALALIFOLD_CMDL_H */
