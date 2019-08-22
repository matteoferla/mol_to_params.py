# mol_to_params.py
molfile_to_params.py ported to python 3.

I am not the author, Ian W. Davis is. I just ported this code to the 21st century.
So any issues, loveletters and royalty checks go to the original author.

Original script is from http://www.pyrosetta.org/scripts.

There does not seem to be a version in python 3 of pyrosetta and I cannot figure out where the parts have gone that it calls. So I ported it and the three files it needs to python3.

Note that there were some additional changes required.

* `isinstance(f, file)` to `isinstance(f, io.IOBase)` &mdash; why did they kill `file` in py3?
* `sort(lambda a,b: cmp(a,b))` to sort(key=lambda a: a) &mdash; __cmp__ died with 2.
* `dot <= 0` to `dt <= 0`


