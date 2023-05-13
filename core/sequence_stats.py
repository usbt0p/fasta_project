from core.sequences import Sequence
import csv

class StatManager:
    '''Performs basic statistical analysis of sequences.'''

    def __init__(self) -> None:
        self.fastaStats = None
        
    def sequence_stats(self, seq_list : list) -> list:
        '''From a sequence list, obtain the following statistics for each sequence:
        sequence length and counts of the letters A, C, T, G, and the character - .'''

        def _sequence_stats(seq : Sequence) -> list:
            length = len(seq.sequenceChain)
            a_count = seq.sequenceChain.count('A')
            c_count = seq.sequenceChain.count('C')
            t_count = seq.sequenceChain.count('T')
            g_count = seq.sequenceChain.count('G')
            dash_count = seq.sequenceChain.count('-')

            return [seq.identifier, length, a_count, c_count, t_count, g_count, dash_count]
        
        header = ['id', 'len', 'A', 'C', 'T', 'G', '-']
        matrix = list(map(_sequence_stats, seq_list))
        matrix.insert(0, header)
        self.fastaStats = matrix
        
        return self.fastaStats

    def write_stats(self, stat_matrix : list, filename : str):
        '''Write stat matrix as a `.csv` file.'''

        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            for seq_stat in stat_matrix:
                writer.writerow(seq_stat)


if __name__ == '__main__':

    seq1, seq2, seq3 = Sequence('S1','ACTG'), Sequence('S1','ACTG'), Sequence('S3','ACTG')
    seq4, seq5, seq6 = Sequence('S1','ACTG'),  Sequence('S1','ACTG'), Sequence('S3','ACTG')

    lista_secuencias = [seq1, seq2, seq3, seq4, seq5, seq6]

    stat_manager = StatManager()
    stat_matrix = stat_manager.sequence_stats(lista_secuencias)
    print(stat_matrix)

    stat_manager.write_stats(stat_matrix, 'savedFiles\\STATS.csv')