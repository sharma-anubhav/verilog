
module mux(a,b,c,d,s0,s1,y);
    input a,b,c,d,s0,s1;
    output y;
    
    assign y = (a&~s0&~s1)|(b&~s0&s1)|(c&s0&~s1)|(d&s0&s1);
endmodule

module test;
    reg a,b,c,d,s0,s1;
    wire y;
    
    mux o1(a,b,c,d,s0,s1,y);
    initial begin;
        $display("s0 s1 a b c d | y");
        $monitor("%d  %d  %d %d %d %d | %d",s0,s1,a,b,c,d,y);
        s0 = 0; s1 = 0; a = 0; b = 0; c = 0; d = 0;
        #10;
        s0 = 0; s1 = 1; a = 0; b = 0; c = 0; d = 1;
        #10;
        s0 = 1; s1 = 0; a = 0; b = 0; c = 1; d = 0;
        #10;
        s0 = 1; s1 = 1; a = 0; b = 0; c = 1; d = 1;
        #10;
        s0 = 0; s1 = 1; a = 0; b = 1; c = 0; d = 0;
        #10;
        s0 = 1; s1 = 0; a = 0; b = 1; c = 0; d = 1;
        #10;
        s0 = 1; s1 = 1; a = 0; b = 1; c = 1; d = 0;
        #10;
        s0 = 0; s1 = 0; a = 0; b = 1; c = 1; d = 1;
        #10;
        s0 = 1; s1 = 0; a = 1; b = 0; c = 0; d = 0;
        #10;
        s0 = 1; s1 = 1; a = 1; b = 0; c = 0; d = 1;
        #10;
        $finish;
    end
endmodule












