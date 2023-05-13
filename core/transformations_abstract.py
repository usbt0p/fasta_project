from abc import ABCMeta, abstractmethod
from copy import deepcopy

class AbstractTransformer(metaclass=ABCMeta):
    '''We define a 'template' for our classes using an abstract class.
    All classes inheriting from AbstractTransformer must implement
    a __init__ and transform method.'''

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def transform(sequence_list : list):
        '''Performs non-destructive transformations in a list of 
        sequence objects'''
        ...

def remove_duplicates(seq_list : list) -> list:
    used_identifs_list, indexes = list(), list()

    new_seq_list = deepcopy(seq_list)

    for index, seq in enumerate(seq_list):
        if seq.identifier not in used_identifs_list:
            used_identifs_list.append(seq.identifier)
        else:
            indexes.append(index) 

    for count, index in enumerate(indexes):
        new_seq_list.pop(index - count) # festival de enumerates!!!
    
    return new_seq_list

def rename_duplicates(seq_list : list) -> list:
    used_identif_list = list()
    duplicate_map = dict() # a map that stores each repeated seq's indexes of occurence
    new_seq_list = deepcopy(seq_list)

    for index, seq in enumerate(new_seq_list):
        if seq.identifier not in used_identif_list:
            used_identif_list.append(seq.identifier)
        else:
            if seq.identifier not in duplicate_map.keys():
                duplicate_map[seq.identifier] = [index]
            else: 
                duplicate_map[seq.identifier].append(index)

    for key in duplicate_map.keys():
        for num, repeated_index in enumerate(duplicate_map[key]):
            # for each repeated seq, and for each occurence of repetition...
            new_seq_list[repeated_index].identifier += ('.' + str(num + 1)) 
            # ...add the number of repetitions as a string to de identifier

    return new_seq_list

def map_reverse(seq_list : list) -> list:
    new_seq_list = deepcopy(seq_list)  

    def reverse(seq):
        seq.sequenceChain = seq.sequenceChain[::-1]
        return seq
    
    return list(map(reverse, new_seq_list))

def map_complement(seq_list : list) -> list:
    new_seq_list = deepcopy(seq_list)

    def complement(seq): 
        '''Substitutes nucleotids in a fasta chain with each one's complementary.'''
        mapping = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

        subchain = ''
        for letter in seq.sequenceChain:
            compl = letter.replace(letter, mapping[letter])
            subchain += compl
        seq.sequenceChain = subchain
        return seq
    
    return list(map(complement, new_seq_list))

class DuplicatedIdentifiersRemover(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list):
        self.transformation = remove_duplicates(sequence_list)

        return self.transformation   

class DuplicatedIdentifiersRenamer(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list):        
        # Set and get .transformation attr
        self.transformation = rename_duplicates(sequence_list) 

        return self.transformation

class Reverse(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list):        
        # Set and get .transformation attr
        self.transformation = map_reverse(sequence_list)       
        return self.transformation

class Complement(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list):        
        # Set and get .transformation attr
        self.transformation = map_complement(sequence_list)
        return self.transformation

class SequenceListTransformer:
    '''Compose a list of functions recursively for a given Sequence object list.
    Given `sequence` and a list `[DuplicatedIdentifiersRenamer(),Reverse(),Complement()]`,
    it will compose like this: `Complement(Reverse(DuplicatedIdentifiersRenamer(sequence)))`.'''

    def __init__(self, transf_list : list) -> None: 
        self.transf_list = transf_list

    def apply_transformations(self, transf_list : list, seq_list : list = None):
        if transf_list == []:
            return seq_list
        else:
            # PROLOG?!?!?!?!?!
            return self.apply_transformations(transf_list[1:], 
            transf_list[0].transform(seq_list))


if __name__ == '__main__':
    from sequences import Sequence

    # From static data...
    seq1, seq2, seq3 = Sequence('S1','ACTG'), Sequence('S1','ACTG'), Sequence('S3','ACTG')
    seq4, seq5, seq6 = Sequence('S1','ACTG'), Sequence('S1','ACTG'), Sequence('S3','ACTG')

    lista_secuencias = [seq1, seq2, seq3, seq4, seq5, seq6]

    # Instantiate some transformers for demonstration
    transformer_renamer = DuplicatedIdentifiersRenamer()
    transformer_reverse = Reverse()

    print('\nUsing Transformers:\n')
    lista_transf = [transformer_reverse, transformer_renamer]

    #Recursively applies one transformation over the other
    transformer_object = SequenceListTransformer(lista_transf)
    optimus_prime = transformer_object.apply_transformations(
        transformer_object.transf_list, lista_secuencias)

    # Results...
    list(map(print, optimus_prime))
    print('\n')
    # firstly applied transformations remain stored as transformer objects, 
    # and transformer classes can be used by themselves
    list(map(print, transformer_reverse.transformation))

    
    


    




    
    

    
