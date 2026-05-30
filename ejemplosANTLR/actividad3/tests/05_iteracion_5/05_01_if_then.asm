.data
var_x: .word 0
.text
.globl main
main:
    li $t0, 1
    sw $t0, var_x
    lw $t0, var_x
    beq $t0, $zero, else_0
    li $t0, 10
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j endif_1
else_0:
endif_1:
    li $t0, 99
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
