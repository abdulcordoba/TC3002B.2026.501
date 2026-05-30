.text
.globl main
main:
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal func_respuesta
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
func_respuesta:
    li $t0, 42
    move $v0, $t0
    j return_respuesta_0
return_respuesta_0:
    jr $ra
