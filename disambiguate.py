'''Scripts for transforming `.fasta` files containing repeated identifiers.

Example command:
python -u "c:\\Users\\Canle\\Desktop\\Uni\\Programacion_2\\Proxecto_FASTA\\fasta_proyect_safe\\disambiguate.py" --input=test_data/test_3.fasta --output=NOAMBIGUO.fasta --mode=rename
'''
import sys # stdlib imports

from argsparser import parseArgs # local imports
import fasta as core
from transformations import remove_duplicates, rename_duplicates
from error_manager import ScriptErrorManager

args = parseArgs(sys.argv[1:])

# Declare script's argument specification
required_args = ['input', 'output', 'mode']
optional_args = []
special_value_args = {'mode':('remove','replace')}

# Checking for script requirements
ScriptErrorManager.general_check(required_args, optional_args, special_value_args, args)

# Cargar o ficheiro de entrada
input_fasta = core.fastaProcessorIO.from_file(args['input'])

if args['mode'] == 'rename':
    rename_duplicates(input_fasta.sequenceObjects)
elif args['mode'] == 'remove':
    remove_duplicates(input_fasta.sequenceObjects)

# Escribir a lista de secuencias no ficheiro de saída.
output_fasta = input_fasta.writeFastaFile(args['output'])

print('Number of sequences after disambiguation: ', (str(len(input_fasta.sequenceObjects)) + '.')) 
# OPT: fix weird ass tracebacks???
