import os

bpms = ['90bpm', '95bpm', '100bpm', '105bpm', 
		'110bpm', '115bpm','120bpm', '125bpm',
		'130bpm']
		
musicalKeys = [ 'c', 'cm', 'c#', 'c#m', 
				'd', 'dm', 'd#', 'd#m',
				'e', 'em',
				'f', 'fm', 'f#', 'f#m',
				'g', 'gm', 'g#', 'g#m',
				'a', 'am', 'a#', 'a#m',
				'b', 'bm']
						
instruments = ['drums', 'bass', 'harms1',
			  'harms2', 'melody']

for i in bpms:
	cmd1 = 'mkdir '+i
	os.system(cmd1)
	for u in musicalKeys:
		cmd2 = 'mkdir '+i+'/'+u 
		os.system(cmd2)
		for b in instruments:
			cmd3 = 'mkdir '+i+'/'+u+'/'+b
			os.system(cmd3)
	
