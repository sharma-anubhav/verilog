/* 
 * Anubhav 
*/
module fadd(a,b,diff,borr);
    output diff,borr;
    input a,b;
    wire x;
    assign diff = (a^b);
    assign x = ~a;
    assign borr = (~a)&b;
endmodule

module test;
    reg a,b;
    wire diff,borr;
    fadd h1(a,b,diff, borr);
    initial begin
        
        $display("a b d br");
        $monitor("%d %d  %d  %d",a,b,diff,borr);
        a = 0; b = 0;
        #10;
        a = 0; b = 1;
        #10;
        a = 1; b = 0;
        #10;
        a = 1; b = 1;
        #10;
        $finish;
    end
endmodule