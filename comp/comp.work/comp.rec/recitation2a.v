module recitation2a(A,B,X);

    input A,B ; 
    output X ;

    wire temp1, temp2, temp3, temp4; 

    assign temp1 = ~(~B | A );
    assign temp2 = A & B;
    assign temp3 = ~(temp1 | temp2);
    assign temp4 = A | B ;
    assign X = ~(temp4 & temp3);

endmodule



