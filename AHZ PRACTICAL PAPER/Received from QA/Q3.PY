#WRITNG IN FILE
fil=open('SENT.TXT','w')                                 #open file
n=input('how many lines you want to enter?')
for i in range(n):
    sentence=raw_input('enter sentence:')
    fil.write(sentence)                           #write in file
    fil.write('\n')
fil.close()                                       #closing file


#READING THE FILE
e,r=0,0
fil1=open('SENT.TXT','r')
read='  '                                   #initially storing in file
while read:
    read=fil1.readline()                   #reading file using readline
    c=read.lower()                         #converting all words to lower
    s=c.split(' ')                         #spliting using space
    for i in range (len(s)):
	if s[i]=='the':                    #counting no of the
	    e+=1
	elif s[i]=='to':                   #counting no of to
	    r+=1
print 'no of the in sent.txt is:',e
print 'no of to in sent.txt is:',r

#OUTPUT

how many lines you want to enter?3
enter sentence:we live in the 21st century
enter sentence:the to tooo that
enter sentence:lan wan the to sun
no of the in sent.txt is: 3
no of to in sent.txt is: 2

