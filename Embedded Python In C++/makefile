# C++ compiler
CXX = g++

# C++ flags
CXXFLAGS = -I/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/include/python3.12

# Linker flags
LDFLAGS = -L/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/lib -lpython3.12 -ldl -framework CoreFoundation

# Name of the output executable
TARGET = main

# Source files to compile
SOURCES = main.cpp

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) $(SOURCES) $(LDFLAGS) -o $(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all clean
