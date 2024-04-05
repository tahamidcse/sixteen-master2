from django.shortcuts import render
from django.http import HttpResponse
import sys
import subprocess
# Create your views here.
def greetings(request):
    res = render(request,'codestar/home.html')
    return res





def runcode3(request):
    if request.method == 'POST':
        code_part = request.POST['code_area3']
        input_part = request.POST['input_area3']
        y = input_part
        input_part = input_part.replace("\n", " ")
        orig_stdout = sys.stdout



        try:
            with open('Main.java', 'w') as file:
                file.write(code_part)

            subprocess.run(['javac', 'Main.java'], check=True)


            sys.stdout = open('file.txt', 'w')
            subprocess.run(['java', 'Main'], input=input_part, text=True)

            sys.stdout = orig_stdout

            output = open('file.txt', 'r').read()
        except Exception as e:

            sys.stdout = orig_stdout
            output = str(e)



    res = render(request, 'codestar/home.html', {"code3": code_part, "input3": y, "output3": output})
    print(output)
    return res


def runcode2(request):
    if request.method == 'POST':
        code_part2 = request.POST['code_area2']
        input_part2 = request.POST['input_area2']
        y2 = input_part2
        input_part2 = input_part2.replace("\n"," ").split(" ")

        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part2)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output2 = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output2 = e
        print(output2)
    res = render(request,'codestar/home.html',{"code2":code_part2,"input2":y2,"output2":output2})
    return res
def runcode(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n", " ")
        input_file = 'input.txt'
        output_file = 'output.txt'

        # Save the input to a file
        with open(input_file, 'w') as f:
            f.write(input_part)




        try:
            # Compile the C++ code
            compile_process = subprocess.run(['g++', '-o', 'program', '-x', 'c++', '-'], input=code_part, text=True,
                                             capture_output=True)
            if compile_process.returncode != 0:
                raise Exception(compile_process.stderr)

            # Run the compiled program with input/output redirection
            run_process = subprocess.run(['./program'], input=input_part, text=True, capture_output=True)
            output = run_process.stdout
            with open(output_file, 'w') as f:
                f.write(output)


        except Exception as e:
            output = str(e)

        print(output)

    res = render(request, 'codestar/home.html', {"code": code_part, "input": y, "output": output})
    return res
