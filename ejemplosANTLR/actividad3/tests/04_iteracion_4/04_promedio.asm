.text
.globl main
main:
    li $t0, 7
    li $t1, 3
    add $t0, $t0, $t1
    sra $t0, $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 3
    neg $t0, $t0
    li $t1, 1
    neg $t1, $t1
    add $t0, $t0, $t1
    sra $t0, $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 3
    neg $t0, $t0
    li $t1, 2
    neg $t1, $t1
    add $t0, $t0, $t1
    sra $t0, $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
