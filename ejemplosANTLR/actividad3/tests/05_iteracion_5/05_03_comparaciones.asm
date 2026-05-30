.data
var_a: .word 0
var_b: .word 0
.text
.globl main
main:
    li $t0, 5
    sw $t0, var_a
    li $t0, 8
    sw $t0, var_b
    lw $t0, var_a
    lw $t1, var_b
    slt $t0, $t0, $t1
    beq $t0, $zero, else_0
    li $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j endif_1
else_0:
endif_1:
    lw $t0, var_b
    lw $t1, var_a
    slt $t0, $t0, $t1
    xori $t0, $t0, 1
    beq $t0, $zero, else_2
    li $t0, 2
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j endif_3
else_2:
endif_3:
    lw $t0, var_a
    li $t1, 5
    sub $t0, $t0, $t1
    sltiu $t0, $t0, 1
    beq $t0, $zero, else_4
    li $t0, 3
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j endif_5
else_4:
    li $t0, 0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
endif_5:
    li $v0, 10
    syscall
