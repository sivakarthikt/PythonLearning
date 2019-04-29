



inp={1,2,3,4,5,"eleven"}
inp2={"eleven","one","two"}
inp.update(inp2) # To update the existing set to another one

inp.remove(4) #To remove an element in a set
inp.discard(10) #To remove an element in a set irrespective of existence
inp.discard(1)


s1={1,2,3,4,5}
s2={3,4,5,6}
s3={5,6,7}
print(s1.intersection(s2,s3))
print(s1.difference(s2,s3))