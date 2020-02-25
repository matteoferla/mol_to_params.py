from types import SimpleNamespace
from typing import Optional, Union


def run(infile,
        name='LIG',
        pdb: str = 'ligand',
        centroid=False,
        chain: Optional[str] = 'X',
        center:str=None,
        max_confs: Optional[int] = 5000,
        root_atom: Optional[int] = None,
        nbr_atom=None,
        kinemage=None,
        amino_acid: Union[None, bool] = None,
        clobber: bool = False,
        no_param: bool = False,
        no_pdb: bool = False,
        extra_torsion_output: bool = False,
        keep_names: bool = False,
        long_names: bool = False,
        recharge: Union[None, bool] = None,
        m_ctrl=None,
        mm_as_virt: bool = False,
        skip_bad_conformers: bool = False,
        conformers_in_one_file: bool = False
        ):
    """
    infile: INPUT.mol | INPUT.sdf | INPUT.mol2
    name: name ligand residues NM1,NM2,... instead of LG1,LG2,...
    pdb: prefix for PDB file names
    centroid: write files for Rosetta centroid mode too
    chain: The chain letter to use for the output PDB ligand.
    center: translate output PDB coords to have given heavy-atom centroid ('X,Y,Z')
    max_confs: don't expand proton chis if above this many total confs
    root_atom: which atom in the molfile is the root? (indexed from 1)
    nbr_atom: which atom in the molfile is the nbr atom? (indexed from 1)
    kinemage: write ligand topology to FILE
    amino_acid: set up params file for modified amino acid; .mol2 only; edit chis afterward.  Implies --keep-names.
    clobber: overwrite existing files
    no_param: skip writing .params files (for debugging)
    no_pdb: skip writing .pdb files (for debugging)
    extra_torsion_output: writing additional torsion files
    keep_names: leaves atom names untouched except for duplications
    long_names: if specified name is longer than 3 letters, keep entire name in param NAME field instead of truncating
    recharge: ignore existing partial charges, setting total charge to CHG
    m_ctrl: read additional M control lines from FILE
    mm_as_virt: assign mm atom types as VIRT, rather than X
    skip_bad_conformers: If a conformer has atoms in the wrong order, skip it and continue rather than dying
    conformers_in_one_file: Output 1st conformer to NAME.pdb and all others to NAME_conformers.pdb

    Original documentation.
    Converts a small molecule in an MDL Molfile with "M SPLT" and "M ROOT"
    records into a series of .params residue definition files for Rosetta.
    Also writes out the ligand conformation as PDB HETATMs.

    If an SD file is given as input instead, the first entry is used for
    generating topology / parameter files, and they all are used for
    generating PDB-style coordinates in separate, numbered files.
    These multiple files can optionally be concatenated into a single file,
    which can then be specified with an additional PDB_ROTAMERS line in the
    .params file to include the extra conformations as ligand rotamers.
    Multiple models may also be supplied in MOL2 format, which does not support
    M ROOT and M SPLT records but does allow for partial charges.
    File type is deduced from the extension.

    To divide a ligand into fragments by "breaking" bonds (optional):
    M SPLT atom_no1 atom_no2

    To specify a neighbor atom for a ligand fragment (optional):
    M NBR atom_no

    To specify a root atom for a ligand fragment (optional):
    M ROOT atom_no

    The "M" records (M SPLT, M NBR, M ROOT) can alternatively be specified in
    a separate control file, which can be used with MOL2 format files.

    Note that for ligands with multiple rotamers, Rosetta overlays the ligands
    based on the neighbor atom (not the root atom), such that the position of the
    neighbor atom and the orientation of the atoms bonded to the neighbor atom is
    the same. When using ligand rotamers, it is recommended to confirm that the
    neighbor atom falls in an appropriate position.

    Expects that the input ligand has already had aromaticity "perceived",
    i.e. that it contains aromatic bonds rather than alternating single and double
    bonds (Kekule structure).

    Optionally writes a kinemage graphics visualization of the atom tree,
    neighbor atom selection, fragments, etc -- very helpful for debugging
    and for visualizing exactly what was done to the ligand.
    """
    fields = ['name', 'pdb', 'centroid', 'chain', 'center', 'max_confs', 'root_atom', 'nbr_atom', 'kinemage',
              'amino_acid', 'clobber', 'no_param', 'no_pdb', 'extra_torsion_output', 'keep_names', 'long_names',
              'recharge', 'm_ctrl', 'mm_as_virt', 'skip_bad_conformers', 'conformers_in_one_file']

    options = SimpleNamespace(**{k: v for k, v in locals().items() if k in fields})
    # namedtuple does not work as it has to change.
    core(infile, options)
