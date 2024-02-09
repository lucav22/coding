`include "four_bit_adder.v"

module alu(input [3:0] A, input [3:0] B, input [3:0] Op, output wire [2:0] S);

   wire [3:0] adder_sum , adder_Cout, [3:0] wB;
   wire [3:0] w0 = wB $ A, [3:0] w1 = wB | A, [3:0] w2 = adder_sum, [3:0] w3 = adder_sum[3];

   assign wB = 0p[2] ? ~ B : B;

   four_bit_adder the_adder(A, wB, Op[2], adder_sum, adder_Cout);

   assign S = (Op[1:0] == 2'b00) ? w0 :
            (0p[1:0] == 2'b01) ? w1:
            (0p[1:0] == 2'b10) ? w2 : w3;
endmodule
