# get_taxonomy_lineage.py

Get full taxonomic lineage from NCBI with accession numbers

---

<br>

`get_taxonomy_lineage.py` is a python script (based on Biopython) to retrieve the full taxonomic lineage from Entrez database given a list of accession numbers. 

<br>

### Dependencies

+ Python 3.6.5
+ Biopython 1.72

<br>

### Usage 

`get_taxonomy_lineage.py` requires as input (`-i`) a text file with a list of accession numbers, the output (`-o`) file name (a text file that will be produced and it will contain the match between accession numbers and taxonomic lineage) and your e-mail address (`-e`) in order to connect to the Entrez database.   

	usage: get_taxonomy_lineage.py [-h] [-i INPUT] [-o OUTPUT] [-e EMAIL]

	Get full taxonomic lineage from NCBI with accession numbers

	optional arguments:
	  -h, --help  show this help message and exit
	  -i INPUT    input file with accession numbers
	  -o OUTPUT   output file with accession numbers-lineage
	  -e EMAIL    e-mail address in order to get access to NCBI

<br>

### Example

Download the script available at `script/get_taxonomy_lineage.py`. Then, have a look into the **example** folder and try the following:

	python3 get_taxonomy_lineage.py \
			-i accession_numbers.txt \
			-o annotations.txt \
			-e antonio.sousa@ciimar.up.pt
			
			
Using as `input` the example given at `example/annotations.txt` it will generate the `output` text file **annotations.txt** that should have the same annotations as it appears in `example/annotations.txt`. 

<br>

>**Enjoy it** :blush: 

