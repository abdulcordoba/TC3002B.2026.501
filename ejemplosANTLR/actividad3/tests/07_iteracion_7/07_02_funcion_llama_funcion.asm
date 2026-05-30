.text
.globl main
main:
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal func_doble_mas_cinco
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    move $t0, $v0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
func_cinco:
    li $t0, 5
    move $v0, $t0
    j return_cinco_0
return_cinco_0:
    jr $ra
func_doble_mas_cinco:
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal func_cinco
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    move $t0, $v0
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
    sll $t0, $t0, 1
    add $t0, $t0, $t1
    move $v0, $t0
    j return_doble_mas_cinco_1
return_doble_mas_cinco_1:
    jr $ra
