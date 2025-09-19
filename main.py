# The first function is using multiple parameters to print multiple names.

def name(n, n1, n2, n3):
    print(n, n1, n2, n3)
    
name("john", "Craig", "Robert", "Alexandra")


# The second function is using a for loop to make these multiple names go onto the next line. The star before the n parameter is used to make it so that you can input as many names you want without making multiple parameters.
def name2(*n):
    for i in range(len(n)):
        print(n[i])
   
name2("james", "rob", "bob", "Jennifer")