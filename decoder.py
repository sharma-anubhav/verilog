module Decoder24(a,b,e,x,y,z,w);
        input a,b,e;
        output x,y,z,w;
        assign x=e&a&b;
        assign y=e&a&~b;
        assign z=e&~a&b;
        assign w=e&~a&~b;
endmodule
module test;
      reg a1,b1,e1;
      wire x1,y1,z1,w1;
      Decoder24 objct(a1,b1,e1,x1,y1,z1,w1);
      initial begin
        $display("e a b x y z w");
        $monitor("%d %d %d %d %d %d %d",e1,a1,b1,x1,y1,z1,w1);
       e1=1;a1=0;b1=0;
       #10 
       e1=1;a1=0;b1=1;
       #10 
       e1=1;a1=1;b1=0; 
       #10 
       e1=1;a1=1;b1=1;
     end
endmodule