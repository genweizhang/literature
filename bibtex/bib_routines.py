import os, sys
write = sys.stdout.write

def get_entry_info(bibfile):
	
	bibf = open(bibfile, "r")
	entries = []
	blocks  = []
	icount = 0
	for line in bibf.readlines():
		cols  = line.split()
		ncols = len(cols)
		if ncols == 1 and cols[0][0:1] == '@':
			entry_name = line[line.rfind("{")+1:-2]
			#print("entry_name:", entry_name)
			entries.append(entry_name)
			blocks.append(icount+1)
		elif ncols == 1 and cols[0] == '}':
			blocks.append(icount+1)
		icount += 1

	return entries, blocks

def get_entryname(bibfile):
	command1 = 'grep @ ' + bibfile + ' > tmp_file'
	os.system(command1)
	file = open("tmp_file", "r")
	entries = []
	for line in file.readlines():
		entry_name = line[line.rfind("{")+1:-2]
		#print("entry_name:", entry_name)
		entries.append(entry_name)

	return entries

def get_entry_block(bibfile, istart, iend):

	bibf = open(bibfile, "r")
	entry_block = []
	for line in bibf.readlines()[istart:iend+1]:
		entry_block.append(line)

	return entry_block

