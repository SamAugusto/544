from Bio.Data import CodonTable
def seq_transcribe(code: str = 'ACGTGAATCGATAATA' ) -> dict:
    # reversing code strand 
    reverse_code: str = code[::-1]
    # defining codon table for protein string
    codon_table = CodonTable.unambiguous_rna_by_name["Standard"]
    # Complementing strand
    noncode_var: str = "".join([ "A" if base  == "T" else ( "T" if base == "A" else ( "G" if base == "C" else ( "C" if base == "G"
                    else "N"))) for base in reverse_code])
    # Using coding strand and replacing thymine wiht uracil to define mrna strand
    mrna_var: str = code.replace("T","U")
    print(mrna_var)
    ## Spliting Codons
    codon_str:str = ""
    i:int = 3
    while i <len(mrna_var) -3:
        if i == len(mrna_var)-3:
            codon_str += (mrna_var[i-3:i])
        else:
            codon_str += (mrna_var[i-3:i]+" ")
        i +=3
    print(codon_str)
    codon_map = codon_str.split(" ")
    print(codon_map)
    ptn:str = "".join([codon_table.forward_table[codon] if codon in codon_table.forward_table.keys() else "*" if codon in codon_table.stop_codons else "ERROR" for codon in codon_map ])




    transcribe = { "noncode" : noncode_var,"mrna":mrna_var,"ptn":ptn}
    return transcribe

if __name__ == "__main__":
   print( seq_transcribe())

