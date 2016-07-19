with open('REVISEDPUMS5_36.txt') as myfile:
    count = sum(1 for line in myfile)

with open('REVISEDPUMS5_36.txt') as myfile:
    count1 = sum(1 for line in myfile if line.rstrip().startswith('p') or line.rstrip().startswith('P'))


with open('REVISEDPUMS5_36.txt') as myfile:
    count2 = sum(1 for line in myfile if line.rstrip('\n'))






print count, count1, count2