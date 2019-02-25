codonToProtein = {"AUG": "Methionine",
                  "UUU": "Phenylalanine",
                  "UUC": "Phenylalanine",
                  "UUA": "Leucine",
                  "UUG": "Leucine",
                  "UCU": "Serine",
                  "UCC": "Serine",
                  "UCA": "Serine",
                  "UCG": "Serine",
                  "UAU": "Tyrosine",
                  "UAC": "Tyrosine",
                  "UGU": "Cysteine",
                  "UGC": "Cysteine",
                  "UGG": "Tryptophan",
                  "UAA": "STOP",
                  "UAG": "STOP",
                  "UGA": "STOP"}
codonLength=3

def proteins(strand):

    # Logic to make sure codon strand length is correct not needed for
    # current unit test suite
    if len(strand) % codonLength != 0:
        raise ValueError(
            f"Expected Codon strand to be a facotor of 3 characters long actuall length: {len(strand)}"
        )
    strand = [strand[codon:codon + codonLength] for codon in range(0, len(strand), codonLength)]
    list = [codonToProtein[item] for item in strand]

    # This is to reduce logic statements and allow list.index to always work
    list.append("STOP")
    return list[:list.index("STOP")]
