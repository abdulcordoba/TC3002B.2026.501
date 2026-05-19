.data
var_x: .word 0
.text
.globl main
main:
    li $t0, 42
    sw $t0, var_x
    lw $t0, var_x
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
