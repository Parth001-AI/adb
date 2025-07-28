#Nested Functions

def greet():
    def messg():
        return "Hello Good Morning"
    return messg()

print(greet())