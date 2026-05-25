.text
.globl main
main:
    li $t0, 2
    li $t1, 3
    li $t2, 4
    sll $t1, $t1, 1
    add $t1, $t1, $t2
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
