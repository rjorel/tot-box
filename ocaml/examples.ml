
let rec belongs list x = match list with
    | [] -> false
    | h :: q -> (h = x) or (belongs q x)
    ;;
    
let maximum list =
    let rec max_rec list a = match list with
        | [] -> a
        | h :: q -> max_rec q (max a h)
        in
        
    max_rec list (List.hd list)
    ;;
    
let generate n =
    let rec create i n = 
        if i = n then []
        else i :: create (i + 1) n
    in
    
    create 0 n
    ;;

let rec map f l = match l with
    | [] -> []
    | x :: xs -> f x :: map f xs
    ;;

let rec filter p l = match l with
    | [] -> []
    | x :: xs -> let queue = filter p xs in
                    if (p x) then x :: queue
                    else queue
    ;;
    
let rec dropwhile p l = match l with
    | [] -> []
    | x :: xs -> if p x = true then dropwhile p xs
                    else x :: xs
    ;;

let rec zip_with f l1 l2 = match l1 with
     | [] -> []
     | x :: xs -> match l2 with
        | [] -> []
        | y :: ys -> f x y :: zip_with f xs ys
    ;;
    
let rec zip = zip_with (fun x y -> (x, y));;

let rec concat l1 l2 = match (l1 , l2) with
    | ([], []) -> []
    | ([], l) -> l
    | ((x :: s), l) -> x :: concat s l
    ;;

let cast_bool = function
    | 0 -> false
    | _ -> true
    ;;

type 'a tree = Null | Node of 'a * 'a tree * 'a tree;;

let rec explore = function
    | Null -> print_string "Rien\n";
    | Node (x, ls, rs) -> print_int x; print_char '\n'; explore ls; explore rs
    ;;

type 'a options = Nothing | One of 'a;;

let est_un = function
    | Nothing -> false
    | One _ -> true
    ;;

let rec find p l = match l with
    | [] -> None
    | x :: xs -> if p x then Some x
                   else find p xs
    ;;
    
let tl = function
    | [] -> None
    | x :: xs -> Some xs
    ;;
    
let ( / ) a b = match b with
    | 0 -> None
    | _ -> Some (a / b)
    ;;
    
let map f x = match x with
    | None -> None
    | Some y -> Some (f y)
    ;;
