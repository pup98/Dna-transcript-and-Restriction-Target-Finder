class Custom(Exception):
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return f'The sequence: {self.string}, it is not a correct DNA sequence'

class Spelling_error(Exception):
    def __str__(self):
        return f'There is a spelling mistake or the enzyme is not present! Plz check'



class Sequence:
    transcription_table = {'A':'U', 'T':'A', 'C':'G' , 'G':'C'}
    
    restriction_dic = {'ECOR1': 'GAATTC', 'BAMH1':'GTTCCC', 'ECORV':'GATATC','PUV1': 'ATTC'}

    def __init__(self, seqstring):
        self.seqstring = seqstring.upper()

    def transcription(self):
        tt = ""
        for letter in self.seqstring:
            if letter in 'ATCG':
                tt += self.transcription_table[letter]
            
            else:
                raise Custom(self.seqstring)
            
        return tt
    
    def cutter(self, enz):
      
        enzyme_target = self.restriction_dic[enz]
        result = self.seqstring.count(enzyme_target)
        
        if result == 0:
            return 'Sorry no targets found'

        elif result >= 1:
            return result
     

user = input('Give a DNA string: ')
print('You can find targets for \nECOR1\nPUV1\nBAHM1\nECORV')

restriction_dic = {'ECOR1': 'GAATTC', 'BAMH1':'GTTCCC', 'ECORV':'GATATC','PUV1': 'ATTC'}
enzyme = input('Give the enzyme target u want to find: ')
if enzyme not in restriction_dic:
    raise Spelling_error

dangerous_virus = Sequence(user)

print('The input string is: ')
print(dangerous_virus.seqstring)

print('The corresponding mRNA is: ')
print(dangerous_virus.transcription())

print(f'Number of sites of {enzyme} is:', dangerous_virus.cutter(enzyme))