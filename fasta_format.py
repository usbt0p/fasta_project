'''Example command:
Comando de exemplo: 
python -u "c:\\Users\\Canle\\Desktop\\Uni\\Programacion_2\\Proxecto_FASTA\\fasta_proyect_safe\\fasta_format.py" --input=test_data/test_2.fasta --output=ficherito_por_cmd.fasta --case=lower --maxLength=2
Funciona maxicamente con este comando para carpetas irmás:
python -m cli.fasta_format --input=test_data/test_2.fasta --output=ficherito_por_cmd.fasta --case=lower --maxLength=2
'''
import sys # stdlib imports

from argsparser import parseArgs # local imports
import fasta as core
from sequences import CaseType
from script_utils import ScriptErrorManager

ARGSET = {'input', 'output', 'case', 'maxLength'}

args = parseArgs(sys.argv[1:])

# Declare script's argument specification
required_args = ['input', 'output']
optional_args = ['case', 'maxLength']
special_value_args = {'case':('upper','lower','original')}

# Checking for script requirements
ScriptErrorManager.general_check(required_args, optional_args, special_value_args, args)

# Cargar o ficheiro de entrada (apartado 2).
input_fasta = core.fastaProcessorIO.from_file(args['input'])

# Crear parametros para formatar secuencias cos parámetros axeitados
chosen_case = CaseType.ORIGINAL # default values 
if 'case' in args.keys():

    if args['case'] == 'upper':
        chosen_case = CaseType.MAYUS
    elif args['case'] == 'lower':
        chosen_case = CaseType.MINUS

maxLength = 0 # default values
if 'maxLength' in args.keys():
    
    maxLength = int(args['maxLength'])

# Escribir a lista de secuencias no ficheiro de saída (apartado 4) e empregando o formatador anterior.
output_fasta = input_fasta.writeFastaFile(args['output'], chosen_case, maxLength)

print(f'Saved ({len(input_fasta.sequenceObjects)}) Sequence objects.') # For sending info to user  





