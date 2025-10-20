(* Simplified BASIC interpretor. *)

(* Basic operations. *)
type op_bin = Plus | Minus | Equal | Mult | Div;;

(* Simple expressions. *)
type expression = 
| ExpInt of int 
| ExpVar of string
| ExpString of string
| ExpBin of expression * op_bin * expression;;

(* Only int and boolean handling. *)
type value = Int of int | Bool of bool | String of string;;

(* Reduced unstruction set. *)
type instruction = 
| Goto of int 
| Print of expression
| Input of string 
| If of expression * int 
| Let of string * expression;;

(* Environment handling, with hashmap. *)
type environment = (string * value) list;;
let get_var var env = List.assoc var env;;

let rec set_var var data env = match env with
  | []          -> [(var, data)]
  | (v, d) :: t ->
    if (var = v) then (var, data) :: t
    else (v, d) :: set_var var data t;;

(* Expression evaluation, with variable environment. *)
let rec eval expr env = match expr with
  | ExpInt integer   -> Int (integer)
  | ExpString str -> String (str)
  | ExpVar var -> get_var var env
  | ExpBin (e1, op, e2) -> let ve1 = (eval e1 env) in
			   let ve2 = (eval e2 env) in
			   match ve1, op, ve2 with
			   | Int v1, Plus, Int v2  -> Int (v1 + v2)
  			   | Int v1, Minus, Int v2 -> Int (v1 - v2)
			   | Int v1, Mult, Int v2  -> Int (v1 * v2)
			   | Int v1, Div, Int v2   -> Int (v1 / v2)
			   | Int v1, Equal, Int v2 -> Bool (v1 = v2)
			   | _ -> failwith "Expression not good";;

(* Value display according type. *)
let print_val v = match v with
  | String str  -> print_string str
  | Int integer -> print_int integer
  | Bool true   -> print_string "true"
  | Bool false  -> print_string "false";;

(* Each line has a number, in a BASIC program. *)
type line = { num : int ; inst : instruction };;

(* Line execution. Returns next line to execute. *)
let exec_line line env = match line.inst with
  | Goto nline       -> (nline, env)
  | Print expr       -> print_val (eval expr env); (line.num + 10, env)

  | Input str        -> let data = read_int () in
		        (line.num + 10, (set_var str (Int data) env))

  | Let (str, expr)  -> let v = eval expr env in
			let new_env = set_var str v env in (line.num + 10, new_env)

  | If (expr, nline) -> let ret = (eval expr env) in 
		        match ret with
		        | Bool true -> (nline, env)
			| Bool false -> (line.num + 10, env)
			| _ -> failwith "Expression is not boolean";;


(* Program execution. *)
let exec_prgm prgm =
  (* Finds the next instruction to execute. 
     Return None if the line number can't be associated with an instruction. *)
  let rec find_instr num_line instr_list = match instr_list with
    | [] -> None
    | h :: t -> 
      if (h.num = num_line) then Some h 
      else find_instr num_line t in

  (* Execute line by line the program, in taking account jumps. *)
  let rec exec_aux instr env = 
    let num_line, nenv = exec_line instr env in
    let next_instr = find_instr num_line prgm in match next_instr with
      | None -> env
      | Some i -> exec_aux i nenv in
  
  exec_aux (List.hd prgm) [];;


(* A program is an instruction list. *)
type program = line list;;


(* Factorial function. *)
(*
0  PRINT "n = "
10 INPUT N
20 LET I = 1
30 LET S = 1
40 LET I = I + 1
50 LET S = S * I
60 IF (I = N) THEN GOTO 80
70 GOTO 40
80 PRINT "result: "
90 PRINT S
100 PRINT "\n"
*)

(* Translation of previous BASIC code. *)
let prog = [
  { num = 0; inst = Print (ExpString "n = ") };
  { num = 10; inst = Input "n" };
  { num = 20; inst = Let ("i",ExpInt 1) };
  { num = 30; inst = Let ("s",ExpInt 1) };
  { num = 40; inst = Let ("i",(ExpBin ((ExpVar "i"),Plus,(ExpInt 1)))) };
  { num = 50; inst = Let ("s",(ExpBin ((ExpVar "s"),Mult,(ExpVar "i")))) };
  { num = 60; inst = If ((ExpBin ((ExpVar "i"),Equal,(ExpVar "n"))),80) };
  { num = 70; inst = Goto 40 };
  { num = 80; inst = Print (ExpString "result: ") };
  { num = 90; inst = Print (ExpVar "s") };
  { num = 100; inst = Print (ExpString "\n") }
];;

exec_prgm prog;;
