.data
var_i: .word 0
.text
.globl main
main:
    li $t0, 1
    sw $t0, var_i
while_0:
    lw $t0, var_i
    li $t1, 3
    slt $t0, $t1, $t0
    xori $t0, $t0, 1
    beq $t0, $zero, endwhile_1
    lw $t0, var_i
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_i
    li $t1, 2
    sub $t0, $t0, $t1
    sltiu $t0, $t0, 1
    beq $t0, $zero, else_2
    li $t0, 20
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j endif_3
else_2:
endif_3:
    lw $t0, var_i
    li $t1, 1
    add $t0, $t0, $t1
    sw $t0, var_i
    j while_0
endwhile_1:
    li $v0, 10
    syscall
