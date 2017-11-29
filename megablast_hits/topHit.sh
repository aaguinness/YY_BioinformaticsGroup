for file in *.HitTable.csv
	do
		cat $file | head -n1 >> topHits.csv
	done

