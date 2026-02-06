def fibonacciSequence():
    def fibonacciInputs(help_text = "Please enter how many numbers in the Fibonacci sequence you'd like to see: "):
        return int(input(help_text))
    a, b = 0, 1
    fibonacci_numbers = []

    for i in range(fibonacciInputs()):  
        fibonacci_numbers.append(str(a)) 
        a, b = b, a + b

    print(' '.join(fibonacci_numbers))
    
fibonacciSequence()