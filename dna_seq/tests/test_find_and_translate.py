
def test_no_aug_present():
    """Logic should stay at 0 if no start codon exists."""
    assert main("CCCTTTGGGAAA") == 0

def test_aug_but_no_stop():
    """If there is a start but no stop, max_count remains 0 per your logic."""
    assert main("ATGGGGCCCCAA") == 0

def test_standard_short_gene():
    """ATG + 1 codon + TAA (Stop). Result should be 1."""
    # Codons: [ATG(start), CGT(1), TAG(2), TAA(stop)]
    # Wait: In your current loop, TAG is counted before TAA is hit.
    # Result: 2
    assert main("ATGCGTTAA") == 1

def test_immediate_stop():
    """ATG followed immediately by TAA. Count should be 0."""
    # [ATG, TAA]
    assert main("ATGTAA") == 0

def test_longest_of_two_genes():
    """First gene has 1 amino acid, second has 2. Should return 2."""
    # Gene 1: [ATG, CGT, TAG] -> Count: 1
    # Gene 2: [ATG, GGG, CCC, TGA] -> Count: 2
    assert main("ATGCGTTAGATGGGGCCCTGA") == 2

def test_nested_start_codons():
    """The second ATG is counted as an amino acid (Methionine)."""
    # [ATG(start), ATG(1), GGG(2), TAA(stop)]
    assert main("ATGATGGGGTAA") == 2

def test_all_three_stop_types():
    """Ensures TAA, TAG, and TGA all trigger the stop logic."""
    # [ATG, CCC, STOP]
    assert main("ATGCCCTAA") == 1
    assert main("ATGCCCTAG") == 1
    assert main("ATGCCCTGA") == 1

def test_junk_at_beginning():
    """Logic ignores everything before the first ATG."""
    # CCC, GGG, AAA, [ATG, GGG, TAA]
    assert main("CCCGGGAAAATGGGGTAA") == 1
