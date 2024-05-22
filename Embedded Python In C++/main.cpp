#include <Python.h>
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
