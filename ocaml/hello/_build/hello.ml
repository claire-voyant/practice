(*
simple hello world
program in ocaml
*)

let squared a b = a ** b;;

let average a b = (a +. b) /. 2.0;;

let sum a b = (a + b);;

let diff a b =
  let minimum = min a b
  and maximum = max a b in
  (maximum - minimum);;

let rec fib n =
  if n < 2 then n else fib (n-1) + fib (n-2);;

(*print_endline ("Hello World");;
print_endline (Printf.sprintf "%f" (average 10.0 20.0));;
print_endline (Printf.sprintf "%d" (sum 1 2));;
print_endline (Printf.sprintf "%d" (diff 9 3));;
print_endline (Printf.sprintf "%d" (diff 21 10));;
*)

let compose f g = fun x -> f (g x)
let compose2 f g = function x -> f (g x)

let rec read_lines () =
  try let line = read_line () in
    int_of_string (line) :: read_lines()
  with  
    End_of_file -> []

let f n arr = 
  let len = List.length arr in
  let arr_ret = [] in
  for i=0 to len-1 do
    for j=0 to n do
      arr_ret = (List.nth arr i)::arr_ret;
    done;
  done;
  arr_ret;;

let main  =
  let n::arr = read_lines() in
  let ans = f n arr in
  List.iter(fun x -> print_int x; print_newline ()) ans;;

main

