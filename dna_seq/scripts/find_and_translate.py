from transcribe_dna import seq_transcribe
def seq_findgene(sequence:str)-> str:
    transcribed_seq:dict = seq_transcribe(sequence)

    forward,reverse= transcribed_seq["mrna"], transcribed_seq["noncode"].replace("T","U")
    reading_frames_indexes:tuple = (0,1,2)
    reading_frames:list = []

    for indexes in reading_frames_indexes: # adding all possible reading frames to a list
        reading_frames.append(forward[indexes:])
        reading_frames.append(reverse[indexes:])


    codon_frames:list = [] 
    for seq in reading_frames:
        idx:int = 0
        sub_codon_frames:list = []
        while idx <= len (seq):
            if len(seq[idx:idx+3])==3:
                sub_codon_frames.append(seq[idx:idx+3])
            idx +=3
        codon_frames.append(sub_codon_frames)
    

    max = 0
    max_seq = ""
    stop_codons = {"UAA","UAG","UGA"}
    for codon_lst in codon_frames:
        if "AUG" in codon_lst:
            start = False
            count = 0
            codon_count = ""
            for codon in codon_lst:
                if start and (codon not in stop_codons):
                    count += 1
                    codon_count += codon
                else:
                    if not start:
                        if codon == "AUG":
                            start = True
                            count+=1
                            codon_count +=codon
                            continue
                        else:
                            continue
                    elif codon in stop_codons:
                        if max < count:
                            max = count
                            max_seq = codon_count+codon
                            start = False
                            count = -1
                            codon_count = ''
                            continue
                        else:
                            codon_count = ''
                            count = -1
                            start = False
                            continue
                    else:
                        continue


        else:
            continue
    return seq_transcribe(max_seq)["ptn"]



   

    






    






