(* snake.ml
--------------

    Exceptions :
        * Victoire,
        * Echec.
        
    Types :
        * direction : haut, bas, gauche, droite (pas de diagonales),
        * coordonnées d'un point : abscisse, ordonnée,
        * cible : coordonnées, couleur,
        * monde d'évolution : largeur, hauteur, taille des cases, couleur de fond, cible du ver,
        * ver de terre : liste des coordonnées, tête, queue, direction, couleur.
        
    Constante :
        * taille maximum du ver.
        
    Fonctions :
        * mise en attente du programme en seconde -> s: durée de l'attente,
        * fin de partie, affichage d'un message, attente de quelques secondes -> msg: message à afficher, color: couleur du message,
        * affichage d'un bloc carré à l'écran -> coord: coordonnées du bloc, size: taille, color: couleur,
        * initialisation d'un jeu -> cols: nombre de colonnes, rows : nombre de lignes, size: taille des bloc du jeu, color_world: couleur de fond,
                                     color_target: couleur des cibles, color_snake: couleur du ver,
        * initialisation de l'affichage -> snake: ver, world: environnement,
        * affichage de l'état du ver -> snake: ver, world: environnement,
        * création d'une nouvelle cible -> snake: ver, world: environnement,
        * vidage de la pile d'évènement -> aucun argument,
        * changement de direction suivant les touches du clavier -> dir: direction du ver actuelle,
        * calcul du nouvel état du ver -> snake: ver, world: environnement, d: direction nouvelle du ver,
        * boucle principale du jeu -> snake: ver, world: environnement,
        * fonction principale lançant une nouvelle partie avec des paramètres par défaut -> aucun argument.
*)


exception Win;;
exception Loose;;


type direction_t = Up | Down | Left | Right;;

type coord_t = {
    x: int;
    y: int;
};;

type bloc_t = {
    coords: coord_t;
    b_color: Graphics.color;
};;

type world_t = {
    width: int;
    height: int;
    size_square: int;
    w_color: Graphics.color;
    target: bloc_t;
};;

type snake_t = {
    list_coords: coord_t list;
    head: coord_t;
    tail: coord_t;
    dir: direction_t;
    s_color: Graphics.color;
};;


let size_max = 30;;


let sleep s =
    let start = Unix.gettimeofday() in
    let rec delay t =
        try
            ignore (Unix.select [] [] [] t)
        with Unix.Unix_error(Unix.EINTR, _, _) ->
            let now = Unix.gettimeofday() in
            let remaining = start +. s -. now in
            if (remaining > 0.0) then delay remaining in
    delay s;;
    
let instructions () = ( Graphics.moveto 0 0;
                           Graphics.draw_string " USE z, q, s, d TO MOVE YOUR SNAKE -- PRESS A TOUCH TO CONTINUE";
                           ignore (Graphics.wait_next_event [Graphics.Key_pressed]); );;
    
let end_game msg world color = (* Affichage du message au milieu de la fenêtre. *)
    ( Graphics.moveto (world.width / 2 - 10) (world.height / 2);
      Graphics.set_color color;
      Graphics.draw_string msg;
      sleep 3.;) ;;
    
let display_bloc coord size color = ( Graphics.set_color color;
                                      Graphics.fill_rect coord.x coord.y (size - 1) (size - 1); );;


let init_game cols rows size color_world color_target color_snake = (* Le ver est positionné au milieu de l'environnement, avec une cible juste devant lui,
                                                                        ainsi on s'assure qu'une génération aléatoire de cette dernière ne tombe pas sur lui. *)
    let c = cols / 2 and r = rows / 2 in
    ({ width = cols * size;
        height = rows * size;
        size_square = size;
        w_color = color_world;
        target = { coords = { x = (c - 1) * size; y = r * size };
                   b_color = color_target } },
      { list_coords = [{ x = c * size; y = r * size }; { x = (c + 1) * size; y = r * size }];
        head = { x = c * size; y = r * size };
        tail = { x = 0; y = 0 };
        dir = Left;
        s_color = color_snake });;

let init_display snake world =  (* Affichage des premiers bloc du ver et remplissage du fond. *)
    let rec display_snake s = match s with
        | [] -> ()
        | h :: t -> ( display_bloc h world.size_square snake.s_color;
                      display_snake t; ) in
    ( Graphics.set_color world.w_color;
      Graphics.fill_rect 0 0 world.width world.height;
      display_snake snake.list_coords; );;

