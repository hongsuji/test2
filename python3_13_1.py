import sys

#print(sys.argv)

sample = sys.argv[1]

print("bwa"+sample+"_1.fastq.gz"+sample"_2.fasta.gz")
print("picard MarkDuplicate" +sample+".bam")
