# tree oxygen output calculator ;D

circumference = float(input("enter circumference of mature oak tree in inches: "))

tree_circs = {7.9:1, 19.7:5.3, 35.4:10.3, 59.1:17.5, 74.8:24.6, 98.4:37.4}

for item in tree_circs:
  if item < circumference:
    print(f"using data for {item} inches circumference")
    data_circ = item
    break

print(tree_circs[data_circ])    
