#ifndef VIENNA_RNA_PACKAGE_CONSTRAINTS_SOFT_SPECIAL_H
#define VIENNA_RNA_PACKAGE_CONSTRAINTS_SOFT_SPECIAL_H

/**
 *  @file     constraints/soft_special.h
 *  @ingroup  soft_constraints, modified_bases
 *  @brief    Specialized implementations that utilize the soft constraint callback mechanism
 */


/**
 *  @addtogroup modified_bases
 *
 *  @{
 *  @brief  Energy parameter corrections for modified bases
 *
 *  Many RNAs are known to be (heavily) modified post-trasnciptionaly. The best
 *  known examples are tRNAs and rRNAs. To-date, more than 150 different modifications
 *  are listed in the MODOMICS database (http://genesilico.pl/modomics/) @cite boccaletto:2022.
 *
 *  Many of the modified bases change the pairing behavior compared to their
 *  unmodified version, affecting not only the pairing partner preference, but
 *  also the resulting stability of the loops the base pairs may form.
 *
 *  Here, we provide a simple soft constraints callback implementation to
 *  correct for some well known modified bases where energy parameters are
 *  available for. This mechanism also supports arbitrary new modified base
 *  energy parameters supplied in JSON format (see @ref modified-bases-params for details).
 */

/**
 *  @brief Modified base parameter data structure
 *
 *  @see  vrna_sc_mod_read_from_jsonfile(), vrna_sc_mod_read_from_json(),
 *        vrna_sc_mod()
 */
typedef struct vrna_sc_mod_param_s *vrna_sc_mod_param_t;


/**
 *  @brief Parse and extract energy parameters for a modified base from a JSON file
 *
 *  @see  vrna_sc_mod_read_from_json(), vrna_sc_mod_parameters_free(), vrna_sc_mod(),
 *        @ref modified-bases-params
 *
 *  @param  filename    The JSON file containing the specifications of the modified base
 *  @param  md          A model-details data structure (for look-up of canonical base pairs)
 *  @return             Parameters of the modified base
 */
vrna_sc_mod_param_t
vrna_sc_mod_read_from_jsonfile(const char *filename,
                               vrna_md_t  *md);


/**
 *  @brief Parse and extract energy parameters for a modified base from a JSON string
 *
 *  @see  vrna_sc_mod_read_from_jsonfile(), vrna_sc_mod_parameters_free(), vrna_sc_mod(),
 *        @ref modified-bases-params
 *
 *  @param  filename    The JSON file containing the specifications of the modified base
 *  @param  md          A model-details data structure (for look-up of canonical base pairs)
 *  @return             Parameters of the modified base
 */
vrna_sc_mod_param_t
vrna_sc_mod_read_from_json(const char *json,
                           vrna_md_t  *md);


/**
 *  @brief Release memory occupied by a modified base parameter data structure
 *
 *  Properly free a #vrna_sc_mod_param_t data structure
 *
 *  @param  params  The data structure to free
 */
void
vrna_sc_mod_parameters_free(vrna_sc_mod_param_t params);


/**
 *  @brief  Prepare soft constraint callbacks for modified base as specified in JSON string
 *
 *  This function prepares all requirements to acknowledge modified bases as specified
 *  in the provided @p json string. All subsequent predictions will treat each
 *  modification site special and adjust energy contributions if necessary.
 *
 *  @see  vrna_sc_mod_jsonfile(), vrna_sc_mod(), vrna_sc_mod_m6A(),
 *        vrna_sc_mod_pseudouridine(), vrna_sc_mod_inosine(),
 *        vrna_sc_mod_7DA(), vrna_sc_mod_purine(), vrna_sc_mod_dihydrouridine(),
 *        @ref modified-bases-params
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  json  The JSON formatted string with the modified base parameters
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 */
int
vrna_sc_mod_json(vrna_fold_compound_t *fc,
                 const char           *json,
                 const unsigned int   *modification_sites);


/**
 *  @brief  Prepare soft constraint callbacks for modified base as specified in JSON string
 *
 *  Similar to vrna_sc_mod_json(), this function prepares all requirements to
 *  acknowledge modified bases as specified in the provided @p json file.
 *  All subsequent predictions will treat each
 *  modification site special and adjust energy contributions if necessary.
 *
 *  @see  vrna_sc_mod_json(), vrna_sc_mod(), vrna_sc_mod_m6A(),
 *        vrna_sc_mod_pseudouridine(), vrna_sc_mod_inosine(),
 *        vrna_sc_mod_7DA(), vrna_sc_mod_purine(), vrna_sc_mod_dihydrouridine(),
 *        @ref modified-bases-params
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  json  The JSON formatted string with the modified base parameters
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 */
int
vrna_sc_mod_jsonfile(vrna_fold_compound_t *fc,
                     const char           *json_file,
                     const unsigned int   *modification_sites);


