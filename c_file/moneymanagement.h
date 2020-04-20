#ifndef MONEYMANAGEMENT_H
#define MONEYMANAGEMENT_H

#include <QMainWindow>

namespace Ui {
class MoneyManagement;
}

class MoneyManagement : public QMainWindow
{
    Q_OBJECT

public:
    explicit MoneyManagement(QWidget *parent = 0);
    ~MoneyManagement();

private:
    Ui::MoneyManagement *ui;
};

#endif // MONEYMANAGEMENT_H
