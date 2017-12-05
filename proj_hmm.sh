#!/usr/bin/env bash

for f in *.sequences.fasta
do
    /Users/sampathkumarbalaji/Downloads/muscle3.8.31_i86darwin64 -in $f -out ${f%.fasta}.align   
    echo $f 
done

for f in *.align
do

	/Users/sampathkumarbalaji/Downloads/hmmer-3.1b2-macosx-intel/binaries/hmmbuild ${f%.align}.hmm $f
	echo $f
done

for f in *.hmm
do
    for fasta_file in *_translated.fasta
    do
	    /Users/sampathkumarbalaji/Downloads/hmmer-3.1b2-macosx-intel/binaries/hmmsearch --tblout ${f%.hmm}.hits $f $fasta_file
	    echo "$f"
	    cat ${f%.hmm}.hits | grep -v "#" | awk '{print $1,$3,$5}' >> ${f%.hmm}.table
    done
done

mkdir align/; mv *.align $_
mkdir hmm/; mv *.hmm $_
mkdir hits_table/; mv *.hits *.table $_


#/Users/sampathkumarbalaji/Downloads/hmmer-3.1b2-macosx-intel/binaries/hmmbuild sporecoat.hmm sporecoat.align
#/Users/sampathkumarbalaji/Downloads/hmmer-3.1b2-macosx-intel/binaries/hmmbuild transporter.hmm transporter.align
