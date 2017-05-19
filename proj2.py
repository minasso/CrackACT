import my_fcns,re,bs4

pat=re.compile(r'uhash')


with open('alist4.txt', 'r') as rf:
	a = rf.read()
array=a.split('\n')
print(array)
i=0
while i<len(array):
	url=array[i]

	soup=my_fcns.makesoup(url) 
	for link in soup.find_all('a',href=pat):
		x=link.get('href')
		print(x)
		with open('alist4.txt', 'a') as wf:
			wf.write('http://www.crackact.com'+str(x))
			wf.write('\n')


	i+=1

