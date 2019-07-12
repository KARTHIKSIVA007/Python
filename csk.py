csk=input()
if((csk>='a' and csk<='z') or (csk>='A' and CSK<='Z')):
  csk=csk.lower()
  if(csk=='a' or csk=='e' or csk=='i' or csk=='o' or csk=='u'):
     print("Vowel")
  else:
     print("Consonant")
else:
    print("Special Characters")
    
