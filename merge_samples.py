import sys



# Out of the sequencer the sequences are separeted by lanes (L1-4)
# Merge them with zcat


CLONES = ["Sample1","Sample2","Sample3","Sample4", \
          "SampleA","SampleB","SampleC","SampleD"]

# Prepare the bash executable
with open ('merge_clones.sh','w') as f:
    f.write('#!/bin/bash\n')

    for number,clone in enumerate(CLONES):
        # Merge all the forward reads for # TODO: his particular clone
        fwfnames = [clone + "_S" + str(1 + number) + "_L00" + str (1 + n) + \
                    "_R1_001.fastq.gz" for n in range(4)]
        outfname = clone + "_Fw_fastq.gz"
        s = " "
        f.write(s.join(["zcat ", s.join(fwfnames), ">", outfname, "&\n"]))
        
        # Merge all the reverse reads for this particular clone
        Revfnames = [clone + "_S" + str(1 + number) + "_L00" + str (1 + n) + \
              "_R2_001.fastq.gz" for n in range(4)]
        outfname = clone + "_Rev_fastq.gz"
        s = " " 
        f.write(s.join(["zcat ", s.join(Revfnames), ">", outfname, "&\n"]))
