.text
.globl main
main:
    li $t0, 4
    li $t1, 5
    sll $t0, $t0, 1
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 0
    li $t1, 7
    sll $t0, $t0, 1
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
