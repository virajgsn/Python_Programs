i = "INSTAGRAM"  # Define a string

print(i[9:5:-1])     # [::-1] = reverse 'RAM' → 'MAR'


print(len(i))    # Prints the length of the string → 9

print(i[:2:-1])   # Reversed = 'MARGAT'


print(i[0:9:2][::-1])  # [: :-1] Reversed = 'MRASI' 

print(i[::2][::-1])    # Reversed = 'MRASI'    

print(i[3:6:-1][::-1])    #blank 

print(i[9:0:-1][::-1])   # Reversed = 'NSTAGRAM'

print(i[::-1])     # Full reverse of the string, then reverse again → original string = 'INSTAGRAM'   

print(i[::-2][::-1])      # Then reversed = 'ISARM' 

print(i[-1:-9:-1][::-1])  # Reversed = 'ISTAGRAM' 

