def greet(fx):
    def mfx(*args,**kargs):
        print("good morning")
        fx(*args,**kargs)
        print("welcome")
    return mfx

@greet
def Hello():
    print("Hello Anup")
Hello()

@greet
def sum(a,b):
    print(a+b)
sum(1,2)
