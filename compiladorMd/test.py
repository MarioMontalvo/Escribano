import mdparser


def main():
	
	f = open('../index1.md','r')
	texto  = f.read()
	f.close()
	parser = analizadorSintactico.parser().parse(texto)
	print parser
	
	
if __name__ == '__main__':

	main()
