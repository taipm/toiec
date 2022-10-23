from dataclasses import dataclass, field

from DbObject import DbObject

@dataclass
class Word(DbObject):
    Word:str
    Meaning:str
    
    def save(self):
        super().db.Words.insert_one({'Word':self.Word, 'Meaning':self.Meaning})
        #super().db.Words.save


word = Word(Word='Hello',Meaning='Xin chào')
word.save()