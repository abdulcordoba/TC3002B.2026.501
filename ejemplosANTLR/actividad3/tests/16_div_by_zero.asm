.data

.text
.globl main
main:
    # int literal 5
    li   $t0, 5
    # int literal 0
    li   $t1, 0
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
