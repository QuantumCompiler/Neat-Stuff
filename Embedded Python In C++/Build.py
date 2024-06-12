import os
import subprocess

def create_file(filename, content):
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as f:
        f.write(content)

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Python.h include path
py_includes_h = run_command('python3-config --includes')
py_includes_h = py_includes_h.split()[0]

# Manually construct the required LDFLAGS
ldflags_path = run_command('python3-config --prefix') + '/lib'
ldflags_lib = run_command('python3-config --ldflags').split()
filtered_ldflags = [flag for flag in ldflags_lib if 'config-' not in flag]
ldflags_filtered = ' '.join(filtered_ldflags)

# Additional linker flags for the Python library and other dependencies
ldflags_final = f"-L{ldflags_path} -lpython3.12 -ldl -framework CoreFoundation"

# Default Python File
py_file = """import numpy as np
import matplotlib.pyplot as plt

# Define the x range (0 to 2*pi with 100 points)
x = np.linspace(0, 2 * np.pi, 100)

# Compute the sine of each x point
y = np.sin(x)

# Create the plot
plt.figure()
plt.plot(x, y)  # Plot the sine of each x point

# Labeling the axes
plt.xlabel('x')
plt.ylabel('sin(x)')

# Title of the plot
plt.title('Plot of the Sine Function')

# Show the plot
plt.show()

# print("Hello, World! From Python!")
"""

# Default CPP File
cpp_file = """#include <Python.h>
#include <cstdio>

int main() {
    Py_Initialize();

    // Open the Python file
    FILE* file = fopen("main.py", "r");
    if (file != nullptr) {
        // Run the Python script
        PyRun_SimpleFile(file, "main.py");
        // Close the file
        fclose(file);
    } else {
        perror("Failed to open file");
    }

    Py_Finalize();

    return 0;
}
"""

# Default makefile
makefile = f"""# C++ compiler
CXX = g++

# C++ flags
CXXFLAGS = {py_includes_h}

# Linker flags
LDFLAGS = {ldflags_final}

# Name of the output executable
TARGET = main

# Source files to compile
SOURCES = main.cpp

all: $(TARGET)

$(TARGET): $(SOURCES)
\t$(CXX) $(CXXFLAGS) $(SOURCES) $(LDFLAGS) -o $(TARGET)

clean:
\trm -f $(TARGET)

.PHONY: all clean
"""

create_file('main.py', py_file)
create_file('main.cpp', cpp_file)
create_file('Makefile', makefile)

print("Files created successfully.")