let display_state snake world = ( display_bloc snake.tail world.size_square world.w_color;
                                  display_bloc snake.head world.size_square snake.s_color; );;
                                   
let rec new_target snake world =    (* La nouvelle cible ne doit pas se trouver sur le ver. *)
    let x' = Random.int world.width and y' = Random.int world.height in
    let c = { x = x' - (x' mod world.size_square); y = y' - (y' mod world.size_square) } in
    if (List.exists (fun coord -> coord.x = c.x && coord.y = c.y) snake.list_coords) then new_target snake world
    else ( display_bloc c world.size_square world.target.b_color; { coords = c; b_color = world.target.b_color } );;
    
let rec empty_stack_event () =  (* L'option Graphics.Poll ne vide pas la pile d'évènements. *)
    let event = Graphics.wait_next_event [Graphics.Poll] in
    if (event.Graphics.keypressed = true) then ( ignore (Graphics.wait_next_event [Graphics.Key_pressed]); empty_stack_event (); )
    else ();;

let change_direction dir =  (* Impossible de faire demi-tour directement (cela reviendrait à perdre immédiatement). *)
    let event = Graphics.wait_next_event [Graphics.Poll] in  
    if (event.Graphics.keypressed = false) then dir
    else match event.Graphics.key with
            | 'z' when (dir = Left || dir = Right) -> Up
            | 's' when (dir = Left || dir = Right) -> Down
            | 'q' when (dir = Up || dir = Down) -> Left
            | 'd' when (dir = Up || dir = Down) -> Right
            | _ -> dir;;
    
let run snake world d = (*
                            * Calcul des nouvelles coordonnées de la tête,
                            * Suppression de la queue si l'on atteint pas de cible,
                            * Génération d'une nouvelle cible si on atteint l'actuelle,
                            * Levée d'exceptions :
                                - Win si le ver atteint la taille limite,
                                - Loose s'il touche un bord ou lui-même.
                         *)
    let next_coord h = match d with
        | Up -> { x = h.x; y = h.y + world.size_square }
        | Down -> { x = h.x; y = h.y - world.size_square }
        | Left -> { x = h.x - world.size_square; y = h.y }
        | Right ->  { x = h.x + world.size_square; y = h.y } in
    let rec del_last_coord l = match l with
        | [] -> failwith "List doesn't exist"
        | h :: [] -> []
        | h :: t -> h :: del_last_coord t in
    let t = List.nth snake.list_coords ((List.length snake.list_coords) - 1) and new_coords = del_last_coord snake.list_coords in
    let h = next_coord snake.head in
    if ((List.exists (fun coord -> coord.x = h.x && coord.y = h.y) new_coords) || (h.x < 0) || (h.y < 0) || (h.x >= world.width) || (h.y >= world.height)) then raise Loose
    else if (List.length snake.list_coords = size_max) then raise Win
    else if (world.target.coords.x == h.x && world.target.coords.y == h.y) then ({ snake with list_coords = h :: snake.list_coords; head = h; tail = t; dir = d },
                                                                                 { world with target = new_target snake world })
    else ({ snake with list_coords = h :: new_coords; head = h; tail = t; dir = d }, world);;

let rec play snake world = (* Interaction avec le joueur, vidage de la pile d'évènement, affichage et attente dégressante suivant la taille du ver. *)
    let (s, w) = run snake world (change_direction snake.dir) in
    (
        empty_stack_event ();
        display_state s w;
        sleep (0.5 /. (float_of_int (List.length s.list_coords)));
        play s w;
    );;

let main () =
    let (world, snake) = init_game 80 40 10 Graphics.black Graphics.blue Graphics.red in
    (
        Random.init (int_of_float (Unix.time ()));
        Graphics.open_graph (" " ^ (string_of_int world.width) ^ "x" ^ (string_of_int world.height));
        Graphics.set_window_title "Snake";

        instructions ();
        init_display snake world;
        try
            play snake world
        with
            | Loose -> end_game "LOOSE" world Graphics.white  
            | Win -> end_game "WIN" world Graphics.white;

        Graphics.close_graph();
    );;


main();;
