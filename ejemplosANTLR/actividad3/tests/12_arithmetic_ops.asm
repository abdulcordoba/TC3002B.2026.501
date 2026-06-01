.data
    var_x: .word 0
    var_y: .word 0

.text
.globl main
main:
    # int literal 10
    li   $t0, 10
    # assign x <-- $t0
    sw   $t0, var_x
    # int literal 3
    li   $t1, 3
    # assign y <-- $t1
    sw   $t1, var_y
    # read var x
    lw   $t2, var_x
    # read var y
    lw   $t3, var_y
    # add $t2 + $t3
    add  $t4, $t2, $t3
    # print (int)
    move $a0, $t4
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    # read var x
    lw   $t5, var_x
    # read var y
    lw   $t6, var_y
    # sub $t5 - $t6
    sub  $t7, $t5, $t6
    # print (int)
    move $a0, $t7
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    # read var x
    lw   $t8, var_x
    # read var y
    lw   $t9, var_y
    # mult $t8 * $t9
    mult $t8, $t9
    mflo $t0
    # print (int)
    move $a0, $t0
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    # read var x
    lw   $t1, var_x
    # read var y
    lw   $t2, var_y
    # div $t1 / $t2
    div  $t1, $t2
    mflo $t3
    # print (int)
    move $a0, $t3
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    li   $v0, 10
    syscall
