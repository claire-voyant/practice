(*
simple hello world
program in ocaml
*)

let average a b =
  (a +. b) /. 2.0;;

print_endline (Printf.sprintf "%f" (average 10.0 20.0))
