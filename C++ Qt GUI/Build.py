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

cpp_file = """#include <QApplication>
#include <QWidget>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QWidget window;
    window.resize(320, 240);
    window.setWindowTitle("Simple Qt App");
    window.show();
    return app.exec();
}
"""

# brew install qt
# brew install pkg-config qt
# qmake -project
# qmake "Project Name"
# make