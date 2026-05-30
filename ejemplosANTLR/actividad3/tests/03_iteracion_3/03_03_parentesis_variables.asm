.data
var_a: .word 0
var_b: .word 0
var_c: .word 0
str_0: .asciiz "ERROR: division entre cero"
.text
.globl main
main:
    li $t0, 6
    sw $t0, var_a
    li $t0, 4
    sw $t0, var_b
    li $t0, 2
    sw $t0, var_c
    lw $t0, var_a
    lw $t1, var_b
    add $t0, $t0, $t1
    lw $t1, var_c
    li $t2, 1
    add $t1, $t1, $t2
    mult $t0, $t1
    mflo $t0
    li $t1, 5
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_a
    lw $t1, var_c
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
    lw $t0, var_a
    lw $t1, var_c
    add $t0, $t0, $t1
    sw $t0, var_a
    lw $t0, var_a
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
