.data
var_x: .word 0
var_y: .word 0
str_0: .asciiz "ERROR: division entre cero"
.text
.globl main
main:
    li $t0, 10
    sw $t0, var_x
    li $t0, 3
    sw $t0, var_y
    lw $t0, var_x
    lw $t1, var_y
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_x
    lw $t1, var_y
    sub $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_x
    lw $t1, var_y
    mult $t0, $t1
    mflo $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_x
    lw $t1, var_y
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
    lw $t0, var_x
    li $t1, 2
    add $t0, $t0, $t1
    lw $t1, var_y
    li $t2, 1
    sub $t1, $t1, $t2
    mult $t0, $t1
    mflo $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 2
    li $t1, 3
    li $t2, 4
    mult $t1, $t2
    mflo $t1
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 2
    li $t1, 3
    add $t0, $t0, $t1
    li $t1, 4
    mult $t0, $t1
    mflo $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
