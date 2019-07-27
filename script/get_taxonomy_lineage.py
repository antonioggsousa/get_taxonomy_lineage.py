import argparse
from Bio import Entrez
import re


parser = argparse.ArgumentParser(description='Get full taxonomic lineage from NCBI with accession numbers')
											
parser.add_argument('-i', action="store", dest="input", type=str, help='input file with accession numbers')
parser.add_argument('-o', action="store", dest="output", type=str, help='output file with accession numbers-lineage')
parser.add_argument('-e', action="store", dest="email", type=str, help='e-mail address in order to get access to NCBI')

args = parser.parse_args()


Entrez.email = args.email  

output_file = open(args.output, 'w')
file_ids = open(args.input, 'r')
ids_list = file_ids.readlines()

ids_parsed = [] 

for acc_id in ids_list: 
    ids_parsed.append(acc_id.replace("\n", ""))



lineage = []

for acc_id in ids_parsed:
    seqio = Entrez.efetch(db="protein", id=acc_id, retmode="xml")
    seqio_read = Entrez.read(seqio)
    seqio.close()
    output_file.write(acc_id + '\t' + seqio_read[0]['GBSeq_taxonomy'] + '\n')
