from enum import Enum
from re import sub
from functools import reduce

class CaseType(Enum):
    ORIGINAL = 0
    MAYUS = 1
    MINUS = 2  

class Sequence: 
    '''In charge of Sequence objects. 
    Stores sequence idfentifier and DNA sequence as attributes of the object.
    '''
    num_instances : int = 0

    def __init__(self, identifier, sequenceChain) -> None:
        self.identifier : str = identifier
        self.sequenceChain : str = sequenceChain
        Sequence.num_instances += 1
        
    def __str__(self) -> str:
        return '{}: {}'.format(self.identifier, self.sequenceChain)
    
    def _seqFormatter(self, case = CaseType.ORIGINAL, maxlenght = 0):

            def _lenght_definer(sequence : str, maxlenght : int):
                if maxlenght == 0:
                    return sequence
                elif maxlenght > 0:
                    '''the objective of this comprehension is to take any arbitrary sequence ( with no newlines 
                    since we have processed and cleared all strings) and return a defined line lenght by 
                    adding newlines.'''
                    x = [sequence[i:(i + maxlenght)] + '\n' for i in range(0, len(sequence), maxlenght)] 
                    x[-1] = x[-1][:-1] # removes last \n so no future processing needed
                    return ''.join(x) 
                else:
                    raise ValueError(f"Expected value 0 or higher, got {maxlenght}.")
            
            if case == CaseType.ORIGINAL:
                original_identif = self.identifier
                formatted_sequence = _lenght_definer(self.sequenceChain, maxlenght)
                return original_identif, formatted_sequence

            elif case == CaseType.MAYUS:
                formatted_identif = self.identifier.upper()
                formatted_sequence = _lenght_definer(self.sequenceChain.upper(), maxlenght) 
                return  formatted_identif, formatted_sequence

            elif case == CaseType.MINUS:
                formatted_identif = self.identifier.lower()
                formatted_sequence = _lenght_definer(self.sequenceChain.lower(), maxlenght) 
                return formatted_identif, formatted_sequence

# TODO cambiar de módulo???
def reverse(seq_list : list) -> list:        
    def _reverse(seq : Sequence):
        seq.sequenceChain = seq.sequenceChain = seq.sequenceChain[::-1]
        return seq
    return list(map(_reverse, seq_list))
    
def complement(seq_list : list) -> list:
    def _complement(seq : Sequence):
        '''Substitutes nucleotids in a fasta chain with each one's complementary.'''
        mapping = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

        seq.sequenceChain = reduce((lambda x, y: x + '' + y),  # TODO optimiza para hacerlo con una sola cadena
                    [letter.replace(letter, mapping[letter]) for letter in seq.sequenceChain])
        return seq
    return list(map(_complement, seq_list))

def complement2(seq_list : list) -> list:
    def _complement2(seq : Sequence): 
        '''Substitutes nucleotids in a fasta chain with each one's complementary.'''
        mapping = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

        subchain = ''
        for letter in seq.sequenceChain:
            compl = letter.replace(letter, mapping[letter])
            subchain += compl
        seq.sequenceChain = subchain

        return seq
    return list(map(_complement2, seq_list))


            
if __name__ == '__main__':
    from fasta import fastaProcessorIO

    # if nothing is changed here this should work from the getgo since the paths are relative
    adn = fastaProcessorIO.from_file('test_data/test_2.fasta')

    print(adn)

    adn.writeFastaFile('example_file', CaseType.MAYUS ,maxlenght = 3) # using this func creates a savedFiles 
    # directory if not given an absolutepath parameter

    # works with generic objects as well!!
    seq1, seq2, seq3 = Sequence('S1','ACTG'), Sequence('S2','ACTG'), Sequence('S3','ACTG')
    lista_de_secuencias = [seq1, seq2, seq3]
    wtf = fastaProcessorIO(lista_de_secuencias)
    
    wtf.writeFastaFile('nonstatic.fasta', maxlenght= 2) # yipee
    #TODO e agora como fago que se garde o filepath para representar en string se se usou .from_file???

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # From static data...
    seq1, seq2, seq3 = Sequence('S1','ACTGGGGCT'), Sequence('S1','ACTG'), Sequence('S3','ACTG')
    seq4, seq5, seq6 = Sequence('S1','ACTGGGGCT'),  Sequence('S1','ACTG'), Sequence('S3','ACTG')
    seq7, seq8, seq9 = Sequence('S1','ACTGGGGCT'),  Sequence('S1','ACTG'), Sequence('S3','ACTG')

    listaaa = [seq1, seq2, seq3]
    listo = [seq4, seq5, seq6]
    asdf = [seq7, seq8, seq9] 

    x = reverse(listaaa)
    for elem in x:
        print(elem, '<- reverse')

    y = complement(listo)
    for elem in y:
        print(elem, '<- compl')

    z = complement2(asdf)
    for elem in z:
        print(elem, '<- compl2')


    '''start = time.time()
    for elem in asdf:
        (complement(elem))
    end = time.time()
    print(end - start, 'compl')'''