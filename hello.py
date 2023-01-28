

# x = 'hello mr fotoohi'
# print(x)
class Hello:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    
        
p1 = Hello("mohammad", "fotoohi")
p2 = Hello( "emran", "shayesteh")

print(f'Hello {p1.name} {p1.lastname}')
print(f'Hello{p2.name} {p2.lastname}')
l = 20
