# mol_to_params.py
`molfile_to_params.py` ported to python 3.

> Please see [https://github.com/matteoferla/rdkit_to_params](rdkit_to_params), which is a complete rewrite.
> I have taken down this 2to3 port as it was incompatible with Rosetta's academic licence.

The `molfile_to_params.py` generates a `.params` file from a ligand given as a mol/sdf/mdl file or a mol2 file. The `.params` file is the topology file for Rosetta and has to be specified with the flag `-in:file:extra_res_fa <file>` (Rosetta Relax, Score etc.)  and `-in:file:extra_res_cen <file>` (required by Remodel).

Herein I am solely sharing a small script that acts as a wrapper for use without proving the 2to3 code.
The script `parameterisation.py` contains a function called `run` that makes it more usable as a module.

The code in the function run is under MIT licence (do whatever).
While molfile_to_params.py is under Rosetta licence.

## Wrapper
The key-arguments are the same as the ones for the parser and are written in full so the IDE can hint them.

Normally, `molfile_to_params.py` file called directly with arguments from the terminal is parsed with argparse in the method called `main`.

What I did is cut out everything from this starting from `crt=None` (after the argparse definitions)
and copied it into a function called `core(infile, options)` and added `core(infile, options)` to the end of `main`.

It is not rocketscience, but has to be `SimpleNamespace` as opposed to a `namedtuple`
to mimic the `argparse` options as these are changed during running —unusual I know.

The next step is copy-pasting in the aforementioned `run` method and one can do the following:

    import mol_to_params
    mol_to_params.run('xxx.mol2', name='XXX', amino_acid=True)

## 2to3
## versions

The version shipped with Rosetta is longer and has more functionality than that with pyrosetta. Why? No idea.
I ported them both to 3.

### changes
**I am not the author**, Ian W. Davis is. I just ported this code to the 2nd decade of 21st century.
So any issues, loveletters and royalty checks go to the original author.

Original script is from http://www.pyrosetta.org/scripts.

There does not seem to be a version in python 3 of pyrosetta and I cannot figure out where the parts have gone that it calls.
So I ported it and the three files it needs to python3.

Note that there were some additional changes required.

* `isinstance(f, file)` to `isinstance(f, io.IOBase)` &mdash; why did they kill `file` in py3?
* `sort(lambda a,b: cmp(a,b))` to `sort(key=lambda a: a)` or `functools.cmp_to_key`
* `dot <= 0` to `dt <= 0`
