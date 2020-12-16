
class Generales:

    #rotaciones
    def srl(self, t1):
        t2 = t1.izquierda
        t1.izquierda = t2.derecha
        t2.derecha = t1
        t1.nivel = self.maxi(self.nivel(t1.izquierda), self.nivel(t1.derecha))+1
        t2.nivel = self.maxi(self.nivel(t2.izquierda), t1.nivel)+1
        return t2

    def srr(self, t1):
        t2 = t1.derecha
        t1.derecha = t2.izquierda
        t2.izquierda = t1
        t1.nivel = self.maxi(self.nivel(t1.izquierda), self.nivel(t1.derecha))+1
        t2.nivel = self.maxi(self.nivel(t2.izquierda), t1.nivel)+1
        return t2

    def drl(self, tmp):
        tmp.izquierda = self.srr(tmp.izquierda)
        return self.srl(tmp)

    def drr(self, tmp):
        tmp.derecha = self.srl(tmp.derecha)
        return self.srr(tmp)

    def jalarValN(self, vali):
        return sum(ord(x) for x in vali)

    def nivel(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.nivel
        
    def maxi(self, r, l):
        return (l,r)[r>l]

    def leMenor(self, tmp):
        while tmp.izquierda != None:
            tmp = tmp.izquierda
        return tmp  

    def nHojas(self, tmp):
        nHojas = 0
        if tmp.izquierda != None:
            nHojas += 1
        if tmp.derecha != None:
            nHojas += 1
        return nHojas

g = Generales()