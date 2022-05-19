import turtle as tp
tp.color('black')

def caraFormato():
    tamanhoDasOrelhas = 65

    tp.begin_fill()
    tp.circle(50)
    tp.end_fill()
    
    tp.setposition(-30,100)
    tp.dot(tamanhoDasOrelhas)
    tp.setposition(30,100)
    tp.setx(30)
    tp.dot(tamanhoDasOrelhas)

    tp.setposition(-15,55)
    tp.dot(55,"white")
    tp.setposition(15,55)
    tp.dot(55,"white")

    tp.setposition(0,40)
    tp.dot(75,"white")

def rostoFormato():
    tamanhoDosOlhos = 25
    
    tp.setposition(-20,55)
    tp.dot(tamanhoDosOlhos,"black")

    tp.setposition(20,55)
    tp.dot(tamanhoDosOlhos,"black")

caraFormato()
rostoFormato()

tp.done()
