# DNA analysis for primer construction 

Tired of performing DNA sequence requirements for primer construction by hand? This folder contains a Python script that reports the length, %GC content, and reverse complementary sequence of a DNA sequence. 

## Getting Started
You will need to download this folder, and in command line, route to this folder using cd command and run this script. 

Example: 
```
git clone https://github.com/ying-li-python/DNA_analyze.git
cd DNA_analyze
python DNA_analyze.py
```

The script will run and will ask you to paste a DNA sequence: 
```
Please paste a DNA sequence (5'->3'): 
```

Demo results:  
<img src="https://raw.githubusercontent.com/ying-li-python/DNA_analyze/master/Images/Example.png">

### Errors 
If your DNA sequence contains a non-DNA letter, the script will give you an error 
```
This is not a valid DNA sequence! Please try again.  
```

### Author 
- Ying Li - *wrote the script*  

### Acknowledgements 
- [Python for Biologists](https://pythonforbiologists.com/) by Dr. Martin Jones

