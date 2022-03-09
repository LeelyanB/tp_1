


class nombreSyracuse:

  def __init__(self, nom): # on suppose que le fichier contient qu'un seul nombre
      self.nom = nom
      self.contenue = 0
  
  def recuperation(self):
     fichier = open(self.nom,"r")
     self.contenue = fichier.read()
     self.contenue = int(self.contenue)
     print(self.contenue)
     fichier.close()
     

  def operation(self): 
    
        l = []
        while self.contenue!=1:
          if (self.contenue%2)==0:
              self.contenue= self.contenue/2
          else:
            self.contenue=self.contenue*3+1
          l.append(self.contenue,)
        fichier =open(self.nom,"w")  
        for i in l :
         i = str(i) + " "    
         fichier.write(i)
        fichier.close()

nbr = nombreSyracuse(input("fichier"))
nbr.recuperation()
nbr.operation()
