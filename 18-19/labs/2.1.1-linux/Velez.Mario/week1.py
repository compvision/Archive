s = "[]" #String; //what the pyramid is made of
x = s + "  " + s # String; 
y = 0 #int;
i = 30 # final int; //number of steps for the pyramid
z = i #int;
a = "" #String;
j = 0 #int;
for y in range(z):
    while(z>y):
        for j in range(len(s)):
            a = a + " ";
        z -= 1;
    print(a + x);
    x = s + x + s;
    a = "";
    z = i;
    y = y + 1;
    
