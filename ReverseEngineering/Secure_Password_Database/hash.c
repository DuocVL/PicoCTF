#include <stdio.h>

typedef unsigned char byte;

int main() {
    // our obf_bytes
    byte param_1[] = {
       0xc3, 0xff, 0xc8, 0xc2, 0x92, 0x9b, 0x8b, 0xc0, 0x80, 0xc2, 0xc4, 0x8b, 0x00
    };

    // make_secret()

    for (int i = 0 ; param_1[i] != 0 ; i++){
                param_1[i] = param_1[i] ^ 0xaa;
    }

    param_1[12] = 0;

    // hash()

    byte *local_20;
    long local_10;

    local_10 = 0x1505;
    local_20 = param_1;

    while (1) {
        if (*local_20 == 0)
            break;

        local_10 = (long)(int)(unsigned int)(*local_20) + local_10 * 0x21;
        local_20 = local_20 + 1;
    }

    // print the result

    printf("%ld\n", local_10);

    return 0;
}
