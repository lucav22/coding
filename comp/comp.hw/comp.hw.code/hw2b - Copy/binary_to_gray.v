module binary_to_gray(B,G);
    input [0:3] B;
    output [0:3] G;

    assign G - B ^[3:1];
    
endmodule
