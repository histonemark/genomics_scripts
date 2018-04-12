import sys
#import  pdb


# This script takes the 1 kb region upstream of the rightmost TSS or leftmost for each gene
# silent in Kc167 cells but active in mixed embryos ( the results of the reverse strand genes are #reversed in the imput file)


def write_line(chrom_prev,start_prev,end_prev,name_prev,score_prev):
    if score_prev > 0:
        strand = '+'
        out = (chrom_prev,str(int(start_prev)-1000),end_prev,name_prev,score_prev,strand)
    elif score_prev < 0:
        strand = '-'
        out = (chrom_prev,start_prev,str(int(end_prev)+1000),name_prev,score_prev,strand)
    sys.stdout.write('%s\t%s\t%s\t%s\t%s\t%s\n' % out)          
#pdb.set_trace()


with open(sys.argv[1]) as f:
    prevLine = "chr2L	3539251	3539252	FBgn0024244	17"
    for line in f:
        items = line.split()
        name = items[3]
        if name == prevLine.split()[3]:
            prevLine = line
            continue
        elif name != prevLine.split()[3]:
            items_prev = prevLine.split()
            name_prev  = items_prev[3]
            chrom_prev = items_prev[0]
            start_prev = items_prev[1]
            end_prev   = items_prev[2]
            score_prev = int(items_prev[4])
            prevLine = line
            write_line(chrom_prev,start_prev,end_prev,name_prev,score_prev)
            

