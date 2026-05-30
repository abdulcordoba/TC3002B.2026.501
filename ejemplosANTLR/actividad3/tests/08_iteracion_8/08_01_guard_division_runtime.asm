.data
var_x: .word 0
str_0: .asciiz "ERROR: division entre cero"
.text
.globl main
main:
    li $t0, 0
    sw $t0, var_x
    li $t0, 10
    lw $t1, var_x
    bne $t1, $zero, division_ok_0
    la $a0, str_0
    li $v0, 4
    syscall
    li $v0, 10
    syscall
division_ok_0:
    div $t0, $t1
    mflo $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
