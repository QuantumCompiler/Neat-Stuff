# Embedding Python In A C++ File

Python is a powerful language with extensive libraries and an active community. However, it is not as computationally efficient as C++. This guide demonstrates how to include Python paths in a C++ project to leverage Python's capabilities within performance-critical C++ applications.

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
-L/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/lib/python3.12/config-3.12-darwin -ldl -framework CoreFoundation
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

## Step 4 - (Optional) Update VS Code Include Paths For Error Squiggles

To disable the error squiggles in Visual Studio Code, update the c_cpp_properties.json file as follows:

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

## Step 5 - Build And Execute File

Now, you can build and run your executable with:

```
make && ./main
```