----------------------Recursion in Python----------------------------
Recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts. In Python, recursion is widely used for tasks that can be divided into identical subtasks.

In Python, a recursive function is defined like any other function, but it includes a call to itself. The syntax and structure of a recursive function follow the typical function definition in Python, with the addition of one or more conditions that lead to the function calling itself.
-----------------Basic Structure of Recursive Function--------------------
def recursive_function(parameters):

    if base_case_condition:

        return base_result

    else:

        return recursive_function(modified_parameters)


Base Case and Recursive Case
Base Case: This is the condition under which the recursion stops. It is crucial to prevent infinite loops and to ensure that each recursive call reduces the problem in some manner. In the factorial example, the base case is
n == 1.
Recursive Case: This is the part of the function that includes the call to itself. It must eventually lead to the base case. In the factorial example, the recursive case is return n * factorial(n-1).

----------------------------Python Functions--------------------------------
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

-----------Creating a Function-----------
In Python a function is defined using the def keyword:

Example
def my_function():
  print("Hello from a function")

------------Calling a Function------------
To call a function, use the function name followed by parenthesis:

Example
def my_function():
  print("Hello from a function")

my_function()

----------------------------------Arguments----------------------------------
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
