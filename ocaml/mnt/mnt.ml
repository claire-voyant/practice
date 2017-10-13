let fire = ref 0;;
let high = ref 0;;

while (true) do
  for i = 0 to 7 do
    let mountainh = int_of_string (input_line stdin) in
    if mountainh > !high then
      fire := i;
      high := mountainh;
    ();
  done;

  print_endline (Printf.sprintf "%d" (!high));

  ();
done;
