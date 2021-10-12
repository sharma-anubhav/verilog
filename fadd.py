/* 
 * Anubhav 
*/
module fadd(c,s,a,b,ci);
    output c,s;
    input a,b,ci;
    
    assign c = (a&b)|(ci&(a^b));
    assign s = ci^(a^b);
endmodule

module test;
    reg a,b,ci;
    wire c,s;
    fadd h1(c,s,a,b,ci);
    initial begin
        
        $display("a b ci c s");
        $monitor("%d %d %d  %d  %d",a,b,ci,c,s);
        a = 0; b = 0; ci = 0;
        #10;
        a = 0; b = 0; ci = 1;
        #10;
        a = 0; b = 1; ci = 0;
        #10
        a = 0; b = 1; ci = 1;
        #10;
        a = 1; b = 0; ci = 0;
        #10;
        a = 1; b = 0; ci = 1;
        #10;
        a = 1; b = 1; ci = 0;
        #10
        a = 1; b = 1; ci = 1;
        #10;
        $finish;
    end
endmodule