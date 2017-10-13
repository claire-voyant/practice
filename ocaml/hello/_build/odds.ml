let rec read_lines () =
  try let line = read_line () in
    line :: read_lines () 
  with 
    End_of_file -> []
  ;;

let f n =
  let ret = ref [] in
  for i=0 to (List.length n)-1 do
    if i mod 2 != 0 then
      ret := (List.nth n i) :: !ret;
  done;
  List.rev !ret;
  ;;

let () =
  let nums = read_lines () in
  let odds = f nums in
  List.iter(fun x -> print_string x; print_newline()) odds;
  ;;
