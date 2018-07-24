import os, sys
write = sys.stdout.write
from bib_routines import *

# source bib file
bibfile = sys.argv[1]
if bibfile[-3:] != 'bib':
	exit(-1)
print('source bibfile = ', bibfile)

#entry
entry = sys.argv[2]
print('entry = ', entry)

# target bib file
bibfile2 = sys.argv[3]
if bibfile2[-3:] != 'bib':
	exit(-1)
print('target bibfile = ', bibfile2)

entries, blocks = get_entry_info(bibfile)

if entry in entries:
	ientry = 0
	for k in range(0, len(entries)):
		if entry == entries[k]:
			ientry = k
			break
else: 
   print("Entry %s not in %s" % (entry, bibfile))

entry_block = get_entry_block(bibfile, blocks[2*ientry]-1, blocks[2*ientry+1]-1)

#print("entry_block=", entry_block)
for line in entry_block:
	write("   %s" % (line))

new_entry = 1
if os.path.isfile(bibfile2):
	if entry in get_entryname(bibfile2): 
		write("Entry %s already exists in %s\n" % (entry, bibfile2))
		new_entry = 0

if new_entry == 1:
	write("Entry %s is added to %s\n" % (entries[k], bibfile2))
	bibf2 = open(bibfile2, "a")
	for line in entry_block:
		bibf2.write("%s" % line)
	bibf2.write("\n")

	write("\n")


	
