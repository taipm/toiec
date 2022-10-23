from dataclasses import dataclass, field
from translate import Translator
from DbObject import DbObject

class Word(DbObject):    
    def __init__(self,word) -> None:
        super().__init__()        
        self.word = word
        self.meaning = self.translate()
                
    def translate(self):
        translator = Translator(to_lang="vi")
        translation = translator.translate(self.word)
        return translation
    
    def is_exits(self):
        query = {'Word':self.word}
        find = super().db.Words.find(query)
        print(find.next())
        if(find is None):
            return False
        return True
    
    def save(self):
        if(not self.is_exits()):
            super().db.Words.insert_one({'Word':self.word, 'Meaning':self.meaning})
            print('Inserted')
        else:
            query = {'Word':self.word}
            command = { "$set": { "Word": self.word, "Meaning":self.meaning}}            
            super().db.Words.update_one(query,command)
            print('Updated')
    
            
word = Word(word='Hi')
print(word.is_exits())
#word.save()