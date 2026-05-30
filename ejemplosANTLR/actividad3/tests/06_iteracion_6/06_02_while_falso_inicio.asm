.data
var_i: .word 0
.text
.globl main
main:
    li $t0, 0
    sw $t0, var_i
while_0:
    lw $t0, var_i
    beq $t0, $zero, endwhile_1
    li $t0, 999
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j while_0
endwhile_1:
    li $t0, 7
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
