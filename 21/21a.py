r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

                                #ip 3
r5 = 123                        # 00 seti 123 5
    
while True:
    r5 = r5 & 456               # 01 bani 5 456 5
    if r5 == 72:                # 02 eqri 5 72 5
                                # 03 addr 5 3 3
                                # 04 seti 0 3
        break

r5 = 0                          # 05 seti 0 5

while True:    
    r4 = r5 or 65536            # 06 bori 5 65536 4    #         1 0000 0000 0000 0000
    r5 = 8858047                # 07 seti 8858047 5    # 1000 0111 0010 1001 1011 1111
 
    while True:
        print r0, r1, r2, r4, r5
        r2 = r4 & 255           # 08 bani 4 255 2
        r5 = r5 + r2            # 09 addr 5 2 5
        r5 = r5 & 16777215      # 10 bani 5 16777215 5 # 1111 1111 1111 1111 1111 1111
        r5 = r5 * 65899         # 11 muli 5 65899 5
        r5 = r5 & 16777215      # 12 bani 5 16777215 5

        if 256 > r4:            # 13 gtir 256 4 2
            break               # 14 addr 2 3 3
                                # 15 addi 3 1 3
                                # 16 seti 27 3

        r2 = 0                  # 17 seti 0 2

        while True:
            r1 = r2+1           # 18 addi 2 1 1
            r1 = r1 * 256       # 19 muli 1 256 1

            if r1 > r4:         # 20 gtrr 1 4 1
                break           # 21 addr 1 3 3
                                # 23 seti 25 3
                                # 22 addi 3 1 3

            r2 = r2 + 1         # 24 addi 2 1 2

                                # 25 seti 17 3

        r4 = r2                 # 26 setr 2 1 4

                                # 27 seti 7 3

    print "First exit", r5
    exit()
    if r5 == r0:                # 28 eqrr 5 0 2
        exit()                  # 29 addr 2 3 3
                                # 30 seti 5 3
