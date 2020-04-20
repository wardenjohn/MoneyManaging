#include "moneymanagement.h"
#include "ui_moneymanagement.h"

MoneyManagement::MoneyManagement(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MoneyManagement)
{
    ui->setupUi(this);
}

MoneyManagement::~MoneyManagement()
{
    delete ui;
}
