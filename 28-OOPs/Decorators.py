def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Exit")
    return mfx

@greet
def hello():
    print("Hello")

hello()