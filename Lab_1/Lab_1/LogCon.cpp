// Функція заперечення (NOT)
// Повертає протилежне значення змінної a
bool NOT(bool a)
{
    if (a == true) return false;
    else return true;
}

// Функція кон'юнкції (AND)
// Повертає true, якщо обидва значення істинні (a && b)
bool AND(bool a, bool b) {
    return a && b;
}

// Функція диз'юнкції (OR)
// Повертає true, якщо хоча б одне значення істинне (a || b)
bool OR(bool a, bool b)
{
    return a || b;
}

// Функція імплікації (IMP)
// Повертає true, якщо з a випливає b (логічне слідування)
bool IMP(bool a, bool b)
{
    return !a || b;
}

// Функція еквівалентності (EQU)
// Повертає true, якщо a і b рівні (a == b)
bool EQU(bool a, bool b)
{
    return a == b;
}

// Функція виключного АБО (XOR)
// Повертає true, якщо a і b різні (a != b)
bool XOR(bool a, bool b)
{
    return a != b;
}

// Функція x1 (спеціальна комбінація логічних операцій)
// Використовує заперечення NOT та операцію XOR
bool x1(bool a, bool b)
{
    bool na = NOT(a); // Заперечення a
    bool nb = NOT(b); // Заперечення b
    return XOR(na, nb); // Виключне АБО між NOT(a) та NOT(b)
}

// Функція x2 (складніша логічна операція)
// Використовує імплікацію та виключне АБО з запереченнями
bool x2(bool a, bool b, bool c)
{
    return IMP(NOT(c), XOR(NOT(a), NOT(b)));
}

// Функція F11 (складна комбінація логічних операцій)
// Використовує імплікацію, виключне АБО та заперечення
bool F11(bool a, bool b, bool c) {
    bool part1 = IMP(a, b); // Імплікація a → b
    bool part2 = XOR(NOT(a), NOT(b)); // Виключне АБО між NOT(a) та NOT(b)
    bool part3 = IMP(NOT(c), part2); // Імплікація NOT(c) → part2
    return part1 && part3; // Кон'юнкція (AND) між part1 та part3
}