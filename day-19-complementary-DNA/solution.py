"""
Challenge: Complementary DNA
Source: freeCodeCamp
Date: 2025-10-25
Problem: Given a string representing a DNA sequence, return its complementary
    strand. DNA consists of the letters "A", "C", "G", and "T". The letters
    "A" and "T" complement each other, and the letters "C" and "G" complement
    each other.
Example: complementary_dna("ACGT") returns "TGCA"
"""

def complementary_dna(strand):
    pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(pairs[char] for char in strand)

# Tests
assert complementary_dna("ACGT") == "TGCA"
assert complementary_dna("ATGCGTACGTTAGC") == "TACGCATGCAATCG"
assert complementary_dna("GGCTTACGATCGAAG") == "CCGAATGCTAGCTTC"
assert complementary_dna("GATCTAGCTAGGCTAGCTAG") == "CTAGATCGATCCGATCGATC"
print("All tests passed!")

