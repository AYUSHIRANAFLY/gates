def OR(A, B):
	return A | B	

print("Output of 0 OR 0 is", OR(0, 0))
print("Output of 0 OR 1 is", OR(0, 1))
print("Output of 1 OR 0 is", OR(1, 0))
print("Output of 1 OR 1 is", OR(1, 1))

def AND(A, B):
	return A & B	

print("Output of 0 AND 0 is", AND(0, 0))
print("Output of 0 AND 1 is", AND(0, 1))
print("Output of 1 AND 0 is", AND(1, 0))
print("Output of 1 AND 1 is", AND(1, 1))

def NOT(A):
	return ~A+2	

print("Output of NOT 0 is", NOT(0))
print("Output of NOT 1 is", NOT(1))
# Function to simulate AND Gate
def AND(A, B):
	return A & B;	

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

# Function to simulate NAND Gate
def NAND(A, B):
	return NOT(AND(A, B))


print("Output of 0 NAND 0 is", NAND(0, 0))
print("Output of 0 NAND 1 is", NAND(0, 1))
print("Output of 1 NAND 0 is", NAND(1, 0))
print("Output of 1 NAND 1 is", NAND(1, 1))
def OR(A, B):
	return A | B;	

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

# Function to simulate NOR Gate
def NOR(A, B):
	return NOT(OR(A, B))


print("Output of 0 NOR 0 is", NOR(0, 0))
print("Output of 0 NOR 1 is", NOR(0, 1))
print("Output of 1 NOR 0 is", NOR(1, 0))
print("Output of 1 NOR 1 is", NOR(1, 1))
def XOR(A, B):
	return A ^ B

print("Output of 0 XOR 0 is", XOR(0, 0))
print("Output of 0 XOR 1 is", XOR(0, 1))
print("Output of 1 XOR 0 is", XOR(1, 0))
print("Output of 1 XOR 1 is", XOR(1, 1))
def XOR(A, B):
	return A ^ B

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

# Function to simulate XNOR Gate
def XNOR(A, B):
	return NOT(XOR(A, B))


print("Output of 0 XNOR 0 is", XNOR(0, 0))
print("Output of 0 XNOR 1 is", XNOR(0, 1))
print("Output of 1 XNOR 0 is", XNOR(1, 0))
print("Output of 1 XNOR 1 is", XNOR(1, 1))
