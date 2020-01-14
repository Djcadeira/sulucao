from time import sleep

class Limpador:
    def __init__(self):
        self.info1 = self.arq = open('page1-1000.txt', 'r')
        print('<Limpador iniciado>')
        self.get_name1()
        self.contador = int
        
    def get_name1(self):
        print('<GET NAME 1>')
        sleep(0.50)
        while True:
            print('<WHILE GET NAME 1>')
            sleep(0.50)
            self.info1 = self.arq.readline()
            
            
            if self.info1.find('Nome:') != -1:
                
                            
                if len(self.info1[5:]) == 1:
                    #print("\033[31m=======================", end='\033[m ')
                    #print(f"len {len(self.info1[5:])} info1 {self.info1[5:]}")
                    self.get_name2()
                    break
                    
                elif self.info1.find('Nascimento:') != -1:
                    self.get_name2()
                    
                else:     
                    #print("\033[32m",self.info1[6:],"\033[m")
                    self.get_number()
                    break
                
        print('==='*50)  
        sleep(0.50)             
                
              
    def get_name2(self):
        print('<GET NAME 2>')
        sleep(0.50)
        LastInfo1 = self.info1
        self.info1 = self.arq.readline()
        
        if self.info1.find('Nascimento:') != -1:
            self.get_name3()
            
        else:
            #print("\033[32m",self.info1)
            self.get_number()
            
        
    def get_name3(self):
        print('<GET NAME 3>')
        self.info1 = self.arq.readline()
        self.info1 = self.arq.readline()
        #print("\033[35m",self.info1)
        self.get_number()
        
        
    def get_number(self):
        print('<GET NUMBER>')
        sleep(0.50)
        self.info2 = self.arq.readline()
        while True:
            print('<WHILE GET NUMBER>')
            sleep(0.50)
            if self.info2.find('Telefones:') != -1:
                self.info2 = self.arq.readline()
                self.info2 = self.arq.readline()
                #print(self.info2)
                self.cliente()
                break
                
            else:
                self.info2 = self.arq.readline() 
        
        try:
            self.clean()
            self.get_name1()
            print(self.info1, self.info2)
            print('<TRY>')
            
        except:
            print(self.info1, self.info2)
            print('<ExCEPT>')
            print('+++FIM+++')
            
    def cliente(self):
        print(f'<CLIENTE>')
        
        if self.info1.find('Nome:') != -1:
            info = f'Nome: {self.info1[6:]} Telefone: {self.info2}'
            print(info)
            save = open('1000.txt', 'a')
            save.write(info)
            save.close()
            
            self.clean()
        else:
            info = f'Nome: {self.info1} Telefone: {self.info2}'
            print(info) 
            self.clean()
    
    def clean(self):
        self.info1 = ''
        self.info2 = ''    

sys = Limpador()
