module majority(A, Y);
 
    input [2:0] A ;
    output Y;

    assign Y = (A[2] == 1) ? 1: (A[1] == 1) ? 1: (A[0] == 0) ? 1 : 0;
    
endmodule
