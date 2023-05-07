'''Scripts for getting statistics from sequences in `.fasta` files and directories with `.fasta` files, 
writing them to csv files, and plotting the statistics saving the image plots.
Example command:
python -u "c:\\<your path>" --input=test_data\\test_3.fasta --output=savedFiles\\stat_table.csv
For saving a single file into `.csv` and saving images of the stats:
python -u "c:\\<your path> --input=test_data/test_4.fasta --output=savedFiles/plot_shit.csv --extra-plots=savedFiles
For saving all of a directory's `.fasta` files stats, and their respective plots:
python -u "c:\\<your path>" --input=test_data --output=statFolder --extra-plots=statFolder
'''
import sys #stdlib imports
from os.path import isdir, join
from os import listdir

from argsparser import parseArgs # local imports
from sequence_stats import StatManager
from script_utils import ScriptErrorManager
from fasta import fastaProcessorIO

args = parseArgs(sys.argv[1:])

# Declare script's argument specification
required_args = ['input', 'output']
optional_args = ['extra-plots']
special_value_args = {}

# Checking for script requirements
ScriptErrorManager.general_check(required_args, optional_args, special_value_args, args)

def __read_statify_write(input_path, output_path, file=None):
    ''' The `file=None` key argument is used internally for
    processing calls to a directory or a file, and should be
    used carfully so as to not break anything.'''

    input = fastaProcessorIO.from_file(input_path)

    stat_manager = StatManager() 
    stat_manager.write_stats(
        stat_manager.sequence_stats(input.sequenceObjects),
        output_path
        )

    print(f'Wrote stats for {len(stat_manager.fastaStats) - 1} sequences.')

    if ('extra-plots' in args.keys()) and isdir(args['extra-plots']):
        import pandas as pd
        import matplotlib.pyplot as plt # DUDA esto non é boa idea non?? rollo importar algo nun condicional

        def __save_image(singleFileEnder, muliFileEnder ): # DUDA polo tanto isto tampouco
            '''Beware that modifying this function might fuck up the internal workings 
            of the image saving process.'''
            if file == None:
                plt.savefig((args['output'].replace('.csv', '_1') + singleFileEnder))
            else:
                plt.savefig(join(args['output'], file.replace('.fasta', muliFileEnder)))
            plt.close()

        # Convert the matrix to a Pandas DataFrame
        data_frame = pd.DataFrame(stat_manager.fastaStats[1:], columns=stat_manager.fastaStats[0])
        data_frame['len'].hist() # the deed does itself

        plt.title('Frequency of sequence lengths')
        plt.xlabel('Sequence length intervals')
        plt.ylabel('Frequency')
        
        __save_image('_bar', '_bar.png')

        # relative percentages of A, C, T, G over sequence length
        for newcol, nucleotid in zip(('A_rel', 'C_rel', 'T_rel', 'G_rel')
                                     , ('A', 'C', 'T', 'G')) :
            data_frame[newcol] = data_frame[nucleotid] / data_frame['len']

        data_frame_rel = data_frame[['A_rel', 'C_rel', 'T_rel', 'G_rel']]
        plt.boxplot(data_frame_rel.values, labels=data_frame_rel.columns)
        plt.ylabel('Relative Percentages')

        __save_image('_box', '_box.png')
        
# Load a directory's .fasta files and dump stats into other dir
if isdir(args['input']) and isdir(args['output']):

    files = listdir(args['input'])

    for file in files:
        if '.fasta' in file:

            newpath_input = join(args['input'], file)
            newpath_output = join(args['output'], file.replace('.fasta', '.csv'))

            __read_statify_write(newpath_input, newpath_output, file)  
else: 
    __read_statify_write(args['input'], args['output'])
    

