import os, sys
write = sys.stdout.write
from bib_routines import *

# source bib file
bibfile = sys.argv[1]
if bibfile[-3:] != 'bib':
	exit(-1)

print('source bibfile = ', bibfile)

entries, blocks = get_entry_info(bibfile)
#print('entries=', entries)
#print('blocks=', blocks)

for k in range(0, len(entries)):
	entry_block = get_entry_block(bibfile, blocks[2*k]-1, blocks[2*k+1]-1)
	#print("entry_block=", entry_block)
	for line in entry_block:
		write("   %s" % (line))

	bib2 = input("\nWhich bib file should this new entry go to? ")
	if bib2 == ' ': bib2 = bib2[:-1]
	#print("bib2=", bib2)
	bibfile2 = bib2 + ".bib"
	new_entry = 1
	if os.path.isfile(bibfile2):
		if entries[k] in get_entryname(bibfile2): 
			write("Entry %s already exists in %s\n" % (entries[k], bibfile2))
			new_entry = 0

	if new_entry == 1:
		write("Entry %s is added to %s\n" % (entries[k], bibfile2))
		bibf2 = open(bibfile2, "a")
		for line in entry_block:
			bibf2.write("%s" % line)
		bibf2.write("\n")

	write("\n")



	
	


	
