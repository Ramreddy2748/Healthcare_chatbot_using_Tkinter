import File_diesies_desc
import File_symptom_precaution 
class Searching:
    def __init__(self,diesis_desc,diesis_prec):
        self.diesis_desc_data = diesis_desc
        self.diesis_prec_data = diesis_prec

    # get Description of Desise 
    def getDescription(self,disease):
        return self.diesis_desc_data[disease]

    # get Precaution of Desise 
    def getPrecaution(self,disease):
        return self.diesis_prec_data["Durg reaction"] + self.diesis_prec_data[disease]
    
    def constants(self,numb):
        if int(numb) > 10:
            return "Consult any Nearest Hospital and Stop Taking Drugs"
        else:
            return "Mild Desies Not to be Worry"

model = Searching(File_diesies_desc.diesis_desc,File_symptom_precaution.diesis_prec)

