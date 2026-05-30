.data
var_i: .word 0
.text
.globl main
main:
    li $t0, 3
    sw $t0, var_i
while_0:
    lw $t0, var_i
    beq $t0, $zero, endwhile_1
    lw $t0, var_i
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, var_i
    li $t1, 1
    sub $t0, $t0, $t1
    sw $t0, var_i
    j while_0
endwhile_1:
    li $v0, 10
    syscall
