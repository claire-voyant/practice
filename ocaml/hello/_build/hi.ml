open Hello

let rec print_hello_n_times n =
  print_endline (Printf.sprintf "%s" "hello")
  if n > 0 then print_hello_n_times (n-1);;

(*print_endline (Printf.sprintf "%d" (Hello.sum 1 4));;*)
print_hello_n_times 5;;
