def name(n, n1, n2, n3):
    print(n, n1, n2, n3)
    
name("john", "Craig", "Robert", "Alexandra")

def name2(*n):
    for i in range(len(n)):
        print(n[i])
   
name2("james", "rob", "bob", "Jennifer")