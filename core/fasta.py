import os.path
from os import mkdir

'''xestiono de esta forma que ambos modulos poidan funcionar dende 
fora dos scripts, chamandose o un ao outro (sequences.py <---> fasta.py) sen problemas.'''
if 'fasta' in __name__: 
    import __main__ as __main__

    if 'sequences.py' in __main__.__file__:
            Sequence = __main__.Sequence 
            CaseType = __main__.CaseType # e así se asegura que cando se chama dende sequences todo funcione
    else:
        from core.sequences import Sequence, CaseType
        __main__ = None 
        # Intento de borrar un paquete enteiro pq non sei se python o fai auto e non quero telo na memoria
else:
    from core.sequences import Sequence, CaseType # isto faise cando fasta.py é __main__


def _fasta_load(fastaFilePath : str) -> list[Sequence]:
    '''Takes the filepath of a FASTA file, turns each identifier-sequence pair
    into a `Sequence` object and returns a list of the created objects. 
    Private function, works within the `fastaProcessorIO` class'''

    sequence_list = []
    identif_list = []

    with open(fastaFilePath, 'r') as file:

        chain = ''
        for line in file:
            if line[0] != '>':
                chain += line.replace('\n', '')
            else:
                sequence_list.append(chain)
                identif_list.append(line.replace('\n', '').replace('>', ''))
                chain = ''
                continue
        
        sequence_list.append(chain) # add the last iteration of the loop
        sequence_list.pop(0) # remove the first ''

        sequenceObjects = [
            Sequence(identifier, sequence) for identifier, sequence in 
            zip(identif_list, sequence_list)]

        return sequenceObjects

class fastaProcessorIO:
    '''Intended to act as a bridge from fasta files to objects and viceversa.

    Upon instantiation, turns all sequence-identifier pairs into Sequence objects, 
    iteratively through the `fasta_load` function
    Can be called normally with a `Sequence` object list, or with the static method `from_file`
    to load `.fasta` files.
    '''
    
    def __init__(self, sequenceObjects : list[Sequence]) -> None:
            self.sequenceObjects : list[Sequence] = sequenceObjects

    @staticmethod
    def from_file(fastaFilePath : str) -> None:
        return fastaProcessorIO(_fasta_load(fastaFilePath))

    def __str__(self) -> str:
        if len(self.sequenceObjects) > 10: # prettify if there are a lot of objects being loaded
            representation = [str(elem) for elem in self.sequenceObjects[:3]]
            representation.append('...')
        else:
            representation = [str(elem) for elem in self.sequenceObjects]
        return 'Saved ({}) Sequence objects: {}'.format(len(self.sequenceObjects), representation)

    def writeFastaFile(self, filename : str, case : CaseType = CaseType.ORIGINAL, 
                       maxlenght : int = 0, absolutepath=''): 
        '''Takes a file name and a path (absolute or relative) ant dumps the loaded objects into a 
        fasta file. Supports sequence formatting.'''        

        if '.fasta' not in filename:
            filename += '.fasta' 

        if not absolutepath:
            dirpath = 'savedFiles'
            if not os.path.isdir(dirpath):
                os.mkdir(dirpath)
        else:
            dirpath = absolutepath

        with open(os.path.join(dirpath, filename), "w") as file:

            for elem in self.sequenceObjects:
                formatted_object = elem._seqFormatter(case, maxlenght)
                file.write('>' + formatted_object[0] + '\n')
                file.write(formatted_object[1] + '\n')


if __name__ == '__main__':
    
    #from fasta import fastaProcessorIO

    # if nothing is changed here this should work from the getgo since the paths are relative
    adn_seqs = fastaProcessorIO.from_file('test_data/test_4.fasta')

    print(adn_seqs)

    adn_seqs.writeFastaFile('example_file', CaseType.MAYUS ,maxlenght = 2) # using this func creates a 
    #savedFiles directory if not given an absolutepath parameter

    # works with generic objects as well!!
    seq1, seq2, seq3 = Sequence('S1','ACTG'), Sequence('S2','ACTG'), Sequence('S3','ACTG')
    lista_de_secuencias = [seq1, seq2, seq3]
    wtf = fastaProcessorIO(lista_de_secuencias)
    
    wtf.writeFastaFile('nonstatic.fasta', maxlenght= 2)
    print(wtf)