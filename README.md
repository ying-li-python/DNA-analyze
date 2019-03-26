# DNA analysis for primer construction 

Tired of performing DNA sequence requirements for primer construction by hand? This folder contains a Python script that reports the length, %GC content, and reverse complementary sequence of a DNA sequence. 

## Getting Started
You will need to download this folder, and in command line, route to this folder using cd command and run this script. 

```
git clone https://github.com/ying-li-python/DNA_analyze.git
cd DNA_analyze
python DNA_analyze.py
```

The script will run and will ask you to paste a DNA sequence. 
```
Please paste a DNA sequence (5'->3'): 
```

Output:  
<img src="https://raw.githubusercontent.com/ying-li-python/DNA_analyze/master/Images/Example.png">

After printing the results, script will automatically asks the user if you would like to analyze another DNA sequence. 


### Errors 
If your DNA sequence contains a non-DNA letter, an error will pop-up and the script will not run.
```
This is not a valid DNA sequence! Please try again.  
```
### Methods 
We would like the script to show: 
- %GC content 
- Sequence length 
- Reverse complemntary sequence (5' -> 3')

For this script, we created nested for-loops and while loops, ```if else``` statements, ```.replace()``` and ```len()``` function. 

### Author 
- Ying Li 

### Acknowledgements 
- [Python for Biologists](https://pythonforbiologists.com/) by Dr. Martin Jones

