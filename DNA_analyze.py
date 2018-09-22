#this script is to make a continuous loop for DNA analysis
 
repeat = True 
while repeat:  
	if raw_input("Do you want to analyze a DNA sequence? Enter y/n:") == "n":
		print("\n"+ "Goodbye!" + "\n")
		break
	else: 	
		seq = raw_input("Please paste your DNA sequence (5'->3'):").lower()
		invalid_dna = seq.count("q") + seq.count("w") + seq.count("e") + seq.count("r") + seq.count("y") + seq.count("u") + seq.count("i") + seq.count("o") + seq.count("p") + seq.count("s") + seq.count("d") + seq.count("f") + seq.count("h") + seq.count("j") + seq.count("k") + seq.count("l") + seq.count("z") + seq.count("x") + seq.count("v") + seq.count("b") + seq.count("n") + seq.count("m")
		
		if invalid_dna > 0: 
			print("\n This is an invalid DNA sequence! Please try again. \n")
				
    	if invalid_dna <= 0:
			sequence2 = seq.upper()
			countseq = len(sequence2)
				
			G=0;
			C=0;
			A=0;
			T=0;
							
			for line in sequence2: 
				for char in line: 
					if char == "G": 
						G+=1
					if char == "A":
						A+=1
					if char == "C":
						C+=1
					if char == "T": 
						T+=1
			
			gc = (G+C+0. ) / (A+T+C+G+0. ) * 100
				
			dna = sequence2
			A = dna.replace("A","X")
			B = A.replace("T","Y")
			C = B.replace("X","T")
			D = C.replace("Y","A")
			E = D.replace("G", "Z")
			F = E.replace("C","W")
			G = F.replace("Z","C")
			finaldna = G.replace("W","G")
	
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
				if countseq in range(18, 22): 
					print("Your sequence is within the recommended 18-22 bp range." + "\n")	
				
		
			
		
		