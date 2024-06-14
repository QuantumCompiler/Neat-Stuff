#include <QApplication>
#include <QMainWindow>
#include <QPushButton>
#include <QMessageBox>
#include <QVBoxLayout>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QMainWindow window;
    window.setWindowTitle("Qt C++ Application");
    window.resize(800, 600);

    QPushButton button("Open Dialog");
    QObject::connect(&button, &QPushButton::clicked, [&]() {
        QMessageBox::information(&window, "Dialog", "You Opened A Window");
    });

    QVBoxLayout* layout = new QVBoxLayout;
    layout->addWidget(&button, 0, Qt::AlignCenter);

    QWidget *centralWidget = new QWidget;
    centralWidget->setLayout(layout);

    window.setCentralWidget(centralWidget);
    window.show();

    return app.exec();
}