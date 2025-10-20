(* draw.ml
-------------

    Type :
        * segment à coordonnées polaires : abscisse, ordonnée, module, angle.
        
    Fonctions :
        * attente d'un clic ou d'une touche pressée par l'utilisateur,
        * transformation de coordonnées polaire en coordonnées carthésiennes d'un segment,
        * dessin d'un segment à l'écran,
        * transformation d'un segment suivant 3 valeurs : rotation, échelle et translation,
        * application d'une liste de transformation sur un segment de façon récursive (deux versions).
*)


type seg_pol = {
    x: float;
    y: float;
    r: float;
    a: float;
};;


let click_or_key() = Graphics.wait_next_event [Graphics.Key_pressed; Graphics.Button_down];;

let to_cart seg =
    (seg.x,
     seg.y,
     seg.x +. seg.r *. cos(seg.a),
     seg.y +. seg.r *. sin(seg.a));;
     
let draw_seg seg =
    let (x0, y0, x1, y1) = to_cart seg in
    ( Graphics.moveto (int_of_float x0) (int_of_float y0);
      Graphics.lineto (int_of_float x1) (int_of_float y1); );;
    
let app_trans seg t =
    let (rot, sc, tr) = t in
    let (_, _, x1, y1) = to_cart { x = seg.x; y = seg.y; r = seg.r *. tr; a = seg.a } in
    { x = x1 ; y = y1 ; r = seg.r *. sc; a = seg.a +. rot };;

let rec draw_r seg n l =
    let rec explore seg n l1 = match l1 with
        | [] -> ()
        | h :: t -> ( draw_r (app_trans seg h) (n - 1) l; explore seg n t; )in
    if (n <= 0) then ()
    else ( draw_seg seg; explore seg n l; );;


let pi = 3.1415926535897932384626383279;;
let s = { x = 200.; y = 0.; r = 100.; a = pi /. 2.};;

Graphics.open_graph " 400x300";;
Graphics.set_window_title "Draw";;

draw_r s 6 [((-.pi /. 2.), 0.6, 1.); ((pi /. 2.), 0.6, 1.)];;
click_or_key();;
Graphics.clear_graph();;

draw_r s 6 [((-.pi /. 6.), 0.6, 0.766); ((-.pi /. 4.), 0.55, 0.333); ((pi /. 3.), 0.4, 0.5)];;
click_or_key();;

Graphics.close_graph();;
