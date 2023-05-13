# fasta_project

First public release of the FASTA project!
Current state: finished!

- *Description of the project*:
This is a project made for the Programming II course.
It provides a series of scripts for manipulating and representing
FASTA sequences and `.fasta` files, which are files in a text-based
format, used for representing nucleotide sequences of amino acid
base pairs.
We use OOP to create sequence objects, that store identifiers and their
nucleotid sequences. On top, multiple classes allow manipulation of
sequences for various purposes.

- *Scripts*:
The project has a total of 5 scripts, each with different
functionalities.

    - `fasta_format.py`: allows for simple text formatting of `.fasta`
    files, like upper or lower case, and inserting newlines for
    defining specified line lenghts.

    - `disambiguate.py`: manages transformations of repeated sequences in
     `.fasta` files.
    Allows for the elimination of sequences with repeated identifiers
    or their renaming.

    - `reverse-complement.py`: this script implements sequence
    transformations such as reversing sequences or substituting each
    nucleic acid with it's complementary.

    - `multiple_transformations.py`: allows to combine all transformations
    in the `disambiguate.py` and `reverse-complement.py` scripts.

    - `fasta_summary.py`: provides a script for making simple
    statistical analysis of a `.fasta` file.
    Allows to export `.csv` files with the number of occurences of each
    nucleic acid, and produce data analysis images for appearance of
    each acid over total sequence length and for frequency of appearance
    of each sequence's length.
    Works both with `.fasta` files and with directories containing them.
