// Лаба 1 дискретка.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "LogCon.h"

int main()
{
#include <iostream>

    using namespace std;

    // Оголошення булевих змінних
    bool a, b, c;

    // Вивід заголовка таблиці для 2 змінних
    cout << "----------------------------------------------------------\n";
    cout << "| a | b | NOT (a) | NOT (b) | AND | OR | IMP | EQU | XOR |\n";
    cout << "|---|---|---------|---------|-----|----|-----|-----|-----|\n";

    // Виведення рядків таблиці для всіх можливих комбінацій змінних a і b

    // Випадок: a = true, b = true
    a = true;
    b = true;
    cout << "| " << a << " | " << b << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |  " << AND(a, b) << "  | " << OR(a, b) << "  |  " << IMP(a, b)
        << "  |  " << EQU(a, b) << "  |  " << XOR(a, b) << "  |\n";
    cout << "|---|---|---------|---------|-----|----|-----|-----|-----|\n";

    // Випадок: a = true, b = false
    a = true;
    b = false;
    cout << "| " << a << " | " << b << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |  " << AND(a, b) << "  | " << OR(a, b) << "  |  " << IMP(a, b)
        << "  |  " << EQU(a, b) << "  |  " << XOR(a, b) << "  |\n";
    cout << "|---|---|---------|---------|-----|----|-----|-----|-----|\n";

    // Випадок: a = false, b = true
    a = false;
    b = true;
    cout << "| " << a << " | " << b << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |  " << AND(a, b) << "  | " << OR(a, b) << "  |  " << IMP(a, b)
        << "  |  " << EQU(a, b) << "  |  " << XOR(a, b) << "  |\n";
    cout << "|---|---|---------|---------|-----|----|-----|-----|-----|\n";

    // Випадок: a = false, b = false
    a = false;
    b = false;
    cout << "| " << a << " | " << b << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |  " << AND(a, b) << "  | " << OR(a, b) << "  |  " << IMP(a, b)
        << "  |  " << EQU(a, b) << "  |  " << XOR(a, b) << "  |\n";
    cout << "----------------------------------------------------------\n\n\n\n\n\n";

    // Вивід заголовка таблиці для 3 змінних
    cout << "-------------------------------------------------------------------------------------------\n";
    cout << "| a | b | c | NOT (a) | NOT (b) | NOT (c) | IMP (a,b) | XOR (-a,-b) | IMP (-c, XOR) | F11 |\n";
    cout << "|---|---|---|---------|---------|---------|-----------|-------------|---------------|-----|\n";

    // Виведення рядків таблиці для всіх можливих комбінацій змінних a, b, c

    // Випадок: a = true, b = true, c = true
    a = true;
    b = true;
    c = true;
    cout << "| " << a << " | " << b << " | " << c << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |    " << NOT(c) << "    |     " << IMP(a, b) << "     |      " << x1(a, b)
        << "      |       " << x2(a, b, c) << "       |  " << F11(a, b, c) << "  |\n";
    cout << "|---|---|---|---------|---------|---------|-----------|-------------|---------------|-----|\n";

    // Випадок: a = true, b = true, c = false
    a = true;
    b = true;
    c = false;
    cout << "| " << a << " | " << b << " | " << c << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |    " << NOT(c) << "    |     " << IMP(a, b) << "     |      " << x1(a, b)
        << "      |       " << x2(a, b, c) << "       |  " << F11(a, b, c) << "  |\n";
    cout << "|---|---|---|---------|---------|---------|-----------|-------------|---------------|-----|\n";

    // Аналогічно повторюємо для інших комбінацій змінних
    a = true;  b = false; c = true;
    cout << "| " << a << " | " << b << " | " << c << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |    " << NOT(c) << "    |     " << IMP(a, b) << "     |      " << x1(a, b)
        << "      |       " << x2(a, b, c) << "       |  " << F11(a, b, c) << "  |\n";
    cout << "|---|---|---|---------|---------|---------|-----------|-------------|---------------|-----|\n";

    a = false; b = true; c = true;
    cout << "| " << a << " | " << b << " | " << c << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |    " << NOT(c) << "    |     " << IMP(a, b) << "     |      " << x1(a, b)
        << "      |       " << x2(a, b, c) << "       |  " << F11(a, b, c) << "  |\n";
    cout << "|---|---|---|---------|---------|---------|-----------|-------------|---------------|-----|\n";

    a = true;  b = false; c = false;
    cout << "| " << a << " | " << b << " | " << c << " |    " << NOT(a) << "    |    " << NOT(b)
        << "    |    " << NOT(c) << "    |     " << IMP(a, b) << "     |      " << x1(a, b)
        << "      |       " << x2(a, b, c) << "       |  " << F11(a, b, c) << "  |\n";
    cout << "|---|---|---|---------|---------|---------|-----------|-------------|---------------|-----|\n";

    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