/**
 *  @brief  Prepare soft constraint callbacks for modified base as specified in JSON string
 *
 *  This function takes a #vrna_sc_mod_param_t data structure as obtained
 *  from vrna_sc_mod_read_from_json() or vrna_sc_mod_read_from_jsonfile()
 *  and prepares all requirements to acknowledge modified bases as specified
 *  in the provided @p params data structure.
 *  All subsequent predictions will treat each
 *  modification site special and adjust energy contributions if necessary.
 *
 *  @see  vrna_sc_mod_read_from_json(), vrna_sc_mod_read_from_jsonfile(),
 *        vrna_sc_mod_json(), vrna_sc_mod_jsonfile(), vrna_sc_mod_m6A(),
 *        vrna_sc_mod_pseudouridine(), vrna_sc_mod_inosine(),
 *        vrna_sc_mod_7DA(), vrna_sc_mod_purine(), vrna_sc_mod_dihydrouridine()
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  json  The JSON formatted string with the modified base parameters
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 *  @return Non-zero if corrections have been added to the fold_compound, 0 otherwise
 */
int
vrna_sc_mod(vrna_fold_compound_t      *fc,
            const vrna_sc_mod_param_t params,
            const unsigned int        *modification_sites);


/**
 *  @brief  Add soft constraint callbacks for N6-methyl-adenosine (m6A)
 *
 *  This is a convenience wrapper to add support for m6A using the
 *  soft constraint callback mechanism. Modification sites are provided
 *  as a list of sequence positions (1-based). Energy parameter corrections
 *  are derived from @cite kierzek:2022.
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 *  @return Non-zero if corrections have been added to the fold_compound, 0 otherwise
 */
int
vrna_sc_mod_m6A(vrna_fold_compound_t  *fc,
                const unsigned int    *modification_sites);


/**
 *  @brief  Add soft constraint callbacks for Pseudouridine
 *
 *  This is a convenience wrapper to add support for pseudouridine using the
 *  soft constraint callback mechanism. Modification sites are provided
 *  as a list of sequence positions (1-based). Energy parameter corrections
 *  are derived from @cite hudson:2013.
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 *  @return Non-zero if corrections have been added to the fold_compound, 0 otherwise
 */
int
vrna_sc_mod_pseudouridine(vrna_fold_compound_t  *fc,
                          const unsigned int    *modification_sites);


/**
 *  @brief  Add soft constraint callbacks for Inosine
 *
 *  This is a convenience wrapper to add support for inosine using the
 *  soft constraint callback mechanism. Modification sites are provided
 *  as a list of sequence positions (1-based). Energy parameter corrections
 *  are derived from @cite wright:2007 and @cite wright:2018.
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 *  @return Non-zero if corrections have been added to the fold_compound, 0 otherwise
 */
int
vrna_sc_mod_inosine(vrna_fold_compound_t  *fc,
                    const unsigned int    *modification_sites);


/**
 *  @brief  Add soft constraint callbacks for 7-deaza-adenosine (7DA)
 *
 *  This is a convenience wrapper to add support for 7-deaza-adenosine using the
 *  soft constraint callback mechanism. Modification sites are provided
 *  as a list of sequence positions (1-based). Energy parameter corrections
 *  are derived from @cite richardson:2016.
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 *  @return Non-zero if corrections have been added to the fold_compound, 0 otherwise
 */
int
vrna_sc_mod_7DA(vrna_fold_compound_t  *fc,
                const unsigned int    *modification_sites);


/**
 *  @brief  Add soft constraint callbacks for Purine (a.k.a. nebularine)
 *
 *  This is a convenience wrapper to add support for Purine using the
 *  soft constraint callback mechanism. Modification sites are provided
 *  as a list of sequence positions (1-based). Energy parameter corrections
 *  are derived from @cite jolley:2017.
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 *  @return Non-zero if corrections have been added to the fold_compound, 0 otherwise
 */
int
vrna_sc_mod_purine(vrna_fold_compound_t *fc,
                   const unsigned int   *modification_sites);


/**
 *  @brief  Add soft constraint callbacks for dihydrouridine
 *
 *  This is a convenience wrapper to add support for dihydrouridine using the
 *  soft constraint callback mechanism. Modification sites are provided
 *  as a list of sequence positions (1-based). This implementation simply
 *  assumes that dihydrouridines favor destacking and destabilize base pair
 *  stacks by at least 1.5kcal/mol, as suggested in @cite dalluge:1996.
 *
 *  @param  fc    The fold_compound the corrections should be bound to
 *  @param  modification_sites  A list of modification site, i.e. positions that contain the modified base (1-based, last element in the list indicated by 0)
 *  @return Non-zero if corrections have been added to the fold_compound, 0 otherwise
 */
int
vrna_sc_mod_dihydrouridine(vrna_fold_compound_t *fc,
                           const unsigned int   *modification_sites);


/**
 * @}
 */
#endif
