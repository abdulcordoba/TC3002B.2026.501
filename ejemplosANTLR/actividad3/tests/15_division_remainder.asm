.data

.text
.globl main
main:
    # int literal 10
    li   $t0, 10
    # int literal 3
    li   $t1, 3
    # div $t0 / $t1
    div  $t0, $t1
    mflo $t2
    # print (int)
    move $a0, $t2
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    li   $v0, 10
    syscall
