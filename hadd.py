module hadd(c,s,a,b);
    output c,s;
    input a,b;
    
    assign c = a&b;
    assign s = a^b;
endmodule

module test;
    reg a,b;
    wire c,s;
    hadd h1(c,s,a,b);
    initial begin
        
        $display("a b c s");
        $monitor("%d %d %d %d",a,b,c,s);
        a = 0; b = 1;
        #10;
        a = 1; b = 1;
        #10;
        a = 1; b = 0;
        #10
        a = 0; b = 0;
        #10;
        $finish;
    end
endmodule