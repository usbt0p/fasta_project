'''Scripts for transforming `.fasta` files containing repeated identifiers.

Example command:
python -u "c:\\<path to root dir>\\fasta_project\\cli\\disambiguate.py" --input=test_data/test_3.fasta --output=NOAMBIGUO.fasta --mode=rename
'''
import sys #stdlib imports

from argsparser import parseArgs # local imports
from script_utils import ScriptErrorManager, script_transforms

args = parseArgs(sys.argv[1:])

# Declare script's argument specification
required_args = ['input', 'output', 'mode']
optional_args = []
special_value_args = {'mode':('remove','rename')}

# Checking for script requirements BEFORE USING THE PAYLOAD FUNCTION!!!!
ScriptErrorManager.general_check(required_args, optional_args, special_value_args, args)

processed_fasta = script_transforms(args['input'], args['output'], args['mode'])

print('Number of sequences after disambiguation: ', (str(len(processed_fasta.sequenceObjects)) + '.')) 
