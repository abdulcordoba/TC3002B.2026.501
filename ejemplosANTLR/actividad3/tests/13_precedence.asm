.data

.text
.globl main
main:
    # int literal 2
    li   $t0, 2
    # int literal 3
    li   $t1, 3
    # int literal 4
    li   $t2, 4
    # mult $t1 * $t2
    mult $t1, $t2
    mflo $t3
    # add $t0 + $t3
    add  $t4, $t0, $t3
    # print (int)
    move $a0, $t4
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    li   $v0, 10
    syscall
