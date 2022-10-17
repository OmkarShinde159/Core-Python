# multiple inheritance
'''
class parent1:
    body
class parent2:
    body
class child(parent1,parent2):
    body
'''
class mother:
    def m(self,m_name):
        self.m_name = m_name
        print(self.m_name)
class father:
    def f(self,f_name):
        self.f_name = f_name
        print(self.f_name)
class child(father,mother):
    def c(self,c_name):
        self.c_name = c_name
        print(self.c_name)

    def name(self):
        print(self.f_name,self.m_name,self.c_name)

ch = child()
ch.c("Python")
ch.f("Programming")
ch.m("Language")
ch.name()

ch1 = child()
ch1.c("Java")
ch1.f("Programming")
ch1.m("Language")
ch1.name()

# example 2
class father:
    def f(self,f_name):
        self.f_name = f_name

class mother:
    def m(self,m_name) -> None:
        self.m_name = m_name

class son(father, mother):
    def s(self,s_name):
        self.s_name = s_name
       
    def name(self):
        print(self.s_name, self.f_name, self.m_name)

son1 = son()
son1.f("Father")
son1.m("Mother")
son1.s("Son")
son1.name()



