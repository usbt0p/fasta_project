'''Scripts for reversing and complementing sequences in `.fasta` files.

Example command:
python -u "c:\\Users\\Canle\\Desktop\\Uni\\Programacion_2\\Proxecto_FASTA\\fasta_proyect_safe\\reverse-complement.py" --input=test_data/test_3.fasta --output=Rev_Compl.fasta --modify=reverse
'''
import sys # stdlib imports

from argsparser import parseArgs # local imports
import fasta as core
from sequences import reverse, complement
from error_manager import ScriptErrorManager

args = parseArgs(sys.argv[1:])

# Declare script's argument specification
required_args = ['input', 'output', 'modify']
optional_args = []
special_value_args = {'modify':('reverse','complement')}

# Checking for script requirements
ScriptErrorManager.general_check(required_args, optional_args, special_value_args, args)

# Cargar o ficheiro de entrada
input_fasta = core.fastaProcessorIO.from_file(args['input'])

if args['modify'] == 'reverse':
    reverse(input_fasta.sequenceObjects) # TODO reverse coge como parametro UN OBJ SECUENCIA, lo una lista de seqs
elif args['modify'] == 'complement':
    complement(input_fasta.sequenceObjects)

# Escribir a lista de secuencias no ficheiro de saída.
output_fasta = input_fasta.writeFastaFile(args['output'])

print('Number of sequences after disambiguation: ', (str(len(input_fasta.sequenceObjects)) + '.')) 