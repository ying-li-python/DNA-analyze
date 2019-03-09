# this script is designed to analyze a DNA sequence continously 
# user will paste a DNA sequence 
 
# create a while loop  
repeat = "y"

while repeat == "y": 
	
	# asks user to paste a DNA sequence, will set to lower case for next line in script
	seq = input("Please paste a DNA sequence (5'->3'):").lower()

	# count the number of letters for a letter NOT in a DNA nucleotide
	invalid_dna = int(seq.count("q") + seq.count("w") + seq.count("e") + seq.count("r") + seq.count("y") + seq.count("u") + seq.count("i") + seq.count("o") + seq.count("p") + seq.count("s") + seq.count("d") + seq.count("f") + seq.count("h") + seq.count("j") + seq.count("k") + seq.count("l") + seq.count("z") + seq.count("x") + seq.count("v") + seq.count("b") + seq.count("n") + seq.count("m"))

	# if there are non-DNA letters, print error message
	if invalid_dna > 0: 
		print("\n This is an invalid DNA sequence! Please try again. \n")
	
	# if valid, then continue to analyze the DNA
	elif invalid_dna == 0:
		# capitalize dna in the sequence
		cap_sequence = seq.upper()

		# create variable to count the length of DNA sequence
		countseq = len(cap_sequence)

		# set values to calculate number of G's, A's, C's, T's
		G=0;
		C=0;
		A=0;
		T=0;
						
		# create for loop to calculate numbers of G's, A's, C's, T's in sequence 
		for line in cap_sequence: 
			for char in line: 
				if char == "G": 
					G+=1
				if char == "A":
					A+=1
				if char == "C":
					C+=1
				if char == "T": 
					T+=1

		# solution to calculate GC content 
		gc = (G+C+0. ) / (A+T+C+G+0. ) * 100
			
		# this is to create the complementary reverse sequence 	
		dna = cap_sequence
		A = dna.replace("A","X")
		B = A.replace("T","Y")
		C = B.replace("X","T")
		D = C.replace("Y","A")
		E = D.replace("G", "Z")
		F = E.replace("C","W")
		G = F.replace("Z","C")
		finaldna = G.replace("W","G")

		# print results 

		print("\n" + "Here are results --- \n"
						+" \n"
						+"Length: " + str(countseq) + " " + "bp" "\n"
						+"The GC content is: " + str(gc) +"%" + "\n"
						+" \n"
						+"The reverse complement is: " 
						+" \n"
						+"\n 5' " + dna + " 3' " + "\n 5' " + finaldna + " 3'"
						+"\n")
		if gc < 50: 
			print("NOTE: Your GC content is under 50%! Try another sequence.") 

		else:  
			print("Your GC content is over 50%!")
	
		if countseq > 22:
			print("NOTE: Your sequence is over 22 bp. It might be too long." + "\n")
		else: 
			if countseq < 18: 
				print("NOTE: Your sequence is under 18 bp. It might be too short." + "\n")
			elif countseq in range(18, 22): 
				print("Your sequence is within the recommended 18-22 bp range." + "\n")	

	# asks user if they want to analyze another DNA sequence		
	repeat = input("Do you want to analyze another DNA sequence (y/n)?")
			
		
		