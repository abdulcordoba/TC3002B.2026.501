.data
var_x: .word 0
.text
.globl main
main:
    li $t0, 10
    sw $t0, var_x
    lw $t0, var_x
    addiu $sp, $sp, -4
    sw $t0, 0($sp)
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal func_siete
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    lw $t0, 0($sp)
    addiu $sp, $sp, 4
    move $t1, $v0
    add $t0, $t0, $t1
    addiu $sp, $sp, -4
    sw $t0, 0($sp)
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal func_cinco
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    lw $t0, 0($sp)
    addiu $sp, $sp, 4
    move $t1, $v0
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
func_siete:
    li $t0, 7
    move $v0, $t0
    j return_siete_0
return_siete_0:
    jr $ra
func_cinco:
    li $t0, 5
    move $v0, $t0
    j return_cinco_1
return_cinco_1:
    jr $ra
