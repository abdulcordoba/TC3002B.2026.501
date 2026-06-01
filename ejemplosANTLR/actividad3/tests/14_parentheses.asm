.data

.text
.globl main
main:
    # int literal 2
    li   $t0, 2
    # int literal 3
    li   $t1, 3
    # add $t0 + $t1
    add  $t2, $t0, $t1
    # int literal 4
    li   $t3, 4
    # mult $t2 * $t3
    mult $t2, $t3
    mflo $t4
    # print (int)
    move $a0, $t4
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    li   $v0, 10
    syscall
