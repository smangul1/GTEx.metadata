import csv
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('inFile', help='matrix from GTEX')
ap.add_argument('out', help='file with genes expressed in brain')
args = ap.parse_args()



file=open("../data/brain.samples.txt","r")
reader=csv.reader(file)
brain_samples=set()


for line in reader:
    brain_samples.add(line[0])



print ("Number of brain samples",len(brain_samples))

file.close()

#------

file=open(args.inFile)
reader=csv.reader(file,delimiter="\t")
row1 = next(reader)
row2 = next(reader)
row3 = next(reader)

print ("Number of GTEX samples",len(row3))


index_number_brain_samples=[]


k=0
for sample in row3:
    if sample in brain_samples:
        index_number_brain_samples.append(k)
    k+=1


fileOut=open(args.out,"w")




for line in reader:
    sum=0.0
    n=0
    gene_id=line[0]
    gene_name=line[1]
    for i in index_number_brain_samples:
        count=int(line[i])
        if count>5:
            n+=1
        sum+=int(line[i])


    fileOut.write(gene_id+","+gene_name+","+str(n)+","+str(float(n/len(brain_samples))))
    fileOut.write("\n")

file.close()



