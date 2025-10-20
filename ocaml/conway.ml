let symb n = match n with
    | 1 -> "1"
    | 2 -> "2"
    | 3 -> "3"
    | _ -> "";;
    
let to_string c = match c with
    | '1' -> "1"
    | '2' -> "2"
    | '3' -> "3"
    | _ -> "";;
    
let rec count str = let len = String.length str in
    if (len = 0) then 0
    else if (len = 1) then 1
    else
        if (str.[0] = str.[1]) then 1 + (count (String.sub str 1 (len - 1)))
        else 1;;
        
let rec read str =
    if (str = "") then ""
    else let nb = count str in (symb nb) ^ (to_string str.[0]) ^ read (String.sub str nb ((String.length str) - nb));;
        
let rec conway n = if (n = 1) then symb 1
                   else let str = conway (n - 1) in (print_string (str ^ "\n"); read str);;


conway 5;;
