temperatures=[10,-20,-289,100]

def converter(temp,file):
    with open(file,"w") as myfile:
        for c in temperatures:
            if c < -273.15:
                return "That temperature doesn't make sense"
            else:
                f=c*9/5+32
                myfile.write(str(f)+"\n")


converter(temperatures,"temp.txt")
