# Embedding Python In A C++ File

Python is a powerful language with extensive libraries and an active community. However, it is not as computationally efficient as C++. This guide demonstrates how to include Python paths in a C++ project to leverage Python's capabilities within performance-critical C++ applications. 

<span style="color:red"> **This is a demo for Unix machines (Particularly MacOS machines), Windows machines will have similar commands, but not exactly as depicted in this demo.** </span>

---

## Step 1 - Find Includes For Python

The first step involves finding the include paths for your Python installation. This can be done using:

```
python3-config --includes
```

You should see an output similar to:

```
-I/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/include/python3.12 
```

## Step 2 - Find Linker Flags For Python

Next, we need to retrieve the linker flags necessary for linking Python with your C++ application:

```
python3-config --ldflags
```

The output might look like:

```
-L/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/lib -lpython3.12 -ldl -framework CoreFoundation
```

## Step 3 - Construct Makefile

With the necessary flags in hand, create a Makefile to simplify the compilation process:

```
# C++ compiler
CXX = g++
# Include flags, add the output from Step 1
CXXFLAGS = $(shell python3-config --includes)
# Linker flags, add the output from Step 2
LDFLAGS = $(shell python3-config --ldflags)

# Name of the output executable
TARGET = main
# Source file(s) to compile
SOURCES = main.cpp

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) $(SOURCES) $(LDFLAGS) -o $(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all clean
```

<span style="color:red">Replace `$(shell python3-config --includes)` and `$(shell python3-config --ldflags)` with the values found in Steps 1 and 2.</span>

## Step 4 - (Optional) Update VS Code Include Paths For Error Squiggles

To disable the error squiggles in Visual Studio Code (in your local directory), update the c_cpp_properties.json file as follows:

```
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}/**",
                "/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/include/python3.12"
            ],
            "defines": [],
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks"
            ],
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "macos-clang-arm64"
        }
    ],
    "version": 4
}
```

If you wish to not have to add this every time you start a new project, you can add the includes to your `settings.json` file by:

1. Open VSCode settings with `cmd + ,`.
2. Open the `settings.json` file for VSCode (located in the top right of the window) by clicking on the file icon (when hovered over, you will get a dialog saying `"Open Settings (JSON)"`).
3. Add the line (if not already present) `"C_Cpp.default.includePath": []` to the JSON file.
4. Add the path found from Step 1 to this array of values, it should look something like what is seen below:
```
"C_Cpp.default.includePath": [
    "${workspaceFolder}/**",
    "/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/include/python3.12"
],
```
5. Save your `settings.json` file. You should no longer see error squiggles in your cpp files for running Python files inside them.

## Step 5 - Build And Execute File

Now, you can build and run your executable with:

```
make && ./main
```

## Step 6 - Have Me Do It For You

If you are apprehensive to going through the aforementioned steps, then just run the Python file `Build.py` found in this directory and all of the above will be completed for you.