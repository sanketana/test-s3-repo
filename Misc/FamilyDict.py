import json

Joshi_family = [
	{
		'name': 'Sidharth',
		'age' : 45,
		'profession' : 'rockstar coder'
	},

	{
		'name' : 'Nikunj',
		'age' : 10,
		'profession': 'budding coder'
	},

	{
		'name' : 'Mandhar',
		'age' : 16,
		'profession': 'fiery teen'
	}	
]

Bhardwaj_family = [
	{
		'name': 'Abhinav',
		'age' : 42,
		'profession' : 'champion coder'
	},

	{
		'name' : 'Advait',
		'age' : 9,
		'profession': 'junior coder'
	},

	{
		'name' : 'Siddhant',
		'age' : 6,
		'profession': 'baby coder'
	}	
]

Coder_families = [Joshi_family, Bhardwaj_family]

print(json.dumps(Coder_families,indent=4))