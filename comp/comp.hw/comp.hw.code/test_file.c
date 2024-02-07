#include <stdio.h> // Include the standard I/O header to get the declaration of printf

unsigned int toggleBit2(unsigned int x){
    return x ^ 2;
}

int main() {
    unsigned int x = 3; // Example input
    printf("Original: %u, Toggled: %u\n", x, toggleBit2(x));
    return 0;
}
