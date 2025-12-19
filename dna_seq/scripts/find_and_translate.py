import transcribe_dna
import sys
def amino_acid_counter(sequence:list)-> int:
# Counting logic
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
    splitted_seq= []

    index_i = 0
    index_f = 3

    while index_f <= len(sequence):
        splitted_seq.append(sequence[index_i:index_f])
        index_i += 3
        index_f += 3
    return splitted_seq

def main(test_seq):
    sequence = test_seq
    transcribed_seq_info = transcribe_dna.seq_transcribe(code=sequence)
    transcribed_mrna_seq = transcribed_seq_info["mrna"]
    splitted_transcribed_seq = spliting(transcribed_mrna_seq)
    print(amino_acid_counter(splitted_transcribed_seq))
    return amino_acid_counter(splitted_transcribed_seq)
 
if __name__ == "__main__":
    main(sys.argv[1])



