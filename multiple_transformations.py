'''Scripts for reversing and complementing sequences in `.fasta` files.
Example command:
python -u "c:\\Users\\Canle\\Desktop\\Uni\\Programacion_2\\Proxecto_FASTA\\fasta_proyect_safe\\multiple_transformations.py" --input=test_data/test_3.fasta --output=MULTI_transf.fasta --rename --reverse --complement
'''
import sys #stdlib imports

from argsparser import parseArgs # local imports
from script_utils import ScriptErrorManager, script_transforms

args = parseArgs(sys.argv[1:])

# Declare script's argument specification
required_args = ['input', 'output']
optional_args = ['reverse', 'complement', 'rename', 'remove']
special_value_args = {}

# Checking for script requirements BEFORE USING THE script_transforms FUNCTION!!!!
ScriptErrorManager.general_check(required_args, optional_args, special_value_args, args)

# Note that for this call to multiple args to work, the argsparser module has been modified
#to return the argument name instead of True when no value is given to an argument, 
# which is the way the transformer args are given to this script
processed_fasta = script_transforms(args['input'], args['output'], 
                                    args.get('reverse'), args.get('complement'), 
                                    args.get('rename'), args.get('remove'))

to_format = (list(args.keys()))
to_format.remove('input')
to_format.remove('output')

print('Applied the following transformations correctly: {}.'.format((to_format)))