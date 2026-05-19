.data
var_add: .word 0
var_sub: .word 0
var_div: .word 0
.text
.globl main
main:
    li $t0, 100
    sw $t0, var_add
    li $t0, 200
    sw $t0, var_sub
    li $t0, 300
    sw $t0, var_div
    lw $t0, var_add
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_sub
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_div
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
