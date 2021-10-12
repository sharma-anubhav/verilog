module Encoder42(a,b,c,d,x,y);
         input a,b,c,d;
         output x,y;
         assign x=a|b;
         assign y=a|c;
endmodule

module test;
    reg a1,b1,c1,d1;
    wire x1,y1;
    Encoder42 obj(a1,b1,c1,d1,x1,y1);
    initial begin
        $display("a b c d x y");
        $monitor("%b %b %b %b %b %b",a1,b1,c1,d1,x1,y1);
        a1=0; b1=0; c1=0;d1=1;
        #10 
        a1=0; b1=0; c1=1;d1=0;
        #10 
        a1=0; b1=1; c1=0;d1=0; 
        #10 
        a1=1; b1=0; c1=0;d1=0;
    end
    
endmodule