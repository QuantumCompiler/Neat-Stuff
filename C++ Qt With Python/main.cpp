#include <Python.h>
#include <QApplication>
#include <QWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include <QMessageBox>
#include <thread>
#include <string>

class MainWindow : public QWidget
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);

private slots:
    void onButtonClick();
};

MainWindow::MainWindow(QWidget *parent)
    : QWidget(parent)
{
    QVBoxLayout *layout = new QVBoxLayout(this);

    QPushButton *button = new QPushButton("Run Python Code", this);
    layout->addWidget(button);

    connect(button, &QPushButton::clicked, this, &MainWindow::onButtonClick);
}

void runPythonScript()
{
    // Define the Python script as a string
    const char* pythonCode = R"(
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Plot of the Sine Function')
plt.show()
    )";

    // Execute the Python script
    PyRun_SimpleString(pythonCode);
}

void MainWindow::onButtonClick()
{
    // Initialize the Python interpreter
    Py_Initialize();
    runPythonScript();
    Py_Finalize();
}

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    MainWindow window;
    window.resize(320, 240);
    window.setWindowTitle("Simple Qt App");
    window.show();

    int result = app.exec();

    return result;
}

#include "main.moc"