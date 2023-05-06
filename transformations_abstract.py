from abc import ABCMeta, abstractmethod
from copy import deepcopy

class AbstractTransformer(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def transform(sequence_list : list):
        '''Performs non-destructive transformations in a list of 
        sequence objects'''
        ...


class DuplicatedIdentifiersRemover(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list):

        def remove_duplicates(seq_list : list) -> list:
            '''Modifies the inputed list of sequences removing all sequences 
            with repeated identifiers.'''

            used_identifs_list, indexes = list(), list()

            new_seq_list = deepcopy(seq_list) # DUDA preguntar: esto es intended?
            # O sería mejor dejar todo como seq list y recibir la lista modificada?

            for index, seq in enumerate(seq_list):
                if seq.identifier not in used_identifs_list:
                    used_identifs_list.append(seq.identifier)
                else:
                    indexes.append(index) 

            for count, index in enumerate(indexes):
                new_seq_list.pop(index - count) # festival de enumerates!!!
            
            return new_seq_list
        
        self.transformation = remove_duplicates(sequence_list)

        return self.transformation   


class DuplicatedIdentifiersRenamer(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list):

        def rename_duplicates(seq_list : list) -> list:
            used_identif_list = list()
            # a map that stores each repeated seq's indexes of occurence
            duplicate_map = dict() 
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
        
        # Set and get .transformation attr
        self.transformation = rename_duplicates(sequence_list) 
        return self.transformation

class Reverse(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list, rev=True, compl=False):

        def reverse(seq_list : list) -> list: 
            new_seq_list = deepcopy(seq_list)  

            def _reverse(seq):
                seq.sequenceChain = seq.sequenceChain = seq.sequenceChain[::-1]
                return seq
            
            return list(map(_reverse, new_seq_list))
        
        # Set and get .transformation attr
        self.transformation = reverse(sequence_list)       
        return self.transformation
    

class Complement(AbstractTransformer):
    def __init__(self) -> None:
        self.transformation = None

    def transform(self, sequence_list: list):

        def complement(seq_list : list) -> list:
            new_seq_list = deepcopy(seq_list)

            def _complement(seq): 
                '''Substitutes nucleotids in a fasta chain with each one's complementary.'''
                mapping = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

                subchain = ''
                for letter in seq.sequenceChain:
                    compl = letter.replace(letter, mapping[letter])
                    subchain += compl
                seq.sequenceChain = subchain
                return seq
            
            return list(map(_complement, new_seq_list))
        
        # Set and get .transformation attr
        self.transformation = complement(sequence_list)
        return self.transformation

class SequenceListTransformer:
    '''Compose a list of functions recursively for a given Sequence object list.'''

    def __init__(self, transf_list : list, seq_list : list) -> None: 
        self.seq_list = seq_list
        self.transf_list = transf_list

    @staticmethod
    def apply_transformations(transf_list : list, seq_list : list):
        
        instance = SequenceListTransformer(transf_list, seq_list)
        if transf_list == []:
            return seq_list
        else:
            # PROLOG?!?!?!?!?!
            return instance.apply_transformations(transf_list[1:], transf_list[0].transform(seq_list))


if __name__ == '__main__':
    from sequences import Sequence

    # From static data...
    seq1, seq2, seq3 = Sequence('S1','ACTG'), Sequence('S1','ACTG'), Sequence('S3','ACTG')
    seq4, seq5, seq6 = Sequence('S1','ACTG'),  Sequence('S1','ACTG'), Sequence('S3','ACTG')

    lista_secuencias = [seq1, seq2, seq3, seq4, seq5, seq6]

    # Instantiate some transformers for demonstration
    transformer_renamer = DuplicatedIdentifiersRenamer()
    transformer_reverse = Reverse()

    print('\nUsing Transformers:\n')
    lista_transf = [transformer_reverse, transformer_renamer]

    optimus_prime = SequenceListTransformer.apply_transformations(lista_transf, lista_secuencias)
    
    # Results...
    list(map(print, optimus_prime))
    print('\n')
    # firstly applied transformations remain stored as transformer objects, 
    # and transformer classes can be used by themselves
    list(map(print, transformer_reverse.transformation)) 

    
    


    




    
    

    
