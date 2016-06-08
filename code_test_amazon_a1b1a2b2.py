code_test_amazon_a1b1a2b2

z= ['a1','a2','a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5']

nn = []

if len(z) % 2==0:
    half = len(z)//2
    
new = zip(z[:half], z[half:])

for i in new:
    nn.extend([i[0], i[0]])

nn