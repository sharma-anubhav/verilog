
module demux(a,b,c,d,s0,s1,i);
    input i,s0,s1;
    output a,b,c,d;
    
    assign a = i&~s0&~s1;
    assign b = i&~s0&s1;
    assign c = i&s0&~s1;
    assign d = i&s0&s1;
endmodule

module test;
    reg i,s0,s1;
    wire a,b,c,d;
    
    demux o1(a,b,c,d,s0,s1,i);
    initial begin;
        $display("s0 s1 i | a b c d");
        $monitor("%d  %d  %d | %d %d %d %d",s0,s1,i,a,b,c,d);
        s0 = 0; s1 = 0; i = 1; 
        #10;
        s0 = 0; s1 = 1; i = 1; 
        #10;
        s0 = 1; s1 = 0; i = 1; 
        #10;
        s0 = 1; s1 = 1; i = 1; 
        #10;
        $finish;
    end
endmodule
