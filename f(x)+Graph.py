#Importing Math for the math functions and matplotlib for graphing
import math
import matplotlib.pyplot as plt

    
def main():
    y = []
    scale = []
    anst=int(input("Do you want a table? "))

    def f():
        user_input = input("f(x) = ")
        fx = lambda x: eval(user_input)
        return fx

    xs = float(input("Enter starting x value: "))
    xe = float(input("Enter ending x value: "))
    inc = float(input("Enter increasing value: "))
    ys = float(input("Enter starting y value: "))
    ye = float(input("Enter ending y value: "))

    def print_table(f):
        x = xs
        if anst == 1:
            print("\nx\tf(x)")
            if xs < xe:
                while (x < xe + 1):
                    try:
                        val = f(x)
                        if val is not None and not (ys <= val <= ye):
                            val = None
                    except:
                        val = None
                    print(f"{x}\t{val if val is not None else 'N/A'}")
                    scale.append(x)
                    y.append(val)
                    x = x + inc
            elif xs > xe:
                while (x > xe - 1):
                    try:
                        val = f(x)
                        if val is not None and not (ys <= val <= ye):
                            val = None
                    except:
                        val = None
                    print(f"{x}\t{val if val is not None else 'N/A'}")
                    scale.append(x)
                    y.append(val)
                    x = x + inc
        else:
            if xs < xe:
                while (x < xe + 1):
                    try:
                        val = f(x)
                        if val is not None and not (ys <= val <= ye):
                            val = None
                    except:
                        val = None
                    scale.append(x)
                    y.append(val)
                    x = x + inc
            elif xs > xe:
                while (x > xe - 1):
                    try:
                        val = f(x)
                        if val is not None and not (ys <= val <= ye):
                            val = None
                    except:
                        val = None
                    scale.append(x)
                    y.append(val)
                    x = x + inc
                
    # Get user-defined function
    fx = f()

    if fx:
        # Print table for user-defined function
        print_table(fx)

    x_values = scale
    y_values = y

    # Create the graph
    plt.plot(x_values , y_values)

    # Customize the graph
    plt.title("Graph of f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # Display the graph
    plt.show()

    ans=int(input("Do you want to graph again? Press 1 for yes, any other key for no: "))
    if ans==1:
        main()

if __name__ == "__main__":
    main()
