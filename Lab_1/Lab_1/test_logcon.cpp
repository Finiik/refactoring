#include "LogCon.h"
#include <gtest/gtest.h>

// Тест для NOT
TEST(LogConTest, NotOperation) {
    EXPECT_EQ(NOT(true), false);
    EXPECT_EQ(NOT(false), true);
}

// Тест для AND
TEST(LogConTest, AndOperation) {
    EXPECT_EQ(AND(true, true), true);
    EXPECT_EQ(AND(true, false), false);
    EXPECT_EQ(AND(false, true), false);
    EXPECT_EQ(AND(false, false), false);
}

// Тест для OR
TEST(LogConTest, OrOperation) {
    EXPECT_EQ(OR(true, true), true);
    EXPECT_EQ(OR(true, false), true);
    EXPECT_EQ(OR(false, true), true);
    EXPECT_EQ(OR(false, false), false);
}

// Тест для IMP (імплікація)
TEST(LogConTest, ImplicationOperation) {
    EXPECT_EQ(IMP(true, true), true);
    EXPECT_EQ(IMP(true, false), false);
    EXPECT_EQ(IMP(false, true), true);
    EXPECT_EQ(IMP(false, false), true);
}

// Тест для EQU (еквівалентність)
TEST(LogConTest, EquivalenceOperation) {
    EXPECT_EQ(EQU(true, true), true);
    EXPECT_EQ(EQU(true, false), false);
    EXPECT_EQ(EQU(false, true), false);
    EXPECT_EQ(EQU(false, false), true);
}

// Тест для XOR (виключне АБО)
TEST(LogConTest, XorOperation) {
    EXPECT_EQ(XOR(true, true), false);
    EXPECT_EQ(XOR(true, false), true);
    EXPECT_EQ(XOR(false, true), true);
    EXPECT_EQ(XOR(false, false), false);
}

// Тест для x1 (XOR з NOT)
TEST(LogConTest, X1Operation) {
    EXPECT_EQ(x1(true, true), false);
    EXPECT_EQ(x1(true, false), true);
    EXPECT_EQ(x1(false, true), true);
    EXPECT_EQ(x1(false, false), false);
}

// Тест для x2 (комбінація XOR і NOT)
TEST(LogConTest, X2Operation) {
    EXPECT_EQ(x2(true, true, true), true);
    EXPECT_EQ(x2(true, true, false), false);
    EXPECT_EQ(x2(false, false, false), false);
    EXPECT_EQ(x2(false, false, true), true);
}

// Тест для F11 (функція трьох змінних)
TEST(LogConTest, F11Operation) {
    EXPECT_EQ(F11(true, true, true), true);
    EXPECT_EQ(F11(true, true, false), false);
    EXPECT_EQ(F11(false, false, true), false);
    EXPECT_EQ(F11(false, false, false), false);
}

// Граничний тест (повторення функцій)
TEST(LogConTest, BoundaryTest) {
    EXPECT_EQ(AND(true, OR(false, NOT(false))), true);
    EXPECT_EQ(IMP(false, AND(true, XOR(false, true))), true);
}
