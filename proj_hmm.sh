#!/usr/bin/env bash

for f in *.sequences.fasta
do
    ../muscle3.8.31_i86darwin64 -in $f -out ${f%.fasta}.align   
    echo $f 
done

for f in *.align
do

	../hmmbuild ${f%.align}.hmm $f
	echo $f
done

for f in *.hmm
do
    for fasta_file in *_translated.fasta
    do
	    ../hmmsearch --tblout ${f%.hmm}.hits $f $fasta_file
	    echo "$f"
	    cat ${f%.hmm}.hits | grep -v "#" | awk '{print $1,$3,$5}' >> ${f%.hmm}.table
    done
done

mkdir align/; mv *.align $_
mkdir hmm/; mv *.hmm $_
mkdir hits_table/; mv *.hits *.table $_


