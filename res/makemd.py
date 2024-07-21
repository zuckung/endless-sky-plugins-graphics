import os

def makemd():
	mds = []
	subfolders = []
	if os.path.isfile('images.zip'):
		os.remove('images.zip')
	aifolder = os.listdir('images/')
	aifolder = sorted(aifolder)
	for ai in aifolder:
		mds.append(ai)
		with open('res/md/' + ai +'.md', 'w') as output:
			if os.path.isdir('images/' + ai + '/'):
				sub1 = os.listdir('images/' + ai + '/')
				sub1 = sorted(sub1)
				output.writelines('images/' + ai + '\n')
				output.writelines('<table>\n')
				pos = 0
				for each in sub1:
					if os.path.isfile('images/' + ai + '/' + each):
						pos +=1
						pic = '		<td><img src="https://github.com/zuckung/endless-sky-plugins-graphics/blob/main/images/' + ai + '/' + each + '?raw=true" width="200"><br>\n'
						pic2 = each + '</td>\n'
						if pos%3 == 1%3:
							output.writelines('	<tr>\n')
							output.writelines(pic)
							output.writelines(pic2)
						elif pos%3 == 2%3:
							output.writelines(pic)
							output.writelines(pic2)
						elif pos%3 == 3%3:
							output.writelines(pic)
							output.writelines(pic2)
							output.writelines('	</tr>\n')
					if os.path.isdir('images/' + ai + '/' + each):
						subfolders.append('images/' + ai + '/' + each + '/')
					if sub1.index(each)+1 == len(sub1):
						if pos%3 == 1%3:
							output.writelines('		<td></td>\n')
							output.writelines('		<td></td>\n')
							output.writelines('	</tr>\n')
							output.writelines('</table>\n')
							output.writelines('\n')
						elif pos%3 == 2%3:
							output.writelines('		<td></td>\n')
							output.writelines('	</tr>\n')
							output.writelines('</table>\n')
							output.writelines('\n')
						else:
							output.writelines('</table>\n')
							output.writelines('\n')
				pos = 0
				for subfolder in subfolders:
					sub2 = os.listdir(subfolder)
					sub2 = sorted(sub2)
					output.writelines(subfolder + '\n')
					output.writelines('<table>\n')
					for each2 in sub2:
						pic = '		<td><img src="https://github.com/zuckung/endless-sky-plugins-graphics/blob/main/' + subfolder + each2 + '?raw=true" width="200"><br>\n'
						pic2 = each2 + '</td>\n'
						pos +=1
						if pos%3 == 1%3:
							output.writelines('	<tr>\n')
							output.writelines(pic)
							output.writelines(pic2)
						elif pos%3 == 2%3:
							output.writelines(pic)
							output.writelines(pic2)
						elif pos%3 == 3%3:
							output.writelines(pic)
							output.writelines(pic2)
							output.writelines('	</tr>\n')
					if sub2.index(each2)+1 == len(sub2):
						if pos%3 == 1%3:
							output.writelines('		<td></td>\n')
							output.writelines('		<td></td>\n')
							output.writelines('	</tr>\n')
							output.writelines('</table>\n')
							output.writelines('\n')
						elif pos%3 == 2%3:
							output.writelines('		<td></td>\n')
							output.writelines('	</tr>\n')
							output.writelines('</table>\n')
							output.writelines('\n')
						else:
							output.writelines('</table>\n')
							output.writelines('\n')
				subfolders= []
	with open('res/template.txt', 'r') as input:
		template = input.readlines()
	with open('README.md', 'w') as target:
		target.writelines(template)
		for each in mds:
			target.writelines('<a href="res/md/' + each + '.md">' + each + '.md</a><br>')



makemd()
