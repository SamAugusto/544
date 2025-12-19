import transcribe_dna
import sys
def amino_acid_counter(sequence:list)-> int:
    '''Counts the amino acid lenght of a reading frame'''
    start = False
    max_count = 0
    curr_count = 0
    
    stop = {"UAA","UAG","UGA"}
    for amino in sequence:
        if amino == "AUG":
            if start == True:
                curr_count +=1
                continue
            start = True
            continue
        if amino in stop:
            if max_count < curr_count:
                max_count = curr_count
                curr_count = 0
                start = False
                continue

            else:
                curr_count = 0
                start = False
                continue
        if start:
            curr_count += 1
            continue
        else:
            continue
    return max_count
def spliting(sequence:str)-> list:
    '''Splits the dna seq in'''
    splitted_seq= []

    index_i = 0
    index_f = 3

    while index_f <= len(sequence):
        splitted_seq.append(sequence[index_i:index_f])
        index_i += 3
        index_f += 3
    return splitted_seq
def reading_frames_assembler(mrna_seq:str,non_coding_dna:str)->set:
    '''Splits a mrna sequence into 6 reading frames'''
    reading_frames_indexes= [0,1,2]
    reading_frames = set()
    for frames in reading_frames_indexes:
        reading_frames.add(mrna_seq[frames:])
        transcribed_non_coding = non_coding_dna.replace("T", "U")
        reading_frames.add(transcribed_non_coding[frames:])   
    return reading_frames



def main(test_seq):
    # Finds the longest reading frame
    sequence = test_seq
    # Function imported from other file
    transcribed_seq_info = transcribe_dna.seq_transcribe(code=sequence)
    transcribed_mrna_seq,non_coding = transcribed_seq_info["mrna"],transcribed_seq_info["noncode"]
    all_reading_frames = reading_frames_assembler(transcribed_mrna_seq,non_coding)
    gene_lenght = [amino_acid_counter(spliting(seqs)) for seqs in all_reading_frames]
    print(max(gene_lenght),len(gene_lenght))
    return max(gene_lenght)
 
if __name__ == "__main__":
    main(sys.argv[1])



