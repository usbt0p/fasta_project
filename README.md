# fasta_project

First public release of the FASTA project!
Current state: finished!

## *Description of the project*:
This is a project made for the Programming II course.
It provides a series of scripts for manipulating and representing
FASTA sequences and `.fasta` files, which are files in a text-based
format, used for representing nucleotide sequences of amino acid
base pairs.
We use OOP to create sequence objects, that store identifiers and their
nucleotid sequences. On top, multiple classes allow manipulation of
sequences for various purposes.

## *Scripts*:
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

## *Installation*:

For correct usage now the user should add the project directory to
the environment variable PYTHONPATH so that Python knows where
to search for the executable files.

One way of doing it is this, do the following after downoading
the project:
- Go, through command line, to the root directory in which the project
was downloaded in your PC.
For example if you downloaded it to C:\user\documents, go to
C:\user\documents\fasta_project.

- Once there, you must add the path to the environment variable.
In Windows, type the followng command: $env:PYTHONPATH = '.'
On Linux, type: export PYTHONPATH=.

- Of course, the same would work if '.' is substituted with the absolute
path of the directory.

- This must be done each time the terminal is opened to use the project,
since the environment variable dissapears after closing it.

- After that, experiment with the sample commands that are listed 
in the script modules's docstrings. You will need `.fasta` files to manipulate.
You can generate them online, save them in a `.txt` or other file format, and
just rename them to the `.fasta` extension.
Beware that the sequences in the file can only contain the following uppercase
letters: A, C, T, G.

