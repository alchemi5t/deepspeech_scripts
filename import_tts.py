from os import path
import glob

files=sorted(glob.glob("*.wav"),key=lambda x:int(x.split(".")[0]))  # sorting numerically
sizes=[]
for i in files:
	p=path.join("./",i)
	sizes.append(path.getsize(p))
op=open("train.csv","a")

f=open("metadata.csv")#metadata.csv has the format = /path/to/.wavs|transcription  e.g., ./location/1.wav|अंगिरस् पहा ऋषि
s=f.readlines()
s=[i[:-1].split("|") for i in s]



# convert this into format /path/to/file,filesize,transcript
for idx,i in enumerate(s):
	i.insert(1,sizes[idx])                 
# write to file
# DO NOT FORGET TO ADD THE HEADERS TO THE FINAL FILE( wav_filename,wav_filesize,transcript ) to the output file
for i in s:
	op.write(",".join([str(j) for j in i]))
	op.write("\n")
