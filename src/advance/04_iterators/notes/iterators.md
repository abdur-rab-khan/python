# Iterators and Generators in Python

    ### What is `yield`?
    
    ---
    
    The `yield` keyword is used in **generator functions** to produce a sequence of values lazily (one at a time). Unlike a regular function that computes all values at once and returns them (e.g., in a list), a generator function **pauses** after yielding each value and **resumes** when the next value is requested.
    
    ### Key Features of `yield`
    
    ---
    
    1. **Lazy Evaluation**: Values are generated on-the-fly, one at a time, instead of computing everything upfront.
    2. **Memory Efficiency**: Since only one value is generated at a time, it saves memory compared to storing an entire sequence in a list.
    3. **Pause and Resume**: The function pauses after each `yield` and resumes from where it left off when the next value is requested.
    
    ### Real-World Example: Streaming Data
    
    ---
    
    Imagine you’re working with a **large dataset**, like a log file with millions of lines. Loading the entire file into memory at once would be inefficient and could crash your program. Instead, you can use a generator with `yield` to process the file **line by line**.
    
    - Code
        
        ```python
        #------------ ❌❌❌ --------------
        def read_file(filename):
            with open(filename, "r") as file:
                lines = file.readlines()  # Reads the entire file into memory
            return lines
        
        # Process the file
        lines = read_file("logfile.txt")
        error_count = 0
        for line in lines:
            if "error" in line:
                error_count += 1
        
        print("Total errors:", error_count)
        
        # ---------- ✅✅✅ ------------ 
        def read_file_lazily(filename):
            with open(filename, "r") as file:
                for line in file:  # Reads one line at a time
                    yield line  # Yields the line to the caller
        
        # Process the file
        error_count = 0
        for line in read_file_lazily("logfile.txt"):
            if "error" in line:
                error_count += 1
        
        print("Total errors:", error_count)
        
        # ---------- Way to working with yield --------------
        def simple_generator():
            yield "apple"
            yield "banana"
            yield "cherry"
        
        gen = simple_generator()
        
        # First way to get the generator values
        print(gen.__next__())
        print(gen.__next__())
        print(gen.__next__())
        
        # Second way to get the generator values
        
        for val in simple_generator():
            print(val)
        ```
        
    
    ### Real-World Analogy
    
    ---
    
    Imagine you’re reading a **huge book**:
    
    - **Without `yield`**: You photocopy the entire book and keep all the pages on your desk. Your desk gets cluttered, and you might run out of space.
    - **With `yield`**: You read one page at a time, process it, and then put it away. Your desk stays clean, and you can handle books of any size.