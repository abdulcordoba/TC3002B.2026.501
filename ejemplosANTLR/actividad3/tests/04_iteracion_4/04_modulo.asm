.data
str_0: .asciiz "ERROR: modulo entre cero"
str_1: .asciiz "ERROR: modulo entre cero"
.text
.globl main
main:
    li $t0, 10
    li $t1, 3
    bne $t1, $zero, modulo_ok_0
    la $a0, str_0
    li $v0, 4
    syscall
    li $v0, 10
    syscall
modulo_ok_0:
    div $t0, $t1
    mfhi $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 20
    li $t1, 6
    bne $t1, $zero, modulo_ok_1
    la $a0, str_1
    li $v0, 4
    syscall
    li $v0, 10
    syscall
modulo_ok_1:
    div $t0, $t1
    mfhi $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
