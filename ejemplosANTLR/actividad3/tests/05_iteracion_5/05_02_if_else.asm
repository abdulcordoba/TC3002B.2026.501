.data
var_x: .word 0
.text
.globl main
main:
    li $t0, 0
    sw $t0, var_x
    lw $t0, var_x
    beq $t0, $zero, else_0
    li $t0, 11
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j endif_1
else_0:
    li $t0, 22
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
endif_1:
    li $v0, 10
    syscall
