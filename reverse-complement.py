'''Scripts for reversing and complementing sequences in `.fasta` files.
Example command:
python -u "c:\\Users\\Canle\\Desktop\\Uni\\Programacion_2\\Proxecto_FASTA\\fasta_proyect_safe\\reverse-complement.py" --input=test_data/test_3.fasta --output=Rev_Compl.fasta --modify=reverse
'''
import sys #stdlib imports

from argsparser import parseArgs # local imports
from script_utils import ScriptErrorManager, script_transforms

args = parseArgs(sys.argv[1:])

# Declare script's argument specification
required_args = ['input', 'output', 'modify']
optional_args = []
special_value_args = {'modify':('reverse','complement')}

# Checking for script requirements BEFORE USING THE PAYLOAD FUNCTION!!!!
ScriptErrorManager.general_check(required_args, optional_args, special_value_args, args)

processed_fasta = script_transforms(args['input'], args['output'], args['modify'])

print('{} transformation correctly applied to {} sequences.'.format(
            (args['modify']).capitalize(), 
            (str(len(processed_fasta.sequenceObjects)) + '.')
        )
    )