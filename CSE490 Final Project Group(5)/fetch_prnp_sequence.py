from Bio import Entrez

def main():
    Entrez.email = "example@example.com"
    Entrez.tool = "fetch_prnp_protein"

    accession_id = "NP_000302"
    output_filename = "prnp_protein.fasta"

    with Entrez.efetch(
        db="protein",
        id=accession_id,
        rettype="fasta",
        retmode="text",
    ) as handle:
        fasta_data = handle.read()

    with open(output_filename, "w", encoding="utf-8") as fasta_file:
        fasta_file.write(fasta_data)

    print(f"Protein FASTA sequence saved to {output_filename}")

if __name__ == "__main__":
    main()
