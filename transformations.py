def remove_duplicates(seq_list : list) -> list:
    '''Modifies the inputed list of sequences removing all sequences 
    with repeated identifiers.
    '''
    used_identifs_list, indexes = list(), list()

    for index, seq in enumerate(seq_list):
        if seq.identifier not in used_identifs_list:
            used_identifs_list.append(seq.identifier)
        else:
            indexes.append(index) 

    for count, index in enumerate(indexes):
        seq_list.pop(index - count) # festival de enumerates!!!
    
    return seq_list

def rename_duplicates(seq_list : list) -> list:
    used_identif_list = list()
    # a map that stores each repeated seq's indexes of occurence
    duplicate_map = dict() 

    for index, seq in enumerate(seq_list):
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
            seq_list[repeated_index].identifier += ('.' + str(num + 1)) 
            # ...add the number of repetitions as a string to de identifier

    return seq_list


if __name__ == '__main__':
    import fasta
    from sequences import Sequence

    # From static data...
    seq1, seq2, seq3 = Sequence('S1','ACTG'), Sequence('S1','ACTG'), Sequence('S3','ACTG')
    seq4, seq5, seq6 = Sequence('S1','ACTG'),  Sequence('S1','ACTG'), Sequence('S3','ACTG')

    lista_de_secuencias = [seq1, seq2, seq3, seq4, seq5, seq6]

    x = remove_duplicates(lista_de_secuencias)       
    print('using the delete_duplicates function:\n')
    for elem in x:
        print(elem)

    lista_de_secuencias_2 = [seq1, seq2, seq3, seq4, seq5, seq6] # remember pasito por referencia 
    print('using the rename_duplicates function:\n')
    y = rename_duplicates(lista_de_secuencias_2)
    for elem in y:
        print(elem)
    print('\n')

    # ...and from a file.
    print('using the functions on files:\n')
    first_fasta = fasta.fastaProcessorIO.from_file('test_data/test_3.fasta')
    for elem in remove_duplicates(first_fasta.sequenceObjects):
        print(elem)

    print('\n')
    second_fasta = fasta.fastaProcessorIO.from_file('test_data/test_3.fasta')
    for elem in rename_duplicates(second_fasta.sequenceObjects):
        print(elem)
    
    '''
    def una_cosa(x):
        return f'una {x}'

    def otra_cosa(x):
        return f'otra {x}'
        
    func_list = [una_cosa, otra_cosa]
    cosa = ['cosa']

    for elem in func_list:
        print(list(map(elem, cosa)))'''
    

    
