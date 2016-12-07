(*
simple hello world
program in ocaml
*)

let squared a b = a ** b;;

let average a b =
  (a +. b) /. 2.0;;

let sum a b = (a + b);;

let diff a b =
  let minimum = min a b
  and maximum = max a b in
  (maximum - minimum);;

let rec fib n =
  if n < 2 then n else fib (n-1) + fib (n-2);;

print_endline ("Hello World");;
print_endline (Printf.sprintf "%f" (average 10.0 20.0));;
print_endline (Printf.sprintf "%d" (sum 1 2));;
print_endline (Printf.sprintf "%d" (diff 9 3));;
print_endline (Printf.sprintf "%d" (diff 21 10));;

let compose f g = fun x -> f (g x)
let compose2 f g = function x -> f (g x)
